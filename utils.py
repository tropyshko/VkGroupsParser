from os import path
import pickle
from elements import *
from time import sleep
from selenium.webdriver.common.keys import Keys
import pyperclip
from script import script
from datetime import datetime

def checktime(group_time,time_diff=24):
    try:
        if time_diff > 24:
            time_diff = 24
        now = datetime.now()
        time_1 = datetime.strptime(str(group_time),'%Y-%m-%d %H:%M:%S.%f')
        diff = (now-time_1).total_seconds() / 60/60
        if diff > time_diff:
            return True
        else:
            return False
    except:
        return True
class Check():
    def ban(self):
        return True
    def limit(self):
        return True
    def captcha(self):
        return True

def tryButton(browser,attempts=20,selector="",xpath="",id="",name=""):
    method_selector = ""
    attempt = 0
    if id:
        method_selector += "1"
    if xpath:
        method_selector += "2"
    if selector:
        method_selector += "3"
    if name:
        method_selector += "4"

    while attempts > attempt:
        if "1" in method_selector:
            try:
                
                browser.find_element("id", id).click()
                break
            except:
                pass
        if "2" in method_selector:
            try:
                browser.find_element("xpath", xpath).click()
                break
            except:
                pass
        if "3" in method_selector:
            try:
                browser.find_element("css_selector", selector).click()
                break
            except:
                pass
        if "4" in method_selector:
            try:
                browser.find_element("name", name).click()
                break
            except:
                pass
        sleep(1)
        attempt+=1
    return False


def tryEnter(browser,attempts=20,selector="",xpath="",id="",name="",text=""):
    method_selector = ""
    attempt = 0
    if id:
        method_selector += "1"
    if xpath:
        method_selector += "2"
    if selector:
        method_selector += "3"
    if name:
        method_selector += "4"
    while attempts > attempt:
        if "1" in method_selector:
            try:
                browser.find_element("id", id).send_keys(text)
                break
            except:
                pass
        if "2" in method_selector:
            try:
                browser.find_element("xpath", xpath).send_keys(text)
                break
            except:
                pass
        if "3" in method_selector:
            try:
                browser.find_element("css_selector", selector).send_keys(text)
                break
            except:
                pass
        if "4" in method_selector:
            try:
                browser.find_element("name", name).send_keys(text)
                break
            except:
                pass
        sleep(1)
        attempt+=1
    return False

def tryEnterCP(browser,attempts=20,selector="",xpath="",id="",name="",text=""):
    method_selector = ""
    attempt = 0
    if id:
        method_selector += "1"
    if xpath:
        method_selector += "2"
    if selector:
        method_selector += "3"
    if name:
        method_selector += "4"
    pyperclip.copy(text)
    while attempts > attempt:
        if "1" in method_selector:
            try:
                browser.find_element("id", id).send_keys(Keys.CONTROL + "v")
                break
            except:
                pass
        if "2" in method_selector:
            try:
                browser.find_element("xpath", xpath).send_keys(Keys.CONTROL + "v")
                break
            except:
                pass
        if "3" in method_selector:
            try:
                browser.find_element("css_selector", selector).send_keys(Keys.CONTROL + "v")
                break
            except:
                pass
        if "4" in method_selector:
            try:
                browser.find_element("name", name).send_keys(Keys.CONTROL + "v")
                break
            except:
                pass
        sleep(1)
        attempt+=1
    return False

def tryCheck(browser,attempts=10,selector="",xpath="",id="",name="",text=""):
    method_selector = ""
    attempt = 0
    if id:
        method_selector += "1"
    if xpath:
        method_selector += "2"
    if selector:
        method_selector += "3"
    if name:
        method_selector += "4"
    while attempts > attempt:
        if "1" in method_selector:
            try:
                browser.find_element("id", id)
                return True
            except:
                pass
        if "2" in method_selector:
            try:
                browser.find_element("xpath", xpath)
                return True
            except:
                pass
        if "3" in method_selector:
            try:
                browser.find_element("css_selector", selector)
                return True
            except:
                pass
        if "4" in method_selector:
            try:
                browser.find_element("name", name)
                return True
            except:
                pass
        sleep(1)
        attempt+=1
    return False

def get_cookies(name):
    if path.exists(f"{name}.pkl"):
            with open(f"{name}.pkl", 'rb') as file:
                return pickle.load(file)                
    else:
        return False

def save_cookies(cookies,name):
    with open(f"{name}.pkl", 'wb') as file:
        pickle.dump(cookies, file)

