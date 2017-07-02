import unittest,glob
from datetime import datetime
import requests
import time,sys,csv,json,os
import HTMLTestRunner
sys.path.append(os.getcwd() + '/ORMPackage')
from data import basedata

# Create your tests here.
class Tquery(unittest.TestCase):
    def __init__(self,req_test,res_test):
        self.req_test=req_test
        self.res_test=res_test

    def receive_param(self):
        lst = glob.glob("*.csv")
        print(lst)
        #B=data_base()


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
    C=Tquery()
    C.receive_param()
