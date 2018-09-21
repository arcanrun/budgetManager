import unittest
import datetime
from app.App import App
from app.BudgetCFI import BudgetCFI
from app.PayDay import PayDay


class AppTest(unittest.TestCase):
    def setUp(self):
        self.payday = PayDay()
        self.payday.now = datetime.date(2018, 9, 21)
        self.payday.setPayDay(10)

        self.app = App(BudgetCFI(), self.payday)
        self.app.execute(10000)

    def test_limit_of_money_for_current_day(self):

        resCommon = self.app.limitForToday(self.app.commonBudget)
        resFun = self.app.limitForToday(self.app.funBudget)

        self.assertEqual(resCommon, 263.16) # common IF payday is on 10
        self.assertEqual(resFun, 157.89) # fun IF payday is on 10

        self.app.timeLine.setPayDay(12)

        resCommon_2 = self.app.limitForToday(self.app.commonBudget)
        resFun_2 = self.app.limitForToday(self.app.funBudget)

        self.assertEqual(resCommon_2, 238.1) # common IF payday is on 12
        self.assertEqual(resFun_2, 142.86) # fun IF payday is on 12

    def test_sub_add_common_fun_invest_whole_budget_money(self):

        self.app.sub(self.app.commonBudget, 100)
        self.assertEqual(self.app.commonBudget.get(), 4900) # common - 100
        self.assertEqual(self.app.budget.get(), 9900) # whole budget

        self.app.add(self.app.funBudget, 200)
        self.assertEqual(self.app.funBudget.get(), 3200) # fun + 200
        self.assertEqual(self.app.budget.get(), 10100)  # whole budget

        self.app.sub(self.app.investBudget, 1000)
        self.assertEqual(self.app.investBudget.get(), 1000) # invest - 1000
        self.assertEqual(self.app.budget.get(), 9100)  # whole budget

        self.app.add(self.app.budget, 10900)
        self.assertEqual(self.app.budget.get(), 20000)
        self.assertEqual(self.app.commonBudget.get(), 10000)
        self.assertEqual(self.app.funBudget.get(), 6000)
        self.assertEqual(self.app.investBudget.get(), 4000)

        self.app.sub(self.app.budget, 10000)
        self.assertEqual(self.app.commonBudget.get(), 5000)

        self.app.sub(self.app.budget, 5000)
        self.assertEqual(self.app.funBudget.get(), 1500)


