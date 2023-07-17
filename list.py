#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 17:15:09 2023

@author: apple
主要是想备忘一下python的常用操作，不然总是忘
这个文件是list的用法
"""
#主要介绍下能让代码变简洁的list comprehension
lis = list(range(10))
lis
[3*x for x in lis]
[s[-1]*2 for s in ['go','terriers!']]
[z for z in range(6)]
[z for z in range(6) if z %2 == 1]
[z %4 == 0 for z in [4,5,6,7,8]]
[1 for x in [4,5,6,7,8] if x % 4 == 0]
sum([1 for x in [4,5,6,7,8] if x % 4 == 0])

#Optimizing a List of Choices
words = ['everybody','loves', 'ice', 'cream']
lengths = [len(w) for w in words]
words_and_lens = [[w, len(w)] for w in words]
max(words_and_lens)
scored_words = [[len(w), w] for w in words]
max(scored_words)#max函数比较的是list的第一个元素

