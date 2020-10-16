from selenium import webdriver
from selenium.webdriver.remote.command import Command
from selenium.webdriver.common.keys import Keys
import time


class InstaBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def Login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        bot.find_element_by_class_name('aOOlW.bIiDR').click()
        time.sleep(3)
        username = bot.find_element_by_name('username')
        password = bot.find_element_by_name('password')
        username.clear()
        password.clear()
        username.send_keys(self.username)
        password.send_keys(self.password)
        time.sleep(3)
        bot.find_element_by_class_name('Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB').click()
        time.sleep(5)


    def openStories(self):
        bot = self.bot
        bot.find_element_by_class_name('sqdOP.yWX7d.y3zKF').click()
        time.sleep(3)
        bot.find_element_by_class_name('aOOlW.HoLwm').click()
        time.sleep(3)
        bot.find_element_by_class_name('Ckrof').click()
        time.sleep(5)
        i = 0
        while i < 1000:
            time.sleep(2)
            bot.find_element_by_class_name('ow3u_').click()



go = InstaBot('your_username','your_password') # @interessanti_curiosita
go.Login()
go.openStories()
