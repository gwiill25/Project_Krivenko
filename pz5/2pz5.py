#Описать функцию AddRightDigit(D, K), добавляющую к целому положительному числу K справа цифру D 
# (D — входной параметр целого типа, лежащий в диапазоне 0-9, K — параметр целого типа, являющийся одновременно входным и выходным). 
# С помощью этой функции последовательно добавить к данному числу K справа данные цифры D1 и D2, выводя результат каждого добавления.
def AddRightDigit(D, K):
    return K * 10 + D

K = input("Введите K: ")
while type(K) != int:
    try:
        K = int(K)
    except ValueError:
        print("Ошибка!")
        K = input("Введите K: ")

D1 = input("Введите D1: ")
while type(D1) != int:
    try:
        D1 = int(D1)
    except ValueError:
        print("Ошибка!")
        D1 = input("Введите D1: ")

D2 = input("Введите D2: ")
while type(D2) != int:
    try:
        D2 = int(D2) 
    except ValueError:
        print("Ошибка!")
        D2 = input("Введите D2: ")

K = AddRightDigit(D1, K)
print("После D1:", K)

K = AddRightDigit(D2, K)
print("После D2:", K)

