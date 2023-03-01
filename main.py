from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from auth import Auth
from utils import tryButton,tryEnter,tryEnterCP,checktime,Check
from elements import *
from db import AccountsDB,GroupsDB
from selenium_stealth import stealth
from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem
import time
from script import script

class Main():
    def __init__(self,user_login,user_password,proxy_user,proxy_password,proxy_ip,proxy_port,useragent) -> None:

        self.proxy_user = proxy_user
        self.proxy_password = proxy_password
        self.proxy_ip = proxy_ip
        self.proxy_port = proxy_port
        self.user_login = user_login
        self.user_password = user_password
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_experimental_option('useAutomationExtension', False)
        self.options.add_argument(r'.\auth')

        if(self.proxy_ip):
            self.add_proxy()
        self.browser = webdriver.Chrome("chromedriver", options=self.options)
        if useragent:
            user_agent = useragent
        else:
            user_agent = self.add_useragent()


        stealth(
            driver= self.browser,
            user_agent = user_agent,
            languages = ["ru-RU", "ru"],
            vendor = "Google Inc.",
            platform = "Win32",
            webgl_vendor = "Intel Inc.",
            renderer = "Intel Iris OpenGL Engine",
            fix_hairline = False,
            run_on_insecure_origins = False,
        )
    def add_proxy(self):
        PROXY = f"{self.proxy_user}:{self.proxy_password}@{self.proxy_ip}:{self.proxy_port}"
        self.options.add_argument('--proxy-server=http://%s' % PROXY)
    
    def add_useragent(self):
        print('USERAGENT')
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   
        user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        user_agent = user_agent_rotator.get_random_user_agent()
        AccountsDB().add_useragent(self.user_login,user_agent)
        return user_agent
        
    def subscribe(self):
        tryButton(browser=self.browser,attempts=5,selector=subscribe_Button_selector,xpath=subscribe_Button_xpath,id=subscribe_Button_id,name=subscribe_Button_name)

    def write_post(self):
        tryEnter(browser=self.browser,selector=post_Input_selector,xpath=post_Input_xpath,id=post_Input_id,name=post_Input_name,text=script)

    def write_post__cp(self):
        tryEnterCP(browser=self.browser,selector=post_Input_selector,xpath=post_Input_xpath,id=post_Input_id,name=post_Input_name,text=script)

    def send_post(self):
        tryButton(browser=self.browser,selector=postSend_Button_selector,xpath=postSend_Button_xpath,id=postSend_Button_id,name=postSend_Button_name)

    def open_group(self, group):
        self.browser.get(group)

    def login(self):
        status = Auth(browser=self.browser,login=self.user_login,passw=self.user_password).main()
        return status

    def main(self):
        groups = GroupsDB().get_groups()
        x = 0
        for group in groups:
            try:
                x+= 1
                lastPost = group[4]
                ct = checktime(group_time=lastPost,time_diff=24)
                print(x,group[1],group[2])
                if ct:
                    self.open_group(group[1])
                    self.subscribe()
                    # self.write_post()
                    self.write_post__cp()
                    self.send_post()
                    st = Check().limit()
                    if st:
                        pass
                    GroupsDB().change_group(group[1])
                    time.sleep(10)
            except Exception as e:
                print(e)
            time.sleep(5)

    def test(self):
        self.browser.get("https://2ip.ru")
  
def main():
    accounts = AccountsDB().get_accounts()
    for account in accounts:
        user_login = account[1]
        user_password = account[2]
        proxy_ip = account[3]
        proxy_port = account[4]
        proxy_user = account[5]
        proxy_password = account[6]
        useragent = account[7]
        work = Main(user_login,user_password,proxy_user,proxy_password,proxy_ip,proxy_port,useragent=useragent)
        auth = work.login()
        st = Check().ban()
        if st:
            if auth:
                work.main()


main()