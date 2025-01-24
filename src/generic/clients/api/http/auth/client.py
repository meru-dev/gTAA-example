from allure import step

from src.adapters.api.http.common.interface import RestHttpClientInterface
from src.generic.clients.api.http.auth.models.sign_up_models import (
    SignUpUserRequest,
    SignUpUserResponse,
)


class AuthApi:
    def __init__(
        self,
        client: RestHttpClientInterface,
    ) -> None:
        self._client = client

    @step("Register user with params {kwargs}")
    def register(
        self,
        payload: SignUpUserRequest,
    ) -> SignUpUserResponse:
        path = "api/v1/signup"
        response = self._client.post(path, json=payload.to_dict())
        return SignUpUserResponse(**response.in_json())
