#!/usr/bin/env python3
# coding=utf-8
from librip.gens import *
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
data2= ['A','a','A','b','B']
data3= gen_random(1,3,5)
data2 = Unique(data2, a=True)
data3 = Unique(data3, a=True)
print (data2.items)
print (data3.items)