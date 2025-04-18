import sqlite3
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Загружаем переменные из .env
load_dotenv()

MONGO_USER = os.getenv('MONGO_USER')
MONGO_PASSWORD = os.getenv('MONGO_PASSWORD')
MONGO_HOST = os.getenv('MONGO_HOST')
MONGO_PORT = int(os.getenv('MONGO_PORT'))

# Подключаемся к SQLite (WSL путь)
sqlite_conn = sqlite3.connect('/mnt/d/udemy/udemy.db')
sqlite_cursor = sqlite_conn.cursor()

sqlite_cursor.execute("""
SELECT title, rating, language, course_url 
FROM items 
WHERE topic = 'Git'
""")
rows = sqlite_cursor.fetchall()

# Конвертируем в список словарей
documents = []
for row in rows:
    documents.append({
        "title": row[0],
        "rating": row[1],
        "language": row[2],
        "course_url": row[3]
    })

# Подключаемся к MongoDB
if MONGO_USER and MONGO_PASSWORD:
    mongo_uri = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}"
else:
    mongo_uri = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"

client = MongoClient(mongo_uri)
db = client["mydatabase"]
collection = db["git_courses"]

# Вставляем документы
if documents:
    collection.insert_many(documents)
    print(f"Вставлено документов: {len(documents)}")
else:
    print("Нет данных для вставки")

# Закрываем соединения
sqlite_conn.close()
client.close()