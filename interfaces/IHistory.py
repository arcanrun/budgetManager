import abc


class IHistory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def addToHistory(self, transName, money, obj, date, wholeBudget):
        pass

    @abc.abstractmethod
    def save(self, payDay, wholeBudget):
        pass

    @abc.abstractmethod
    def setDB(self, db):
        pass

    @abc.abstractmethod
    def clear(self):
        pass