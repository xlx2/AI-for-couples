import uuid
from datetime import datetime
from pydantic import Field
from fastapi_users import schemas


class UserRead(schemas.BaseUser[uuid.UUID]):
    name: str = Field(None, max_length=64)
    created_at: datetime
    updated_at: datetime


class UserCreate(schemas.BaseUserCreate):
    pass


class UserUpdate(schemas.BaseUserUpdate):
    name: str | None = Field(None, max_length=64)