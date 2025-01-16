import requests
from bs4 import BeautifulSoup 
import urllib.parse
import re

url = "https://ru.wikipedia.org/wiki/"

#encoded_word = urllib.parse.quote(word)

word = input()
#word = "физика"
encoding_word = urllib.parse.quote(word)

response = requests.get(url+encoding_word)
#print(response)
#print(response.text)
src_image = None
soup = BeautifulSoup(response.text, 'html.parser')
title = soup.find(class_="mw-page-title-main")
p = soup.find('p')
table = soup.find('table', class_=lambda x: x and x.startswith('infobox infobox-'))
if table:
    image = table.find('img')
    print(image)
   
    if image:        
        src_image = image['src']
        print(src_image)


print(title.text)
print(p.text)
if src_image:
    print(src_image)