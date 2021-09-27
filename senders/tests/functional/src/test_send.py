
def test_send_email(email_notificator):
    message = {
        "service": "auth",
        "channel": "email",
        "type": "welcome_letter",
        "recipient": "alice@email.com",
        "subject": "Welcome",
        "payload": {
            "user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f",
            "name": "alice",
            "body": "welcome!"
        }
    }
    expected_answer = {'service': 'auth', 'channel': 'email', 'type': 'welcome_letter', 'recipient': 'alice@email.com',
                        'subject': 'Welcome',
                        'payload': {
                             'user_id': 'ad0ec496-8c65-42c5-8fa7'
                                        '-3cf17bdaca7f',
                             'name': 'alice', 'body': 'welcome!'
                         },
                         'msg': 'Привет ad0ec496-8c65-42c5-8fa7'
                                '-3cf17bdaca7f ! Спасибо за '
                                'регистрацию в нашем бомбическом '
                                'электротеатре.\nДля подтверждения '
                                'регистрации пройди по ссылке \n\nС '
                                'презрением, управление '
                                'электротеатра.'}
    body = email_notificator.send(**message)
    assert body == expected_answer


def test_send_sms(sms_notificator):
    message = {
        "service": "auth",
        "channel": "sms",
        "type": "auth_sms",
        "recipient": "89991111111",
        "subject": "Welcome",
        "payload": {
            "user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f",
            "name": "alice",
            "body": "welcome!"
        }
    }

    expected_answer = {'service': 'auth', 'channel': 'sms', 'type': 'auth_sms', 'recipient': '89991111111',
                        'subject': 'Welcome',
                        'payload': {
                            'user_id': 'ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f',
                            'name': 'alice', 'body': 'welcome!'
                        },
                        'msg': 'Добрый день, alice! Ваш код для входа в учетную '
                               'запись: 211DB3'}
    body = sms_notificator.send(**message)
    assert body == expected_answer
