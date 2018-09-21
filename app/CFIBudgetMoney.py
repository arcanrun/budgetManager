from interfaces.IMoney import IMoney


class CFIBudgetMoney(IMoney):
    def __init__(self, state):
        self.state = state

    def set(self):
        pass

    def get(self):
        return self.state

    def change(self):
        pass