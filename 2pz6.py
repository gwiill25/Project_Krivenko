# Дан список размера N. Найти минимальный из его локальных максимумов
#(локальный максимум — это элемент, который больше любого из своих соседей).
import random

N = int(input("Введите размер списка N: "))
numbers = []
for i in range(N):
    numbers.append(random.randint(1, 100))

print("Исходный список:", numbers)

local_maxima = []
for i in range(len(numbers)):
    if i == 0:  
        if numbers[i] > numbers[i+1]:
            local_maxima.append(numbers[i])
    elif i == len(numbers) - 1:  
        if numbers[i] > numbers[i-1]:
            local_maxima.append(numbers[i])
    else: 
        if numbers[i] > numbers[i-1] and numbers[i] > numbers[i+1]:
            local_maxima.append(numbers[i])

if local_maxima:
    min_local_max = min(local_maxima)
    print("Локальные максимумы:", local_maxima)
    print("Минимальный локальный максимум:", min_local_max)
else:
    print("Локальные максимумы отсутствуют")