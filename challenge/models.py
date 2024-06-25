from datetime import datetime
from typing import Self
from uuid import UUID

import pytz
from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    status: str
    role: str
    last_activity: int


class UserList(BaseModel):
    users: list[User]


class FormattedUser(BaseModel):
    id: UUID | None
    email: EmailStr
    lastActivity: str | None

    @staticmethod
    def obfuscate_email(email: EmailStr) -> EmailStr:
        min_alias_length = 4
        alias, domain = email.split('@')
        if domain == 'niuco.com.br':
            return email
        if len(alias) <= min_alias_length:
            return email
        masked_alias = f"{alias[0:2]}{'*' * (len(alias) - 4)}{alias[-2:]}"
        return f'{masked_alias}@{domain}'

    @classmethod
    def from_user(cls, user: User) -> Self:
        email = cls.obfuscate_email(user.email)
        lastActivity = datetime.fromtimestamp(
            user.last_activity, pytz.utc
        ).isoformat()
        return cls(id=user.id, email=email, lastActivity=lastActivity)


class FormattedUserList(BaseModel):
    users: list[FormattedUser]
