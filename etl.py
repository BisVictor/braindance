from dotenv import load_dotenv
import os
from selenium import webdriver
import time


#from extract.wiki.wiki_article import get_article
#from extract.google_api.google_books import get_article
from extract.bio_py.bio_article import get_article
from transform.wiki_brain import from_wiki_articles_to_steps
from load.braindance.steps import execute_steps_with_data
from load.braindance.steps import wrap_with_game_creation, execute_steps_with_data, insert_moves


load_dotenv()
BASE_URL = os.getenv("BASE_URL")

with webdriver.Chrome() as browser:
    browser.get(BASE_URL)
    browser.set_window_size(1400, 800)
    
    articles = []    
    articles.append(get_article("AAV physics"))
    #articles.append(get_article("химия"))
    #articles.append(get_article("география"))    
    
    #print(articles)
    turn_steps = from_wiki_articles_to_steps(articles)
    #print(turn_steps)
    steps = wrap_with_game_creation(turn_steps)
    #print(steps)
    steps_and_moves = insert_moves(steps)
    #print(steps_and_moves)
    execute_steps_with_data(browser, steps_and_moves)
    time.sleep(15)
    