import unittest
import datetime
from app.PayDay import PayDay


class PayDayTest(unittest.TestCase):
    def setUp(self):
        self.payDay = PayDay()
        self.testPayDay = 12
    def test_counting_days_before_pay_day(self):

        self.payDay.setPayDay(self.testPayDay)
        days = self.payDay.daysBeforePay()

        self.assertEqual(days, 21) # 19 becasue of today date

    def test_date_of_next_payment(self):

        self.payDay.setPayDay(self.testPayDay)
        payDay = self.payDay.getPayDay()

        self.assertEqual(payDay, 12)

    def test_date_format_of_next_payment(self):

        self.payDay.setPayDay(self.testPayDay)
        nextPayDate = self.payDay.getDateNextPay()

        self.assertEqual(nextPayDate, datetime.date(datetime.date.today().year, datetime.date.today().month % 12 + 1, self.testPayDay))

    def test_on_edit_change_date(self):

        self.payDay.setPayDay(15)
        payDay = self.payDay.getPayDay()

        self.assertEqual(payDay, 15)

        self.payDay.setPayDay(20)
        payDay = self.payDay.getPayDay()

        self.assertEqual(payDay, 20)