import abc

import requests
from senders.celery_app import app
from senders.celery_config import AUTH_SERVICE


class BaseAlert(abc.ABC):

    def __init__(self, template: str, channels: list[str]):
        self.template = template
        self.channels = channels

    @abc.abstractmethod
    def send(self):
        pass

    def _send(self, to: str, data: dict):

        for channel in self.channels:
            payload = self._get_payload(to, channel, data)
            app.send_task(channel, kwargs=payload)

    def _get_payload(self, to: str, channel: str, data: dict) -> dict:
        return {
            "service": "alert",
            "recipient": to,
            "channel": channel,
            "type": self.template,
            "payload": data
        }

    def _get_users(self):

        params = {
            "offset": 0,
            "count": 100,
        }

        offset = 0
        tries = 0
        while tries < 5:
            params["offset"] = offset
            response = requests.get(f"http://{AUTH_SERVICE}/users", params=params)

            users = response.json()
            offset += 100
            tries += 1
            for user in users:
                yield user
