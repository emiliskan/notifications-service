from .base import BaseNotificator


class EmailNotificator(BaseNotificator):

    def _send(self, **kwargs):
        print(kwargs)


email_notificator = EmailNotificator()
