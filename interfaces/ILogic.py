import abc

class ILogic(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, data):
        pass

    @abc.abstractmethod
    def add(self, money, data):
        pass

    @abc.abstractmethod
    def sub(self, money, data):
        pass

    @abc.abstractmethod
    def change(self, money, new_data):
        pass

    @abc.abstractmethod
    def limitForToday(self, moneyType):
        pass