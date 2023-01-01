import pytest
from starlette import status


@pytest.mark.asyncio
async def test_healthcheck(client):
    response = client.get("/healthcheck")
    assert response.status_code == 200
    assert response.json() == "OK"


@pytest.mark.asyncio
async def test_router_basis(client):
    response = client.get("/test_only/test_string")
    assert response.status_code == 200
    assert response.json() == "hello world"

    response = client.get("/test_only/test_dict")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}

    response = client.get("/test_only/test_query?msg=hello")
    assert response.status_code == 200
    assert response.json() == {"msg": "hello"}

    response = client.post("/test_only/test_post", json={"title": "title", "content": "content"})
    assert response.status_code == 200
    assert response.json() == {"title": "response: title", "content": "response: content"}

    response = client.patch("/test_only/test_patch", json={"title": "title", "content": "content"})
    assert response.status_code == 200
    assert response.json() == {"title": "response: title", "content": "response: content"}

    response = client.delete("/test_only/test_delete?target_id=1")
    assert response.status_code == status.HTTP_204_NO_CONTENT

    response = client.post("/test_only/test_post_form", json={"title": "title", "content": "content"})
    assert response.status_code == 200
    assert response.json() == {"title": "response: title", "content": "response: content"}

    response = client.post(
        "/test_only/complex_case_post?item_id=1",
        json={"title": "title", "content": "content"},
    )
    assert response.status_code == 200
    assert response.json() == {"title": "response: title", "item_id": 1, "content": "response: content"}

    response = client.post(
        "/test_only/complex_case_form?item_id=1",
        data={"title": "title", "content": "content"},
    )
    assert response.status_code == 200
    assert response.json() == {"title": "response: title", "item_id": 1, "content": "response: content"}

    response = client.post(
        "/test_only/complex_case_form_and_body?item_id=1",
        data={"title": "title", "content": "content"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "title": "response: title",
        "item_id": 1,
        "content": "response: content",
        "body": "response: body",
    }

    response = client.post(
        "/test_only/test_upload_file",
        files={"file": ("test.txt", b"some file data")},
    )
    assert response.status_code == 200
    assert response.json() == {"file_name": "test.txt", "file_content": "some file data"}
