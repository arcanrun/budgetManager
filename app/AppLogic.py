from app.BudgetCFI import BudgetCFI
from interfaces.ILogic import ILogic


class AppLogic(ILogic):
    """
    work with money, history and time - somekind controller
    """
    def __init__(self, budgetManager, timeLine, history):
        self.budgetManager = budgetManager
        self.history = history
        self.timeLine = timeLine

        self.commonBudget = None
        self.funBudget = None
        self.investBudget = None
        self.budget = None

    def execute(self, data):
        if isinstance(self.budgetManager, BudgetCFI):
            self.commonBudget = self.budgetManager.execute(data)[0]
            self.funBudget = self.budgetManager.execute(data)[1]
            self.investBudget = self.budgetManager.execute(data)[2]
            self.budget = self.budgetManager.execute(data)[3]
        else:
            raise NotImplementedError()

    def limitForToday(self, moneyType):
        if moneyType is None:
            return None
        return round((moneyType.get() / self.timeLine.daysBeforePay()),2)

    def sub(self, money, data):
        transName = '-'
        if self.isInstanceOfBudgetMoney(money):
            self.execute(self.budget.get() - data)
            self.history.addToHistory(transName, data, money, self.timeLine.now)
        else:
            money.sub(data)
            self.budget.sub(data)
            self.history.addToHistory(transName,data, money, self.timeLine.now)

    def add(self, money, data):
        transName = '+'
        if self.isInstanceOfBudgetMoney(money):
            self.execute(self.budget.get() + data)
            self.history.addToHistory(transName, data, money, self.timeLine.now)
        else:
            money.add(data)
            self.budget.add(data)
            self.history.addToHistory(transName, data, money, self.timeLine.now)

    def change(self, money, new_data):
        if self.isInstanceOfBudgetMoney(money):
            self.execute(new_data)
        else:
            money.set(new_data)
            self.budget.set(self.commonBudget.get() + self.funBudget.get() + self.investBudget.get())

    def isInstanceOfBudgetMoney(self, moneyType):
        if isinstance(moneyType, self.budget.__class__):
            return True
        return False
