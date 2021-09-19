from celery import Celery

import db
from config import CELERY_BROKER_URL, BD_DSN, TEMPLATES, HISTORY
from notificators import EmailNotificator, SMSNotificator

# TODO close db connection
app = Celery("senders", broker=CELERY_BROKER_URL)
db.connection = db.connect_to_db(BD_DSN)

email_notificator = EmailNotificator(db.connection, HISTORY, TEMPLATES)
sms_notificator = SMSNotificator(db.connection, HISTORY, TEMPLATES)


@app.task(name="email", acks_late=True)
def send_email(**kwargs):
    email_notificator.send(**kwargs)


@app.task(name="sms", acks_late=True)
def send_sms(**kwargs):
    sms_notificator.send(**kwargs)


if __name__ == "__main__":
    app.start()
