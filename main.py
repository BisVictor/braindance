# основной код, который запускает сценарии состоящие из функций

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
from load.braindance.steps import execute_steps
from load.braindance.game import *
from load.braindance.lobby import *


import os

load_dotenv()

BASE_URL = os.getenv('BASE_URL')

#header_text = 'Selenium'
#url = 'https://www.selenium.dev/images/selenium_4_logo.png'
#video_url = 'https://youtu.be/sLQLUed6izY?si=-zP4kRTx0QfJ1bUd'
#text = 'Promo text. Selenium test'


#save_article("физика", "wiki-data-2.json")

with webdriver.Chrome() as browser:
    browser.get(BASE_URL)
    #browser.get('https://braindance.space/game/view/57b')
    browser.set_window_size(1200, 800)  
    time.sleep(3)
    execute_steps(browser, r'load\braindance\steps.json')   
    time.sleep(10)


