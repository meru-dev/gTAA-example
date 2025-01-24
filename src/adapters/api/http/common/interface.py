from abc import ABC, abstractmethod
from typing import Any

from src.adapters.api.http.common.entities import RestHttpResponse

KwargsType: type = dict[str, Any]


class RestHttpClientInterface(ABC):
    @abstractmethod
    def get(self, endpoint: str, **kwargs: KwargsType) -> RestHttpResponse:
        raise NotImplementedError

    @abstractmethod
    def post(self, endpoint: str, **kwargs: KwargsType) -> RestHttpResponse:
        raise NotImplementedError

    @abstractmethod
    def put(self, endpoint: str, **kwargs: KwargsType) -> RestHttpResponse:
        raise NotImplementedError

    @abstractmethod
    def delete(self, endpoint: str, **kwargs: KwargsType) -> RestHttpResponse:
        raise NotImplementedError
