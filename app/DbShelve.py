import shelve
from interfaces.IDataBase import IDataBase

class DbShelve(IDataBase):
    def __init__(self):
        pass

    def update(self, date, wholeBudget, history):
        db = shelve.open('ShelveDb')
        db['history'] = history
        db['payDay'] = date
        db['wholeBudget'] = wholeBudget
        db.close()
    def load(self):
        pass

