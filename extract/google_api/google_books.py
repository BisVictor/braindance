from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

def get_article(word):
    try:        
        service = build('books', 'v1', developerKey=GOOGLE_API_KEY)
        results = service.volumes().list(q=word, maxResults=1).execute()
        if 'items' not in results:
            print("По вашему запросу ничего не найдено.")
            return
        item = results['items'][0]
        volume_info = item.get('volumeInfo', {})
        
        # Извлекаем данные
        title = volume_info.get('title', 'Нет названия')
        description = volume_info.get('description', 'Описание отсутствует')
        info_link = volume_info.get('infoLink', 'Нет ссылки')
        image_links = volume_info.get('imageLinks', {})
        image_src = image_links.get('thumbnail', '')  
        text = (f"Описание: {description} Ссылка: {info_link}")         

        json_object = {"title": title,
                        "img_src": image_src,
                        "text": text}   
    except:
        print("Ошибка выполнения функции")
    
    #print(json_object)
    return json_object
    

