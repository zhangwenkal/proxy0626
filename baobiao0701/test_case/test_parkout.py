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
    # def __init__(self,re_url,req_test,res_test):
    #     self.url=re_url
    #     self.req_test=req_test
    #     self.res_test=res_test

    # def receive_param(self):
    #     B=basedata.data_base('parkout.csv')
    #     receive_data=B.data_cut()
    #     print(receive_data)
    #     self.url=receive_data[0]
    #     self.req_test=receive_data[1]
    #     self.res_test=receive_data[2]

    def setUp(self):
        print('start test')

    def test_query(self):
        # url=self.url
        # payload=self.req_test
        # b3=self.res_test
        B = basedata.data_base('parkout.csv')
        receive_data = B.data_cut()
        for re_data in receive_data:
            r=requests.post(re_data[0],data=re_data[1])
            result=r.json()
            print(result)
            self.assertEqual(re_data[2], result)

if __name__=='__main__':
    # testload=unittest.TestLoader().loadTestsFromTestCase(Tquery)
    # realtest=unittest.TestSuite(testload)
    # fp=open("F:\\baobiao0621\\report\\result1.html",'wb')
    # runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='出场报表',description='record_out')
    # runner.run(realtest)
    '''
     B=basedata.data_base('parkout.csv')
    receive_data=B.data_cut()
    #print(receive_data)
    for re_data in receive_data:
        C = Tquery(re_data[0], re_data[1], re_data[2])
    '''

    testload=unittest.TestLoader().loadTestsFromTestCase(Tquery)
    realtest=unittest.TestSuite(testload)
    fp=open("..\\report\\result1.html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='出场报表',description='record_out')
    runner.run(realtest)




