from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys
import time

from utils.selenium_helpers import wait_for_element
from utils.selenium_helpers import wait_for_clickable

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
