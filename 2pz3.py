#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер. Дан номер единицы массы (целое число в диапазоне 1-5) и масса тела в этих единицах (вещественное число). Найти массу тела в килограммах.
try:
    unit = int(input("Введите номер единицы массы (1-5): "))
    if unit not in range(1, 6):
        print("Ошибка: номер должен быть от 1 до 5!")
        exit()
except ValueError:
    print("Ошибка: введите целое число!")
    exit()

try:
    mass = float(input("Введите массу: "))
except ValueError:
    print("Ошибка: введите число!")
    exit()

if unit == 1:
    result = mass
elif unit == 2:
    result = mass / 1_000_000
elif unit == 3:
    result = mass / 1000
elif unit == 4:
    result = mass * 1000
elif unit == 5:
    result = mass * 100

print(f"Масса в килограммах: {result} кг.")