from app.AppLogic import AppLogic
from app.BudgetCFI import BudgetCFI
from app.PayDay import PayDay
from interfaces.IMoney import IMoney
from app.CFIBudgetMoney import CFIBudgetMoney
from app.CFICommonMoney import CFICommonMoney
from app.CFIFunMoney import CFIFunMoney
from app.CFIInvestMoney import CFIInvestMoney
from interfaces.ITimeLine import ITimeLine

import inspect
import sys

class View:
    def __init__(self, appLogic):
        self.app = appLogic

    def allInfo(self):

        res = [
                self.todayDay,
                self.getCommonLimitToday,
                self.getFunLimitToday,
                self.getBudgetMoney,
                self.getCommonMoney,
                self.getFunLimitToday,
                self.getInvestMoney,
                self.getAmountDaysBeforePayment,
                self.dateOfNextPayment
               ]
        for i in res:
            i()

        self.menu()


    def getCommonMoney(self):
        self.checkOnEmptyValue(self.app.commonBudget, 1)
        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def getFunMoney(self):
        self.checkOnEmptyValue(self.app.funBudget, 1)
        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def getInvestMoney(self):
        self.checkOnEmptyValue(self.app.investBudget,1)
        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def getBudgetMoney(self):
        self.checkOnEmptyValue(self.app.budget, 1)
        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def getCommonLimitToday(self):
        self.checkOnEmptyValue(self.app.commonBudget, 2)
        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def getFunLimitToday(self):
        self.checkOnEmptyValue(self.app.funBudget, 2)
        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def getAmountDaysBeforePayment(self):
        res = self.app.timeLine.daysBeforePay()
        if res is None:
            self.editor()
        print('До следующей зарплаты осталось: {} дня(ей)'.format(res))
        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def todayDay(self):
        print('Сегодня: ')
        print(self.app.timeLine.now)


        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def dateOfNextPayment(self):
        res = self.app.timeLine.getDateNextPay()
        if res is None:
            self.editor()
        print('Следующая зарплата:')
        print(res)
        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def checkOnEmptyValue(self, value, trigger):
        if value is None:
            print('Не заполненно!')
            self.editor()
        else:
            if trigger == 1:
                if isinstance(value, CFIBudgetMoney):
                    print('Весь бюджет')
                if isinstance(value, CFICommonMoney):
                    print('Общий бюджет')
                if isinstance(value, CFIFunMoney):
                    print('Бюджет на развлечения')
                if isinstance(value, CFIInvestMoney):
                    print('Инвестиции')
                print(value.get())

            if trigger == 2:
                if isinstance(value, CFICommonMoney):
                    print('Лимит из общих средств на сегодня:')

                    print(self.app.limitForToday(value))
                if isinstance(value, CFIFunMoney):
                    print('Лимит из бюджета на развлечения:')
                    print(self.app.limitForToday(value))



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
11. Заполнить информацию
12. История
13. Сохранить
14. Редактировать,
+. Вычесть
-. Прибавить
15. Выход
            """

        )
        n = str(input())

        mainDict = {
            '1': self.allInfo,
            '2': self.getCommonLimitToday,
            '3': self.getFunLimitToday,
            '4': self.getBudgetMoney,
            '5': self.getCommonMoney,
            '6': self.getFunMoney,
            '7': self.getInvestMoney,
            '8': self.getAmountDaysBeforePayment,
            '9': self.dateOfNextPayment,
            '10': self.todayDay,
            '14': self.editor,
            '15': self.exit

        }.get(n, self.menu)()

    def editor(self):
        if self.app.budget is None:
            print('Введите бюджет:')
            v = input()
            self.app.execute(v)


        if self.app.timeLine.getPayDay() is None:
            print('Введите день зарплаты:')
            v = input()
            self.app.timeLine.setPayDay(v)
        self.menu()

    def exit(self):
        sys.exit('Bye! Bye!')






if __name__ == '__main__':
    budgetCFI = BudgetCFI()
    payDay = PayDay()
    app = AppLogic(budgetCFI, payDay)


    mainView = View(app)
    mainView.menu()

