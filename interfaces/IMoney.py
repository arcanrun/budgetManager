import abc


class IMoney(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def set(self):
        pass

    @abc.abstractmethod
    def get(self):
        pass

    @abc.abstractmethod
    def change(self):
        pass