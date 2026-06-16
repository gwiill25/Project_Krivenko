#Средствами языка Python в базе данных создать одну таблицу заполнить ее тремя записями выполнить запрос на обновление любой записи 
#(использовать условие). Таблица Товары должна содежать следующщие данные: Код товара, Наименование товара, Количество товара на складе, 
#Оптовая цена
import sqlite3

conn = sqlite3.connect("shop.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS Товары")
cur.execute("""
CREATE TABLE Товары (
    Код_товара INTEGER PRIMARY KEY,
    Наименование TEXT NOT NULL,
    Количество INTEGER NOT NULL,
    Оптовая_цена REAL NOT NULL
)
""")
products = [
    (1, 'Телевизор', 10, 25000),
    (2, 'Холодильник', 5, 45000),
    (3, 'Микроволновка', 15, 8000)
]
cur.executemany("INSERT INTO Товары VALUES (?, ?, ?, ?)", products)
conn.commit()

print("=== ИСХОДНЫЕ ДАННЫЕ ===")
for row in cur.execute("SELECT * FROM Товары"):
    print(row)

cur.execute("UPDATE Товары SET Количество = Количество + 10 WHERE Код_товара = 2")
conn.commit()

print("\n=== ПОСЛЕ ОБНОВЛЕНИЯ ===")
for row in cur.execute("SELECT * FROM Товары"):
    print(row)

conn.close()