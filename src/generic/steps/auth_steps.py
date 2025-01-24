from allure import step

from src.generic.clients.api.http.auth.client import AuthApi
from src.generic.clients.api.http.auth.models.sign_up_models import (
    SignUpUserRequest,
    SignUpUserResponse,
)


class AuthSteps:
    def __init__(self, auth_api: AuthApi) -> None:
        self._auth_api = auth_api

    @step("Register user with: {kwargs}")
    def register_user(
        self, username: str, email: str, password: str,
    ) -> SignUpUserResponse:
        return self._auth_api.register(
            payload=SignUpUserRequest(
                username=username, password=password, email=email,
            ),
        )
