from app.AppLogic import AppLogic
from app.BudgetCFI import BudgetCFI
from app.PayDay import PayDay
from app.History import History
from app.CFIBudgetMoney import CFIBudgetMoney
from app.CFICommonMoney import CFICommonMoney
from app.CFIFunMoney import CFIFunMoney
from app.CFIInvestMoney import CFIInvestMoney
from app.DbShelve import DbShelve

import inspect
import sys
import shelve


class View:
    def __init__(self, appLogic):
        self.app = appLogic

    def allInfo(self):
        print('='*30)
        res = [
                self.todayDay,
                self.getCommonLimitToday,
                self.getFunLimitToday,
                self.getBudgetMoney,
                self.getCommonMoney,
                self.getFunMoney,
                self.getInvestMoney,
                self.getAmountDaysBeforePayment,
                self.dateOfNextPayment
               ]
        for i in res:
            i()
        print('=' * 30)
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
        print('Сегодня: {}'.format(self.app.timeLine.now))
        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def dateOfNextPayment(self):
        res = self.app.timeLine.getDateNextPay()
        if res is None:
            self.editor()
        print('Следующая зарплата: {}'.format(res))

        if not inspect.stack()[1][3] == 'allInfo': self.menu()

    def printHistory(self):
        history = self.app.history.getHistoryDict()

        for k,v in history.items():
            print(k, ':')
            for i in v:
                print('\t', i)

        self.menu()

    def add(self):
        print("""
1. Ко всему бюджету
2. К общим средствам
3. К средствам на развлечение
4. К Инвестициям    
        """)
        choose = {
            '1': self.app.budget,
            '2': self.app.commonBudget,
            '3': self.app.funBudget,
            '4': self.app.investBudget
        }
        v = input()
        v = choose.get(v)
        if not v:
            self.add()
        print('Сумма: ')
        m = float(input())
        self.app.add(v, m)
        self.menu()

    def sub(self):
        print("""
1. Из всего бюджета
2. Из общих средств
3. Из средств на развлечения
4. Из Инвестиций    
                """)
        choose = {
            '1': self.app.budget,
            '2': self.app.commonBudget,
            '3': self.app.funBudget,
            '4': self.app.investBudget
        }
        v = input()
        v = choose.get(v)
        if not v:
            self.sub()
        print('Сумма: ')
        m = float(input())
        self.app.sub(v, m)
        self.menu()

    def checkOnEmptyValue(self, value, trigger):
        if value is None:
            print('Не заполненно!')
            self.editor()
        else:
            if trigger == 1:
                if isinstance(value, CFIBudgetMoney):
                    print('Весь бюджет: {}'.format(value.get()))
                if isinstance(value, CFICommonMoney):
                    print('Общий бюджет: {}'.format(value.get()))
                if isinstance(value, CFIFunMoney):
                    print('Бюджет на развлечения: {}'.format(value.get()))
                if isinstance(value, CFIInvestMoney):
                    print('Инвестиции: {}'.format(value.get()))

            if trigger == 2:
                if isinstance(value, CFICommonMoney):
                    print('Лимит из общих средств на сегодня: {}'.format(self.app.limitForToday(value)))
                if isinstance(value, CFIFunMoney):
                    print('Лимит из бюджета на развлечения: {}'.format(self.app.limitForToday(value)))

    def menu(self):

        print(
            """
1. Вся информация
2. Лимит из 50% на сегодня
3. Лимит из 30% на сегодня
4. Бюджет
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
-. Вычесть
+. Прибавить
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
            '11': self.editor,
            '12': self.printHistory,
            '14': self.editor,
            '+': self.add,
            '-': self.sub,
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
        sys.exit('Bye-Bye!')







if __name__ == '__main__':
    db = shelve.open('ShelveDb')

    if len(db) == 0:
        budgetCFI = BudgetCFI()
        history = History()
        history.setDB(DbShelve())
        payDay = PayDay()

        app = AppLogic(budgetCFI, payDay, history)
        mainView = View(app)
        mainView.menu()
    else:
        history = History()
        history.setDB(DbShelve())
        budgetCFI = BudgetCFI()

        payDayDb = db['payDay']
        print(payDayDb)

        wholeBudgetDb = db['wholeBudget']
        print(wholeBudgetDb)

        app = AppLogic(budgetCFI, payDayDb, history)
        app.execute(wholeBudgetDb)

        mainView = View(app)
        mainView.menu()





        budgetCFI = BudgetCFI()
        history = History()
        history.setDB(DbShelve())
        payDay = PayDay()

        app = AppLogic(budgetCFI, payDay, history)
        mainView = View(app)
        mainView.menu()

