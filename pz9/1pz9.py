#Туристические агентства предлагают следующие туры. Вояж – Мексика,Канада,Израиль,
#Италия,США. РейнаТур – Англия,Япония,Канада,ЮАР. Радуга – США,Испания,Швеция, Австралия.
#Определить в каких турагенствах можно приобрести туры в Канаду, а в каких в США
voyage = {"Мексика", "Канада", "Израиль", "Италия", "США"}
reina_tur = {"Англия", "Япония", "Канада", "ЮАР"}
raduga = {"США", "Испания", "Швеция", "Австралия"}

print("Исходные данные:")
print(f"Вояж: {voyage}")
print(f"РейнаТур: {reina_tur}")
print(f"Радуга: {raduga}")
print()

canada_agencies = []
if "Канада" in voyage:
    canada_agencies.append("Вояж")
if "Канада" in reina_tur:
    canada_agencies.append("РейнаТур")
if "Канада" in raduga:
    canada_agencies.append("Радуга")

usa_agencies = []
if "США" in voyage:
    usa_agencies.append("Вояж")
if "США" in reina_tur:
    usa_agencies.append("РейнаТур")
if "США" in raduga:
    usa_agencies.append("Радуга")

print("Результаты:")
print(f"Туры в Канаду можно приобрести в: {canada_agencies}")
print(f"Туры в США можно приобрести в: {usa_agencies}")