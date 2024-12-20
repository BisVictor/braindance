 # функции до захода в игру

from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.selenium_helpers import wait_for_element
from utils.selenium_helpers import wait_for_clickable

# URL
BASE_URL = "https://test.braindance.space"
GAME_URL = f"{BASE_URL}/game"

# create_game
S_BTN_CREATE_GAME = 'body > div.flex.flex-col.h-screen.px-4 > header > div.lobby-block.flex.gap-2.divider-r.pb-2 > button:nth-child(2)'
S_CPOINT_PRIVATE_GAME = 'body > div.ui-modal.ui-modal_visible > div > div.base-card__body > form > div.w-100.my-3.relative.flex.gap-4 > div:nth-child(2) > input'
S_INPUT_GAME_NAME = 'body > div.ui-modal.ui-modal_visible > div > div.base-card__body > form > div:nth-child(2) > input'
S_BTN_CREATE_GAME2 = 'body > div.ui-modal.ui-modal_visible > div > div.base-card__body > form > div.mt-3.text-end > button:nth-child(2)'
S_BTN_CONFIRM_GO_TO_THE_GAME_OK = 'body > div.ui-modal.ui-modal_visible > div > div.base-card__body > div > div.mt-3.flex.justify-end.gap-2 > button:nth-child(2)'
S_BTN_CONFIRM_GO_TO_THE_GAME_CANCEL = 'body > div.ui-modal.ui-modal_visible > div > div.base-card__body > div > div.mt-3.flex.justify-end.gap-2 > button:nth-child(1)'

# enter_game
S_NICKNAME_FORM = 'body > div > div > div > div > div > form > div.flex.gap-3 > div:nth-child(1) > input'
S_VISITOR_MODE_BUTTON = 'div.flex.gap-3 > div:nth-child(2) > div > div'
S_VISITOR_OPTION_ROLE = '.rc-virtual-list-holder-inner > div[title="Visitor"]'
S_VISITOR_OPTION_ROLE2 = '.rc-virtual-list-holder-inner > div[title="Owner"]'
S_SKIP_SPAN = '.game-dialog form .ant-checkbox-input'
S_BTN_GO_TO_THE_GAME = 'body > div > div > div > div > div > form > div.flex.justify-end > button'


def create_game(browser, private_game=False, go_to_game=True):
    #№browser.get('https://test.braindance.space/')    
    button_create_game = wait_for_element(browser, By.CSS_SELECTOR, S_BTN_CREATE_GAME, timeout=10)    
    button_create_game.click()        
    if private_game:
        cursor_pointer = wait_for_element(browser, By.CSS_SELECTOR, S_CPOINT_PRIVATE_GAME, timeout=5)
        cursor_pointer.click()
    input_game_name = wait_for_element(browser,By.CSS_SELECTOR, S_INPUT_GAME_NAME, timeout=5)    
    input_game_name.click()  
    now = datetime.now()
    input_game_name.send_keys('%s' % now)    
    button_create_game_start = browser.find_element(By.CSS_SELECTOR, S_BTN_CREATE_GAME2)
    button_create_game_start.click()    
    if go_to_game:
        button_confirm_game_ok = wait_for_element(browser, By.CSS_SELECTOR, S_BTN_CONFIRM_GO_TO_THE_GAME_OK, timeout=10)
        button_confirm_game_ok.click()
    else:
        button_confirm_game_cancel = wait_for_element(browser, By.CSS_SELECTOR, S_BTN_CONFIRM_GO_TO_THE_GAME_CANCEL, timeout=10)
        button_confirm_game_cancel.click()    

def enter_game(browser, nickname, role, skip=False):
    #browser.get(f'{GAME_URL}?hash=864')    
    nickname_form = wait_for_element(browser, By.CSS_SELECTOR, S_NICKNAME_FORM, timeout=10)
    nickname_form.click()
    browser.execute_script("arguments[0].value = '';", nickname_form)
    nickname_form.send_keys('%s' % nickname)
    if role == 'visitor':
        button_mode = wait_for_clickable(browser, By.CSS_SELECTOR, S_VISITOR_MODE_BUTTON, timeout=5)
        button_mode.click()        
        option_role = wait_for_clickable(browser, By.CSS_SELECTOR, S_VISITOR_OPTION_ROLE, timeout=5)
        option_role.click()
    elif role == 'owner':
        button_mode = wait_for_clickable(browser, By.CSS_SELECTOR, S_VISITOR_MODE_BUTTON, timeout=5)
        button_mode.click()        
        option_role = wait_for_clickable(browser, By.CSS_SELECTOR, S_VISITOR_OPTION_ROLE2, timeout=5)
        option_role.click()
    if skip:
        skip_span = browser.find_element(By.CSS_SELECTOR, S_SKIP_SPAN)
        skip_span.click()
    game_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_BTN_GO_TO_THE_GAME, timeout=5)
    game_button.click()