import datetime

from models.base import AbstractModel


class Email(AbstractModel):
    to: str
    data: str
    send_time: datetime.date = None
