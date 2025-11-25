#Дан список размера N. Возвести в квадрат все его локальные минимумы (то есть числа, меньшие своих соседей).
import random

N = int(input("Введите размер списка N: "))
numbers = []
for i in range(N):
    numbers.append(random.randint(1, 100))

print("Исходный список:", numbers)

for i in range(len(numbers)):
    if i == 0:  
        if numbers[i] < numbers[i+1]:
            numbers[i] = numbers[i] ** 2
    elif i == len(numbers) - 1: 
        if numbers[i] < numbers[i-1]:
            numbers[i] = numbers[i] ** 2
    else:  
        if numbers[i] < numbers[i-1] and numbers[i] < numbers[i+1]:
            numbers[i] = numbers[i] ** 2

print("Результирующий список:", numbers)