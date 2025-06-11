# src/config/settings.py
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class ApplicationSettings(BaseSettings):
    model_config = {
        "env_file": str(BASE_DIR / ".env"),
        "env_file_encoding": "utf-8",
        "case_sensitive": False,
        "extra": "allow",
    }
    app_name: str = Field(default="Enterprise Challenge")
    environment: str = Field(default="local")
    db_type: str = Field(default="postgres")

    sqlite_db_file: str = Field(default="sensor_data.db")

    postgres_user: str = Field(default="")
    postgres_password: str = Field(default="")
    postgres_host: str = Field(default="")
    postgres_port: int = Field(default=5432)
    postgres_db_name: str = Field(default="")


app_settings = ApplicationSettings()
