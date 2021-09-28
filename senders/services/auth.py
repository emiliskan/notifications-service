import requests

from senders.celery_config import AUTH_SERVICE


class AuthUnavailable(Exception):
    ...


class AuthService:

    @staticmethod
    def get_users():
        params = {
            "offset": 0,
            "count": 100,
        }

        offset = 0
        tries = 0
        while tries < 5:
            params["offset"] = offset

            try:
                response = requests.get(f"http://{AUTH_SERVICE}/users", params=params)
            except Exception:
                raise AuthUnavailable

            users = response.json()
            offset += 100
            tries += 1
            for user in users:
                yield user
