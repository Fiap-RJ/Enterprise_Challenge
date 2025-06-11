# src/repositories/reading_repository.py
import sqlite3
from typing import Dict
from utils.utils import logger
from schemas.reading_schema import ReadingSchema


class ReadingRepository:
    def __init__(self, db: sqlite3.Connection):
        """
        Initializes the ReadingRepository with a database connection.

        Args:
            db (sqlite3.Connection): The database connection.
        """
        self.db = db

    def save(self, reading_data: ReadingSchema) -> int:
        """
        Saves a new reading to the database using raw SQL.

        Args:
            db (sqlite3.Connection): The database connection.
            reading_data (Dict): A dictionary containing 'temperature' and 'humidity'.

        Returns:
            int: The ID of the newly inserted record.
        """
        try:
            logger.debug(
                "[Repository] Saving reading: Temp=%s, Humidity=%s",
                reading_data.temperatura,
                reading_data.umidade,
            )
            cursor = self.db.cursor()
            sql = "INSERT INTO readings (temperature_c, humidity_pct) VALUES (?, ?)"

            cursor.execute(sql, (reading_data.temperatura, reading_data.umidade))

            self.db.commit()
        except sqlite3.Error as e:
            self.db.rollback()
            logger.error("[Repository] Error saving reading: %s", e)
            raise
        return cursor.lastrowid
