import psycopg2
from psycopg2 import sql
from flask import current_app

def get_db_connection():
    """Establishes a connection to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname=current_app.config['DB_NAME'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            host=current_app.config['DB_HOST']
        )
        return conn
    except Exception as e:
        print(f"Database connection error: {e}")
        return None
