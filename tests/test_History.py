import unittest
import datetime
from app.AppLogic import AppLogic
from app.BudgetCFI import BudgetCFI
from app.PayDay import PayDay
from app.History import History
from app.DbShelve import DbShelve


class HistoryTest(unittest.TestCase):
    def setUp(self):
        self.payDay = PayDay()
        self.payDay.now = datetime.date(2018, 9, 10)

        self.budgetManager = BudgetCFI()

        self.history = History()
        self.db = DbShelve()
        self.history.setDB(self.db)

        self.app = AppLogic(self.budgetManager, self.payDay, self.history)
        self.app.execute(10000)


    def test_add_to_history(self):
        self.history.addToHistory('+', 50, self.app.budget, self.app.timeLine, self.app.budget.get())
        res = self.history.getHistoryDict()
        self.assertEqual(res, {'2018-09-10': ['+budget:50.0']})

        self.history.addToHistory('+', 30,self.app.budget,self.app.timeLine, self.app.budget.get())
        res = self.history.getHistoryDict()
        self.assertEqual(res, {'2018-09-10': ['+budget:50.0', '+budget:30.0']})

        self.history.addToHistory('-', 100,self.app.commonBudget, self.app.timeLine, self.app.budget)
        res = self.history.getHistoryDict()
        self.assertEqual(res, {'2018-09-10': ['+budget:50.0', '+budget:30.0', '-common:100.0']})

        self.history.addToHistory('-', 2, self.app.funBudget, self.app.timeLine, self.app.budget.get())
        res = self.history.getHistoryDict()
        self.assertEqual(res, {'2018-09-10': ['+budget:50.0', '+budget:30.0', '-common:100.0', '-fun:2.0']})

        self.history.addToHistory('+', 10, self.app.investBudget, self.app.timeLine, self.app.budget.get())
        res = self.history.getHistoryDict()
        self.assertEqual(res, {'2018-09-10': ['+budget:50.0', '+budget:30.0', '-common:100.0', '-fun:2.0', '+invest:10.0']})

        # change date
        self.payDay.now = datetime.date(2018, 9, 15)
        self.history.addToHistory('+', 9, self.app.investBudget, self.app.timeLine, self.app.budget.get())
        res = self.history.getHistoryDict()
        self.assertEqual(res, {
            '2018-09-10': [
                '+budget:50.0',
                '+budget:30.0',
                '-common:100.0',
                '-fun:2.0',
                '+invest:10.0'],
            '2018-09-15': ['+invest:9.0']})

        self.history.addToHistory('-',18, self.app.commonBudget, self.app.timeLine, self.app.budget.get())
        res = self.history.getHistoryDict()
        self.assertEqual(res, {
            '2018-09-10': [
                '+budget:50.0',
                '+budget:30.0',
                '-common:100.0',
                '-fun:2.0',
                '+invest:10.0'],
            '2018-09-15': [
                '+invest:9.0',
                '-common:18.0']})

    def test_add_sub_on_real_objects(self):

        self.app.sub(self.app.budget,10)
        res = self.app.history.getHistoryDict()

        self.assertEqual(res,{'2018-09-10':['-budget:10.0']})