import sqlite3
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

# Логи для Постгрес ДБ
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Подключаемся к SQLite (WSL путь!)
sqlite_conn = sqlite3.connect('/mnt/d/udemy/udemy.db')
sqlite_cursor = sqlite_conn.cursor()

# Достаём нужные данные
sqlite_cursor.execute("""
SELECT title, rating, language, course_url 
FROM items 
WHERE topic = 'Git'
""")
rows = sqlite_cursor.fetchall()

# Подключаемся к PostgreSQL в Docker
pg_conn = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    dbname=DB_NAME,     
    user=DB_USER,       
    password=DB_PASSWORD        
)
pg_cursor = pg_conn.cursor()

# Создаём таблицу в PostgreSQL (если нужно)
pg_cursor.execute("""
CREATE TABLE IF NOT EXISTS git_courses (
    id SERIAL PRIMARY KEY,
    title TEXT,
    rating REAL,
    language TEXT,
    course_url TEXT
)
""")

# Вставляем данные
pg_cursor.executemany("""
INSERT INTO git_courses (title, rating, language, course_url)
VALUES (%s, %s, %s, %s)
""", rows)

# Завершаем
pg_conn.commit()
sqlite_conn.close()
pg_conn.close()

print("Данные успешно перенесены в PostgreSQL")