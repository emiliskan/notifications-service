from .base import BaseNotificator

# TODO add SanGrid


class EmailNotificator(BaseNotificator):

    def _send(self, **kwargs) -> str:
        message_type = kwargs.get("type")
        channel = kwargs.get("channel")
        payload = kwargs.get("payload")
        # FIXME uncomment after add welcome_letter alert
        # recipient = kwargs.get("recipient")
        recipient = 'alice@email.com'
        template, sender = self.get_metadata(message_type, channel)
        body = self.render_message(template, payload)
        print(f'from {sender}')
        print(f'to {recipient}')
        print(body)
        return body
