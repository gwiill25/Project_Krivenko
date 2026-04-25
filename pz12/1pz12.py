#В матрице элементы строки N (N задать с клавиатуры) увеличить на 3.
matr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Исходная матрица:")
for row in matr:
    print(row)

n = int(input("Введите номер строки N (1, 2 или 3): "))

index = n - 1

if 0 <= index < len(matr):
    matr[index] = [x + 3 for x in matr[index]]
    print(f"\nРезультат (строка {n} увеличена на 3):")
else:
    print(f"\nОшибка: строки с номером {n} не существует.")

for row in matr:
    print(row)