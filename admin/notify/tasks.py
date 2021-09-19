from notify.celery import app
from notify.notificators.email import email_notificator


@app.task(name="email", acks_late=True)
def send_email(**kwargs):
    email_notificator.send(**kwargs)
