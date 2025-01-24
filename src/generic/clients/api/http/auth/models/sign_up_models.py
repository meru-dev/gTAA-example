from src.generic.clients.api.common.base_body import BaseBody


class SignUpUserRequest(BaseBody):
    username: str
    password: str
    email: str


class SignUpUserResponse(BaseBody):
    user_id: str
    username: str
    email: str
