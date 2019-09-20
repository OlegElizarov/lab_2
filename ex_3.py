#!/usr/bin/env python3
# coding=utf-8

def sort(items):
    a = False
    b = []
    c = 0
    x = 0
    w = []
    for x in items:
        if x < 0:
            b.append(x)
            c = c + 1
            w.append(abs(x))
        else:
            w.append(x)
    w = sorted(w)
    print (w)
    for x in range(len(w)):
        if -w[x] in b:
            b.remove(-w[x])
            w[x] = w[x] * -1
    return w


data = [4, -30, 100, -100, 123, 1, 0, -1, -4]
# Реализация задания 3

data = sort(data)
print (data)
