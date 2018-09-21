import unittest
from app.BudgetCFI import BudgetCFI
from interfaces.IMoney import IMoney


class BudgetCFITest(unittest.TestCase):
    def setUp(self):
        self.budgetManager = BudgetCFI()

    def test_if_returning_value_is_instance_of_IMoney(self):

        data = 10000

        returning_val = self.budgetManager.execute(data)

        for v in returning_val:
            self.assertEqual(v.__class__.__bases__[0].__name__, IMoney.__name__)

    def test_right_calculation(self):

        data = 10000

        returning_val = self.budgetManager.execute(data)
        arr = [i.state for i in returning_val]

        self.assertEqual(arr, [5000, 3000, 2000, 10000])


