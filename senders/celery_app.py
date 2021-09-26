from celery import Celery
from .celery_config import CELERY_BROKER_URL, POSTGRES_URI

app = Celery('senders', broker=CELERY_BROKER_URL)

app.conf.update(
    {'beat_dburi': POSTGRES_URI}
)