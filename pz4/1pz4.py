#Даны два целых числа A и B (A < Б). Найти произведение всех целых чисел от A до B включительно.
try:
    A = int(input('Введите первое число: '))
    B = int(input('Введите второе число: '))

    if A > B:
        print("Введите так, чтобы первое значение было больше второго")
    else:
        result = 0
        for i in range(A, B+1):
            result += i*i
        print(result)
except ValueError:
    print('Ошибка!')