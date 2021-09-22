import abc
from datetime import datetime
from uuid import uuid4
from jinja2 import Template
from psycopg2.extensions import connection as pg_conn
import psycopg2.extras


class BaseNotificator(abc.ABC):
    def __init__(self, conn: pg_conn, history: str, template: str):
        self.conn = conn
        self.history = history
        self.template = template

    @abc.abstractmethod
    def _send(self, **kwargs) -> str:
        pass

    def get_metadata(self, message_type: str, channel: str) -> (Template, str):
        with self.conn.cursor() as cursor:
            query = f"SELECT body, sender FROM {self.template} WHERE type = %s AND channel = %s"
            cursor.execute(query, (message_type, channel))
            template, sender = cursor.fetchone()
        return Template(template), sender

    @staticmethod
    def render_message(template: Template, payload: dict) -> str:
        return template.render(**payload)

    def _save_history(self, service: str, channel: str, type: str, recipient: str,  msg: str, **kwargs):
        with self.conn.cursor() as cursor:
            psycopg2.extras.register_uuid()
            query = f"""INSERT INTO {self.history} 
            (id, service, channel, type, recipient, send_time, body)
             VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(query, (uuid4(), service, channel, type, recipient, datetime.now(), msg))

    def send(self, **kwargs):
        msg = self._send(**kwargs)
        recipient = kwargs.get("recipient")
        self._save_history(msg=msg, recipient=recipient, **kwargs)
        print('save log')
