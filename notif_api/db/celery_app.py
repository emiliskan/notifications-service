from celery import Celery
from core import config

app = Celery('senders', broker=config.CELERY_BROKER_URL)
