from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
import os

# open chrome browser


def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver')
    driver.start_client()
    return driver


def q(st, en):
    return f'?is_ori=1&key_word=&start_time={st}&end_time={en}&is_search=1&is_searchadv=1#_0'


def scroll_down():
    html_page = driver.find_element_by_tag_name('html') # 找到网页
    for i in range(15):
        print(i)
        html_page.send_keys(Keys.END)
        time.sleep(0.6)


driver = start_chrome()
time.sleep(5)
scroll_down()
