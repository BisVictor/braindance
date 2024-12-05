from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time

from support_f import wait_for_clickable
from support_f import wait_for_element

S_BTN_CLASSES = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(3)'
S_BTN_INFO = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(4)'
S_BTN_MINIMAP = 'body > div.game-bg > div > div.position_bottom_right.actions.panel > button:nth-child(5)'


def classes(browser):
    classes_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_BTN_CLASSES, timeout=10)
    classes_button.click()

def info(browser):
    info_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_BTN_INFO, timeout=10)
    info_button.click()

def minimap(browser):
    minimap_button = wait_for_clickable(browser, By.CSS_SELECTOR, S_BTN_MINIMAP, timeout=10)
    minimap_button.click()

def open_modal(browser, btn_selector, modal_selector, modal_name):    
    btn = wait_for_clickable(browser, By.CSS_SELECTOR, btn_selector, timeout=10)
    btn.click() 
    time.sleep(1) 
    modal = wait_for_element(browser, By.CSS_SELECTOR, modal_selector, timeout=10)
    if modal.is_displayed():
        print(f"Модальное окно {modal_name} открылось. Все ОК.")
    else:
        raise Exception(f"Модальное окно {modal_name}  НЕ открылось")

def close_modal(browser, btn_selector, modal_selector, modal_name):   
    btn = wait_for_clickable(browser, By.CSS_SELECTOR, btn_selector, timeout=10)
    btn.click()    
    time.sleep(1)  
    try:
        WebDriverWait(browser, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, modal_selector)))
        print(f"Модальное окно {modal_name} закрыто. Все ОК.")
    except TimeoutException:
        raise Exception(f"Модальное окно {modal_name} НЕ закрыто")
