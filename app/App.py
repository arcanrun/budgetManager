from app.BudgetCFI import BudgetCFI


class App:
    def __init__(self, budgetManager):
        self.budgetManager = budgetManager
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