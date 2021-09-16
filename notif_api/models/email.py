from models.base import AbstractModel


class Email(AbstractModel):
    to: str
    data: str
