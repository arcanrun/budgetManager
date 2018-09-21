import unittest
from app.App import App
from app.BudgetCFI import BudgetCFI
from app.PayDay import PayDay
from app.CFICommonMoney import CFICommonMoney
from app.CFIFunMoney import CFIFunMoney


class AppTest(unittest.TestCase):
    def setUp(self):
        self.payday = PayDay()
        self.payday.setPayDay(10)
        self.app = App(BudgetCFI(), self.payday)
        self.commonBudget = CFICommonMoney(5000)
        self.funBudget = CFIFunMoney(3000)

    def test_limit_of_money_for_current_day(self):


        resCommon = self.app.limitForToday(self.commonBudget)
        resFun = self.app.limitForToday(self.funBudget)

        self.assertEqual(resCommon, 263.16) # common IF payday is on 10
        self.assertEqual(resFun, 157.89) # fun IF payday is on 10
