import time,sys,csv,json

# csv_reader = csv.reader(open('req.csv', encoding='utf-8'))
# for i in csv_reader:
#     data=i.rstrip().split()
#     print(data)

def read_csv():
    # 按行读取
    with open('F:\\baobiao0621\\data\\req.csv','r') as csvfile:
        reader = csv.reader(csvfile)
        rows= [row for row in reader]
        a1=rows[0][1]

        a2=[]
        for i in rows[1:] :
            i=i[0:2]
            a2.append(i)
        a2=dict(a2)                                    #嵌套序列转换成字典

        a3 = []
        for j in rows[0:4]:
            j = j[2:4]
            a3.append(j)
        a3 = dict(a3)

    # 按列读取
    # with open('req.csv', 'r') as csvfile:
    #     reader = csv.reader(csvfile)
    #     column = [col[1] for col in reader]
    #     column1= [col[0] for col in reader]
    #     b1=column[0]
    print(a1)
    print(a2)
    print(a3)
    return a1,a2,a3

if __name__=='__main__':
    read_csv()
