from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class liker_Bot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox()

    def login(self):
        bot =self.bot
        #bot.get('https://facebook.com/')
        bot.get("https://www.instagram.com/accounts/login/?source=auth_switcher/")
        time.sleep(5)   #time to load up the webpage
        email=bot.find_element_by_name('username')
        password=bot.find_element_by_name('password')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password) 
        password.send_keys(Keys.RETURN)
        time.sleep(3)

    def like_post(self,hashtag):
        bot=self.bot
        #bot.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        bot.get('https://www.instagram.com/')
        time.sleep(3)
#############scroll
        # for _ in range(0,3):
        #     bot.execute_script('window.scrollTo(document.body.scrollHeight)')
        #     time.sleep(3)
        #     post=bot.find_elements_by_class_name("eLApa")
        #     t=bot.find_element_by_class_name("v1Nh3 kIKUG _bz0w")
        #     links=[elem.get_attribute(t)for elem in post]
        #     print(links)

        #fBody  = bot.find_element_by_xpath("//div[@role='dialog']")
        #fBody.send_keys(Keys.PAGE_DOWN) 


ed=liker_Bot('humble__bubble','@mytestingpwd')    
ed.login()  
#ed.like_post("quote")




