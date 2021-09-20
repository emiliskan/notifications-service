from .base import BaseNotificator


# TODO add SanGrid

class SMSNotificator(BaseNotificator):

    def _send(self, **kwargs):
        message_type = kwargs.get("type")
        channel = kwargs.get("channel")
        payload = kwargs.get("payload")
        body = self.render_message(message_type, channel, payload)
        print(body)


# sms_notificator = SMSNotificator()
