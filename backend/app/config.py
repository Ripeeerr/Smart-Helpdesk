from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL

BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    postgres_password: str
    postgres_user: str
    postgres_db: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def database_url(self):
        database_url = URL.create(
            "postgresql+psycopg",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db,
        )
        return database_url


settings = Settings()
