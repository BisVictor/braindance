from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
#from bs4 import BeautifulSoup
import time

from support_f import wait_for_element
from support_f import wait_for_clickable

#окно поиска
S_SEARCH_WIKI='#searchInput'

#кнопка запускает поиск
S_SEARCH_BTN='#searchButton'

#изображение "Физика"
S_IMG_PHYSICS2 = '#mw-content-text > div.mw-content-ltr.mw-parser-output > table.infobox.infobox-6293bbd65e3d65bd > tbody > tr:nth-child(4) > td > span > span > a > img'

START_URL = r'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
EXPECTED_URL = r'https://ru.wikipedia.org/wiki/%D0%A4%D0%B8%D0%B7%D0%B8%D0%BA%D0%B0'

SEARCH_OBJECT = 'физика'

with webdriver.Chrome() as browser:
    browser.get(START_URL)
    search = wait_for_element(browser, By.CSS_SELECTOR, S_SEARCH_WIKI)
    search.click()
    search.send_keys(SEARCH_OBJECT)
    search_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_SEARCH_BTN)
    search_button.click()
    if browser.current_url == EXPECTED_URL:
        print("Всё ОК. Мы на нужном URL")
    else:
        print("Мы не на нужной странице!")
    article_title_element = wait_for_element(browser, By.TAG_NAME, "h1")
    article_title = article_title_element.text
    #print(article_title)    
    image_element = wait_for_element(browser, By.CSS_SELECTOR, S_IMG_PHYSICS2)
    image_src = image_element.get_attribute("src")
    #print(image_src)
    paragraph_element = wait_for_element(browser, By.TAG_NAME, "p")    
    paragraph_text = paragraph_element.text
    #print(paragraph_text)
    json_object = {"title": article_title,
                    "img_src": image_src,
                      "text": paragraph_text}   
    
    #print(json_object) 
with open('wiki-data-1.json', 'w', encoding='utf-8') as json_file:
        json.dump(json_object, json_file, ensure_ascii=False, indent=4)
