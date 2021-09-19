import os

from celery import Celery
from config import CELERY_BROKER_URL


app = Celery('senders', broker=CELERY_BROKER_URL)
