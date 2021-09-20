import os

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "pyamqp://guest:guest@localhost//")
BD_DSN = {
    "dbname": os.environ.get("POSTGRES_DB", "notify"),
    "user": os.environ.get("POSTGRES_USER", "postgres"),
    "password": os.environ.get("POSTGRES_PASSWORD", "password"),
    "host": os.environ.get("POSTGRES_HOST", "localhost"),
    "port": os.environ.get("POSTGRES_PORT", 5432)
}

TEMPLATES = os.environ.get("TEMPLATE_TABLE", 'template_table')
HISTORY = os.environ.get("HISTORY_TABLE", 'message_history')
