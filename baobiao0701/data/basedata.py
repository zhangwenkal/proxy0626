import time,sys,csv
import pandas as pd
import os

'''
with open('F:\\baobiao0621\\data\\req.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    rows = [row for row in reader]
    a1=rows
    # for i in rows:
    #     del i[2:4]
    #     #print(i)

    print(rows)
    print(col)

x = [1, 2, 3, 4, 5, 6, 7]

y = ["one", "two", "three", "four", "five"]

dic = dict(zip(x, y))

print(dic)

{1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

'''
class data_base():
    def read_csv(self):                #读取csv文件
        path = os.getcwd()+'\\parkin.csv'
        f = open(path, encoding='utf-8')
        data = pd.read_csv(f)
        z=(data.shape)                 #返回数据的格式，数组，（行数，列数）
        # aa=list(data)                #将header转换成序列
        # print(aa)

        #遍历csv每行数据
        a,a1=[],[]
        for i in range(z[0]):
            a1=list(data.ix[i,:])
            a.append(a1)
        print(a)

    def data_al(self):                #封装参数




if __name__=="__main__":
    data_base().read_csv()


#数据统计
#print(data.describe())

#读取csv前5行
# headdata = data.head(5)
# print(headdata)


#第一行所有列的数据
#print(data.ix[0,:])
#print(type(data.ix[1,:]))
# a=list(data.ix[0,:])
# print(a)
# b=a.index('')                            #从列表中找出某个值第一个匹配项的索引位置
# print(b)
#print(type(dict(data.ix[1,:])))

#获取第2/4/6行的数据
#print(data.ix[[1,3,5],:])

#获取所有行所有列
# print(data.ix[:,:])

#读取username列所有的数据
#print(data.ix[:, 'username'])

#读取
#print(data.ix[[1,3,5], ['username','verified_type','comment']])