from fastapi import status

from tests.utils.common import create_bearer_token


def test_tag_crud(client, test_name):
    # create
    bearer_token = create_bearer_token("normal")
    response = client.post(
        "/v1/tag",
        json={
            "name": "test_tag",
            "description": "test_tag_description",
        },
        headers={
            "Authorization": bearer_token,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    tag_id = response.json()["id"]

    # get
    response = client.get(
        f"/v1/tag/{tag_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "test_tag"
    assert response.json()["description"] == "test_tag_description"

    # update
    response = client.patch(
        f"/v1/tag/{tag_id}",
        json={
            "name": "test_tag_updated",
            "description": "test_tag_description_updated",
        },
        headers={
            "Authorization": bearer_token,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "test_tag_updated"
    assert response.json()["description"] == "test_tag_description_updated"

    # delete
    response = client.delete(
        f"/v1/tag/{tag_id}",
        headers={
            "Authorization": bearer_token,
        },
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # get again
    response = client.get(
        f"/v1/tag/{tag_id}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # delete again
    response = client.delete(
        f"/v1/tag/{tag_id}",
        headers={
            "Authorization": bearer_token,
        },
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # update again
    response = client.patch(
        f"/v1/tag/{tag_id}",
        json={
            "name": "test_tag_updated",
            "description": "test_tag_description_updated",
        },
        headers={
            "Authorization": bearer_token,
        },
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND

    # create again
    response = client.post(
        "/v1/tag",
        json={
            "name": "test_tag",
            "description": "test_tag_description",
        },
        headers={
            "Authorization": bearer_token,
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
