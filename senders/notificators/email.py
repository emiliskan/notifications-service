import abc

from psycopg2.extensions import connection as pg_conn
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from senders.models import Notification, SentResult
from senders.notificators.base import BaseNotificator
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


class MockSender(EmailSender):

    def send(self, from_email: str, recipient: str, subject: str, body: str):
        print('we can imagine everything')


class EmailNotificator(BaseNotificator):

    def _send(self, data: Notification) -> SentResult:
        notification_metadata = self.get_metadata(data.type, data.channel)
        body = self.render_message(notification_metadata.template, data.payload)

        self.sender.send(
            notification_metadata.sender,
            data.recipient,
            notification_metadata.subject,
            body
        )

        return SentResult(**data.__dict__, **notification_metadata.__dict__, body=body)
