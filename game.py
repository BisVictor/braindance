# функции внутри игры
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support_f import wait_for_element
from support_f import wait_for_clickable


S_BTN_ADD_TURN = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(1)'
S_BTN_ADD_TEXT_PICTURE = r'body > div.game-bg > div > div.position_upper_right.panel > div > div:nth-child(1) > div:nth-child(1) > div.w-1/6 > button'
S_HEADER_INPUT = 'input[placeholder="Header:"]'
S_IMAGE_URL_INPUT = 'body > div.game-bg > div > div.position_upper_right.panel > div > div:nth-child(1) > div.row.image-url-row.mb-2 > div > input'
X_TEXT_INPUT = '//*[@id="editor-container-new"]/div[1]'
S_BTN_SAVE = 'body > div.game-bg > div > div.position_upper_right.panel > div > div:nth-child(3) > div > button.btn.btn-primary.btn-accent'

def create_turn_picture(browser, header_text, image_url, text): # тип хода, хэдер, url картинки и текст
    #browser.get('https://test.braindance.space/game/view/8b1')
    browser.set_window_size(1200, 800)    
    turn_button = wait_for_element(browser, By.CSS_SELECTOR, S_BTN_ADD_TURN, timeout=10)
    turn_button.click()   
    #text_picture_button = wait_for_element(browser, By.CSS_SELECTOR, S_BTN_ADD_TEXT_PICTURE, timeout=5)
    #text_picture_button.click()
    header_input = wait_for_element(browser, By.CSS_SELECTOR, S_HEADER_INPUT, timeout=5)
    header_input.click()
    header_input.send_keys(header_text)
    image_url_input = browser.find_element(By.CSS_SELECTOR, S_IMAGE_URL_INPUT)
    image_url_input.click()
    image_url_input.send_keys(image_url)
    text_input = browser.find_element(By.XPATH, X_TEXT_INPUT)
    text_input.click()
    text_input.send_keys(text)
    save_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_BTN_SAVE, 10)
    save_button.click()    
   
