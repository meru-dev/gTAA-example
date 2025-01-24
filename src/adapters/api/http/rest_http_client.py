from httpx import request

from src.adapters.api.http.common.entities import (
    RestHttpRequest,
    RestHttpResponse,
    RestMethods,
)
from src.adapters.api.http.common.interface import (
    KwargsType,
    RestHttpClientInterface,
)


class RestHttpClient(RestHttpClientInterface):
    _last_response: RestHttpResponse

    def __init__(
        self,
        base_url: str,
    ) -> None:
        self._base_url = base_url

    def _request(
        self, method: RestMethods, endpoint: str, **kwargs: KwargsType,
    ) -> RestHttpResponse:

        request_data = RestHttpRequest(
            method=method, url=self._base_url + endpoint, **kwargs,
        )
        response = request(
            method=request_data.method,
            url=self._base_url + request_data.url,
            **kwargs,
        )
        self._last_response = RestHttpResponse(response)
        return self._last_response

    def get(self, endpoint: str, **kwargs: KwargsType) -> RestHttpResponse:
        return self._request(RestMethods.get, endpoint=endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: KwargsType) -> RestHttpResponse:
        return self._request(RestMethods.post, endpoint=endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs: KwargsType) -> RestHttpResponse:
        return self._request(RestMethods.put, endpoint=endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs: KwargsType) -> RestHttpResponse:
        return self._request(RestMethods.delete, endpoint=endpoint, **kwargs)
