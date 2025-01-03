from dotenv import load_dotenv
import os
from selenium import webdriver
import time


from extract.wiki.wiki_article import get_article
from transform.wiki_brain import from_wiki_articles_to_steps
from load.braindance.steps import execute_steps_with_data
from load.braindance.steps import wrap_with_game_creation, execute_steps_with_data

# todo: 4. реализовать функцию execute_steps_with_data аналогичную execute_steps,
# но получающую массив данных вместо адреса файла
#

load_dotenv()
BASE_URL = os.getenv("BASE_URL")

with webdriver.Chrome() as browser:
    browser.get(BASE_URL)
    browser.set_window_size(1200, 800)
    
    articles = []
    articles.append(get_article("физика"))
    articles.append(get_article("химия"))
    
    #print(articles)
    turn_steps = from_wiki_articles_to_steps(articles)
    #print(turn_steps)
    steps = wrap_with_game_creation(turn_steps)
    #print(steps)
    execute_steps_with_data(browser, steps)
    time.sleep(15)