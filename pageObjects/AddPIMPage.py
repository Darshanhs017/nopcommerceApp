from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
class AddPIM():
    lnkCustomer_menu_xpath="//span[text()='PIM']"
    btnAdd_xapth="//button[normalize-space()='Add']"
    txtFirst_name="firstName"
    txtMiddle_name="middleName"
    txtLast_name="lastName"
    btnsave_xapth="//button[normalize-space()='Save']"
    toast_successful_xpath="//div[@class='oxd-toast-content oxd-toast-content--success']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCutomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_menu_xpath).click()
    def clickOnAddButton(self):
        self.driver.find_element(By.XPATH,self.btnAdd_xapth).click()
    def setFirstName(self):
        self.driver.find_element(By.NAME,self.txtFirst_name).send_keys("Jimy")
    def setMiddleName(self):
        self.driver.find_element(By.NAME,self.txtMiddle_name).send_keys("saul")
    def setLastName(self):
        self.driver.find_element(By.NAME,self.txtLast_name).send_keys("goodman")
    def clickSave(self):
        self.driver.find_element(By.XPATH,self.btnsave_xapth).click()
    def successmsg(self):
        self.driver.find_element(By.XPATH,self.toast_successful_xpath)


