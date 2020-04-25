# #############################################  Libraries  ################################################################
from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import sys
# Create your views here.

# ###########################################################################################################
def index(request):
    return render(request,'Basics.html')

def index1(request):
    return render(request,'instagram.html')


def index2(request):
    return render(request,'Twitter.html')    
    
def index3(request):
    return render(request,'LinkedIn.html')    
#######################################################################################33333

def print_same_line(text):
    sys.stdout.write('\r')
    sys.stdout.flush()
    sys.stdout.write(text)
    sys.stdout.flush()


########################INSTAGRAM#########################################################




class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(3)
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        time.sleep(3)

        user_name_elem = driver.find_element_by_xpath("//input[@name='username']")
        user_name_elem.clear()
        user_name_elem.send_keys(self.username)

        pwd = driver.find_element_by_xpath("//input[@name='password']")
        pwd.clear()
        pwd.send_keys(self.password)
        pwd.send_keys(Keys.RETURN)
        time.sleep(3)


    def like_photo(self, hashtag):
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/" + hashtag + "/")
        time.sleep(3)

        # gathering photos
        pic_hrefs = []
        for _ in range(1, 7):
            try:
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                # print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        # Liking photos
        unique_photos = len(pic_hrefs)
        for pic_href in pic_hrefs:
            driver.get(pic_href)
            time.sleep(3)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(random.randint(2, 4))
                like_button = lambda: driver.find_element_by_xpath('//span[@aria-label="Like"]').click()
                like_button().click()
                for second in reversed(range(0, random.randint(18, 28))):
                    print_same_line("#" + hashtag + ': unique photos left: ' + str(unique_photos)
                                    + " | Sleeping " + str(second))
                    time.sleep(1)
            except Exception:
                time.sleep(3)
            unique_photos -= 1

def insta_liker(request):
    username = request.GET['uname']
    password = request.GET['psw']
    print(username,password)
    ig = InstagramBot(username, password)
    ig.login()
    hashtags=request.GET['Hashtag']
    while True:
        try:
            # Choose a random tag from the list of tags
            
            ig.like_photo(hashtags)
        except Exception:
            ig.closeBrowser()
            time.sleep(60)
            ig = InstagramBot(username, password)
            ig.login()

    return render(request,'instagram.html')
      


######################################     TWITTER     ##########################################
def Twitter_fun(request):
    class TwitterBot:
        def __init__(self, username, password):
            self.username = username
            self.password = password
            self.bot = webdriver.Firefox()

        def login(self):
            bot = self.bot
            bot.get('https://twitter.com/')
            time.sleep(3)

            email = bot.find_element_by_class_name('text-input')
            password = bot.find_element_by_name('session[password]')
            email.clear()
            password.clear()
            email.send_keys(self.username)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(5)

        def like(self,hashtag):
            bot = self.bot
            bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
            time.sleep(3)


            for _ in range(1,5):
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(3)
                
                tweets = bot.find_elements_by_class_name('tweet')
                links = [elem.get_attribute('data-permalink-path')for elem in tweets]
                print(links)
                
                # for link in links:
                #     bot.get('https://twitter.com'+link)
                #     try:
                #        # bot.find_element_by_class_name('HeartAnimation').click()
                #         pyautogui.click(pyautogui.locateCenterOnScreen('1.png'),duration=2)
                #         time.sleep(10)
                #     except Exception as ex:
                #         time.sleep(60) 
                #   

    # hashta = request.POST.get('High','')
    # userna= request.POST.get('uname','')
    # passwor = request.POST.get('psw','')
    hasta = request.GET['High']
    userna = request.GET['uname']
    passwor = request.GET['psw']

    # print(username)

    # print(username)

    # print(username)


    T= TwitterBot(userna,passwor) 
    T.login()
    T.like(hasta)
         
    return render(request,'Twitter.html')
    ##########################################      LINKED IN     #########################################


def LinkedIn_fun(request):
    class LinkedINBot:
        def __init__(self, username, password):
            self.username = username
            self.password = password
            self.bot = webdriver.Firefox()

        def L_login(self):
            bot = self.bot
            bot.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
            time.sleep(3)
            
            email = bot.find_element_by_xpath("//input[@id='username']")
            password = bot.find_element_by_xpath("//input[@id='password']")
            email.clear()
            password.clear()
            email.send_keys(self.username)
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN)
            time.sleep(5)

        def L_like(self,hashtag):
            bot = self.bot
            bot.get('https://www.linkedin.com/search/results/content/?keywords='+ hashtag +'&origin=SWITCH_SEARCH_VERTICAL')
            time.sleep(3)
            
            c=0
            for _ in range(0,8):
                
                try:    
                    like=bot.find_element_by_xpath('//*[@class="reactions-react-button ember-view"]')
                    like.click()
                    c=c+1
                    time.sleep(3)
                except:
                    c=c-1
                    continue   
                bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(5)

            print("No. of likes : ",c)

        
    hashtag_LinkedIn = request.GET['Hashtag_linked']
    username_LinkedIn = request.GET['username_linked']
    password_LinkedIn = request.GET['password_linked']
    print(username_LinkedIn)
    print(password_LinkedIn)
    print(hashtag_LinkedIn)
    L= LinkedINBot(username_LinkedIn,password_LinkedIn) 
    L.L_login()
    L.L_like(hashtag_LinkedIn)
    return render(request,'LinkedIn.html')

