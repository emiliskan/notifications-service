import pytest

from senders.notificators import (MockNotificator, MockSender,)
from senders.db import connect_to_db
from .settings import BD_DSN, TEMPLATES, HISTORY


@pytest.fixture
async def shared_mock_notificator():
    connection = connect_to_db(BD_DSN)
    mock_sender = MockSender()
    mock_notificator = MockNotificator(connection, HISTORY, TEMPLATES, sender=mock_sender)
    yield mock_notificator

