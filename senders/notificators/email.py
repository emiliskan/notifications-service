from .base import BaseNotificator


class EmailNotificator(BaseNotificator):

    def _send(self, **kwargs):
        message_type = kwargs.get("type")
        channel = kwargs.get("channel")
        payload = kwargs.get("payload")
        body = self.render_message(message_type, channel, payload)
        print(body)


email_notificator = EmailNotificator()
