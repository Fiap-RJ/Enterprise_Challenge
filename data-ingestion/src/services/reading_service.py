# src/services/reading_service.py
from typing import Dict
from repositories.reading_repository import ReadingRepository
from schemas.reading_schema import ReadingSchema
from utils.utils import logger


class ReadingService:
    def __init__(self, repository: ReadingRepository):
        self.repository = repository

    def create_reading(self, reading_data: ReadingSchema) -> Dict:
        """
        Processes and saves a new sensor reading.

        Args:
            db (sqlite3.Connection): The database connection.
            reading_data (Dict): The sensor reading data.

        Returns:
            Dict: A dictionary with a success message and the record ID.
        """
        logger.debug(
            "[Service] Creating a new sensor reading with data: %s", reading_data
        )

        reading_id = self.repository.save(reading_data)

        return {"id": reading_id}
