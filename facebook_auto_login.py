
from selenium import webdriver
import time
browser = webdriver.Chrome()

browser.get('https://www.facebook.com/')

emailElem = browser.find_element_by_id('email')

emailElem.send_keys('Enter your email:')


passwordElem = browser.find_element_by_id('pass')

passwordElem.send_keys('Enter your password:')

login = browser.find_element_by_id('loginbutton')
login.click()

