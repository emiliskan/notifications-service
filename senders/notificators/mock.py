from .base import BaseNotificator, BaseSender, logger


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

    def _send(self, **kwargs):
        message_type = kwargs.get("type")
        channel = kwargs.get("channel")
        payload = kwargs.get("payload")
        recipient = kwargs.get("recipient")
        template, sender, subject = self.get_metadata(message_type, channel)
        body = self.render_message(template, payload)
        self.sender.send(sender, recipient, subject, body)
        return sender, recipient, subject, body

    def send(self, **kwargs):
        handeled_data = self._send(**kwargs)
        logger.info(handeled_data)
        return handeled_data

