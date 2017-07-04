import glob,re,os

# 用glob 读当前目录下所有的csv文件，读到一个list，再循环调用上面的函数。
# lst = glob.glob(r'^parkout/$./csv')
# print(lst)
# for i3 in lst:
#     A=data_base(i3)
#     A.data_cut()
path = os.path.dirname(os.path.abspath('data'))
print(path)