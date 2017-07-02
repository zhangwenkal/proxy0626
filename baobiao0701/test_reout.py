import unittest
from datetime import datetime
import requests
import time,sys,csv,json
import HTMLTestRunner
from data import basedata_1

# Create your tests here.
class Tquery(unittest.TestCase):
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

if __name__=='Tquery':
    testload=unittest.TestLoader().loadTestsFromTestCase(Tquery)
    realtest=unittest.TestSuite(testload)
    fp=open("F:\\baobiao0621\\report\\result1.html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='出场报表',description='record_out')
    runner.run(realtest)
