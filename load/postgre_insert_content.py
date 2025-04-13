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

# Подключение один раз к серверу
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

def insert_content(content):
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO content (title, image, text)
    VALUES (%s, %s, %s)
""", (content["title"], content["img_src"], content["text"]))
    conn.commit()  
    print(f"Документ вставлен в Postgres_DB")
    

def get_all_content():
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, image, text, created_at FROM content;")
    rows = cursor.fetchall()

    for row in rows:
        print(f"🆔 {row[0]}")
        print(f"📘 Title: {row[1]}")
        print(f"🖼 Image: {row[2]}")
        print(f"📝 Text: {row[3]}")
        print(f"📅 Created at: {row[4]}")
        print("-" * 40)


