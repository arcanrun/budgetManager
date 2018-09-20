import unittest
from app.BudgetCFI import BudgetCFI
from interfaces.IMoney import IMoney

class BudgetCFITest(unittest.TestCase):
    def setUp(self):
        self.budgetManager = BudgetCFI()

    def test_if_returning_value_is_instance_of_IMoney(self):

        data = 10000

        self.budgetManager.execute(data)

        self.assertIs(self.budgetManager.execute(data), IMoney)


    def test_right_calculation(self):

        data = 10000

        self.budgetManager.execute(data)

        self.assertEqual(self.budgetManager.execute(data), [5000, 3000, 2000, 10000])


