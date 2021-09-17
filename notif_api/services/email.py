from functools import lru_cache

from fastapi import Depends

from db.celery_app import app, get_celery_app
from models.email import Email


class EmailService:

    def __init__(self, celery):
        self.celery = celery

    async def send(self, email_data: Email) -> None:
        self.celery.send_task("send_email", kwargs=email_data.dict())


@lru_cache(maxsize=128)
def get_email_service(celery=Depends(get_celery_app)) -> EmailService:
    return EmailService(celery)
