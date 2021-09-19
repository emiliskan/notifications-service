import abc
from jinja2 import Template


class BaseNotificator:
    def __init__(self, db=None):
        self.db = db

    @abc.abstractmethod
    def _send(self, **kwargs):
        pass

    def render_message(self, message_type: str, channel: str,
                       payload: dict) -> str:
        template = Template("<strong> hello {{ user_id }} !</strong>")
        return template.render(**payload)

    def _save_history(self):
        # TODO implement me
        print("Save history")

    def send(self, **kwargs):
        self._send(**kwargs)
        self._save_history()

