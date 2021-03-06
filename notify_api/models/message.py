from typing import Dict
from enum import Enum
from pydantic import Field

from .base import AbstractModel


class Service(str, Enum):
    auth = "auth"
    ugc = "ugc"
    admin = "admin"


class Channel(str, Enum):
    # Yes, it isn't best idea to leave it in production
    email = "email"
    sms = "sms"
    mock = "mock"


class MessageType(str, Enum):
    welcome_letter = "welcome_letter"
    mock_letter = "mock_letter"


example_payload = {
    "user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f",
    "name": "alice",
    "contact": "alice@email.com"
}


class Message(AbstractModel):
    service: Service
    channel: Channel
    type: MessageType
    payload: Dict = Field(..., example=example_payload)
