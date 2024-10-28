# основной код, который запускает сценарии состоящие из функций

from lobby import*
from game import*

header_text = 'Selenium'
image_url = 'https://www.selenium.dev/images/selenium_4_logo.png'
text = 'Promo text. Selenium test'

options_chrome = webdriver.ChromeOptions()
options_chrome.add_argument('user-data-dir=C://Users//kharin//AppData//Local//Google//Chrome//User%20Data//Default/')

with webdriver.Chrome(options=options_chrome) as browser:
    #create_game(browser, privat_game=True)
    #enter_game(browser, 'victor', 'owner', skip=True)
    #browser.get('https://test.braindance.space/game/view/8b1')
    #create_turn_picture(browser, header_text, image_url, text)
    time.sleep(30)