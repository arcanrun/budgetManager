from interfaces.IMoney import IMoney


class CFICommonMoney(IMoney):
    def __init__(self, state):
        self.state = state

    def set(self):
        pass

    def get(self):
        return self.state

    def change(self):
        pass

if __name__ == '__main__':

    print(CFICommonMoney)