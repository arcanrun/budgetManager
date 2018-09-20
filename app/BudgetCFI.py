from interfaces.IBudgetManager import IBudgetManager
from interfaces.IMoney import IMoney
from app.CFICommonMoney import CFICommonMoney
from typing import List


class BudgetCFI(IBudgetManager):
    def execute(self, data) -> List[IMoney]:
        return CFICommonMoney(data*0.5)