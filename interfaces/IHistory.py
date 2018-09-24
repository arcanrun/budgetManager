import abc


class IHistory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addToHistory(self, transName, money, obj, date):
        pass

    @abc.abstractmethod
    def save(self):
        pass

    @abc.abstractmethod
    def setDB(self, db):
        pass