import abc


class IMoney(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set(self, v):
        pass

    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def sub(self, data):
        pass

    @abc.abstractmethod
    def add(self, data):
        pass

    # @abc.abstractmethod
    # def change(self):
    #     pass