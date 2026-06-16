#Составить генератор (yield), который преобразует все буквенные символы в строчные.
def v_nizhnij_registr(stroka):
    yield from map(lambda s: s.lower() if s.isalpha() else s, stroka)

text = input("Введите строку: ")

print("Исходная строка:", text)
print("Результат:", ''.join(v_nizhnij_registr(text)))