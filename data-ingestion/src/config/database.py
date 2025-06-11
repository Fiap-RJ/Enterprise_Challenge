# src/config/database.py
import os
import sqlite3
import psycopg2
from contextlib import contextmanager
from utils.utils import logger
from config.settings import app_settings

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
SQLITE_DATABASE_FILE = os.path.join(CURRENT_DIR, app_settings.sqlite_db_file)


def get_sqlite_connection():
    db = sqlite3.connect(SQLITE_DATABASE_FILE, check_same_thread=False)
    db.row_factory = sqlite3.Row
    logger.debug(f"Connected to SQLite database at {SQLITE_DATABASE_FILE}")
    return db


def get_postgres_connection():
    conn = psycopg2.connect(
        dbname=app_settings.postgres_db_name,
        user=app_settings.postgres_user,
        password=app_settings.postgres_password,
        host=app_settings.postgres_host,
        port=app_settings.postgres_port,
    )
    logger.debug("Connected to PostgreSQL database.")
    return conn


def get_db(db_type: str):
    """
    Factory function to get the appropriate database connection based on the DB_TYPE.
    """
    if db_type == "sqlite":
        return get_sqlite_connection()
    elif db_type == "postgres":
        return get_postgres_connection()
    else:
        raise ValueError(f"Unsupported DB_TYPE {app_settings.db_type}")
