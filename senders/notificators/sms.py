from .base import BaseNotificator


class SMSNotificator(BaseNotificator):

    def _send(self, **kwargs):
        message_type = kwargs.get("type")
        channel = kwargs.get("channel")
        payload = kwargs.get("payload")
        recipient = kwargs.get("recipient")
        template, from_number, _ = self.get_metadata(message_type, channel)
        body = self.render_message(template, payload)

        self.sender.send(from_number, recipient, body)
        return body

