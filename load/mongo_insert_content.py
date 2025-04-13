from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

# Логи для MongoDB
MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = int(os.getenv('MONGO_PORT'))

# Подключение к MongoDB
client = MongoClient(f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/")

# Выбор базы данных и коллекции
db = client['mydatabase']
collection = db['content']

# Вставляем контент в БД
def insert_content(content):
    collection.insert_one(content)
    print(f"Документ вставлен в Mongo_DB")

# Принтуем БД
def get_all_content():
    contents = collection.find()  # Выполняем запрос ко всем данным в коллекции
    for content in contents:
        print(f"🆔 {content['_id']}")
        print(f"📘 Title: {content['title']}")
        print(f"🖼 Image: {content['img_src']}")
        print(f"📝 Text: {content['text']}")        
        print("-" * 40)

get_all_content()
