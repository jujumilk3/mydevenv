from time import sleep

from fastapi import status

from app.model.bucket import BucketDto
from tests.utils.bearer_creater import create_bearer_token


def test_bucket_crud(client, current_test_name):
    bearer_token = create_bearer_token(current_test_name)

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
    assert response.status_code == status.HTTP_201_CREATED
    assert BucketDto.WithBaseInfo(**response.json())
    assert response.json()["name"] == "test bucket"
    assert response.json()["path"] == "test-bucket"
    assert response.json()["description"] == "test bucket description"
    assert response.json()["memo"] == "test bucket"
    assert response.json()["created_at"]
    assert response.json()["updated_at"]
    assert response.json()["id"]
    created_bucket_id = response.json()["id"]

    # get bucket
    response = client.get(
        f"/v1/bucket/{created_bucket_id}",
        headers={
            "Authorization": bearer_token,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert BucketDto.WithBaseInfo(**response.json())
    assert response.json()["name"] == "test bucket"
    assert response.json()["path"] == "test-bucket"
    assert response.json()["description"] == "test bucket description"
    assert response.json()["memo"] == "test bucket"
    assert response.json()["created_at"]
    assert response.json()["updated_at"]
    assert response.json()["id"] == created_bucket_id
    updated_at = response.json()["updated_at"]
    sleep(1)  # to check updated_at changed

    # update bucket
    response = client.patch(
        f"/v1/bucket/{created_bucket_id}",
        headers={
            "Authorization": bearer_token,
        },
        json={
            "name": "test bucket updated",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert BucketDto.WithBaseInfo(**response.json())
    assert response.json()["name"] == "test bucket updated"
    assert response.json()["path"] == "test-bucket"
    assert response.json()["description"] == "test bucket description"
    assert response.json()["memo"] == "test bucket"
    assert response.json()["created_at"]
    assert response.json()["updated_at"] != updated_at
    assert response.json()["id"] == created_bucket_id

    # update 2 fields
    response = client.patch(
        f"/v1/bucket/{created_bucket_id}",
        headers={
            "Authorization": bearer_token,
        },
        json={
            "name": "test bucket updated 2",
            "description": "test bucket description updated",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert BucketDto.WithBaseInfo(**response.json())
    assert response.json()["name"] == "test bucket updated 2"
    assert response.json()["path"] == "test-bucket"
    assert response.json()["description"] == "test bucket description updated"
    assert response.json()["memo"] == "test bucket"
    assert response.json()["created_at"]
    assert response.json()["updated_at"] != updated_at
    assert response.json()["id"] == created_bucket_id

    # delete bucket
    response = client.delete(
        f"/v1/bucket/{created_bucket_id}",
        headers={
            "Authorization": bearer_token,
        },
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # get deleted bucket
    response = client.get(
        f"/v1/bucket/{created_bucket_id}",
        headers={
            "Authorization": bearer_token,
        },
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND
