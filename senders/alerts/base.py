import requests
from celery_app import app
from celery_config import AUTH_SERVICE

class BaseAlert:

    template: str

    def _send(self, data: dict, users: list[dict] = None):

        if not users:
            users = self._get_users()

        for user in users:
            data["user_id"] = user["id"]
            payload = self._get_payload(data)
            app.send_task("email", kwargs=payload)

    def _get_payload(self, data: dict) -> dict:
        return {
            "service": "auth",
            "channel": "email",
            "type": self.template,
            "payload": data
        }

    def _get_users(self):

        # get top 10 of the week
        params = {
            "offset": 0,
            "count": 100,

        }

        offset = 0
        data = []

        while data:
            params["offset"] = offset
            response = requests.get(f"{AUTH_SERVICE}/users", params=params)

            yield response.json()
            offset += 100
