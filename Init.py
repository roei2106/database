
class Init:
    def __init__(self):
        self.dict = {}

    def set_value(self, key, val):
        self[key] = val

    def get_value(self, key):
        if key in self:
            return self[key]
        return None

    def delete_value(self, key):
        if key in self:
            c = self[key]
            del self[key]
            return c
        return None
    
    import pickle
from database import DataBase


class BaseData(DataBase):
    def __init__(self, file):
        super().__init__(file)

    def get_value(self, key):
        file = open("roei.txt", "w")
        self.dict = pickle.load(file)
        file.close()
        return super().get_value(key)

    def set_value(self, key, val):
        file = open("roei.txt", "w")
        self.dict = pickle.load(file)
        file.close()
        super().get_value(key)

    def delete_value(self, key):
        self.dict = super().delete_value(key)
        file = open("roei.txt", "w")
        pickle.dump(dict)
        file.close()
