from interfaces.IBudgetManager import IBudgetManager
from app.CFICommonMoney import CFICommonMoney
from app.CFIFunMoney import CFIFunMoney
from app.CFIInvestMoney import CFIInvestMoney
from app.CFIBudgetMoney import CFIBudgetMoney


class BudgetCFI(IBudgetManager):
    def execute(self, data):
        data = float(data)
        return (
            self.createCommonMoney(data),
            self.createFunMoney(data),
            self.createInvestMoney(data),
            self.creatBudgetMoney(data)
        )

    def createCommonMoney(self, data):
        return CFICommonMoney(round(data*0.5, 2))

    def createFunMoney(self, data):
        return CFIFunMoney(round(data*0.3, 2))

    def createInvestMoney(self, data):
        return CFIInvestMoney(round(data*0.2, 2))

    def creatBudgetMoney(self, data):
        return CFIBudgetMoney(round(data, 2))


if __name__ == '__main__':

    a = BudgetCFI()
    print(a.execute(100).__class__.__bases__)