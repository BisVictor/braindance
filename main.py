# основной код, который запускает сценарии состоящие из функций

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from dotenv import load_dotenv
from steps import execute_steps
import os

load_dotenv()

BASE_URL = os.getenv('BASE_URL')

header_text = 'Selenium'
image_url = 'https://www.selenium.dev/images/selenium_4_logo.png'
video_url = 'https://youtu.be/sLQLUed6izY?si=-zP4kRTx0QfJ1bUd'
text = 'Promo text. Selenium test'

with webdriver.Chrome() as browser:
    browser.get(BASE_URL)
    browser.set_window_size(1200, 800)  
    time.sleep(3)
    execute_steps(browser, 'steps.json')
    #create_game(browser, private_game=True, go_to_game=True)    
    #enter_game(browser, 'Victor', 'owner', skip=True)        
    #create_turn_picture(browser, header_text, image_url, text)    
    #create_turn_video(browser, header_text, video_url, text)
    #save_field(browser)
    #get_lobby(browser)
    time.sleep(10)


