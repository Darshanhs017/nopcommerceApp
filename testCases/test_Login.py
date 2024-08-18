import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
class Test_001_Login:
    baseURL="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username="Admin"
    password="admin123"
    logger= LogGen.loggen()


    def test_homepagetitle(self,setup):
        # self.logger.info("*****Test_001_Login****")
        # self.logger.info("*****verifying homepagetitle****")
        self.driver=setup
        self.driver.get(self.baseURL)
        time.sleep(3)
        act_title=self.driver.title
        if act_title=="OrangeHRM":
            assert True
            # self.driver.close()
            # self.logger.info("***** homepagetitle test case passed****")

        else:
            # self.driver.save_screenshot(".\\screenshots\\"+"test_homepagetitle.png")
            assert False
            # self.logger.error("***** homepagetitle test case failed****")


    def test_loginpage(self,setup):
        self.driver=setup
        # self.logger.info("*****verify loginpage****")
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp=LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        if act_title=="OrangeHRM":
            assert True
            # self.driver.close()
            # self.logger.info("***** loginpage test case passed****")

        else:
            self.driver.save_screenshot(".\\screenshots\\"+"test_loginpage.png")
            # self.driver.close()
            assert False
            # self.logger.error("***** loginpage test case passed****")

