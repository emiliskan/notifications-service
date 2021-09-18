from celery import Celery

import config

app = Celery("senders", broker=config.CELERY_BROKER_URL)

if __name__ == "__main__":
    app.start()
