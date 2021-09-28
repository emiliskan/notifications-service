from dataclasses import dataclass

from jinja2 import Template


@dataclass
class Notification:
    service: str
    channel: str
    type: str
    recipient: str
    payload: dict


@dataclass
class NotificationMetadata:
    template: Template
    sender: str
    subject: str


@dataclass
class SentResult(Notification, NotificationMetadata):
    body: str


