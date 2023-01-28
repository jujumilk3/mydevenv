from fastapi import status

from tests.utils.common import create_bearer_token


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


def test_register_tool(client, test_name):
    # request without token
    response = client.post(
        "/v1/admin/register/tool",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # normal user request
    normal_user_bearer_token = create_bearer_token("normal")
    response = client.post(
        "/v1/admin/register/tool",
        headers={
            "Authorization": normal_user_bearer_token,
        },
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json()["detail"] == "It's not a super user"

    # admin user request
    super_user_bearer_token = create_bearer_token("admin")
    response = client.post(
        "/v1/admin/register/tool",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "python",
            "description": "python tool",
            "image_url": "https://www.python.org/static/img/python-logo@2x.png",
            "is_open_source": True,
            "site_url": "https://www.python.org/",
            "github_url": "https://github.com/python/cpython",
        },
    )

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
