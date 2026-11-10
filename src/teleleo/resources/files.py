# File generated from spec/openapi.yaml by scripts/generate.py. Do not edit by hand.

from __future__ import annotations

from typing import Optional, Union, cast

from typing_extensions import Literal

from .._models import construct_type
from .._resource import AsyncAPIResource, SyncAPIResource
from .._types import NOT_GIVEN, Body, Headers, NotGiven, Query, Timeout
from .._utils import path_param
from ..types import TmpFile

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    """Downloads, temporary audio uploads and text-to-speech."""

    def download(
        self,
        file_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bytes:
        """
        Get file.

        Downloads a file of the account: a call recording, the audio of a call scenario or a mailing, an
        invoice document. The file_id comes from those objects (file_id, call_scenario_file_id, invoice and
        receipt files).

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, FILE_NOT_FOUND_EXCEPTION.
        """
        return self._client._request_bytes(
            "GET",
            f"/file/{path_param(file_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def download_tmp(
        self,
        file_id: str,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bytes:
        """
        Get temporary file.

        Served only to the user who uploaded the file. A missing file and somebody else's upload both answer
        404 TMP_FILE_NOT_FOUND.

        Args:
          file_id: tmp_file_id as returned by POST /file/upload-tmp or POST /file/generate-speech: `<2 hex>/<32
                hex>/<file name>`. Put it into the path as is: the slashes are path separators and must
                not be percent-encoded (most SDK generators encode `/` in a path parameter by default;
                turn it off for this one). Percent-encode only characters of the file name that are not
                allowed in a path segment.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, TMP_FILE_NOT_FOUND.
        """
        return self._client._request_bytes(
            "GET",
            f"/file/tmp/{path_param(file_id, keep_slashes=True)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    def upload_tmp(
        self,
        *,
        file_base64: str,
        file_name: str,
        scenario: Literal[
            "SCENARIO_CONVERT_TO_DONGLE_AUDIO_AND_UPLOAD_TMP"
        ] = "SCENARIO_CONVERT_TO_DONGLE_AUDIO_AND_UPLOAD_TMP",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> TmpFile:
        """
        Upload temporary file.

        Uploads an audio file as a temporary file, converted to the modem format; pass the returned
        tmp_file_id to a call scenario or a call mailing.

        Args:
          file_base64: Content of the audio file, base64-encoded.
          file_name: Name of the file; it becomes the last segment of tmp_file_id.
          scenario: The only upload scenario: the audio is converted to the modem format (wav) and stored as a
                temporary file.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, FILE_ERROR_IDENTIFIER_EMPTY_FIELDS,
        FILE_ERROR_FILE_NOT_VALID_BASE_64, FILE_ERROR_FILE_WRONG_TYPE, FILE_ERROR_FILE_NOT_VALID_SIZE,
        FILE_ERROR_CONVERT_TO_DONGLE_AUDIO, FILE_ERROR_DONGLE_AUDIO_TOO_LARGE.
        """
        data = self._client._request(
            "POST",
            "/file/upload-tmp",
            body={"file_base64": file_base64, "file_name": file_name, "scenario": scenario},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(TmpFile, construct_type(TmpFile, data))

    def generate_speech(
        self,
        *,
        text: str,
        voice: Literal["onyx", "echo", "shimmer", "nova"],
        language: Literal["en-GB", "it-IT", "tr-TR", "de-DE", "es-ES", "pt-PT", "fr-FR"],
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> TmpFile:
        """
        Generate speech.

        Synthesises the text into a temporary audio file for a call scenario or a call mailing; pass the
        returned tmp_file_id as the audio of those. Limited to 5 calls per day per user: the 6th answers 429
        RATE_LIMIT_EXCEEDED.

        Args:
          text: Text to synthesise.

        Error codes (``error_message``): RATE_LIMIT_EXCEEDED, FILE_GENERATE_SPEECH_IDENTIFIER_EMPTY_FIELDS,
        FILE_GENERATE_SPEECH_IDENTIFIER_NOT_ALLOWED_VOICE,
        FILE_GENERATE_SPEECH_IDENTIFIER_NOT_ALLOWED_LANGUAGE, FILE_GENERATE_SPEECH_IDENTIFIER_LONG_TEXT.
        """
        data = self._client._request(
            "POST",
            "/file/generate-speech",
            body={"text": text, "voice": voice, "language": language},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(TmpFile, construct_type(TmpFile, data))


class AsyncFilesResource(AsyncAPIResource):
    """Downloads, temporary audio uploads and text-to-speech."""

    async def download(
        self,
        file_id: int,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bytes:
        """
        Get file.

        Downloads a file of the account: a call recording, the audio of a call scenario or a mailing, an
        invoice document. The file_id comes from those objects (file_id, call_scenario_file_id, invoice and
        receipt files).

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, FILE_NOT_FOUND_EXCEPTION.
        """
        return await self._client._request_bytes(
            "GET",
            f"/file/{path_param(file_id)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def download_tmp(
        self,
        file_id: str,
        *,
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> bytes:
        """
        Get temporary file.

        Served only to the user who uploaded the file. A missing file and somebody else's upload both answer
        404 TMP_FILE_NOT_FOUND.

        Args:
          file_id: tmp_file_id as returned by POST /file/upload-tmp or POST /file/generate-speech: `<2 hex>/<32
                hex>/<file name>`. Put it into the path as is: the slashes are path separators and must
                not be percent-encoded (most SDK generators encode `/` in a path parameter by default;
                turn it off for this one). Percent-encode only characters of the file name that are not
                allowed in a path segment.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, TMP_FILE_NOT_FOUND.
        """
        return await self._client._request_bytes(
            "GET",
            f"/file/tmp/{path_param(file_id, keep_slashes=True)}",
            extra_headers=extra_headers,
            extra_query=extra_query,
            timeout=timeout,
        )

    async def upload_tmp(
        self,
        *,
        file_base64: str,
        file_name: str,
        scenario: Literal[
            "SCENARIO_CONVERT_TO_DONGLE_AUDIO_AND_UPLOAD_TMP"
        ] = "SCENARIO_CONVERT_TO_DONGLE_AUDIO_AND_UPLOAD_TMP",
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> TmpFile:
        """
        Upload temporary file.

        Uploads an audio file as a temporary file, converted to the modem format; pass the returned
        tmp_file_id to a call scenario or a call mailing.

        Args:
          file_base64: Content of the audio file, base64-encoded.
          file_name: Name of the file; it becomes the last segment of tmp_file_id.
          scenario: The only upload scenario: the audio is converted to the modem format (wav) and stored as a
                temporary file.

        Error codes (``error_message``): REQUEST_VALIDATION_EXCEPTION, FILE_ERROR_IDENTIFIER_EMPTY_FIELDS,
        FILE_ERROR_FILE_NOT_VALID_BASE_64, FILE_ERROR_FILE_WRONG_TYPE, FILE_ERROR_FILE_NOT_VALID_SIZE,
        FILE_ERROR_CONVERT_TO_DONGLE_AUDIO, FILE_ERROR_DONGLE_AUDIO_TOO_LARGE.
        """
        data = await self._client._request(
            "POST",
            "/file/upload-tmp",
            body={"file_base64": file_base64, "file_name": file_name, "scenario": scenario},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(TmpFile, construct_type(TmpFile, data))

    async def generate_speech(
        self,
        *,
        text: str,
        voice: Literal["onyx", "echo", "shimmer", "nova"],
        language: Literal["en-GB", "it-IT", "tr-TR", "de-DE", "es-ES", "pt-PT", "fr-FR"],
        extra_headers: Optional[Headers] = None,
        extra_query: Optional[Query] = None,
        extra_body: Optional[Body] = None,
        timeout: Union[Timeout, NotGiven] = NOT_GIVEN,
    ) -> TmpFile:
        """
        Generate speech.

        Synthesises the text into a temporary audio file for a call scenario or a call mailing; pass the
        returned tmp_file_id as the audio of those. Limited to 5 calls per day per user: the 6th answers 429
        RATE_LIMIT_EXCEEDED.

        Args:
          text: Text to synthesise.

        Error codes (``error_message``): RATE_LIMIT_EXCEEDED, FILE_GENERATE_SPEECH_IDENTIFIER_EMPTY_FIELDS,
        FILE_GENERATE_SPEECH_IDENTIFIER_NOT_ALLOWED_VOICE,
        FILE_GENERATE_SPEECH_IDENTIFIER_NOT_ALLOWED_LANGUAGE, FILE_GENERATE_SPEECH_IDENTIFIER_LONG_TEXT.
        """
        data = await self._client._request(
            "POST",
            "/file/generate-speech",
            body={"text": text, "voice": voice, "language": language},
            extra_headers=extra_headers,
            extra_query=extra_query,
            extra_body=extra_body,
            timeout=timeout,
        )
        return cast(TmpFile, construct_type(TmpFile, data))
