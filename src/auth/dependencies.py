from sqlalchemy.ext.asyncio import AsyncSession

from fastapi import Depends
from fastapi_users.db import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import SQLAlchemyAccessTokenDatabase

from src.core.database import get_db
from src.auth.model import User, AccessToken


async def get_user_db(session: AsyncSession = Depends(get_db)):
    """ 获取用户数据库连接 """
    yield SQLAlchemyUserDatabase(session, User)

async def get_access_token_db(session: AsyncSession = Depends(get_db)):
    """ 获取访问令牌数据库依赖 """
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)