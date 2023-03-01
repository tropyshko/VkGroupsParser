from os import path
import pickle
import time
from utils import tryButton,tryEnter, get_cookies,save_cookies,tryCheck
from elements import *

class Auth():
    def __init__(self, browser,login,passw) -> None:
        self.browser = browser
        self.login = login
        self.passw = passw

    def number(self):
        tryEnter(browser=self.browser,xpath=login_Input_xpath,selector=login_Input_selector,id=login_Input_id,name=login_Input_name,text=self.login)
        tryButton(browser=self.browser,xpath=loginEnter_Button_xpath,selector=loginEnter_Button_selector,id=loginEnter_Button_id,name=loginEnter_Button_name)

    def password(self):
        tryEnter(browser=self.browser,xpath=password_Input_xpath,selector=password_Input_selector,id=password_Input_id,name=password_Input_name,text=self.passw)
        tryButton(browser=self.browser,xpath=passwordEnter_Button_xpath,selector=passwordEnter_Button_selector,id=passwordEnter_Button_id,name=passwordEnter_Button_name)

    def F2A(self):
        pass
    
    def sms(self):
        tryButton(browser=self.browser,xpath=selectPassword_Button_xpath,selector=selectPassword_Button_selector,id=selectPassword_Button_id,name=selectPassword_Button_name)

    def check_auth(self):
        if(tryButton(browser=self.browser,xpath=checkAuth_Button_xpath,selector=checkAuth_Button_selector,id=checkAuth_Button_id)):
            return True
        else:
            return False

    def authMain(self):
        self.browser.get("https://vk.com/")
        self.number()
        self.sms()
        self.password()
        self.browser.get("https://vk.com/")
        time.sleep(15)
        save_cookies(self.browser.get_cookies(),self.login)

    def authCookies(self):
        file = get_cookies(self.number)
        if file!=False:
            for cookie in file:
                self.browser.add_cookie(cookie)
            self.browser.refresh()
        else:
            return False
    
    def main(self):
        if (self.authCookies()==False):
            self.authMain()
        # return tryCheck(browser=self.browser,selector=ban_Label_selector,xpath=ban_Label_xpath,id=ban_Label_id,name=ban_Label_name)
        return True