#Составить генератор (yield), который преобразует все буквенные символы в строчные.
def v_nizhnij_registr(stroka):
    for simvol in stroka:
        if simvol.isalpha():
            yield simvol.lower()
        else:
            yield simvol

text = "Практическая Работа Номер 11"
print("Исходная строка:", text)
print("Результат:", ''.join(v_nizhnij_registr(text)))