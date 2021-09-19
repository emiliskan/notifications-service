from celery import Celery

import config
from notificators import email_notificator

app = Celery("senders", broker=config.CELERY_BROKER_URL)


@app.task(name="email", acks_late=True)
def send_email(**kwargs):
    email_notificator.send(**kwargs)


if __name__ == "__main__":
    app.start()
