import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(browser, by, value, timeout=10):
    return WebDriverWait(browser, timeout).until(EC.presence_of_element_located((by, value)))

def wait_for_clickable(browser, by, value, timeout=10):
     return WebDriverWait(browser, timeout).until(EC.element_to_be_clickable((by, value)))




