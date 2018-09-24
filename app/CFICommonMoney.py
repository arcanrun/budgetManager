from interfaces.IMoney import IMoney


class CFICommonMoney(IMoney):
    def __init__(self, state):
        self.state = state
        self.name = 'common'

    def set(self, state):
        self.state = state

    def get(self):
        return self.state

    def sub(self, data):
        self.state -= data

    def add(self, data):
        self.state += data
