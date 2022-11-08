#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 22:50:34 2022

@author: ml
"""
import json
import matplotlib.pyplot as plt

numlist = []
dict = {}

f = open("/Users/ml/Desktop/midterm-project/numbers.txt", "r")
text = f.read()

for num in text:
    if num.isdigit():
        numlist.append(int(num))

for num in numlist:
    if num in dict.keys():
        dict[num] += 1
    else:
        dict[num] = 1
        
for key, value in dict.items():
    print(f"{key} : {value}")
   
plt.bar(list(dict.keys()), dict.values(), color='g')
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title('Frequency of Text File')
plt.show()

y = json.dumps(dict)
print(y)
with open("out.json", "w") as outfile:
    json.dump(y, outfile)