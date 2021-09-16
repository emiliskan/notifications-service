from functools import lru_cache

from db.celery_app import app
from models.email import Email


class EmailService:

    async def send(self, email_data: Email) -> None:
        app.send_task("send_email", kwargs=email_data.dict())


@lru_cache(maxsize=128)
def get_email_service() -> EmailService:
    return EmailService()
