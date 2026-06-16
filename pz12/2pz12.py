#В матрице элементы последнего столбца заменить на -1.
import random

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))

matr = [[random.randint(-10, 10) for _ in range(cols)] for _ in range(rows)]

print("Исходная матрица:\n" + "\n".join(map(str, matr)))

matr = [row[:-1] + [-1] for row in matr]

print("\nРезультат (последний столбец заменён на -1):")
print("\n".join(map(str, matr)))