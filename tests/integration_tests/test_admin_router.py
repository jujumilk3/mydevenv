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


def test_tool_crud(client, test_name):
    # request without token
    response = client.post(
        "/v1/admin/tool",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # normal user request
    normal_user_bearer_token = create_bearer_token("normal")
    response = client.post(
        "/v1/admin/tool",
        headers={
            "Authorization": normal_user_bearer_token,
        },
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json()["detail"] == "It's not a super user"

    # admin user request
    super_user_bearer_token = create_bearer_token("admin")
    response = client.post(
        "/v1/admin/tool",
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
    python_tool_id = response.json()["id"]

    # get tool
    response = client.get(
        f"/v1/tool/{python_tool_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == python_tool_id
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"

    # admin patch
    response = client.patch(
        f"/v1/admin/tool/{python_tool_id}",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "python",
            "description": "python tool updated",
            "image_url": "https://www.python.org/static/img/python-logo@2x.png",
            "is_open_source": True,
            "site_url": "https://www.python.org/",
            "github_url": "https://github.com/python/cpython",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool updated"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"

    # get tool
    response = client.get(
        f"/v1/tool/{python_tool_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == python_tool_id
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool updated"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"

    # remove tool
    response = client.delete(
        f"/v1/admin/tool/{python_tool_id}",
        headers={
            "Authorization": super_user_bearer_token,
        },
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # get tool
    response = client.get(
        f"/v1/tool/{python_tool_id}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND


def test_tool_with_tags_and_reference_tool(client):
    # request without token
    response = client.post(
        "/v1/admin/tool",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED

    # normal user request
    normal_user_bearer_token = create_bearer_token("normal")
    response = client.post(
        "/v1/admin/tool",
        headers={
            "Authorization": normal_user_bearer_token,
        },
    )
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert response.json()["detail"] == "It's not a super user"

    # admin user request
    super_user_bearer_token = create_bearer_token("admin")
    response = client.post(
        "/v1/admin/tool",
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
    python_tool_id = response.json()["id"]

    # admin patch
    response = client.patch(
        f"/v1/admin/tool/{python_tool_id}",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "python",
            "description": "python tool updated",
            "image_url": "https://www.python.org/static/img/python-logo@2x.png",
            "is_open_source": True,
            "site_url": "https://www.python.org/",
            "github_url": "https://github.com/python/cpython",
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool updated"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"

    # create tool node.js
    response = client.post(
        "/v1/admin/tool",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "node.js",
            "description": "node.js tool",
            "image_url": "https://nodejs.org/static/images/logo.svg",
            "is_open_source": True,
            "site_url": "https://nodejs.org/",
            "github_url": "https://github.com/nodejs/node",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == "node.js"
    assert response.json()["description"] == "node.js tool"
    assert response.json()["image_url"] == "https://nodejs.org/static/images/logo.svg"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://nodejs.org/"
    assert response.json()["github_url"] == "https://github.com/nodejs/node"

    # remove tool
    response = client.delete(
        f"/v1/admin/tool/{python_tool_id}",
        headers={
            "Authorization": super_user_bearer_token,
        },
    )
    assert response.status_code == status.HTTP_204_NO_CONTENT

    # create tag
    response = client.post(
        "/v1/tag",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "language",
            "description": "language tag",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == "language"
    assert response.json()["description"] == "language tag"

    response = client.post(
        "/v1/tag",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "framework",
            "description": "framework tag",
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == "framework"
    assert response.json()["description"] == "framework tag"

    response = client.post(
        "/v1/tag",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "web",
            "description": "web tag",
        },
    )

    # create tool python with tag
    response = client.post(
        "/v1/admin/tool",
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
            "tag_names": ["language", "framework"],
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "language" in only_tag_names
    assert "framework" in only_tag_names
    python_tool_id = response.json()["id"]

    # patch tool python with tag
    response = client.patch(
        f"/v1/admin/tool/{python_tool_id}",
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
            "tag_names": ["language", "web"],
        },
    )
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" in only_tag_names
    assert "web" in only_tag_names
    python_tool_id = response.json()["id"]

    # get tool python
    response = client.get(
        f"/v1/tool/{python_tool_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == python_tool_id
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" in only_tag_names
    assert "web" in only_tag_names

    # patch tool python with tag
    response = client.patch(
        f"/v1/admin/tool/{python_tool_id}",
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
            "tag_names": ["web"],
        },
    )
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" not in only_tag_names
    assert "web" in only_tag_names

    # get tool python
    response = client.get(
        f"/v1/tool/{python_tool_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == python_tool_id
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" not in only_tag_names
    assert "web" in only_tag_names

    # patch tool python with tag
    response = client.patch(
        f"/v1/admin/tool/{python_tool_id}",
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
            "tag_names": ["language", "framework", "web"],
        },
    )
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" in only_tag_names
    assert "language" in only_tag_names
    assert "web" in only_tag_names

    # get tool python
    response = client.get(
        f"/v1/tool/{python_tool_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == python_tool_id
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" in only_tag_names
    assert "language" in only_tag_names
    assert "web" in only_tag_names

    # patch tool python with tag
    response = client.patch(
        f"/v1/admin/tool/{python_tool_id}",
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
            "tag_names": [],
        },
    )
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" not in only_tag_names
    assert "web" not in only_tag_names

    # get tool python
    response = client.get(
        f"/v1/tool/{python_tool_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == python_tool_id
    assert response.json()["name"] == "python"
    assert response.json()["description"] == "python tool"
    assert response.json()["image_url"] == "https://www.python.org/static/img/python-logo@2x.png"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://www.python.org/"
    assert response.json()["github_url"] == "https://github.com/python/cpython"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" not in only_tag_names
    assert "web" not in only_tag_names

    # create tool pynecone
    response = client.post(
        "/v1/admin/tool",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "pynecone",
            "description": "pynecone tool",
            "image_url": "https://",
            "is_open_source": True,
            "site_url": "https://",
            "github_url": "https://",
            "tag_names": ["framework", "language", "web"],
            "tool_names": ["python", "node.js"],
        },
    )
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json()["name"] == "pynecone"
    assert response.json()["description"] == "pynecone tool"
    assert response.json()["image_url"] == "https://"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://"
    assert response.json()["github_url"] == "https://"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" in only_tag_names
    assert "language" in only_tag_names
    assert "web" in only_tag_names
    tools = response.json()["tools"]
    only_tool_names = [tool["name"] for tool in tools]
    assert "python" in only_tool_names
    assert "node.js" in only_tool_names
    tool_pynecone_id = response.json()["id"]

    # get tool pynecone
    response = client.get(
        f"/v1/tool/{tool_pynecone_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == tool_pynecone_id
    assert response.json()["name"] == "pynecone"
    assert response.json()["description"] == "pynecone tool"
    assert response.json()["image_url"] == "https://"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://"
    assert response.json()["github_url"] == "https://"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" in only_tag_names
    assert "language" in only_tag_names
    assert "web" in only_tag_names
    tools = response.json()["tools"]
    only_tool_names = [tool["name"] for tool in tools]
    assert "python" in only_tool_names
    assert "node.js" in only_tool_names

    # patch tool pynecone with tag
    response = client.patch(
        f"/v1/admin/tool/{tool_pynecone_id}",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "pynecone",
            "description": "pynecone tool",
            "image_url": "https://",
            "is_open_source": True,
            "site_url": "https://",
            "github_url": "https://",
            "tag_names": ["language", "web"],
            "tool_names": ["python"],
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == tool_pynecone_id
    assert response.json()["name"] == "pynecone"
    assert response.json()["description"] == "pynecone tool"
    assert response.json()["image_url"] == "https://"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://"
    assert response.json()["github_url"] == "https://"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" in only_tag_names
    assert "web" in only_tag_names
    tools = response.json()["tools"]
    only_tool_names = [tool["name"] for tool in tools]
    assert "python" in only_tool_names
    assert "node.js" not in only_tool_names

    # get tool pynecone
    response = client.get(
        f"/v1/tool/{tool_pynecone_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == tool_pynecone_id
    assert response.json()["name"] == "pynecone"
    assert response.json()["description"] == "pynecone tool"
    assert response.json()["image_url"] == "https://"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://"
    assert response.json()["github_url"] == "https://"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" in only_tag_names
    assert "web" in only_tag_names
    tools = response.json()["tools"]
    only_tool_names = [tool["name"] for tool in tools]
    assert "python" in only_tool_names
    assert "node.js" not in only_tool_names

    # patch tool pynecone with tag
    response = client.patch(
        f"/v1/admin/tool/{tool_pynecone_id}",
        headers={
            "Authorization": super_user_bearer_token,
        },
        json={
            "name": "pynecone",
            "description": "pynecone tool",
            "image_url": "https://",
            "is_open_source": True,
            "site_url": "https://",
            "github_url": "https://",
            "tag_names": [],
            "tool_names": [],
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == tool_pynecone_id
    assert response.json()["name"] == "pynecone"
    assert response.json()["description"] == "pynecone tool"
    assert response.json()["image_url"] == "https://"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://"
    assert response.json()["github_url"] == "https://"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" not in only_tag_names
    assert "web" not in only_tag_names
    tools = response.json()["tools"]
    only_tool_names = [tool["name"] for tool in tools]
    assert "python" not in only_tool_names
    assert "node.js" not in only_tool_names

    # get tool pynecone
    response = client.get(
        f"/v1/tool/{tool_pynecone_id}",
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["id"] == tool_pynecone_id
    assert response.json()["name"] == "pynecone"
    assert response.json()["description"] == "pynecone tool"
    assert response.json()["image_url"] == "https://"
    assert response.json()["is_open_source"] is True
    assert response.json()["site_url"] == "https://"
    assert response.json()["github_url"] == "https://"
    tags = response.json()["tags"]
    only_tag_names = [tag["name"] for tag in tags]
    assert "framework" not in only_tag_names
    assert "language" not in only_tag_names
    assert "web" not in only_tag_names
    tools = response.json()["tools"]
    only_tool_names = [tool["name"] for tool in tools]
    assert "python" not in only_tool_names
    assert "node.js" not in only_tool_names