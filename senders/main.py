
from celery import Task

from senders.models import Notification
from senders.notificators.email import MockSender
from senders.services.ugc import UGCUnavailable, UGCServiceMock

from senders.services.auth import AuthUnavailable, AuthServiceMock
from senders.notificators.exceptions import GetMetadata

from senders.alerts import TopMoviesAlert
from senders.db import connect_to_db
from senders.celery_app import app
from senders.celery_config import BD_DSN, TEMPLATES, HISTORY
from senders.notificators import EmailNotificator, SMSNotificator, SendGrid


connection = connect_to_db(BD_DSN)


email_sender = MockSender()
email_notificator = EmailNotificator(connection, HISTORY, TEMPLATES, email_sender)

sms_notificator = SMSNotificator(connection, HISTORY, TEMPLATES)

auth_service = AuthServiceMock()
ugc_service = UGCServiceMock()
top_movies_alert = TopMoviesAlert("top_movies", ["email"], auth_service, ugc_service)


class BaseTaskWithRetry(Task):
    """ Handle connection errors."""

    autoretry_for = (GetMetadata, UGCUnavailable, AuthUnavailable)
    retry_kwargs = {'max_retries': 3}
    retry_backoff = True


@app.task(name="top_movies", bind=True, base=BaseTaskWithRetry)
def send_top_movies(self):
    top_movies_alert.send()


@app.task(name="email", bind=True, base=BaseTaskWithRetry)
def send_email(self, **kwargs):
    email_notificator.send(Notification(**kwargs))


@app.task(name="sms", bind=True, base=BaseTaskWithRetry)
def send_sms(self, **kwargs):
    sms_notificator.send(**kwargs)


if __name__ == "__main__":
    app.start()
