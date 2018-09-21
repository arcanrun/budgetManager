import abc


class ITimeLine(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def setPayDay(self, day):
        pass

    @abc.abstractmethod
    def getPayDay(self):
        pass

    @abc.abstractmethod
    def daysBeforePay(self):
        pass

    @abc.abstractmethod
    def getDateNextPay(self):
        pass
