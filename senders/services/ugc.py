import requests
import datetime

from senders.celery_config import UGA_SERVICE


class UGCUnavailable(Exception):
    ...


class UGCService:

    @staticmethod
    def get_top_10_movies():

        params = {
            "date_end": datetime.datetime.now(),
            "date_start": datetime.datetime.now() - datetime.timedelta(7),
            "count": 10,
        }

        try:
            response = requests.get(f"http://{UGA_SERVICE}/scores/movies/top", params=params)
        except Exception:
            raise UGCUnavailable

        data = response.json()

        return {"movies": data}

