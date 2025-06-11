# src/config/settings.py
from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class ApplicationSettings(BaseSettings):
    app_name: str = Field(default="Enterprise Challenge")
    environment: str = Field(default="local")
    db_type: str = Field(default="sqlite")

    sqlite_db_file: str = Field(default="sensor_data.db")

    postgres_user: str = Field(default="")
    postgres_password: str = Field(default="")
    postgres_host: str = Field(default="")
    postgres_port: int = Field(default=5432)
    postgres_db_name: str = Field(default="")


app_settings = ApplicationSettings()
