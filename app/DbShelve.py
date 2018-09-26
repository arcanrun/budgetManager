import shelve
from interfaces.IDataBase import IDataBase


class DbShelve(IDataBase):
    def __init__(self):
        pass

    def update(self, date, wholeBudget, history):
        pass
        db = shelve.open('ShelveDb')

        db['history'] = history
        db['payDay'] = date
        db['wholeBudget'] = wholeBudget

        db.close()

    def clear(self):
        db = shelve.open('ShelveDb')
        db.clear()
        db.close()

    def load(self):
        pass

