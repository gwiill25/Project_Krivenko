#Приложение АПТЕКА для автоматизации работы аптечных пунктов. Таблица Лекарственные Средства должна содержать следующую информацию: 
#Код, Название препарата, Применение, Количество, Цена, Страна-производитель.
import sqlite3 as sq

with sq.connect('apteka.bd') as con:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS Medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            use TEXT,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            country TEXT NOT NULL
        )
    """)
    cur.execute("DELETE FROM Medicines")
    
    medicines_data = [
        (1, 'Нурофен', 'Головная боль', 100, 250.0, 'Великобритания'),
        (2, 'Парацетамол', 'Температура', 200, 120.0, 'Россия'),
        (3, 'Амоксициллин', 'Антибиотик', 50, 300.0, 'Германия'),
        (4, 'Цитрамон', 'Мигрень', 150, 90.0, 'Россия'),
        (5, 'Лоратадин', 'Аллергия', 80, 180.0, 'Польша'),
        (6, 'Мезим', 'Пищеварение', 60, 220.0, 'Германия'),
        (7, 'Но-шпа', 'Спазмы', 110, 200.0, 'Венгрия'),
        (8, 'Аквамарис', 'Нос', 40, 280.0, 'Франция'),
        (9, 'Линекс', 'Кишечник', 70, 350.0, 'Словения'),
        (10, 'Витамин C', 'Иммунитет', 300, 50.0, 'Россия')
    ]
    cur.executemany("INSERT INTO Medicines (id, name, use, quantity, price, country) VALUES (?, ?, ?, ?, ?, ?)", medicines_data)
    print("Добавлено 10 записей.\n")

print("--- ПОИСК ---")
with sq.connect('apteka.bd') as con:
    cur = con.cursor()
    print("1 - поиск по названию препарата")
    print("2 - поиск по стране-производителю")
    print("3 - поиск по цене меньше заданной")
    choice = input("Выберите вариант: ")
    
    if choice == '1':
        name = input("Введите название препарата: ")
        cur.execute("SELECT * FROM Medicines WHERE name LIKE ?", (f'%{name}%',))
        for row in cur.fetchall():
            print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}")
    elif choice == '2':
        country = input("Введите страну-производителя: ")
        cur.execute("SELECT * FROM Medicines WHERE country = ?", (country,))
        for row in cur.fetchall():
            print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}")
    elif choice == '3':
        max_price = float(input("Максимальная цена: "))
        cur.execute("SELECT * FROM Medicines WHERE price < ?", (max_price,))
        for row in cur.fetchall():
            print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}")
    else:
        print("Неверный выбор")

print("\n--- УДАЛЕНИЕ ---")
with sq.connect('apteka.bd') as con:
    cur = con.cursor()
    print("1 - удалить по id")
    print("2 - удалить по названию препарата")
    print("3 - удалить все лекарства с количеством меньше N")
    choice = input("Выберите вариант: ")
    
    if choice == '1':
        uid = int(input("Введите id: "))
        cur.execute("DELETE FROM Medicines WHERE id = ?", (uid,))
        print("Удалено записей:", cur.rowcount)
    elif choice == '2':
        name = input("Введите название препарата: ")
        cur.execute("DELETE FROM Medicines WHERE name = ?", (name,))
        print("Удалено записей:", cur.rowcount)
    elif choice == '3':
        min_quantity = int(input("Количество меньше (шт): "))
        cur.execute("DELETE FROM Medicines WHERE quantity < ?", (min_quantity,))
        print("Удалено записей:", cur.rowcount)
    else:
        print("Неверный выбор")

print("\n--- РЕДАКТИРОВАНИЕ ---")
with sq.connect('apteka.bd') as con:
    cur = con.cursor()
    print("1 - изменить цену по id")
    print("2 - изменить количество по названию препарата")
    print("3 - увеличить цену на % для всех лекарств из определенной страны")
    choice = input("Выберите вариант: ")
    
    if choice == '1':
        uid = int(input("Введите id: "))
        new_price = float(input("Новая цена: "))
        cur.execute("UPDATE Medicines SET price = ? WHERE id = ?", (new_price, uid))
        print("Обновлено записей:", cur.rowcount)
    elif choice == '2':
        name = input("Введите название препарата: ")
        new_quantity = int(input("Новое количество: "))
        cur.execute("UPDATE Medicines SET quantity = ? WHERE name = ?", (new_quantity, name))
        print("Обновлено записей:", cur.rowcount)
    elif choice == '3':
        country = input("Введите страну-производителя: ")
        percent = float(input("На сколько процентов увеличить цену: "))
        cur.execute("UPDATE Medicines SET price = price * (1 + ?/100) WHERE country = ?", (percent, country))
        print("Обновлено записей:", cur.rowcount)
    else:
        print("Неверный выбор")

print("\n--- ВСЕ ЗАПИСИ ПОСЛЕ ИЗМЕНЕНИЙ ---")
with sq.connect('apteka.bd') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM Medicines")
    for row in cur.fetchall():
        print(f"{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}")