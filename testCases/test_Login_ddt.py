import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities import XLUtils
class Test_002_DDT_Login:
    baseURL="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    path=".//TestData/LoginData.xlsx"
    # username="Admin"
    # password="admin123"
    # logger= LogGen.loggen()

    def test_login_ddt(self,setup):
        self.driver=setup
        # self.logger.info("*****verify loginpage****")
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("No of rows in a excel", self.rows)
        lst_status=[]
        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.pwd = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUsername(self.user)
            self.lp.setPassword(self.pwd)
            self.lp.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="OrangeHRM"


            if act_title==exp_title:
                if self.exp=="pass":
                    lst_status.append("pass")
                elif self.exp=='fail':
                    lst_status.append("fail")
            elif act_title!=exp_title:
                if self.exp=="pass":
                    lst_status.append("fail")
                elif self.exp=="fail":
                    lst_status.append("pass")






