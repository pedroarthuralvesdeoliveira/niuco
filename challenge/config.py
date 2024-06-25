# from pydantic import Field
# from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
#


# settings = Settings()
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=..., env_file_encoding='utf-8')
    api_url: str = Field(..., env='API_URL')


settings = Settings()
