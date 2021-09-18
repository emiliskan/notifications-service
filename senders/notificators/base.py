import abc


class BaseNotificator:
    @abc.abstractmethod
    def _send(self, **kwargs):
        pass

    def _save_history(self):
        # TODO implement me
        print("Save history")

    def send(self, **kwargs):
        self._send(**kwargs)
        self._save_history()

