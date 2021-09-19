from typing import Dict
from enum import Enum

from .base import AbstractModel


class Service(str, Enum):
    auth = "auth"
    ugc = "ugc"
    admin = "admin"


class Channel(str, Enum):
    email = "email"


class MessageType(str, Enum):
    welcome_letter = "welcome_letter"


class Message(AbstractModel):
    service: Service
    channel: Channel
    type: MessageType
    payload: Dict
