from senders.alerts.base import BaseAlert


class TopMoviesAlert(BaseAlert):

    def send(self):

        data = self.ugc_service.get_top_10_movies()
        users = self.auth_service.get_users()

        for user in users:
            data["user_id"] = user["id"]
            self._send(user["email"], data)


