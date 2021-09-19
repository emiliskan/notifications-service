from celery import Celery
from config import CELERY_BROKER_URL

app = Celery('senders', broker=CELERY_BROKER_URL)

beat_dburi = 'postgresql+psycopg2://postgres:postgres@notify_db:5432/postgres'

app.conf.update(
    {'beat_dburi': beat_dburi}
)
