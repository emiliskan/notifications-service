from celery import Celery
from core import config

app = Celery('proj', broker=config.CELERY_BROKER_URL)


if __name__ == '__main__':
    app.start()
