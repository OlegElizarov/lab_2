# coding=utf-8

import time


class timer():
    def __enter__(self):
        self.t = time.clock()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.t = time.clock() - self.t
        print (self.t)
