from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddPIMPage import AddPIM

import pytest
import time
class Test_003_PIM:
    baseURL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_addPIM(self,setup):
        self.driver = setup
        # self.logger.info("*****verify loginpage****")
        self.driver.get(self.baseURL)
        time.sleep(3)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        print(act_title)
        time.sleep(3)
#******* AddPIM ********
        self.addPIM=AddPIM(self.driver)
        self.addPIM.clickOnCutomerMenu()
        time.sleep(3)
        self.addPIM.clickOnAddButton()
        time.sleep(3)
        self.addPIM.setFirstName()
        self.addPIM.setMiddleName()
        self.addPIM.setLastName()
        time.sleep(3)
        self.addPIM.clickSave()
        time.sleep(4)
        self.msg= self.addPIM.toast_successful_xpath.title()
        print(self.msg)
        if "Success" in self.msg:
            assert True==True
        else:
            self.driver.save_screenshot(".\\screenshots\\"+"testaddPIM.png")
            assert True==False
            self.driver.close()