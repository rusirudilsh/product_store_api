from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str
    app_version: str
    env_name: str
    base_url: str
    allowed_origins: str

    class Config:
         env_file = "app/.env"

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
