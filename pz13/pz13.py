#В исходном текстовом файле(Dostoevsky.txt) найти все годы деятельности писателя (например, 1821 года, 1837 год,
#1843 году и так далее по всему тексту). Посчитать количество полученных элементов.
import re

with open("Dostoevsky (1).txt", "r", encoding="utf-8") as f:
    text = f.read()

pattern = r'\b\d{4}\s+(года|год|году)\b'
found = re.findall(pattern, text)

years_with_words = re.findall(r'\b\d{4}\s+(?:года|год|году)\b', text)

unique_years_with_words = sorted(set(years_with_words))

print("Найденные годы деятельности писателя:")
print(unique_years_with_words)
print(f"\nКоличество: {len(unique_years_with_words)}")

with open("years_output.txt", "w", encoding="utf-8") as f:
    f.write("Годы деятельности писателя:\n")
    f.write(", ".join(unique_years_with_words))
    f.write(f"\n\nОбщее количество: {len(unique_years_with_words)}")