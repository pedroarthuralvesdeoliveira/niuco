from uuid import UUID

import httpx
from fastapi import HTTPException

from challenge.config import settings
from challenge.models import FormattedUser, User


async def get_users():
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{settings.api_url}/users')
        response.raise_for_status()
        return [User(**user_data) for user_data in response.json()]


async def get_user(id: UUID) -> User:
    async with httpx.AsyncClient() as client:
        response = await client.get(f'{settings.api_url}/users/{id}')
        response.raise_for_status()
        user_data = response.json()
        if user_data is None:
            raise HTTPException(status_code=404, detail='User not found')
        return User(**user_data)


async def get_formatted_users():
    users = await get_users()
    formatted_users = [FormattedUser.from_user(user) for user in users]
    return [user.model_dump() for user in formatted_users]


async def get_formatted_user(id: UUID):
    user = await get_user(id)
    formatted_user: FormattedUser = FormattedUser.from_user(user)
    return formatted_user.model_dump()
