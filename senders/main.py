from requests.exceptions import ConnectionError

from celery import Celery, Task
from psycopg2 import OperationalError

from .alerts import TopMoviesAlert
from .db import connect_to_db
from .celery_app import app
from .celery_config import BD_DSN, TEMPLATES, HISTORY, DEBUG
from .notificators import (EmailNotificator, SMSNotificator, SendGrid,
                           MockNotificator, MockSender,)


connection = connect_to_db(BD_DSN)

email_sender = SendGrid()
email_notificator = EmailNotificator(connection, HISTORY, TEMPLATES, email_sender)

sms_sender = MockSender()
sms_notificator = SMSNotificator(connection, HISTORY, TEMPLATES, sms_sender)

top_movies_alert = TopMoviesAlert("top_movies", ["email"])


class BaseTaskWithRetry(Task):
    """ Handle connection errors."""

    autoretry_for = (ConnectionError, OperationalError)
    retry_kwargs = {'max_retries': 5}
    retry_backoff = True


@app.task(name="top_movies", acks_late=True, bind=True, base=BaseTaskWithRetry)
def send_top_movies(self):
    top_movies_alert.send()


@app.task(name="email", acks_late=True, bind=True, base=BaseTaskWithRetry)
def send_email(self, **kwargs):
    email_notificator.send(**kwargs)


@app.task(name="sms", acks_late=True, bind=True, base=BaseTaskWithRetry)
def send_sms(self, **kwargs):
    sms_notificator.send(**kwargs)


if DEBUG:
    mock_sender = MockSender()
    mock_notificator = MockNotificator(connection, HISTORY, TEMPLATES, sms_sender)


    @app.task(name="mock", acks_late=True, bind=True, base=BaseTaskWithRetry)
    def send_mock(self, **kwargs):
        mock_notificator.send(**kwargs)

if __name__ == "__main__":
    app.start()
