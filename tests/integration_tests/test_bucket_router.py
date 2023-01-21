from fastapi import status

from app.model.bucket import BucketDto


def test_create_bucket(client):
    response = client.post(
        "/v1/bucket",
        json={
            "name": "test bucket",
            "path": "test-bucket",
            "description": "test bucket description",
            "memo": "test bucket",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert BucketDto.WithBaseInfo(**response.json())
    assert response.json()["name"] == "test bucket"
    assert response.json()["path"] == "test-bucket"
    assert response.json()["description"] == "test bucket description"
    assert response.json()["memo"] == "test bucket"
    assert response.json()["created_at"]
    assert response.json()["updated_at"]
    assert response.json()["id"]
