#Даны два целых числа A и B (A < Б). Найти произведение всех целых чисел от A до B включительно.
try:
    A = int(input('Введите первое число A: '))
    B = int(input('Введите второе число B: '))

    if A >= B:
        print("Ошибка: A должно быть меньше B")
    else:
        product = 1 
        for i in range(A, B + 1):
            product *= i 
        print(f"Произведение чисел от {A} до {B}: {product}")
        
except ValueError:
    print('Ошибка: введите целые числа!')