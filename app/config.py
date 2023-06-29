from functools import lru_cache
from pydantic import BaseSettings
from dotenv import dotenv_values

config = dotenv_values("app/.env")

class Settings(BaseSettings):
    app_name: str = config.get("APP_NAME")
    app_version: str = config.get("APP_VERSION")
    env_name: str = config.get("ENV_NAME")
    base_url: str = config.get("BASE_URL")
    origins : list[str] = config.get("ALLOWED_ORIGINS").split(",")

@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    return settings
