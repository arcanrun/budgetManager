from app.AppLogic import AppLogic
from app.BudgetCFI import BudgetCFI
from app.PayDay import PayDay


class View:
    def __init__(self, appLogic):
        self.app = appLogic

    def allInfo(self):
        print('All info')
        return [
                self.app.timeLine.now,
                self.app.timeLine.daysBeforePay(),
                self.app.timeLine.getDateNextPay(),
                self.app.budget.get(),
                self.app.commonBudget.get(),
                self.app.funBudget.get(),
                self.app.investBudget.get(),
                self.app.limitForToday(self.app.commonBudget),
                self.app.limitForToday(self.app.funBudget)
               ]

    def getCommonMoney(self):
        return self.app.commonBudget.get()

    def getFunMoney(self):
        return self.app.funBudget.get()

    def getInvestMoney(self):
        return self.app.investBudget.get()

    def getBudgetMoney(self):
        return self.app.budget.get()

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
        n = input()
        mainDict = {
            '1': self.allInfo

        }.get(n)()


if __name__ == '__main__':
    budgetCFI = BudgetCFI()
    payDay = PayDay()
    app = AppLogic(budgetCFI, payDay)

    mainView = View(app)
    mainView.menu()

