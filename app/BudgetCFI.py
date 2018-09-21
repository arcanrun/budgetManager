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
        return CFICommonMoney(data*0.5)

    def createFunMoney(self, data):
        return CFIFunMoney(data*0.3)

    def createInvestMoney(self, data):
        return CFIInvestMoney(data*0.2)

    def creatBudgetMoney(self, data):
        return CFIBudgetMoney(data)


if __name__ == '__main__':

    a = BudgetCFI()
    print(a.execute(100).__class__.__bases__)