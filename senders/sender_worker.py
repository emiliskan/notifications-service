from celery_app import app
from notificators.email import email_notificator


@app.task(name="email", acks_late=True)
def send_email(**kwargs):
    email_notificator.send(**kwargs)
