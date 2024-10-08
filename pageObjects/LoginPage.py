from selenium.webdriver.common.by import By


class LoginPage:   #step1 Locators
    username_textbox_xpath="//input[@placeholder='Username']"
    password_textbox_xpath="//input[@placeholder='Password']"
    login_button_xpath="//button[normalize-space()='Login']"
    # logout_link_linktext="Logout"

#step 2 --Locators action

    def __init__(self,driver):
        self.driver=driver

    def setUsername(self,username):
        self.driver.find_element(By.XPATH, self.username_textbox_xpath).clear()
        self.driver.find_element(By.XPATH,self.username_textbox_xpath).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element(By.XPATH,self.password_textbox_xpath).clear()
        self.driver.find_element(By.XPATH,self.password_textbox_xpath).send_keys(password)
    def clickLogin(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()
    # def clickLogout(self):
    #     self.driver.find_element(By.LINK_TEXT,self.logout_link_linktext).click()


