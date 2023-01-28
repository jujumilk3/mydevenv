from tests.utils.common import create_bearer_token
from fastapi import status


# inserted from "tests.conftest.insert_default_test_data"
def test_check_admin(client):
    super_user_bearer_token = create_bearer_token("admin")
    response = client.get(
        "/v1/admin/check",
        headers={
            "Authorization": super_user_bearer_token,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["is_admin"] is True
