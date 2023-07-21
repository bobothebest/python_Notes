#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 15:13:52 2023

@author: zzy
pandas 简易操作
"""

import numpy as np
import pandas as pd
#创建dataframe
df = pd.DataFrame(data = np.random.random(size = (100,3)), columns = ['a','b','c'])
df
#给行和列命名
df = pd.DataFrame(data = np.random.random(size = (5,3)), columns = ['a','b','c'],index = ['1','2','3','4','5'])
df
#取出某一列
df.iloc[0,:]
#画图(折线图)
df = pd.DataFrame(data = np.random.random(size = (100,3)), columns = ['a','b','c'])
df
df.plot()
#画直方图
df.hist()
#拼接两个dataframe(拼接的时候要保证行数一致)
df1 = pd.DataFrame(np.random.random((3,4)),
                   columns = ['a','b','c','d'])
df2 = pd.DataFrame(np.random.random((3,1)),
                   columns = ['q'])
df1.join(df2)

#创建series
s = pd.Series(data = np.random.random(size = 5),
              index = ['a','b','c','d','e'])
s
s * 10
#删去第一个数
s.shift(1)

#使用pandas创建时间序列数据
index = pd.date_range('2020-08-01',periods = 10) 
index
index = pd.date_range('2020-08-15 12:00:00',periods = 10,freq = 'h') 
index
index = pd.date_range('2020-08-01','2020-08-31') 
index
data = np.random.random(31)
s = pd.Series(data = data, index = index)
s.head()
s.tail()

#读取csv数据
df = pd.read_csv('/Users/apple/Downloads/科科/python_Notes/AAPL.csv')
df.tail()

df.index = df['Date']#将Date列设定为index
s = df['Adj Close']#从中取出一列记为Series
s.plot()


df = pd.read_csv('/Users/apple/Downloads/科科/python_Notes/AAPL.csv')
# set the date as index
df.index = pd.to_datetime(df['Date']) # converting from string to datetime
 
# extract 1 column of data 
price = df['Adj Close'] 
# create a new DataFrame for 1-year worth of events
index = pd.date_range(start='2020-01-01', end='2021-01-01')
df = pd.DataFrame(index=index)
df['price'] = price # copy the column (matching index only)
df.ffill(inplace=True) # fill in na values with previous
 
# calculate 30-day rolling mean, store into DataFrame
rm = df.rolling(30).mean()
df['rm'] = rm
 
# plot price and rolling mean:
df.plot()

# create a data structure to keep track of buy/sell signal
signal = pd.Series(index=df.index, dtype=float)
 
# iterate over all periods;  set the signal to buy (+1) or sell (-1) 
for i in range(30, len(df.index)):
    
    if df['price'].iloc[i] > df['rm'].iloc[i]:
        signal[i] = 1 # buy
    else:
        signal[i] = -1 # sell
        
# add the columnb signal into the data frame        
df['signal'] = signal


# calculate the market return for a buy-and-hold investor
mkt_return = df['price'] / df['price'].shift(1) - 1
df['mkt_ret'] = mkt_return
df.tail()

# the strategy return is the market return multiplied by the signal
df['str_ret'] = df['mkt_ret'] * df['signal']
df.tail()

# calculate the abnormal return:
df['ab_ret'] = df['str_ret'] - df['mkt_ret']
df.tail()

# calculate and plot the cumulative sum of returns
df[['mkt_ret', 'str_ret', 'ab_ret']].cumsum().plot()



