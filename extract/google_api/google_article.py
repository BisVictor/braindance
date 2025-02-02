from googleapiclient.discovery import build
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

service = build('books', 'v1', developerKey=GOOGLE_API_KEY)

query = "Физика. Учебник"
results = service.volumes().list(q=query, maxResults=1).execute()

for item in results.get('items', []):
    volume_info = item.get('volumeInfo', {})
    title = volume_info.get('title', 'Нет названия')
    authors = ', '.join(volume_info.get('authors', ['Автор неизвестен']))
    print(f"Название: {title}")
    print(f"Авторы: {authors}")
    print(f"Ссылка: {volume_info.get('infoLink', 'Нет ссылки')}")
    image_links = volume_info.get('imageLinks', {})
    thumbnail = image_links.get('thumbnail', 'Нет ссылки')
    print(f"Изображение: {thumbnail}")
    print('---')