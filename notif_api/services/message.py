from functools import lru_cache

from fastapi import Depends

from db.celery_app import get_celery_app
from models import Message


class MessageService:

    def __init__(self, celery):
        self.celery = celery

    async def send(self, message: Message) -> None:
        self.celery.send_task("send_email", kwargs=message.dict())


@lru_cache(maxsize=128)
def get_message_service(celery=Depends(get_celery_app)) -> MessageService:
    return MessageService(celery)
