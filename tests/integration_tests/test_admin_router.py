from tests.utils.common import create_bearer_token
from fastapi import status


# users have been inserted from "tests.conftest.insert_default_test_data"
def test_check_admin(client, test_name):
    # request without token
    response = client.get(
        "/v1/admin/check",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # normal user request
    normal_user_bearer_token = create_bearer_token("normal")
    response = client.get(
        "/v1/admin/check",
        headers={
            "Authorization": normal_user_bearer_token,
        },
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json()["detail"] == "It's not a super user"

    # admin user request
    super_user_bearer_token = create_bearer_token("admin")
    response = client.get(
        "/v1/admin/check",
        headers={
            "Authorization": super_user_bearer_token,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["is_admin"] is True
