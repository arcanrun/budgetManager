from interfaces.IMoney import IMoney


class CFICommonMoney(IMoney):
    def __init__(self, state):
        self.state = state

    def set(self, state):
        self.state = state

    def get(self):
        return self.state

    def sub(self, data):
        self.state -= data

    def add(self, data):
        self.state += data

if __name__ == '__main__':

    print(CFICommonMoney)