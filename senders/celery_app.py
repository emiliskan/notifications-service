import os

from celery import Celery
import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')

app = Celery('senders', broker=config.CELERY_BROKER_URL)

if __name__ == '__main__':
    app.start()
