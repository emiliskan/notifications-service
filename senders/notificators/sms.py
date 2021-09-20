from .base import BaseNotificator


class SMSNotificator(BaseNotificator):

    def _send(self, **kwargs):
        message_type = kwargs.get("type")
        channel = kwargs.get("channel")
        payload = kwargs.get("payload")

        template, sender = self.get_metadata(message_type, channel)
        body = self.render_message(template, payload)
        print(f'from {sender}')
        print(body)
