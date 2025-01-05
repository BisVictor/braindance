from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
#from bs4 import BeautifulSoup
import time

from utils.selenium_helpers import wait_for_element
from utils.selenium_helpers import wait_for_clickable
from urllib.parse import quote

#окно поиска
S_SEARCH_WIKI='#searchInput'

#кнопка запускает поиск
S_SEARCH_BTN='#searchButton'

#изображения, универсальный селектор
S_IMG = '.infobox tbody tr:nth-child(4) img'
#стратовая страница вики
START_URL = r'https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'
#ожидаемые страницы
WIKI_URL = r'https://ru.wikipedia.org/wiki/'


def save_article(word, target_file):
    json_object = get_article(word)
    with open(target_file, 'w', encoding='utf-8') as json_file:
            json.dump(json_object, json_file, ensure_ascii=False, indent=4)


def get_article(word):
    with webdriver.Chrome() as browser:
        browser.get(START_URL)
        search = wait_for_element(browser, By.CSS_SELECTOR, S_SEARCH_WIKI)
        search.click()
        search.send_keys(word)
        search_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_SEARCH_BTN)
        search_button.click()
        expected_url = WIKI_URL + quote(word.capitalize())        
        if browser.current_url == expected_url:
            print(f"Всё ОК. Мы на нужном URL. Запрос {word}")
        else:
                print(f"Мы не на нужной странице! Запрос {word}")   
        article_title_element = wait_for_element(browser, By.TAG_NAME, "h1")
        article_title = article_title_element.text
        #print(article_title)        
        image_element = wait_for_element(browser, By.CSS_SELECTOR, S_IMG)        
        image_src = image_element.get_attribute("src")
        #print(image_src)
        paragraph_element = wait_for_element(browser, By.TAG_NAME, "p")    
        paragraph_text = paragraph_element.text
        #print(paragraph_text)
        json_object = {"title": article_title,
                        "img_src": image_src,
                        "text": paragraph_text}   
        
        return json_object
    