import pytest

from senders.db import connect_to_db
from .settings import BD_DSN, TEMPLATES, HISTORY
from senders.notificators import MockSender, EmailNotificator, SMSNotificator


@pytest.fixture()
def sms_notificator():
    connection = connect_to_db(BD_DSN)
    sender = MockSender()
    notificator = SMSNotificator(connection, HISTORY, TEMPLATES, sender=sender)
    yield notificator


@pytest.fixture()
def email_notificator():
    connection = connect_to_db(BD_DSN)
    sender = MockSender()
    notificator = EmailNotificator(connection, HISTORY, TEMPLATES, sender=sender)
    yield notificator

