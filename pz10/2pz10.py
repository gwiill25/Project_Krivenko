#Из предложенного текстового файла (text18-7.txt) вывести на экран его содержимое, количество букв в нижнем регистре.
#Сформировать новый файл, в который поместить текст в стихотворной форме предварительно поставив последнюю строку между второй и третьей.
#Простой тест
print("Содержимое файла text18-7.txt:")
print("-" * 50)

from pathlib import Path

base_dir = Path(__file__).resolve().parent
input_path = base_dir / "text18-7.txt"
output_path = base_dir / "text18-7_result.txt"

def read_lines(path):
    data = path.read_bytes()
    if data.startswith(b'\xff\xfe'):
        return data.decode('utf-16-le').splitlines(keepends=True)
    if data.startswith(b'\xfe\xff'):
        return data.decode('utf-16-be').splitlines(keepends=True)
    try:
        return data.decode('utf-8').splitlines(keepends=True)
    except UnicodeDecodeError:
        return data.decode('cp1251').splitlines(keepends=True)

lines = read_lines(input_path)
for line in lines:
    print(line, end='')

lowercase_count = 0
for line in lines:
    for char in line:
        if char.islower():  
            lowercase_count += 1

print("\n" + "-" * 50)
print(f'Количество букв в нижнем регистре: {lowercase_count}')

if len(lines) >= 4:  
    last_line = lines[-1]
    
    lines_without_last = lines[:-1]
    
    new_lines = lines_without_last[:2] + [last_line] + lines_without_last[2:]
    
    with output_path.open('w', encoding='utf-8') as f:
        f.writelines(new_lines)
    
    print("\nСформирован новый файл 'text18-7_result.txt' с переставленной последней строкой")
    print("Последняя строка помещена между второй и третьей")
else:
    print("В файле недостаточно строк для выполнения перестановки")