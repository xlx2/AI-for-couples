from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthSettings(BaseSettings):
    """ 用户认证模块专用配置 """
    # JWT 配置
    jwt_secret: str = "CHANGE_ME"

    model_config = SettingsConfigDict(
        env_file='.env', 
        env_file_encoding='utf-8',
        case_sensitive=False
        )
    
auth_settings = AuthSettings()