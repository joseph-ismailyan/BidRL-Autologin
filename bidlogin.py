# python v3.5.1
# prompts for password and performs a login 

import os, sys, getpass
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

user = {'name': 'YOUR EMAIL HERE', 'pw': ''} # hardcode your own email here
user['pw'] = getpass.getpass('Enter Password: ', ) # no need to hardcode password
browser = webdriver.Chrome()
browser.get('https://www.bidrl.com/login')
browser.set_window_position(0, 0)
browser.maximize_window()
userName = browser.find_element_by_id('user_name')
password = browser.find_element_by_name('password')
login = browser.find_element_by_name('login')
actions = ActionChains(browser)
actions.move_to_element(userName).send_keys(user['name'])
actions.send_keys(Keys.TAB).send_keys(user['pw'])
actions.move_to_element(login).click()
actions.perform()





