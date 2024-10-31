# основной код, который запускает сценарии состоящие из функций

from lobby import*
from game import*
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = os.getenv('BASE_URL')

header_text = 'Selenium'
image_url = 'https://www.selenium.dev/images/selenium_4_logo.png'
text = 'Promo text. Selenium test'

with webdriver.Chrome() as browser:
    browser.get(BASE_URL)
    create_game(browser, private_game=True, go_to_game=True)
    enter_game(browser, 'victor', 'owner', skip=True)    
    create_turn_picture(browser, header_text, image_url, text)
    time.sleep(10)