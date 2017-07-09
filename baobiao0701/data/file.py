import glob,re,os,sys
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from data import basedata


# 用glob 读当前目录下所有的csv文件，读到一个list，再循环调用上面的函数。
# lst = glob.glob(r'^parkout/$./csv')
# print(lst)
# for i3 in lst:
#     A=data_base(i3)
#     A.data_cut()
# path = os.path.dirname(os.path.abspath('data'))
# print(path)

B = basedata.data_base('parkout.csv')
receive_data = B.data_cut()
# print(receive_data)
# print(len(receive_data[0]))
a=[]
for list1 in receive_data:
    for l2 in list1:
        a.append(list(l2))
print(a)
