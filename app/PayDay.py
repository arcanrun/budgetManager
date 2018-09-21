from interfaces.ITimeLine import ITimeLine
import datetime

class PayDay(ITimeLine):
    def __init__(self):
        self.payDay = None
        self.now = datetime.date.today()

    def setPayDay(self, day):
        self.payDay = int(day)

    def getPayDay(self):
        return self.payDay

    def daysBeforePay(self):
        payDay = self.getDateNextPay()

        amountDays = payDay - self.now

        return amountDays.days

    def getDateNextPay(self):
        payDay = datetime.date(
            datetime.date.today().year,
            datetime.date.today().month % 12 + 1,
            self.payDay
        )

        return payDay
