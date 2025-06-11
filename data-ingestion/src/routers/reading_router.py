# src/routers/reading_router.py
from fastapi import APIRouter, Depends, HTTPException, Request
from typing import Annotated
from services.reading_service import ReadingService
from schemas.reading_schema import ReadingSchema
from utils.utils import logger

ReadingRouter = APIRouter(prefix="/sensors", tags=["Sensors"])


def get_service(request: Request) -> ReadingService:
    """
    Dependency to get the ReadingService instance.
    """
    return request.state.reading_service


@ReadingRouter.post("/data", status_code=201, summary="Receive sensor data")
def receive_data(
    reading: ReadingSchema,
    reading_service: Annotated[ReadingService, Depends(get_service)],
):
    """
    Endpoint to receive temperature and humidity data and save it using raw SQL.
    """
    logger.debug("[Router] Received sensor data: %s", reading)
    try:
        result = reading_service.create_reading(reading)
        return result
    except Exception as e:
        logger.error("[Router] Error processing sensor data: %s", e)
        raise HTTPException(
            status_code=500, detail="Internal server error while processing data."
        )
