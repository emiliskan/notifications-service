from abc import abstractmethod


class AbstractSender(object):

    @abstractmethod
    def send(self, to: any, data: any):
        raise NotImplemented
