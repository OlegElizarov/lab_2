# coding=utf-8

import json
import sys

with open("./data_package.json") as f:
    data = json.load(f)

for str in data:
    print str
    for s in str:
        print ("   ")
