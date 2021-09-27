import pytest

from senders.notificators import BaseNotificator, EmailNotificator, SMSNotificator


@pytest.mark.parametrize(
    "notificator, channel, recipient, type, expected_answer",
    [
        (EmailNotificator, "email", "alice@email.com", "welcome_letter", {'service': 'auth', 'channel': 'email',
                                                                          'type': 'welcome_letter',
                                                                          'recipient': 'alice@email.com',
                                                                          'subject': 'Welcome',
                                                                          'payload': {
                                                                              'user_id': 'ad0ec496-8c65-42c5-8fa7'
                                                                                         '-3cf17bdaca7f',
                                                                              'name': 'alice', 'body': 'welcome!'},
                                                                          'msg': 'Привет ad0ec496-8c65-42c5-8fa7'
                                                                                 '-3cf17bdaca7f ! Спасибо за '
                                                                                 'регистрацию в нашем бомбическом '
                                                                                 'электротеатре.\nДля подтверждения '
                                                                                 'регистрации пройди по ссылке \n\nС '
                                                                                 'презрением, управление '
                                                                                 'электротеатра.'}),

        (SMSNotificator, "sms", "89991111111", "auth_sms", {'service': 'auth', 'channel': 'sms',
                                                            'type': 'auth_sms', 'recipient': '89991111111',
                                                            'subject': 'Welcome',
                                                            'payload': {
                                                                'user_id': 'ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f',
                                                                'name': 'alice', 'body': 'welcome!'},
                                                            'msg': 'Добрый день, alice! Ваш код для входа в учетную '
                                                                   'запись: 211DB3'})
    ]
)
def test_send_notification(shared_notificator,
                           notificator: BaseNotificator,
                           channel: str, recipient,
                           type: str,
                           expected_answer: dict):
    message = {
        "service": "auth",
        "channel": channel,
        "type": type,
        "recipient": recipient,
        "subject": "Welcome",
        "payload": {
            "user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f",
            "name": "alice",
            "body": "welcome!"
        }
    }
    body = shared_notificator.send(**message)
    assert body == expected_answer
