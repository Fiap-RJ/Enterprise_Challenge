# src/config/database.py
import sqlite3
from utils.utils import logger

DATABASE_FILE = "sensors.db"


def create_db_and_tables():
    """Function to create the database and the required tables if they do not exist."""
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS leituras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            temperature_c REAL NOT NULL,
            humidity_pct REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    logger.info("Database and tables created successfully.")
    conn.commit()
    conn.close()


def get_db():
    """
    Function to get a database connection.
    """
    db = sqlite3.connect(DATABASE_FILE)
    logger.debug("Connecting to the database at %s", DATABASE_FILE)

    # Set row factory to return rows as dictionaries
    db.row_factory = sqlite3.Row
    try:
        yield db
    finally:
        db.close()
