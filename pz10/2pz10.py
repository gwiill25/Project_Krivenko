#Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое, количество букв в нижнем регистре.
#Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю строку между второй и третьей.
#Простой тест
with open('text18-7.txt', 'r', encoding='utf-8') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]

print("\nСодержимое файла text18-7.txt:")
for line in lines:
    print(line)

lower_count = sum(1 for line in lines for ch in line if ch.islower())
print(f"\nКоличество строчных букв: {lower_count}")

if len(lines) >= 4:
    last = lines.pop()
    lines.insert(2, last)

with open('text18-7_result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Задача 2: файл text18-7_result.txt создан")