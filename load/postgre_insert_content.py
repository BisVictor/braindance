import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_NAME = os.getenv('DB_NAME')
DB_USE = os.getenv('DB_USE')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')

# Подключение один раз к серверу
conn = psycopg2.connect(
        dbname= DB_NAME,
        user= DB_USE,
        password= DB_PASSWORD,
        host= DB_HOST,
        port= DB_PORT
)

def insert_content(content):
    cursor = conn.cursor()
    cursor.execute(""""
        INSERT INTO content (title, image, text)
        VALUES (%s, %s, %s)
    """, (content["title"], content["img_src"], content["text"]))

