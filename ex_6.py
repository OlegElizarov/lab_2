#!/usr/bin/env python3
# coding=utf-8

import json
import sys
from librip.ctxmngrs import timer
from librip.decorators import print_result
from librip.gens import field, gen_random
from librip.iterators import Unique

path = sys.argv[1]
print (path)
# Здесь необходимо в переменную path получить
# путь до файла, который был передан при запуске

with open(path) as f:
    data = json.load(f)


# Далее необходимо реализовать все функции по заданию, заменив `raise NotImplemented`
# Важно!
# Функции с 1 по 3 дожны быть реализованы в одну строку
# В реализации функции 4 может быть до 3 строк
# При этом строки должны быть не длиннее 80 символов

@print_result
def f1(arg):
    a = field(data, arg)
    a = Unique(a, x=True)

    return a.items


@print_result
def f2(arg):
    q=[]
    for x in arg:
        if str(x).startswith('программист'):
            q.append(x)
    if len(q)==0:
        q.append(None)
    q=list(q)
    return q


@print_result
def f3(arg):
    w=list(map(lambda x: x+' на питоне',arg))
    return w

@print_result
def f4(arg):
    j=list(zip(arg,['зарплата-' for i in range(len(arg))],gen_random(100000,200000,len(arg))))
    return j


# with timer():
#    f4(f3(f2(f1(data))))

x1=f1("job-name")
x2=f2(x1)
x3=f3(x2)
x4=f4(x3)
print ()
