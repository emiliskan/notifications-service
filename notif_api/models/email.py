import datetime

from models.base import AbstractModel


class Email(AbstractModel):
    to: str
    data: str


class EmailFuture(Email):
    date: datetime.datetime
