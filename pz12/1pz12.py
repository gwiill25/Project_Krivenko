#В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.
import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matr = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:\n" + "\n".join(map(str, matr)))

n = int(input(f"Введите номер строки N (1, {rows}): "))
index = n - 1

matr = [
    matr[i] if i != index else [x + 3 for x in matr[i]]
    for i in range(len(matr))
] if 0 <= index < len(matr) else matr

print(
    f"\nРезультат (строка {n} увеличена на 3):"
    if 0 <= index < len(matr)
    else f"\nОшибка: строки с номером {n} не существует."
)

print("\n".join(map(str, matr)))