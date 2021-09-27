
def test_send(shared_mock_notificator):
    message = {
        "service": "auth",
        "channel": "email",
        "type": "welcome_letter",
        "recipient": "alice@email.com",
        "subject": "Welcome",
        "payload": {
            "user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f",
            "name": "alice"
        }
    }
    body = shared_mock_notificator.send(**message)
    expected_answer = ('noreplay@bigbung.cc', 'alice@email.com', 'Я бы задумался, стоит ли продолжать регистрацию.',
                       'Привет ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f ! Спасибо за регистрацию в нашем бомбическом '
                       'электротеатре.\nДля подтверждения регистрации пройди по ссылке \n\nС презрением, '
                       'управление электротеатра.')
    assert body == expected_answer
