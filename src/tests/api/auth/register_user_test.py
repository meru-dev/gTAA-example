from uuid import UUID

import pytest


@pytest.mark.parametrize(
    "params", [("username", "username@mail.com", "Pa$$w0rd")],
)
def test_register_user_with_valid_params(auth_steps, params):
    username, email, password = params

    registered_user = auth_steps.register_user(username, email, password)

    assert UUID(registered_user.user_id).version == 4
    assert registered_user.username == username
    assert registered_user.email == email
