import requests
from bs4 import BeautifulSoup 
import urllib.parse
import re

url = "https://ru.wikipedia.org/wiki/"

#encoded_word = urllib.parse.quote(word)

def get_article(word):
    encoding_word = urllib.parse.quote(word)
    response = requests.get(url+encoding_word)
    if response.status_code == 200:
        print(f"Всё ОК. Мы на нужном URL. Запрос: {word}")
        src_url = None
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find(class_="mw-page-title-main")
        paragraph = soup.find('p')
        table = soup.find('table', class_=lambda x: x and x.startswith('infobox infobox-'))
        if table:
            image = table.find('img')                   
            if image:        
                src_url = image['src']                
        print(title.text)
        print(paragraph.text)
        if src_url:
            print(src_url)
    else:
        print(f"Мы не на нужной странице! Запрос: {word}")
    
    json_object = {"title": title.text,
                        "img_src": src_url,
                        "text": paragraph.text} 
    return json_object