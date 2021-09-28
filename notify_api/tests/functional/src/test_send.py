import pytest

URL = "/send"


@pytest.mark.asyncio
async def test_send_email(make_post_request):
    data = {
        "service": "auth",
        "channel": "email",
        "type": "welcome_letter",
        "contact": "alice@email.com",
        "payload": {
            "user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f",
            "name": "alice"
        }
    }
    response = await make_post_request(url=URL, data=data)
    assert response.status == 200, "Couldn't send email message."


@pytest.mark.asyncio
async def test_send_junk(make_post_request):
    data = {
        "service": "auth",
        "channel": "junk",
        "type": "welcome_letter",
        "contact": "alice@email.com",
        "payload": {
            "user_id": "ad0ec496-8c65-42c5-8fa7-3cf17bdaca7f",
            "name": "alice"
        }
    }
    response = await make_post_request(url=URL, data=data)
    assert response.status == 422, "Get unsupported data"
    
    detail = response.body["detail"][0]["loc"]
    assert "channel" in detail, "Incorrect error message"
