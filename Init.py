
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


import multiprocessing
import threading
from threading import *
from basedata import BaseData


class Sync(BaseData):
    MAX_SEMAPHORES = 10

    def __init__(self, thread_mode):
        super(Sync, self).__init__()
        if thread_mode:
            self.lock = threading.Lock()
            self.sem = threading.Semaphore(self.MAX_SEMAPHORES)
        else:
            self.lock = multiprocessing.Lock()
            self.sem = multiprocessing.Semaphore(self.MAX_SEMAPHORES)

    def write_lock(self):
        self.lock.acquire()
        for i in range(self.MAX_SEMAPHORES):
            self.sem.acquire()

    def write_release(self):
        self.lock.release()
        for i in range(self.MAX_SEMAPHORES):
            self.sem.release()

    def read_lock(self):
        self.lock.acquire()
        self.sem.acquire()

    def read_release(self):
        self.lock.release()
        self.sem.release()

    def get_value(self, key):
        self.read_lock()
        super(Sync, self).get_value()
        self.read_release()
        
    def set_value(self, key, val):
        self.write_lock()
        super(Sync, self).set_value()
        self.write_release()
        
    def delete_value(self, key):
        self.write_lock()
        super(Sync, self).delete_value()
        self.write_release()


