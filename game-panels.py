from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from support_f import wait_for_clickable

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