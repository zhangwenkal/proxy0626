import pandas as pd
import os

path = os.getcwd()+'\\data\\parkin.csv'
f = open(path, encoding='utf-8')
data = pd.read_csv(f)
#print(data)

#数据统计
#print(data.describe())

#读取csv前5行
#headdata = data.head(5)
#print(headdata)


#第一行所有列的数据
#print(data.ix[0,:])
#print(type(data.ix[1,:]))
a=list(data.ix[0,:])
print(a)
b=a.index('nan')                      #从列表中找出某个值第一个匹配项的索引位置
print(b)
#print(type(dict(data.ix[1,:])))

#获取第2/4/6行的数据
#print(data.ix[[1,3,5],:])

#获取所有行所有列
#print(data.ix[:, :])

#读取username列所有的数据
#print(data.ix[:, 'username'])

#读取
#print(data.ix[[1,3,5], ['username','verified_type','comment']])