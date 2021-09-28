import abc
import logging
from jinja2 import Template
from psycopg2.extensions import connection as pg_conn
import psycopg2.extras

from senders.models import Notification, NotificationMetadata, SentResult
from senders.notificators.exceptions import SaveHistory, TemplateNotFound, GetMetadata
from ..celery_config import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class BaseSender(abc.ABC):
    def send(self, *args, **kwargs) -> None:
        pass


class BaseNotificator(abc.ABC):
    def __init__(self, conn: pg_conn, history: str, template: str, sender: BaseSender):
        self.conn = conn
        self.history = history
        self.template = template
        self.sender = sender

    @abc.abstractmethod
    def _send(self, data: Notification) -> SentResult:
        pass

    def get_metadata(self, message_type: str, channel: str) -> NotificationMetadata:
        with self.conn.cursor() as cursor:
            query = f"SELECT body, sender, subject FROM {self.template} WHERE type = %s AND channel = %s"
            try:
                cursor.execute(query, (message_type, channel))
            except Exception:
                raise GetMetadata

            result = cursor.fetchone()
            if not result:
                raise TemplateNotFound(f"Given template {message_type} in {channel} not found in database!")

            template, sender, subject = result

        return NotificationMetadata(template=Template(template), sender=sender, subject=subject)

    @staticmethod
    def render_message(template: Template, payload: dict) -> str:
        return template.render(**payload)

    def _save_history(self, data: SentResult):
        with self.conn.cursor() as cursor:
            psycopg2.extras.register_uuid()
            query = f"""INSERT INTO {self.history} 
             (service, channel, type, recipient, subject, body)
             VALUES (%s, %s, %s, %s, %s)"""

            try:
                cursor.execute(query, (data.service, data.channel, data.type, data.recipient, data.subject, data.body))
            except Exception:
                raise SaveHistory

    def send(self, data: Notification):
        sent_result = self._send(data)
        self._save_history(sent_result)

        logger.info("sent notification")
