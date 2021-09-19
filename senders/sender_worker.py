from celery_app import app
from notificators.email import EmailNotificator


@app.task(name="send_email", acks_late=True)
def send_email(to: any, data: any):
    EmailNotificator(to, data).send()
