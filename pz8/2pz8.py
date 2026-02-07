#Дана строка 'груши 45 991 63 100 12 морковь 13 47 26 0 16', отражающая продажи продукции по дням в кг. 
#Преобразовать информацию из строки в словари, с использованием функции найти минимальные продажи по каждому виду продукции, 
#результаты вывести на экран.
def find_min_sales(sales_str):
    items = sales_str.split()
    data = {}
    i = 0
    while i < len(items):
        product = items[i]
        i += 1
        sales = []
        while i < len(items) and items[i].isdigit():
            sales.append(int(items[i]))
            i += 1
        data[product] = sales
    return data

sales_str = 'груши 45 991 63 100 12 морковь 13 47 26 0 16'
sales_dict = find_min_sales(sales_str)

for product, values in sales_dict.items():
    min_sales = min(values)
    print(f"{product}: минимальные продажи = {min_sales}")
    