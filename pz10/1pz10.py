#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел.
#Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#Исходные данные:
#Количество элементов:
#Среднее арифметическое элементов:
#Положительные четные элементы:
#Сумма положительных четных элементов:
#Среднее арифметическое положительных четных элементов:
numbers = [15, -3, 8, -12, 20, 6, -7, 4, 10, -5, 18, 22]

with open('numbers_7.txt', 'w', encoding='utf-8') as f:
    f.write(' '.join(map(str, numbers)))

with open('numbers_7.txt', 'r', encoding='utf-8') as f:
    nums = list(map(int, f.read().split()))

count = len(nums)
mean = sum(nums) / count

even_pos = [x for x in nums if x > 0 and x % 2 == 0]
sum_even_pos = sum(even_pos)    
mean_even_pos = sum_even_pos / len(even_pos) if even_pos else 0

with open('result_7.txt', 'w', encoding='utf-8') as f:
    f.write("Исходные данные:\n")
    f.write(' '.join(map(str, nums)) + "\n")
    f.write(f"Количество элементов: {count}\n")
    f.write(f"Среднее арифметическое элементов: {mean:.2f}\n")
    f.write(f"Положительные четные элементы: {even_pos}\n")
    f.write(f"Сумма положительных четных элементов: {sum_even_pos}\n")
    f.write(f"Среднее арифметическое положительных четных элементов: {mean_even_pos:.2f}\n")

print("Задача 1: Результат в файле 'result_7.txt'")