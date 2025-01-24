from dataclasses import dataclass
from enum import StrEnum, auto
from typing import Any

from httpx import Response


class RestMethods(StrEnum):
    get = auto()
    post = auto()
    put = auto()
    delete = auto()


@dataclass
class RestHttpRequest:
    method: RestMethods
    url: str
    params: dict[str, Any] | None = None
    headers: dict[str, Any] | None = None
    json: Any | None = None


class RestHttpResponse:
    def __init__(self, response_lib_obj: Response) -> None:
        self.response = response_lib_obj

    def in_content(self) -> bytes:
        return self.response.content

    def in_text(self) -> str:
        return self.response.text

    def in_json(self) -> dict[Any, Any]:
        return self.response.json()
