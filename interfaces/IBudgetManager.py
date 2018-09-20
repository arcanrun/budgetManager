import abc


class IBudgetManager(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def execute(self, data):
        pass