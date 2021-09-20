import abc
from jinja2 import Template
from psycopg2.extensions import connection as pg_conn


class BaseNotificator(abc.ABC):
    def __init__(self, conn: pg_conn, history: str, template: str):
        self.conn = conn
        self.history = history
        self.template = template

    @abc.abstractmethod
    def _send(self, **kwargs):
        pass

    def get_metadata(self, message_type: str, channel: str) -> (Template, str):
        cursor = self.conn.cursor()
        query = f"SELECT body, sender FROM {self.template} WHERE type = %s AND channel = %s"
        cursor.execute(query, (message_type, channel))
        template, sender = cursor.fetchone()
        cursor.close()
        return Template(template), sender

    @staticmethod
    def render_message(template: Template, payload: dict) -> str:
        return template.render(**payload)

    def _save_history(self, service: str, msg_type: str):
        cursor = self.conn.cursor()
        query = f"INSERT INTO {self.history} service type VALUES (%s, %s)"
        cursor.execute(query, (service, msg_type))
        cursor.close()

    def send(self, **kwargs):
        self._send(**kwargs)
        # self._save_history(kwargs['service'], kwargs['type'])
