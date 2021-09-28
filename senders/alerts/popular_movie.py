from senders.alerts.base import BaseAlert
from senders.services.auth import AuthService
from senders.services.ugc import UGCService


class TopMoviesAlert(BaseAlert):
    def __init__(self,
                 template: str,
                 channels: list[str],
                 auth_service: AuthService,
                 ugc_service: UGCService
                 ):
        super().__init__(template, channels)
        self.auth_service = auth_service
        self.ugc_service = ugc_service

    def send(self):
        data = self.ugc_service.get_top_10_movies()
        users = self.auth_service.get_users()

        for user in users:
            data["user_id"] = user["id"]
            self._send(user["email"], data)
