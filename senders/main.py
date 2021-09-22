from requests.exceptions import ConnectionError

from celery import Celery, Task
from psycopg2 import OperationalError

from .alerts import TopMoviesAlert
from .db import connect_to_db
from .celery_config import CELERY_BROKER_URL, BD_DSN, TEMPLATES, HISTORY
from .notificators import EmailNotificator, SMSNotificator

# TODO close db connection
app = Celery("senders", broker=CELERY_BROKER_URL)
connection = connect_to_db(BD_DSN)

email_notificator = EmailNotificator(connection, HISTORY, TEMPLATES)
sms_notificator = SMSNotificator(connection, HISTORY, TEMPLATES)

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


if __name__ == "__main__":
    app.start()
