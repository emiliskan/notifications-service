from queue.celery import app

from db.base import AbstractSender


class EmailSender(AbstractSender):

    @app.task(name="send_email")
    def send(self, to: any, data: any):
        print("Sended email")


def get_email_sender():
    return EmailSender()
