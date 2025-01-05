# функции внутри игры
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


from utils.selenium_helpers import wait_for_element
from utils.selenium_helpers import wait_for_clickable


S_BTN_ADD_TURN = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(1)'
S_BTN_ADD_TEXT_PICTURE = r'body > div.game-bg > div > div.position_upper_right.panel > div > div:nth-child(1) > div:nth-child(1) > div.w-1\/6 > button'
#S_BTN_ADD_TEXT_PICTURE = r'body > div.game-bg > div > div.position_upper_right.panel > div > div:nth-child(1) > div:nth-child(1) > div.w-1/6 > button'
#S_BTN_ADD_TEXT_PICTURE2 = 'body > div.game-bg > div > div.position_upper_right.panel > div > div:nth-child(1) > div:nth-child(1) > div.w-1\/6 > button'
X_BTN_ADD_TEXT_PICTURE = '/html/body/div[3]/div/div[2]/div/div[1]/div[1]/div[1]/button'


S_HEADER_INPUT = 'input[placeholder="Header:"]'
S_IMAGE_URL_INPUT = 'body > div.game-bg > div > div.position_upper_right.panel > div > div:nth-child(1) > div.row.image-url-row.mb-2 > div > input'
X_TEXT_INPUT = '//*[@id="editor-container-new"]/div[1]'
S_BTN_SAVE = 'body > div.game-bg > div > div.position_upper_right.panel > div > div:nth-child(3) > div > button.btn.btn-primary.btn-accent'
X_BTN_ADD_TEXT_VIDEO = '/html/body/div[3]/div/ul/li[2]'
S_VIDEO_URL_INPUT = 'body > div.game-bg > div > div.position_upper_right.panel > div > div:nth-child(1) > div.row.video-url-row.mb-2 > div > input'
S_BTN_SAVE_FIELD = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(2)'
S_BTN_LOBBY = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(6)'

#кнопки панели
S_BTN_CLASSES = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(3)'
S_BTN_INFO = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(4)'
S_BTN_MINIMAP = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(5)'

#для проверки открытия окна classes
S_BTN_CLASSES_BTN_ADD = 'body > div.game-bg > div > div.position_upper_left.panel > div > form > button'
#для проверки открытия окна info
S_BTN_INFO_ENTER_GAME = 'body > div.game-bg > div > div.position_upper_center.panel > div > table > tbody > tr:nth-child(6) > td:nth-child(2) > form > div:nth-child(3) > button'
#для проверки открытия окна minimap
S_BTN_MINIMAP_MAP_ICON = 'body > div.game-bg > div > div.position_bottom_left.panel-minimap-styles.panel > div > div.percent-map-wrap-holder > div > div.map-icon > svg'

panel_settings = {
    "classes": [S_BTN_CLASSES, S_BTN_CLASSES_BTN_ADD],
    "info": [S_BTN_INFO, S_BTN_INFO_ENTER_GAME],
    "minimap": [S_BTN_MINIMAP, S_BTN_MINIMAP_MAP_ICON],
}

def create_turn(browser, type, header_text, text, url=None, sleep_after_create_turn=3): # тип хода, хэдер, url картинки/видео и текст
    turn_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_BTN_ADD_TURN, timeout=10)     
    turn_button.click() 
    text_picture_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_BTN_ADD_TEXT_PICTURE, timeout=5)     
    text_picture_button.click()   
    if type == "picture":
        image_url_input = browser.find_element(By.CSS_SELECTOR, S_IMAGE_URL_INPUT)
        image_url_input.click()
        image_url_input.send_keys(url)               
    elif type == "video":
        text_video_button = wait_for_clickable(browser, By.XPATH, X_BTN_ADD_TEXT_VIDEO, timeout=10)     
        text_video_button.click()
        video_url_input = wait_for_element(browser, By.CSS_SELECTOR, S_VIDEO_URL_INPUT, timeout=10)     
        video_url_input.click()     
        video_url_input.send_keys(url)       
    header_input = wait_for_element(browser, By.CSS_SELECTOR, S_HEADER_INPUT, timeout=5)
    header_input.click()
    header_input.send_keys(header_text)
    text_input = browser.find_element(By.XPATH, X_TEXT_INPUT)
    text_input.click()
    text_input.send_keys(text)
    save_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_BTN_SAVE, timeout=5)        
    save_button.click()
    time.sleep(sleep_after_create_turn)
    

def drag_and_drop_screen(browser, start_x, start_y, end_x, end_y):
    actions = ActionChains(browser)    
    actions.move_by_offset(start_x, start_y).click_and_hold()    
    actions.move_by_offset(end_x - start_x, end_y - start_y)   
    actions.release().perform()

def save_field(browser):   
    save_field_button = wait_for_element(browser, By.CSS_SELECTOR, S_BTN_SAVE_FIELD, timeout=5)
    save_field_button.click()
    print("Окно сохранено")

def get_lobby(browser):
    lobby_button = wait_for_element(browser, By.CSS_SELECTOR, S_BTN_LOBBY, timeout=5)
    lobby_button.click()   




