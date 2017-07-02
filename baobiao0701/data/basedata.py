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
    def __init__(self,file):
        self.file=file

    def read_csv(self):                                      #读取csv文件
        path = os.getcwd()+'\\'+self.file
        f = open(path, encoding='utf-8')
        self.data = pd.read_csv(f)
        z=(self.data.shape)                                  #返回数据的格式，数组，（行数，列数）
        self.head=list(self.data)                            #将header转换成序列
        # print(aa)

        #遍历csv每行数据
        a,a1=[],[]
        for i in range(z[0]):
            a1=list(self.data.ix[i,:])                     #将每行数据转换成序列
            a.append(a1)                                   #将序列a1, 添加到一个新的序列里面
        return a

    def data_cut(self):                                    #将请求的参数和，响应的参数分开
        receive_b=self.read_csv()
        req_b,resp_b,h_url=[],[],[]                        #req_b,resp_b请求参数和响应参数，分别放到字典中
        for b in receive_b:
            req_b.append(b[1:b.index('nul1')])             #b.index('nul1')从列表中找出nul1第一个匹配项的索引位置
            h_url.append(b[0])
            resp_b.append(b[b.index('nul1')+1:])
        # print(h_url)
        # print(req_b)
        # print(resp_b)

        #将请求参数,响应参数分别整理成字典
        req_dict, resp_dict = {}, {}
        head1 = self.head[1:self.head.index('response')]
        head2 = self.head[self.head.index('response') + 1:]
        #print(head1,head2)
        req_c, resp_c = [], []
        for i1 in req_b:
            req_c.append(dict(zip(head1, i1)))

        for i2 in resp_b:
            resp_c.append(dict(zip(head2, i2)))
        print(req_c)
        print(resp_c)

if __name__=="__main__":
        A=data_base()
        A.data_cut()







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