import abc

from senders.celery_app import app


class BaseAlert(abc.ABC):

    def __init__(self, template: str, channels: list[str]):
        self.template = template
        self.channels = channels

    @abc.abstractmethod
    def send(self):
        pass

    def _send(self, to: str, data: dict) -> None:
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
