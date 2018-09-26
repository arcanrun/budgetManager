from interfaces.IHistory import IHistory


class History(IHistory):
    def __init__(self):
        self.db = None
        self.historyDict = {}


    def addToHistory(self, transName, money, obj, date, wholeBudget):
        res = '{}{}:{}'.format(transName, obj.name, float(money))

        if str(date) in self.historyDict:
            self.historyDict[str(date.now)].append(res)
        else:
            self.historyDict[str(date.now)] = [res]
            self.save(date, wholeBudget)

    def getHistoryDict(self):
        return self.historyDict

    def save(self, date, wholeBudget):
        self.db.update(date, wholeBudget, self.historyDict)


    def setDB(self, db):
        self.db = db