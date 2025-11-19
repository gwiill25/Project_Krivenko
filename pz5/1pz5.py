#Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить функцией с параметрами. 
# Значения n и m программа должна запрашивать.
def sum_range(n, m):
    s = 0
    for i in range(n, m + 1):
        s += i
    return s

n = input("Введите n: ")
while type(n) != int:
    try:
        n = int(n)
    except ValueError:
        print("Ошибка!")
        n = input("Введите n: ")

m = input("Введите m: ")
while type(m) != int:
    try:
        m = int(m)
    except ValueError:
        print("Ошибка!")
        m = input("Введите m: ")

print("Сумма:", sum_range(n, m))