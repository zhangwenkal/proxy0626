import csv
import pandas as pd

#   数据
# data = [
# {'Petal.Length': '1.4', 'Sepal.Length': '5.1', 'Petal.Width': '0.2', 'Sepal.Width': '3.5', 'Species': 'setosa'},
# {'Petal.Length': '1.4', 'Sepal.Length': '4.9', 'Petal.Width': '0.2', 'Sepal.Width': '3', 'Species': 'setosa'},
# {'Petal.Length': '1.3', 'Sepal.Length': '4.7', 'Petal.Width': '0.2', 'Sepal.Width': '3.2', 'Species': 'setosa'},
# {'Petal.Length': '1.5', 'Sepal.Length': '4.6', 'Petal.Width': '0.2', 'Sepal.Width': '3.1', 'Species': 'setosa'}
# ]
# #   表头
# header = ['Petal.Length', 'Sepal.Length', 'Petal.Width', 'Sepal.Width', 'Species']
# print(len(data))
# with open('E:/dst.csv', 'wb') as dstfile:   #写入方式选择wb，否则有空行
#     writer = csv.DictWriter(dstfile, fieldnames=header)
#     writer.writeheader()    #   写入表头
#     writer.writerows(data)  # 批量写入
# dstfile.close()


# 读取csv文件为DataFrame
# dframe = pd.DataFrame.from_csv('F:\\baobiao0621\\data\\parkin.csv')
# print(type(dframe))
# print(dframe)


with open('F:\\baobiao0621\\data\\parkin.csv') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=None)   # fieldnames默认为None,如果所读csv文件没有表头，则需要指定
    list_1 = [e for e in reader]  # 每行数据作为一个dict存入链表中
csvfile.close()
dfrme = pd.DataFrame.from_records(list_1)
#print(list_1[0])
#print(dfrme.shape)    #返回数据的格式，数组，（行数，列数）
#print(dfrme.loc[1:5])   #返回切片列数据
#print(dfrme['url'])      #返回列
#print(dfrme[1:2])        #返回行
print(dfrme[1:2][:2])