#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 16:36:56 2023

@author: zzy
主要是想备忘一下python的常用操作，不然总是忘
这个文件是用python读取文件
"""

'''
Don’t forget!

Test your code carefully!
这样一个文档，等价于
Don’t forget!\n\Test your code carefully!\n
'''

f = open('/Users/apple/Downloads/reminder.csv', 'r')
f.readline()
f = open('/Users/apple/Downloads/reminder.csv', 'r')
f.read()

'''
courses.csv

cs,111,MwF 10-11
MA,123,TR 3-5
Cs,105,MWF 1-2
EC,100,MWF 2-3

csv文件在txt中是用逗号分隔的，
'''
file = open('/Users/apple/Downloads/courses.csv', 'r')
count = 0
for line in file:
    line = line[:-1]
    fields = line.split(',')
    if fields[0] =='cs':
        print(fields[0],fields[1])
        count += 1

#用pandas打开csv
df = pd.read_csv('/Users/apple/Downloads/科科/python_Notes/AAPL.csv')
df.tail()






