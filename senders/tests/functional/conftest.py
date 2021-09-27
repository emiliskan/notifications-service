import pytest

from senders.db import connect_to_db
from .settings import BD_DSN, TEMPLATES, HISTORY
from senders.notificators import MockSender


@pytest.fixture()
async def shared_notificator(notificator):
    connection = connect_to_db(BD_DSN)
    mock_sender = MockSender()
    mock_notificator = notificator(connection, HISTORY, TEMPLATES, sender=mock_sender)
    yield mock_notificator

