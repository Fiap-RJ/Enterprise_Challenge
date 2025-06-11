# src/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.reading_router import ReadingRouter
from config.database import get_db
from services.reading_service import ReadingService
from repositories.sqlite_reading_repository import SQLiteReadingRepository
from repositories.postgres_reading_repository import PostgresReadingRepository
from datetime import datetime
from utils.utils import logger
from config.settings import app_settings


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    Application lifespan event to initialize resources.
    """
    logger.info("Starting application...")
    repositories = {
        "sqlite": SQLiteReadingRepository,
        "postgres": PostgresReadingRepository,
    }
    db_type = app_settings.db_type

    if db_type not in repositories:
        raise ValueError(f"Unsupported DB_TYPE: {db_type}")

    db_client = get_db(db_type)

    reading_repository = repositories[db_type](db_client)

    reading_service = ReadingService(reading_repository)
    logger.info("Application started successfully.")
    yield {"reading_service": reading_service}


app = FastAPI(
    title="Sensor Data API",
    description="A FastAPI project to receive sensor data.",
    version="0.0.1",
    lifespan=lifespan,
)


app.include_router(ReadingRouter)


@app.get("/", tags=["Root"])
def read_root():
    return {"status": "API is running!"}


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "Healthy", "timestamp": datetime.now().isoformat()}
