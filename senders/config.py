import os

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "pyamqp://user:bitnami@localhost//")
