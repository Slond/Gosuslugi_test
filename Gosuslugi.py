from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import os

login = '' # Значение логина
password = '' # Значение пароля
dir = os.path.abspath(os.curdir)
new_dir = dir+'/passport'

try:
    os.mkdir(new_dir)
except Exception as e:
    print('Dir already exist')

browser = webdriver.Safari()

browser.get('https://lk.gosuslugi.ru')
sleep(3)

# Sleep менее корректен, но быстрее приводит к MVP

login_web = browser.find_element_by_id('login')
login_web.send_keys(login)

sleep(1)

pass_web = browser.find_element_by_id('password')
pass_web.send_keys(password + Keys.ENTER)

sleep(2)

browser.get('https://lk.gosuslugi.ru/profile/personal')

sleep(5)

passport = browser.find_element_by_xpath('//*[@id="passport"]/lk-doc-card/section/a/div[2]/lk-doc-card-row[1]/h5').text

file_write = open(new_dir+f'/{login}.txt', 'w+')
file_write.write(passport)

browser.quit()