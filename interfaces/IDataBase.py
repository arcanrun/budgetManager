import abc

class IDataBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self, *args):
        pass

    @abc.abstractmethod
    def load(self):
        pass