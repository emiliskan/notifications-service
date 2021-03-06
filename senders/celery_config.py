import os
import pathlib

import logging.config as logging_config

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

AUTH_SERVICE = os.environ.get("AUTH_SERVICE", 'auth-api')
UGA_SERVICE = os.environ.get("UGA_SERVICE", 'uga-api')

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')

POSTGRES_DB = os.environ.get('POSTGRES_DB', 'postgres')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', "localhost")
POSTGRES_USER = os.environ.get('POSTGRES_USER', 'postgres')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT', 5432)
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')

POSTGRES_DB_URL = f"{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
POSTGRES_URI = f'postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_DB_URL}'

DEBUG = os.environ.get('DEBUG', False)

LOGGER_CONFIG = pathlib.Path(__file__).parent / 'logging.conf'
LOGGER_NAME = 'senders'
logging_config.fileConfig(LOGGER_CONFIG)
