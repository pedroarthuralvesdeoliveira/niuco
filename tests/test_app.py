
import pytest
from fastapi.testclient import TestClient

from challenge.app import app

client = TestClient(app)


@pytest.mark.asyncio()
async def test_get_users(mocker):
    mocker.patch('challenge.services.get_users', return_value=[
        {
            "id": "some-valid-uuid",
            "name": "John Doe",
            "email": "john.doe@example.com",
            "last_activity": 1622499200,
            "role": "admin",
            "status": "enabled"
        }
    ])

    response = client.get("/users/")
    assert response.status_code == 200
    data = response.json()
    assert "users" in data
    assert isinstance(data["users"], list)
    assert len(data["users"]) > 0


@pytest.mark.asyncio()
async def test_get_user(mocker):
    user_id = "some-valid-uuid"
    mocker.patch('challenge.services.get_user', return_value={
        "id": user_id,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "last_activity": 1622499200,
        "role": "admin",
        "status": "enabled"
    })

    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id


@pytest.mark.asyncio()
async def test_get_formatted_users(mocker):
    mocker.patch('challenge.services.get_formatted_users', return_value=[
        {
            "id": "some-valid-uuid",
            "email": "jo****oe@example.com",
            "last_activity": "2021-06-01T00:00:00Z",
        }
    ])

    response = client.get("/formattedUsers/")
    assert response.status_code == 200
    data = response.json()
    assert "formattedUsers" in data
    assert isinstance(data["formattedUsers"], list)
    assert len(data["formattedUsers"]) > 0


@pytest.mark.asyncio()
async def test_get_formatted_user(mocker):
    user_id = "some-valid-uuid"
    mocker.patch('challenge.services.get_formatted_user', return_value={
        "id": user_id,
        "email": "jo****oe@example.com",
        "last_activity": "2021-06-01T00:00:00Z"
    })

    response = client.get(f"/formattedUsers/{user_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == user_id
