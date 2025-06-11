# src/repositories/interfaces/reading_repository_interface.py
from abc import ABC, abstractmethod
from schemas.reading_schema import ReadingSchema

class IReadingRepository(ABC):

    @abstractmethod
    def save(self, reading_data: ReadingSchema) -> int:
        """Saves a new reading to the database."""
        pass
