from functools import lru_cache
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str
    env_name: str
    base_url: str
    origins = list[str]

    class Config:
        env_file = ".env"

    @lru_cache()
    def get_settings():
        return Settings()