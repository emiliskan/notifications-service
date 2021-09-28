import abc

from psycopg2.extensions import connection as pg_conn
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .base import BaseNotificator, BaseSender
from senders.celery_config import SENDGRID_API_KEY


class EmailSender(BaseSender):

    @abc.abstractmethod
    def send(self, from_email: str, recipient: str, subject: str, body: str) -> None:
        pass


class SendGrid(EmailSender):

    def send(self, from_email: str, recipient: str, subject: str, body: str):
        message = Mail(
            from_email=from_email,
            to_emails=recipient,
            subject=subject,
            html_content=body)
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        sg.send(message)


class EmailNotificator(BaseNotificator):

    def _send(self, **kwargs) -> str:
        message_type = kwargs.get("type")
        channel = kwargs.get("channel")
        payload = kwargs.get("payload")
        recipient = kwargs.get("recipient")
        template, from_email, subject = self.get_metadata(message_type, channel)
        body = self.render_message(template, payload)

        self.sender.send(from_email, recipient, subject, body)
        return body
