
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
        

from threading import *
from basedata import BaseData

sem = Semaphore(10)
lock = Semaphore(1)
based = BaseData()


def sync(func, key, val):
    if func == 'r':
        sem.acquire()
        based.get_value(key)
    if func == 'd':
        sem.acquire(10)
        lock.acquire()
        based.set_value(key, val)
    if func == 'w':
        sem.acquire(10)
        lock.acquire(key, val)


def main():
    threads = []
    data = ''
    while True:
        for i in range(10):
            func = input("w - writing, r - reading, d - deleting:")
            key = input()
            val = input()
            t = Thread(target=sync, args=(func, key, val))
            threads.insert(i, t)


if __name__ == "__main__":
    main()

