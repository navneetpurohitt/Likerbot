from selenium import webdriver
from selenium.common.exceptions         import TimeoutException
from selenium.webdriver.support.ui      import WebDriverWait 
from selenium.webdriver.support         import expected_conditions as EC
from selenium.webdriver.chrome.options  import Options
from selenium.webdriver.common.keys     import Keys
import time 

username = 'humble__bubble'
password = '@mytestingpwd'
message  = 'blahblah'
tryTime  = 2

#create driver and log in
driver = webdriver.Firefox()
logIn(driver, username, password, tryTime)

#gets rid of preference pop-up
a = driver.find_elements_by_class_name("HoLwm")
a[0].click()

#go to profile
driver.get("https://www.instagram.com/{}/".format(username))

#go to followers list
followers = driver.find_element_by_xpath("//a[@href='/{}/followers/']".format(username))
followers.click()
time.sleep(tryTime) 

#find all li elements in list
fBody  = driver.find_element_by_xpath("//div[@role='dialog']")
fBody.send_keys(Keys.PAGE_DOWN) 

fList  = fBody.find_elements_by_tag("li")
print("fList len is {}".format(len(fList)))

time.sleep(tryTime)

print("ended")
driver.quit()

