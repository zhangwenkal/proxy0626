import csv
import glob
import pandas as pd


#使用DictReader，和reader函数类似，接收一个可迭代的对象，能返回一个生成器，
# 但是返回的每一个单元格都放在一个字典的值内，而这个字典的键则是这个单元格的标题（即列头）
# with open('F:\\baobiao0621\\data\\parkin.csv') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         print(row)
...

# with open('F:\\baobiao0621\\data\\parkin.csv','r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     column = [row for row in reader]
#     print (column)

# 按行读取
# with open('F:\\baobiao0621\\data\\parkin.csv','r') as csvfile:
#     reader = csv.reader(csvfile)
#     rows= [row for row in reader]
#     print(rows)


obj=pd.read_csv('F:\\baobiao0621\\data\\parkin.csv')
#print(obj)
print(obj[2:3])
# print(type(obj))
# print(obj.dtypes)


#用glob 读当前目录下所有的csv文件，读到一个list，再循环调用上面的函数。

# lst = glob.glob("F:\\baobiao0621\\data\\*.csv")
# for i in lst:
#     print(i)

