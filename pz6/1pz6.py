#Дан целочисленный список размера 10. Вывести все содержащиеся в данном списке
#нечетные числа в порядке возрастания их индексов, а также их количество K.
import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))

print("Исходный список:", numbers)

odd_numbers = []
for i in range(len(numbers)):
    if numbers[i] % 2 != 0:
        odd_numbers.append(numbers[i])
        print(f"Нечетное число: {numbers[i]}, индекс: {i}")

K = len(odd_numbers)
print(f"Количество нечетных чисел: {K}")