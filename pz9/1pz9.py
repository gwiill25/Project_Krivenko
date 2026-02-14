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
canada_agencies = set()
usa_agencies = set()

if "Канада" in voyage:
    canada_agencies.add("Вояж")
if "Канада" in reina_tur:
    canada_agencies.add("РейнаТур")
if "Канада" in raduga:
    canada_agencies.add("Радуга")

if "США" in voyage:
    usa_agencies.add("Вояж")
if "США" in reina_tur:
    usa_agencies.add("РейнаТур")
if "США" in raduga:
    usa_agencies.add("Радуга")

print("Результаты:")
print(f"Туры в Канаду можно приобрести в: {canada_agencies}")
print(f"Туры в США можно приобрести в: {usa_agencies}")