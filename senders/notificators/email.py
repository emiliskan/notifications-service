from notificators.base import BaseNotificator


class EmailNotificator(BaseNotificator):

    email_data: str

    def __init__(self, to, data):
        self.to = to
        self.data = data

    def send(self):
        self.email_data = self._get_data()
        self._send_email()

    def _send_email(self):
        print(f"sending email to {self.to}")

