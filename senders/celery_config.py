import os

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "pyamqp://guest:guest@localhost//")
BD_DSN = {
    "dbname": os.environ.get("POSTGRES_DB", "notify"),
    "user": os.environ.get("POSTGRES_USER", "postgres"),
    "password": os.environ.get("POSTGRES_PASSWORD", "password"),
    "host": os.environ.get("POSTGRES_HOST", "localhost"),
    "port": os.environ.get("POSTGRES_PORT", 5432)
}

TEMPLATES = os.environ.get("TEMPLATE_TABLE", 'message_template')
HISTORY = os.environ.get("HISTORY_TABLE", 'message_history')
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')