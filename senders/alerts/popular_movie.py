import datetime
import requests

from alerts.base import BaseAlert
from celery_config import UGA_SERVICE


class TopMoviesAlert(BaseAlert):

    def __init__(self):
        self.template = "top_movies"

    def send(self):
        data = self._get_data()
        self._send(data)

    def _get_data(self):

        # get top 10 of the week
        params = {
            "date_start":  datetime.datetime.now(),
            "date_end": datetime.datetime.now() - datetime.timedelta(7),
            "count": 10,

        }
        response = requests.get(f"{UGA_SERVICE}/scores/movies/top", params=params)

        data = response.json()

        return {"movies": data}
