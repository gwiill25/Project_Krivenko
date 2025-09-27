# извлеките из числа две последние цифры
try:
    n = int(input("Введите число: "))
    last_two = n % 100  
    tens = last_two // 10  
    units = last_two % 10  
    print(f"Последние две цифры: {tens} и {units}")
except ValueError:
    print("Это не число!") 