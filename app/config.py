from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str
    env_name: str
    base_url: str

    class Config:
        env_file = ".env"