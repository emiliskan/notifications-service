from senders.notificators.base import BaseNotificator, BaseSender, logger
from senders.models import Notification, SentResult
from senders.services.auth import AuthService
from senders.services.ugc import UGCService


class MockSender(BaseSender):
    def __init__(self):
        super().__init__()
        self.args = []
        self.kwargs = {}

    def send(self, *args, **kwargs) -> None:
        self.args = args
        self.kwargs = kwargs
        logger.info(f"get: {args}")
        logger.info(f"get: {kwargs}")


class MockNotificator(BaseNotificator):

    def _send(self, data: Notification) -> SentResult:
        notification_metadata = self.get_metadata(data.type, data.channel)
        body = self.render_message(notification_metadata.template, data.payload)

        self.sender.send(
            notification_metadata.sender,
            data.recipient,
            notification_metadata.subject,
            body
        )

        return SentResult(**data.__dict__, **notification_metadata.__dict__, body=body)

    def send(self, **kwargs):
        handeled_data = self._send(**kwargs)
        logger.info(handeled_data)
        return handeled_data


class AuthServiceMock(AuthService):

    @staticmethod
    def get_users():
        return [
            {'id': 1, 'email': 'me@sobaka.com'},
            {'id': 2, 'email': 'you@sobaka.com'},
        ]


class UGCServiceMock(UGCService):

    @staticmethod
    def get_top_10_movies():
        return {
            "movies": [
                {'id': 1, 'name': 'Duna'},
                {'id': 2, 'name': 'Duna 2'},
            ]
        }
