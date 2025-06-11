# src/repositories/sqlite_reading_repository.py
import sqlite3
from schemas.reading_schema import ReadingSchema
from utils.utils import logger
from repositories.interfaces.reading_repository_interface import IReadingRepository


class SQLiteReadingRepository(IReadingRepository):
    def __init__(self, db: sqlite3.Connection):
        self.db = db
        self._initialize()

    def _initialize(self):
        try:
            with self.db as conn:
                cursor = conn.cursor()
                logger.debug("Initializing database and tables...")
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS readings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        temperature_c REAL NOT NULL,
                        humidity_pct REAL NOT NULL,
                        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                conn.commit()
                logger.info("Database and tables created successfully.")
        except sqlite3.Error as e:
            logger.error("Error initializing database: %s", e)
            raise

    def save(self, reading_data: ReadingSchema) -> int:
        try:
            logger.debug(
                "[SQLiteRepository] Saving reading: Temp=%s, Humidity=%s",
                reading_data.temperature_c,
                reading_data.humidity_pct,
            )
            with self.db as conn:
                cursor = conn.cursor()
                sql = "INSERT INTO readings (temperature_c, humidity_pct) VALUES (?, ?)"
                cursor.execute(
                    sql, (reading_data.temperature_c, reading_data.humidity_pct)
                )
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            logger.error("[SQLiteRepository] Error saving reading: %s", e)
            raise
