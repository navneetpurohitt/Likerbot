
    def Tlogin(self):
        bot=self.bot
        #bot.get('https://facebook.com/')
        bot.get("https://twitter.com/")
        time.sleep(5)   #time to load up the webpage
        email=bot.find_element_by_name('session[username_or_email]')
        password=bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password) 
        password.send_keys(Keys.RETURN)
        time.sleep(3)


uname=input('Enter the username : ')
pwd=input("Enter the password : ")
ed=liker_Bot(uname,pwd)    
ed.login()  
#ed.like_post("quote")




