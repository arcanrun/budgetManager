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

        print(db['wholeBudget'])
        print(db['history'])
        print(len(db))

        db.close()

    def load(self):
        pass

