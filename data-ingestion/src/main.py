# src/main.py
from fastapi import FastAPI
from contextlib import asynccontextmanager
from routers.reading_router import ReadingRouter
from config.database import create_db_and_tables, get_db
from services.reading_service import ReadingService
from datetime import datetime
from utils.utils import logger


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    Application lifespan event to initialize resources.
    """
    logger.info("Starting application...")
    db_client = get_db()
    create_db_and_tables()
    reading_service = ReadingService(db_client)
    logger.info("Application started successfully.")
    yield {"reading_service": reading_service}


app = FastAPI(
    title="Sensor Data API",
    description="A FastAPI project to receive sensor data.",
    version="0.0.1",
)


app.include_router(ReadingRouter)


@app.get("/", tags=["Root"])
def read_root():
    return {"status": "API is running!"}


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "Healthy", "timestamp": datetime.now().isoformat()}
