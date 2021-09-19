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

    def get_template(self, message_type: str, channel: str) -> Template:
        cursor = self.conn.cursor()
        query = f"SELECT template FROM  {self.template} WHERE VALUES (%s, %s)"
        cursor.execute(query, (message_type, channel))
        template = cursor.cur.fetchone()
        cursor.close()
        return Template(template)

    def render_message(self, message_type: str, channel: str,
                       payload: dict) -> str:
        template = self.get_template(message_type, channel)
        return template.render(**payload)

    def _save_history(self, service: str, msg_type: str):
        cursor = self.conn.cursor()
        query = f"INSERT INTO {self.history} service type VALUES (%s, %s)"
        cursor.execute(query, (service, msg_type))
        cursor.close()

    def send(self, **kwargs):
        self._send(**kwargs)
        self._save_history(kwargs['service'], kwargs['type'])
