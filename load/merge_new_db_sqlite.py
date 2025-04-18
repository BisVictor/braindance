import sqlite3

# Пути к файлам баз данных
source_db_path = '/mnt/d/udemy/udemy.db'
target_db_path = 'new_udemy.db'

# Подключаемся к исходной базе
source_conn = sqlite3.connect(source_db_path)
source_cursor = source_conn.cursor()

# Подключаемся к целевой базе
target_conn = sqlite3.connect(target_db_path)
target_cursor = target_conn.cursor()

# Шаг 1: Выборка нужных данных из исходной базы
source_cursor.execute("""
SELECT title, rating, language, course_url 
FROM items 
WHERE topic = 'Git'
""")
rows = source_cursor.fetchall()

# Шаг 2: Создаём таблицу в целевой базе, если её ещё нет
target_cursor.execute("""
CREATE TABLE IF NOT EXISTS git_courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    rating REAL,
    language TEXT,
    course_url TEXT
)
""")

# Шаг 3: Вставляем данные
insert_query = """
INSERT INTO git_courses (title, rating, language, course_url)
VALUES (?, ?, ?, ?)
"""
target_cursor.executemany(insert_query, rows)

# Завершаем
target_conn.commit()
source_conn.close()
target_conn.close()

print("Данные по Git-курсам успешно перенесены.")