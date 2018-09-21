from interfaces.IMoney import IMoney


class CFIFunMoney(IMoney):
    def __init__(self, state):
        self.state = state

    def set(self):
        pass

    def get(self):
        return self.state

    def sub(self, data):
        self.state -= data

    def add(self, data):
        self.state += data