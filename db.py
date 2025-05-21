import psycopg2
from psycopg2.extras import RealDictCursor
from psycopg2 import sql
from config import DB_CONF


# establish a connection to the db
def get_connection():
    """
    Establishes a connection to the PostgreSQL database using the provided configuration.

    Returns:
        conn: A connection object to the PostgreSQL database.
    """

    try:
        conn = psycopg2.connect(**DB_CONF)
        print("Library platform db connected successfully...")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
