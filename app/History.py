from interfaces.IHistory import IHistory


class History(IHistory):
    def __init__(self):
        self.db = None
        self.historyDict = {}

    def addToHistory(self, transName, money, obj, date):
        res = '{}{}:{}'.format(transName, obj.name, float(money))

        if str(date) in self.historyDict:
            self.historyDict[str(date)].append(res)
        else:
            self.historyDict[str(date)] = [res]

    def getHistoryDict(self):
        return self.historyDict

    def save(self):
        pass

    def setDB(self, db):
        self.db = db