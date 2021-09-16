import os
from logging import config as logging_config

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)

PROJECT_NAME = os.getenv("PROJECT_NAME", "notifier")

BACKOFF_FACTOR = float(os.getenv("BACKOFF_FACTOR", 0.5))
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "strong_secret")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "bitnami")
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "pyamqp://user:bitnami@localhost//")
