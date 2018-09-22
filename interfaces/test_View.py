import unittest
import datetime
from app.View import View
from app.AppLogic import AppLogic
from app.BudgetCFI import BudgetCFI
from app.PayDay import PayDay


class ViewTest(unittest.TestCase):
    def setUp(self):
        self.budgetCFI = BudgetCFI()
        self.payDay = PayDay()
        self.payDay.now = datetime.date(2018,9,22)
        self.payDay.setPayDay(12)

        self.app = AppLogic(self.budgetCFI, self.payDay)
        self.app.execute(15000)
        self.view = View(self.app)

    def test_all_info_output(self):

        res = self.view.allInfo()

        self.assertEqual(datetime.date.today(),res[0]) # today day
        self.assertEqual(20, res[1]) # amount of days before payment
        self.assertEqual(datetime.date(2018,10,12), res[2]) # the date of next payment
        self.assertEqual(15000, res[3]) # whole budget
        self.assertEqual(7500, res[4]) # common money
        self.assertEqual(4500, res[5])  # fun money
        self.assertEqual(3000, res[6])  # fun money
        self.assertEqual(375, res[7])  # common limit
        self.assertEqual(225, res[8])  # fun limit

    def test_out_common_money(self):
        res = self.view.getCommonMoney()

        self.assertEqual(res, 7500)

    def test_out_fun_money(self):
        res = self.view.getFunMoney()

        self.assertEqual(res, 4500)

    def test_out_invest_money(self):
        res = self.view.getInvestMoney()

        self.assertEqual(res, 3000)

    def test_out_budget_money(self):
        res = self.view.getBudgetMoney()

        self.assertEqual(res, 15000)

