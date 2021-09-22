from .base import BaseNotificator, TemplateNotFound


# TODO add SanGrid


class EmailNotificator(BaseNotificator):

    def _send(self, **kwargs):
        message_type = kwargs.get("type")
        channel = kwargs.get("channel")
        payload = kwargs.get("payload")

        try:
            template, sender = self.get_metadata(message_type, channel)
        except TemplateNotFound:
            print("Template not found")
            return
        body = self.render_message(template, payload)
        print(f'from {sender}')
        print(body)
