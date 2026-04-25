#Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых положительных и отрицательных чисел.
#Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
#Исходные данные:
#Количество элементов:
#Среднее арифметическое элементов:
#Положительные четные элементы:
#Сумма положительных четных элементов:
#Среднее арифметическое положительных четных элементов:
numbers_list = ['-15 23 -8 42 -3 17 -6 31 -11 9 -24 14 -5 28 -7 19']

with open('data_7_original.txt', 'w', encoding='utf-8') as f:
    f.writelines(numbers_list)

with open('data_7_result.txt', 'w', encoding='utf-8') as f:
    f.write('Исходные данные: ')
    f.write('\n')
    f.writelines(numbers_list)

with open('data_7_original.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    numbers = data.split()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])

total_count = len(numbers)

average_all = sum(numbers) / total_count

positive_even = [num for num in numbers if num > 0 and num % 2 == 0]

sum_positive_even = sum(positive_even)

if positive_even:
    average_positive_even = sum_positive_even / len(positive_even)
else:
    average_positive_even = 0

with open('data_7_result.txt', 'a', encoding='utf-8') as f:
    f.write('\n')
    f.write(f'Количество элементов: {total_count}\n')
    f.write(f'Среднее арифметическое элементов: {average_all:.2f}\n')
    f.write(f'Положительные четные элементы: {positive_even}\n')
    f.write(f'Сумма положительных четных элементов: {sum_positive_even}\n')
    f.write(f'Среднее арифметическое положительных четных элементов: {average_positive_even:.2f}\n')

print("Результаты сохранены в файл 'data_7_result.txt'")
