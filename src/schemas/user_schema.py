from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field


class UserResponse(BaseModel):
    id: Union[str, UUID] = Field(None, alias='id')
    user_name: str = Field(None, alias='user_name')
    email: str = Field(None, alias='email')
    password: str = Field(None, alias='password')
    phone_number: str = Field(None, alias='phone_number')
    is_admin: bool = Field(None, alias='is_admin')

    class Config:
        orm_mode = True


class UserCreate(UserResponse):
    pass


class UserUpdate(UserResponse):
    class Config:
        fields = {
            "id": {"exclude": True},
        }
