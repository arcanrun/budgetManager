from app.AppLogic import AppLogic
from app.BudgetCFI import BudgetCFI
from app.PayDay import PayDay
from interfaces.IMoney import IMoney
from interfaces.ITimeLine import ITimeLine

class View:
    def __init__(self, appLogic):
        self.app = appLogic

    def allInfo(self):
        print('All info')
        res = [
                self.app.timeLine.now,
                self.app.timeLine.daysBeforePay(),
                self.app.timeLine.getDateNextPay(),
                self.getBudgetMoney(),
                self.getCommonMoney(),
                self.getFunMoney(),
                self.getInvestMoney(),
                self.app.limitForToday(self.app.commonBudget),
                self.app.limitForToday(self.app.funBudget)
               ]
        for i in res:
            print(i)
        return res

    def getCommonMoney(self):
        if self.checkOnEmptyValue(self.app.commonBudget):
            return None
        return self.app.commonBudget.get()

    def getFunMoney(self):
        if self.checkOnEmptyValue(self.app.funBudget):
            return None
        return self.app.funBudget.get()

    def getInvestMoney(self):
        if self.checkOnEmptyValue(self.app.investBudget):
            return None
        return self.app.investBudget.get()

    def getBudgetMoney(self):
        if self.checkOnEmptyValue(self.app.budget):
            return None
        return self.app.budget.get()


    def getCommonLimitToday(self):
        if self.checkOnEmptyValue(self.app.limitForToday(self.app.commonBudget)):
            return None
        return self.app.limitForToday(self.app.commonBudget)

    def getFunLimitToday(self):
        if self.checkOnEmptyValue(self.app.limitForToday(self.app.funBudget)):
            return None
        return self.app.limitForToday(self.app.funBudget)

    def checkOnEmptyValue(self, value):
        if value is None:
            return True
        return False

    def menu(self):
        print(
            """
1. Вся информация
2. Лимит из 50% на сегодня
3. Лимит из 30% на сегодня
4. Бюдзет
5. 50%
6. 30%
7. 20%
8. Количество дней до ЗП
9. Дата следующей ЗП
10. Сегодняшняя дата
11. Выход
            """

        )
        n = str(input())

        mainDict = {
            '1': self.allInfo,
            '2': self.getCommonLimitToday,
            '3': self.getFunLimitToday,
            '4': self.getBudgetMoney

        }.get(n, self.menu)()

    def editor(self, value):
        if value.__class__.__bases__[0] is IMoney:
            print('Введите бюджет:')
            v = input()
            self.app.execute(v)
            self.menu()

        if value.__class__.__bases__[0] is ITimeLine:
            print('Введите день зарплаты:')
            v = input()
            self.app.timeLine.setPayDay(v)





if __name__ == '__main__':
    budgetCFI = BudgetCFI()
    payDay = PayDay()
    app = AppLogic(budgetCFI, payDay)


    mainView = View(app)
    mainView.menu()

