from celery_app import app
from senders.notificators.email import EmailNotificator


@app.task(name="send_email", acks_late=True)
def send_email(to: any, data: any):
    EmailNotificator(to, data).send()
