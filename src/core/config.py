from functools import lru_cache
from typing import Literal
from pydantic import computed_field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """ 应用配置（支持 PostgreSQL 和 SQLite，含连接池设置） """

    app_name: str = "AI for Couples"
    debug: bool = False

    # 数据库类型
    db_type: Literal["postgres", "sqlite"] = "sqlite"

    # PostgreSQL 配置
    db_host: str = "localhost"
    db_port: int = 5432
    db_user: str = "postgres"
    db_password: str = "postgres"
    db_name: str = "aiforcouples"

    # 连接池配置（PostgreSQL 有效）
    # --- 必选参数：中等并发常用 ---
    pool_size: int = 20            # 连接池基础大小，低：- 高：+
    max_overflow: int = 10         # 超出 pool_size 的最大连接数，低：- 高：+
    pool_timeout:int = 30          # 连接超时时间（秒），低：+ 高：-
    pool_pre_ping: bool = True     # 获取连接前是否检查可用性，低：False 高：True

    # --- 可选调优参数（高级场景） ---
    pool_recycle:int = 3600        # 连接最大存活时间（秒），低：+ 高：-，避免长连接数据库踢掉
    pool_use_lifo:bool = False     # 连接池取连接顺序，False=FIFO（默认），True=LIFO 可提高高并发命中率
    echo:bool = False              # 是否打印 SQL，开发可打开，生产关闭

    # SQLite 配置
    sqlite_db_path: str = "./data/aiforcouples.sqlite3"

    @computed_field
    @property
    def database_url(self) -> str:
        """ 返回对应数据库类型的 URL """
        if self.db_type == "postgres":
            return (
                f"postgresql+asyncpg://{self.db_user}:{self.db_password}"
                f"@{self.db_host}:{self.db_port}/{self.db_name}"
                )
        elif self.db_type == "sqlite":
            return f"sqlite+aiosqlite:///{self.sqlite_db_path}"
        else:
            raise ValueError(f"Unsupported DB_TYPE: {self.db_type}")
    
    @computed_field
    @property
    def engine_options(self) -> dict:
        """ 统一封装 engine options，供 create_async_engine 使用 """
        if self.db_type == "postgres":
            return {
                "pool_size": self.pool_size,
                "max_overflow": self.max_overflow,
                "pool_timeout": self.pool_timeout,
                "pool_recycle": self.pool_recycle,
                "pool_use_lifo": self.pool_use_lifo,
                "echo": self.echo
            }
        elif self.db_type == "sqlite":
            return {"echo": self.echo}
        else:
            raise ValueError(f"Unsupported DB_TYPE: {self.db_type}")
    
    # JWT 配置
    jwt_secret: str = "jowfeofi2039fj002bug03j2j230ffj903fj0egr93jfn"

    modelmodel_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='utf-8',
        case_sensitive=False
        )

settings = Settings()