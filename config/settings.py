import os
from functools import lru_cache

from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    # database config
    db_name: str = Field(..., env='POSTGRES_DB')
    db_user: str = Field(..., env='POSTGRES_USER')
    db_pass: str = Field(..., env='POSTGRES_PASSWORD')
    db_host: str = Field(..., env='POSTGRES_HOST')
    db_port: int = Field(..., env='POSTGRES_PORT')

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    class Config:
        env_file = './config/.env'


@lru_cache()
def get_settings() -> Settings:
    return Settings()
