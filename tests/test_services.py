import pytest
from uuid import UUID
from fastapi import HTTPException
from challenge.services import get_users, get_user, get_formatted_users, get_formatted_user
from challenge.models import User, FormattedUser

@pytest.mark.asyncio
async def test_get_users(mocker):
    mocker.patch('challenge.services.get_users', return_value=[
        User(
            id="0373e634-2d03-457e-a24d-2b0c8c3b7c37",
            name="John Doe",
            email="john.doe@example.com",
            last_activity=1622499200,
            role="admin",
            status="enabled"
        )
    ])

    users = await get_users()
    assert isinstance(users, list)
    assert all(isinstance(user, User) for user in users)

@pytest.mark.asyncio
async def test_get_user(mocker):
    user_id = UUID("some-valid-uuid")
    mocker.patch('challenge.services.get_user', return_value=User(
        id=user_id,
        name="John Doe",
        email="john.doe@example.com",
        last_activity=1622499200,
        role="admin",
        status="enabled"
    ))

    user = await get_user(user_id)
    assert isinstance(user, User)

@pytest.mark.asyncio
async def test_get_user_not_found(mocker):
    user_id = UUID("non-existent-uuid")
    mocker.patch('challenge.services.get_user', side_effect=HTTPException(status_code=404, detail="User not found"))

    with pytest.raises(HTTPException) as exc_info:
        await get_user(user_id)
    assert exc_info.value.status_code == 404

@pytest.mark.asyncio
async def test_get_formatted_users(mocker):
    mocker.patch('challenge.services.get_formatted_users', return_value=[
        FormattedUser(
            id="0373e634-2d03-457e-a24d-2b0c8c3b7c37",
            email="jo****oe@example.com",
            last_activity="2021-06-01T00:00:00Z",
        )
    ])

    formatted_users = await get_formatted_users()
    assert isinstance(formatted_users, list)
    assert all(isinstance(user, FormattedUser) for user in formatted_users)

@pytest.mark.asyncio
async def test_get_formatted_user(mocker):
    user_id = UUID("0373e634-2d03-457e-a24d-2b0c8c3b7c37")
    mocker.patch('challenge.services.get_formatted_user', return_value=FormattedUser(
        id=user_id,
        email="jo****oe@example.com",
        last_activity="2021-06-01T00:00:00Z",
    ))

    formatted_user = await get_formatted_user(user_id)
    assert isinstance(formatted_user, FormattedUser)
