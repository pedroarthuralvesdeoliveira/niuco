from pydantic import BaseSettings, Field
from pydantic_settings import SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )

    api_url: str = Field(..., env='API_URL')

settings = Settings()
