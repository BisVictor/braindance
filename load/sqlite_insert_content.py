import sqlite3

# Подключение к SQLite
conn_sqlite = sqlite3.connect('sqlite_database.db')

def insert_content_sqlite(content):
    cursor = conn_sqlite.cursor()
    cursor.execute("""
    INSERT INTO content (title, image, text)
    VALUES (?, ?, ?)
    """, (content["title"], content["img_src"], content["text"]))
    conn_sqlite.commit()
    print("Документ вставлен в SQLite_DB")