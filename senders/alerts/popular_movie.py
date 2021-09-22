import datetime
import requests

from senders.alerts.base import BaseAlert
from senders.celery_config import UGA_SERVICE


class TopMoviesAlert(BaseAlert):

    def send(self):

        data = self._get_top_10_movies()
        users = self._get_users()

        for user in users:
            data["user_id"] = user["id"]
            self._send(data)

    def _get_top_10_movies(self):

        params = {
            "date_end":  datetime.datetime.now(),
            "date_start": datetime.datetime.now() - datetime.timedelta(7),
            "count": 10,
        }

        response = requests.get(f"http://{UGA_SERVICE}/scores/movies/top", params=params)

        data = response.json()

        return {"movies": data}
