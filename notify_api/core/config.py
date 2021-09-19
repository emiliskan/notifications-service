import os
from logging import config as logging_config

from core.logger import LOGGING

logging_config.dictConfig(LOGGING)

PROJECT_NAME = os.getenv("PROJECT_NAME", "notifier")

RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "bitnami")
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "pyamqp://user:bitnami@localhost//")
