from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class liker_Bot:
    def __init__(self,username,password):
        self.username=username
        self.password=password
        self.bot=webdriver.Firefox()
############################# Instagram ##############################################
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

    def Ilike(self,hashtag):
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
        
######################### Twitter ###########################################

    def Tlogin(self):
        bot =self.bot
        #bot.get('https://facebook.com/')
        bot.get("https://twitter.com/home/")
        time.sleep(5)   #time to load up the webpage
        # email=bot.find_element_by_name('session[username_or_email]')
        # password=bot.find_element_by_name('session[password]')
        # #email.clear()
        # #password.clear()
        # # email.send_keys(self.username)
        # # password.send_keys(self.password) 
        # # password.send_keys(Keys.RETURN)
        # time.sleep(3)

    def Tlike(self,hashtag):
        bot=self.bot
        bot.get("https://twitter.com/search?q="+hashtag+"&src=typed_query")
        time.sleep(3)
        for _ in range(1,4):
            bot.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(2)
            tweets=bot.find_element_by_class_name("tweet")
            links=[elem.get_attribute('data-permalink-path') for elem in tweets]
            for link in links:
                bot.get("https://twitter.com"+ link)
                try:
                    bot.find_element_by_class_name("HeartAnimation").click()
                    time.sleep(10)


                except Exception as ex:
                    time.sleep(20)
                    











# ed=liker_Bot('humble__bubble','@mytestingpwd')    
# ed.login()  
#ed.like_post("quote")

# uname=input('Enter the username : ')
# pwd=input("Enter the password : ")
uname="humble__bubble"
pwd="@mytestingpwd"
hashtag="quote"
ed=liker_Bot(uname,pwd)    
ed.Tlogin()  
ed.Tlike(hashtag)


