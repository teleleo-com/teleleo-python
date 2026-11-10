# Teleleo Python library

Teleleo is a platform for managing SIM-card modems from the cloud: SMS, calls, USSD, mailings, redirections, Wi-Fi, VPN and SOCKS proxy. `teleleo` is the official Python library for the [Teleleo REST API](https://github.com/teleleo-com/teleleo-openapi).

- Sync and async clients
- Typed models and enums for every answer, docstrings on every method
- Every error is an exception with the API error code
- Automatic pagination and retries
- Python 3.9+

## Installation

```bash
pip install teleleo
```

## Quickstart

Take the API key in the Teleleo cabinet (Settings → API key) and put it into the `TELELEO_API_KEY` environment variable.

```python
from teleleo import Teleleo

client = Teleleo()  # reads TELELEO_API_KEY

for dongle in client.dongles.list():
    print(dongle.dongle_id, dongle.name, dongle.number)

sms = client.sms.send(
    1234,  # dongle_id of the modem that sends the SMS
    number="+447700900123",
    message="Hello from Teleleo",
)
print(sms.sms_id, sms.sms_status_id)
```

## Usage

### Read incoming SMS

```python
from datetime import datetime, timedelta, timezone

from teleleo import Teleleo
from teleleo.types import SmsType

client = Teleleo()

since = datetime.now(timezone.utc) - timedelta(days=1)
for sms in client.sms.list(sms_type_ids=[SmsType.INCOMING], from_=since, limit=100):
    print(sms.created_at, sms.number_caller, sms.message_decoded)
```

Dates in answers are timezone-aware `datetime` objects in UTC. Date arguments take a `datetime` (a naive one is taken as UTC) or a string in the API format, `YYYY-MM-DD HH:MM:SS`.

### Pagination

List methods return a page. `page.items` holds one page; iterating the page goes through every item and requests the next pages as needed.

```python
page = client.contacts.list(limit=50)
print(page.total_count, len(page.items))

for contact in page:  # all contacts, 50 per request
    print(contact.name)

while page.has_next_page():  # or page by page
    page = page.get_next_page()
```

Without `page` and `limit` the API returns the whole list in one answer (mailings return the first 50).

### Modem commands

```python
client.dongles.reboot(1234)
info = client.dongles.get_network_info(1234)
print(info.current_network_name, info.network_type, info.is_roaming)
```

Every method and its arguments are listed in [api.md](api.md).

### Errors

Every error is a subclass of `teleleo.TeleleoError`. When the API answers with an error, the exception carries the machine-readable code in `error_message`, details in `error_details` and `request_id` for support.

```python
import teleleo
from teleleo import Teleleo

client = Teleleo()

try:
    client.contacts.get(999999)
except teleleo.NotFoundError as e:
    print("No such contact:", e.error_message)
except teleleo.BadRequestError as e:
    print(e.status_code, e.error_message, e.error_details)
except teleleo.APIStatusError as e:
    print("Teleleo error", e.status_code, e.error_message, "request_id:", e.request_id)
except teleleo.APIConnectionError:
    print("Teleleo is unreachable")
```

| Status | Exception |
|---|---|
| 400 | `BadRequestError` |
| 400 with `*NOT_FOUND*`, 404 | `NotFoundError` |
| 401 | `AuthenticationError` |
| 403 | `PermissionDeniedError` |
| 409 | `ConflictError` |
| 429 | `RateLimitError` |
| 5xx | `InternalServerError` |
| no answer | `APIConnectionError`, `APITimeoutError` |

API v1 answers 400, not 404, for a missing object; the library raises `NotFoundError` for both, so your code keeps working when the API moves to 404.

### Retries and timeouts

Requests that failed for a transient reason are repeated twice with exponential backoff: connection errors, 429, and 408/502/503/504 for requests that are safe to repeat. A POST (sending an SMS, creating a call) is repeated only when the server could not have acted on it, so a retry never sends an SMS twice.

```python
client = Teleleo(timeout=20, max_retries=3)
client.with_options(timeout=5, max_retries=0).dongles.list()
```

The default timeout is 60 seconds.

### Async

```python
import asyncio

from teleleo import AsyncTeleleo


async def main() -> None:
    async with AsyncTeleleo() as client:
        page = await client.sms.list(limit=100)
        async for sms in page:
            print(sms.message_decoded)


asyncio.run(main())
```

### Configuration

| Argument | Environment variable | Default |
|---|---|---|
| `api_key` | `TELELEO_API_KEY` | required |
| `base_url` | `TELELEO_BASE_URL` | `https://app.teleleo.com/react_api` |
| `timeout` | | 60 seconds |
| `max_retries` | | 2 |
| `default_headers` | | |
| `http_client` | | your own `httpx.Client` / `httpx.AsyncClient`, for proxies or custom transports |

### Fields the library does not know yet

Answers are not validated, so a new field or enum value in the API never breaks your code: unknown fields are kept as attributes, unknown enum values stay plain integers. `model.to_dict()` and `model.to_json()` give the answer as it came. To send a parameter the library does not have yet, use `extra_query`, `extra_body` or `extra_headers` on any method.

## Versioning

The library follows [semver](https://semver.org/). Changes are listed in [CHANGELOG.md](CHANGELOG.md).

## Development

Models and resources in `src/teleleo/resources` and `src/teleleo/types` are generated from [`spec/openapi.yaml`](spec/openapi.yaml):

```bash
pip install -e . -r requirements-dev.txt
python scripts/generate.py
pytest
```

## Support

support@teleleo.com · [teleleo.com](https://teleleo.com) · [issues](https://github.com/teleleo-com/teleleo-python/issues)

## License

[MIT](LICENSE)
