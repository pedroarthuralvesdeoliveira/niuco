from uuid import UUID

from fastapi import FastAPI

from challenge.models import FormattedUser, FormattedUserList, User, UserList
from challenge.services import (
  get_formatted_user,
  get_formatted_users,
  get_user,
  get_users,
)

app = FastAPI()


@app.get('/users/', response_model=UserList)
async def users():
  users = await get_users() 
  return {"users": users}


@app.get('/users/{user_id}', response_model=User)
async def user(user_id: UUID):
  user = await get_user(user_id)
  return {"formattedUser": user}


@app.get('/formattedUsers/', response_model=FormattedUserList)
async def formattedUsers():
  users = await get_formatted_users()
  return {"formattedUsers": users}


@app.get('/formattedUsers/{user_id}', response_model=FormattedUser)
async def formattedUser(user_id: UUID):
  return await get_formatted_user(user_id)
