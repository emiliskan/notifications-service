import psycopg2
from psycopg2.extensions import connection as pg_conn
from psycopg2.extras import DictCursor

connection = None


def connect_to_db(dsn: dict) -> pg_conn:
    return psycopg2.connect(**dsn, cursor_factory=DictCursor)


def get_db_connection() -> pg_conn:
    return connection
