from __future__ import annotations

import datetime as dt
import json
from typing import Any, List

import httpx
import pytest
import respx

import teleleo
from teleleo import AsyncTeleleo, Teleleo
from teleleo.types import SmsType

BASE_URL = "https://api.example.test/react_api"


@pytest.fixture
def client() -> Teleleo:
    return Teleleo(api_key="test-key", base_url=BASE_URL, max_retries=2)


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch: pytest.MonkeyPatch) -> List[float]:
    delays: List[float] = []

    async def fake_async_sleep(seconds: float) -> None:
        delays.append(seconds)

    monkeypatch.setattr("teleleo._base_client.time.sleep", lambda s: delays.append(s))
    monkeypatch.setattr("teleleo._base_client.asyncio.sleep", fake_async_sleep)
    return delays


# --------------------------------------------------------------------------------------------- configuration


def test_api_key_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TELELEO_API_KEY", "env-key")
    monkeypatch.delenv("TELELEO_BASE_URL", raising=False)
    client = Teleleo()
    assert client.api_key == "env-key"
    assert client.base_url == "https://app.teleleo.com/react_api"


def test_missing_api_key(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.delenv("TELELEO_API_KEY", raising=False)
    with pytest.raises(teleleo.TeleleoError, match="TELELEO_API_KEY"):
        Teleleo()


def test_base_url_from_env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TELELEO_BASE_URL", "https://api.teleleo.example/v1/")
    client = Teleleo(api_key="k")
    assert client.base_url == "https://api.teleleo.example/v1"


@respx.mock
def test_headers(client: Teleleo) -> None:
    route = respx.get(f"{BASE_URL}/dongle").mock(return_value=httpx.Response(200, json={"data": {"dongles": []}}))
    client.with_options(default_headers={"X-Trace": "1"}).dongles.list()
    request = route.calls.last.request
    assert request.headers["auth-key"] == "test-key"
    assert request.headers["accept"] == "application/json"
    assert request.headers["user-agent"] == f"teleleo-python/{teleleo.__version__}"
    assert request.headers["x-trace"] == "1"


# --------------------------------------------------------------------------------------------- request encoding


@respx.mock
def test_query_encoding(client: Teleleo) -> None:
    route = respx.get(f"{BASE_URL}/sms").mock(
        return_value=httpx.Response(200, json={"data": {"smses": [], "total_count": 0}})
    )
    since = dt.datetime(2026, 11, 9, 15, 42, tzinfo=dt.timezone(dt.timedelta(hours=3)))
    client.sms.list(
        sms_type_ids=(t for t in [SmsType.INCOMING, 5]),
        dongle_ids=[7],
        from_=since,
        to="2026-11-10 00:00:00",
        limit=10,
        extra_query={"custom": True},
    )
    params = route.calls.last.request.url.params
    assert params.get_list("sms_type_ids[]") == ["2", "5"]
    assert params.get_list("dongle_ids[]") == ["7"]
    assert params["from"] == "2026-11-09 12:42:00"
    assert params["to"] == "2026-11-10 00:00:00"
    assert params["limit"] == "10"
    assert params["custom"] == "1"
    assert "page" not in params


@respx.mock
def test_body_encoding(client: Teleleo) -> None:
    route = respx.put(f"{BASE_URL}/dongle/5/sms/9").mock(return_value=httpx.Response(200, json={"data": {}}))
    client.sms.update(5, 9, message="hi", new_dongle_id=6, scheduled_at=None, extra_body={"x": 1})
    assert json.loads(route.calls.last.request.content) == {
        "message": "hi",
        "dongle_id": 6,
        "scheduled_at": None,
        "x": 1,
    }


@respx.mock
def test_datetime_in_body(client: Teleleo) -> None:
    route = respx.post(f"{BASE_URL}/dongle/5/outgoing-sms").mock(return_value=httpx.Response(200, json={"data": {}}))
    client.sms.send(5, number="+447700900123", message="hi", scheduled_at=dt.datetime(2026, 12, 1, 8, 30))
    assert json.loads(route.calls.last.request.content)["scheduled_at"] == "2026-12-01 08:30:00"


@respx.mock
def test_tmp_file_id_keeps_slashes(client: Teleleo) -> None:
    file_id = "ab/0123456789abcdef0123456789abcdef/hello world.wav"
    route = respx.get(url__regex=r".*/file/tmp/.*").mock(return_value=httpx.Response(200, content=b"RIFF"))
    assert client.files.download_tmp(file_id) == b"RIFF"
    assert route.calls.last.request.url.raw_path == (
        b"/react_api/file/tmp/ab/0123456789abcdef0123456789abcdef/hello%20world.wav"
    )


def test_path_param_is_escaped(client: Teleleo) -> None:
    with respx.mock() as mock:
        route = mock.get(url__regex=r".*/contact/.*").mock(return_value=httpx.Response(200, json={"data": {}}))
        client.contacts.get("1/../2")  # type: ignore[arg-type]
        assert route.calls.last.request.url.raw_path == b"/react_api/contact/1%2F..%2F2"


# --------------------------------------------------------------------------------------------- errors


def _error(status: int, body: Any) -> httpx.Response:
    if isinstance(body, (dict, list)) or (isinstance(body, str) and body.startswith('"')):
        return httpx.Response(status, json=body if not isinstance(body, str) else json.loads(body))
    return httpx.Response(status, text=body, headers={"content-type": "text/html"})


@pytest.mark.parametrize(
    "status, body, exc, error_message, details",
    [
        (
            400,
            {
                "is_successful": False,
                "code": 400,
                "error_message": "REQUEST_VALIDATION_EXCEPTION",
                "error_details": ["limit: must be at most 1000"],
                "request_id": "r-1",
            },
            teleleo.BadRequestError,
            "REQUEST_VALIDATION_EXCEPTION",
            ["limit: must be at most 1000"],
        ),
        (
            400,
            {"is_successful": False, "error_message": "CONTACT_NOT_FOUND_EXCEPTION", "error_details": None},
            teleleo.NotFoundError,
            "CONTACT_NOT_FOUND_EXCEPTION",
            [],
        ),
        (
            400,
            {"is_successful": False, "code": 400, "error_message": "Bad request", "error_message_detail": None},
            teleleo.BadRequestError,
            "Bad request",
            [],
        ),
        (404, {"error_message": "ROUTE_NOT_FOUND"}, teleleo.NotFoundError, "ROUTE_NOT_FOUND", []),
        (401, {"error_message": "UNAUTHORIZED"}, teleleo.AuthenticationError, "UNAUTHORIZED", []),
        (403, {"error_message": "PUBLIC_API_ROUTE_FORBIDDEN"}, teleleo.PermissionDeniedError, None, []),
        (405, '"Error 405"', teleleo.APIStatusError, None, ["Error 405"]),
        (409, {"error_message": "CONFLICT"}, teleleo.ConflictError, "CONFLICT", []),
        (500, "<html>oops</html>", teleleo.InternalServerError, None, []),
    ],
)
@respx.mock
def test_error_mapping(status: int, body: Any, exc: type, error_message: Any, details: List[str]) -> None:
    client = Teleleo(api_key="k", base_url=BASE_URL, max_retries=0)
    respx.get(f"{BASE_URL}/contact/1").mock(return_value=_error(status, body))
    with pytest.raises(exc) as info:
        client.contacts.get(1)
    err = info.value
    assert isinstance(err, teleleo.APIStatusError)
    assert err.status_code == status
    if error_message is not None:
        assert err.error_message == error_message
    assert err.error_details == details


@respx.mock
def test_error_message_text(client: Teleleo) -> None:
    respx.get(f"{BASE_URL}/contact/1").mock(
        return_value=httpx.Response(
            400,
            json={
                "is_successful": False,
                "code": 400,
                "error_message": "CONTACT_NOT_FOUND_EXCEPTION",
                "error_details": ["Contact not found"],
                "request_id": "abc",
            },
        )
    )
    with pytest.raises(teleleo.NotFoundError) as info:
        client.contacts.get(1)
    assert str(info.value) == "Error code: 400 - CONTACT_NOT_FOUND_EXCEPTION: Contact not found (request_id: abc)"
    assert info.value.request_id == "abc"


@respx.mock
def test_success_with_html_body(client: Teleleo) -> None:
    respx.get(f"{BASE_URL}/contact/1").mock(
        return_value=httpx.Response(200, text="<html></html>", headers={"content-type": "text/html"})
    )
    with pytest.raises(teleleo.APIResponseValidationError, match="Expected a JSON answer"):
        client.contacts.get(1)


# --------------------------------------------------------------------------------------------- retries


@respx.mock
def test_get_is_retried(client: Teleleo, no_sleep: List[float]) -> None:
    route = respx.get(f"{BASE_URL}/dongle/1").mock(
        side_effect=[
            httpx.Response(503),
            httpx.Response(429, headers={"retry-after": "2"}),
            httpx.Response(200, json={"data": {"dongle_id": 1}}),
        ]
    )
    assert client.dongles.get(1).dongle_id == 1
    assert route.call_count == 3
    assert no_sleep[1] == 2.0


@respx.mock
def test_post_is_not_retried_on_503(client: Teleleo) -> None:
    route = respx.post(f"{BASE_URL}/dongle/1/outgoing-sms").mock(return_value=httpx.Response(503))
    with pytest.raises(teleleo.InternalServerError):
        client.sms.send(1, number="+447700900123", message="hi")
    assert route.call_count == 1


@respx.mock
def test_post_is_retried_on_429(client: Teleleo) -> None:
    route = respx.post(f"{BASE_URL}/dongle/1/outgoing-sms").mock(
        side_effect=[httpx.Response(429), httpx.Response(200, json={"data": {"sms_id": 3}})]
    )
    assert client.sms.send(1, number="+447700900123", message="hi").sms_id == 3
    assert route.call_count == 2


@respx.mock
def test_post_is_retried_when_not_sent(client: Teleleo) -> None:
    route = respx.post(f"{BASE_URL}/dongle/1/reboot").mock(
        side_effect=[httpx.ConnectError("refused"), httpx.Response(200, json={"data": {"status": True}})]
    )
    assert client.dongles.reboot(1) is True
    assert route.call_count == 2


@respx.mock
def test_post_is_not_retried_after_read_timeout(client: Teleleo) -> None:
    route = respx.post(f"{BASE_URL}/dongle/1/reboot").mock(side_effect=httpx.ReadTimeout("slow"))
    with pytest.raises(teleleo.APITimeoutError):
        client.dongles.reboot(1)
    assert route.call_count == 1


@respx.mock
def test_retries_give_up(client: Teleleo) -> None:
    route = respx.get(f"{BASE_URL}/dongle/1").mock(side_effect=httpx.ConnectError("refused"))
    with pytest.raises(teleleo.APIConnectionError):
        client.dongles.get(1)
    assert route.call_count == 3


@respx.mock
def test_500_is_not_retried(client: Teleleo) -> None:
    route = respx.get(f"{BASE_URL}/dongle/1").mock(return_value=httpx.Response(500, json={"error_message": "X"}))
    with pytest.raises(teleleo.InternalServerError):
        client.dongles.get(1)
    assert route.call_count == 1


# --------------------------------------------------------------------------------------------- async


@respx.mock
async def test_async_client() -> None:
    respx.get(f"{BASE_URL}/dongle/1").mock(
        side_effect=[httpx.Response(502), httpx.Response(200, json={"data": {"dongle_id": 1, "name": "A"}})]
    )
    respx.get(f"{BASE_URL}/contact/2").mock(
        return_value=httpx.Response(400, json={"error_message": "CONTACT_NOT_FOUND_EXCEPTION"})
    )
    async with AsyncTeleleo(api_key="k", base_url=BASE_URL) as client:
        dongle = await client.dongles.get(1)
        assert dongle.name == "A"
        with pytest.raises(teleleo.NotFoundError):
            await client.contacts.get(2)


def test_with_options_shares_connection_pool(client: Teleleo) -> None:
    copy = client.with_options(timeout=5, max_retries=0)
    assert copy._http is client._http
    assert copy.timeout == 5 and copy.max_retries == 0
    copy.close()
    assert not client._http.is_closed
