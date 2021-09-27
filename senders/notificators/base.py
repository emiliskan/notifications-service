import abc
import datetime
import logging
import uuid

from jinja2 import Template
from psycopg2.extensions import connection as pg_conn
import psycopg2.extras

from ..celery_config import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class TemplateNotFound(Exception):
    ...


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
    def _send(self, **kwargs) -> str:
        pass

    def get_metadata(self, message_type: str, channel: str) -> (Template, str):
        with self.conn.cursor() as cursor:
            query = f"SELECT body, sender, subject FROM {self.template} WHERE type = %s AND channel = %s"
            cursor.execute(query, (message_type, channel))
            result = cursor.fetchone()
            if not result:
                raise TemplateNotFound(f"Given template {message_type} in {channel} not found in database!")

            template, sender, subject = result
        return Template(template), sender, subject

    @staticmethod
    def render_message(template: Template, payload: dict) -> str:
        return template.render(**payload)

    def _save_history(self, service: str, channel: str, type: str, recipient: str,
                      msg: str, subject: str, **kwargs):
        with self.conn.cursor() as cursor:
            psycopg2.extras.register_uuid()
            id = uuid.uuid4()
            time = datetime.datetime.now()
            query = f"""INSERT INTO {self.history} 
             (id, send_time, service, channel, type, recipient, subject, body)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            logger.info((service, channel, type, recipient, subject, msg))
            cursor.execute(query, (id, time, service, channel, type, recipient, subject, msg))
            logger.info(f"message for {recipient} is registered in db")

    def send(self, **kwargs):
        self._save_history(msg=kwargs.get("body"), **kwargs)
