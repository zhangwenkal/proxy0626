import unittest,glob
from datetime import datetime
import requests
import time,sys,csv,json,os
import HTMLTestRunner
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
from data import basedata

# Create your tests here.
class Tquery(unittest.TestCase):
    def __init__(self,req_test,res_test,re_url):
        self.url=re_url
        self.req_test=req_test
        self.res_test=res_test

    # def receive_param(self):
    #     B=basedata.data_base('parkout.csv')
    #     receive_data=B.data_cut()
    #     print(receive_data)
    #     self.url=receive_data[0]
    #     self.req_test=receive_data[1]
    #     self.res_test=receive_data[2]

    def setUp(self):
        print('start test')
        #att=basedata.read_csv()

    def test_query(self):
        url,payload,b3=basedata_1.read_csv()
        r=requests.post(url,data=payload)
        print(r.status_code)
        result=r.json()
        print(b3)
        self.assertEqual(b3, result)

if __name__=='__main__':
    # testload=unittest.TestLoader().loadTestsFromTestCase(Tquery)
    # realtest=unittest.TestSuite(testload)
    # fp=open("F:\\baobiao0621\\report\\result1.html",'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='出场报表',description='record_out')
    # runner.run(realtest)
    B=basedata.data_base('parkout.csv')
    receive_data=B.data_cut()
    print(receive_data)
    print(receive_data[0])
    print(receive_data[1])
    print(receive_data[2])
    C=Tquery(receive_data[0],receive_data[1],receive_data[2])

