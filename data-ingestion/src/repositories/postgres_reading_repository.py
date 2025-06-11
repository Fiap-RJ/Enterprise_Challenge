# src/repositories/postgres_reading_repository.py
import psycopg2
from psycopg2.extensions import connection
from schemas.reading_schema import ReadingSchema
from utils.utils import logger
from repositories.interfaces.reading_repository_interface import IReadingRepository

class PostgresReadingRepository(IReadingRepository):
    def __init__(self, db: connection):
        self.db = db
        self._initialize()

    def _initialize(self):
        try:
            with self.db.cursor() as cursor:
                logger.debug("Initializing PostgreSQL database and tables...")
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS readings (
                        id SERIAL PRIMARY KEY,
                        temperature_c REAL NOT NULL,
                        humidity_pct REAL NOT NULL,
                        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                """)
                self.db.commit()
                logger.info("PostgreSQL tables initialized successfully.")
        except psycopg2.Error as e:
            logger.error("Error initializing PostgreSQL database: %s", e)
            self.db.rollback()
            raise

    def save(self, reading_data: ReadingSchema) -> int:
        try:
            logger.debug("[PostgresRepository] Saving reading: Temp=%s, Humidity=%s",
                         reading_data.temperature_c, reading_data.humidity_pct)
            with self.db.cursor() as cursor:
                sql = "INSERT INTO readings (temperature_c, humidity_pct) VALUES (%s, %s) RETURNING id"
                cursor.execute(sql, (reading_data.temperature_c, reading_data.humidity_pct))
                reading_id = cursor.fetchone()[0]
                self.db.commit()
                return reading_id
        except psycopg2.Error as e:
            logger.error("[PostgresRepository] Error saving reading: %s", e)
            self.db.rollback()
            raise
