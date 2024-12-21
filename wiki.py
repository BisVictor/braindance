from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import json
import time

from extract.wiki.wiki_article import save_article

save_article("физика", "wiki-data-2.json")