from functools import lru_cache
from fastapi import Depends

from db.email import EmailSender, get_email_sender
from models.email import Email, EmailFuture


class EmailService:

    def __init__(self, sender: EmailSender):
        self.sender = sender

    async def send(self, email_data: Email) -> None:
        self.sender.send.delay(email_data.to, email_data.data)

    async def send_future(self, email_data: EmailFuture) -> None:
        self.sender.send.delay(email_data.to, email_data.data)


@lru_cache(maxsize=128)
def get_email_service(sender: EmailSender = Depends(get_email_sender)) -> EmailService:
    return EmailService(sender)
