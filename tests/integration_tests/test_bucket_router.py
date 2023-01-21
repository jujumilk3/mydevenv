from fastapi import status

from app.model.bucket import BucketDto
from app.core.security import create_access_token
from app.model.user import AuthDto


def test_create_bucket(client):
    access_token = create_access_token(AuthDto.Payload(
        email="test@test.com",
        nickname="test_nickname",
        user_token="test_user_token",
    ))
    bearer_token = f"Bearer {access_token['access_token']}"

    response = client.post(
        "/v1/bucket",
        headers={
            "Authorization": bearer_token,
        },
        json={
            "name": "test bucket",
            "path": "test-bucket",
            "description": "test bucket description",
            "memo": "test bucket",
        },
    )
    print(response.json())
    assert response.status_code == status.HTTP_201_CREATED
    assert BucketDto.WithBaseInfo(**response.json())
    assert response.json()["name"] == "test bucket"
    assert response.json()["path"] == "test-bucket"
    assert response.json()["description"] == "test bucket description"
    assert response.json()["memo"] == "test bucket"
    assert response.json()["created_at"]
    assert response.json()["updated_at"]
    assert response.json()["id"]
