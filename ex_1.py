#!/usr/bin/env python3
# coding=utf-8
from librip.gens import *

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# realize task
field(goods,'title','price','color')
field(goods,'title','price')
field(goods,'title')
field(goods,None)
gen_random(0,6,2)
