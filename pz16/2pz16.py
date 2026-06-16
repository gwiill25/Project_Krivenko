#Создание базового класса «Транспортное средство» и его наследование для создания классов «Автомобиль» и «Мотоцикл». 
#В классе «Транспортное средство» будут общие свойства, такие как максимальная скорость и количество колес, 
#а классы-наследники будут иметь свои уникальные свойства и методы.class TransportnoeSredstvo:
class TransportnoeSredstvo:
    def __init__(self, marka, max_skorost, koles):
        self.marka, self.max_skorost, self.koles = marka, max_skorost, koles

    def dvigatsya(self):
        return f"{self.marka} движется."

    def info(self):
        return f"Марка: {self.marka}, Макс. скорость: {self.max_skorost} км/ч, Количество колёс: {self.koles}"


class Avtomobil(TransportnoeSredstvo):
    def __init__(self, marka, max_skorost, koles, tip_kuzova, dverei):
        super().__init__(marka, max_skorost, koles)
        self.tip_kuzova, self.dverei = tip_kuzova, dverei

    def signalid(self):
        return f"{self.marka}: Бип-бип!"

    def info(self):
        return f"{super().info()}, Тип кузова: {self.tip_kuzova}, Дверей: {self.dverei}"


class Mototsikl(TransportnoeSredstvo):
    def __init__(self, marka, max_skorost, koles, tip, est_kolyaska):
        super().__init__(marka, max_skorost, koles)
        self.tip, self.est_kolyaska = tip, est_kolyaska

    def vypolnit_truk(self):
        return f"{self.marka} выполняет трюк — вилли!"

    def info(self):
        return f"{super().info()}, Тип: {self.tip}, Коляска: {'есть' if self.est_kolyaska else 'нет'}"


if __name__ == "__main__":
    print(TransportnoeSredstvo("Неизвестно", 100, 4).info())
    
    avto1 = Avtomobil("Toyota Camry", 200, 4, "Седан", 4)
    print(avto1.info(), avto1.dvigatsya(), avto1.signalid(), sep="\n")
    
    avto2 = Avtomobil("BMW X5", 240, 4, "Внедорожник", 4)
    print(avto2.info(), avto2.signalid(), sep="\n")
    
    moto1 = Mototsikl("Honda CBR", 280, 2, "Спортивный", False)
    print(moto1.info(), moto1.dvigatsya(), moto1.vypolnit_truk(), sep="\n")
    
    moto2 = Mototsikl("Ural", 120, 3, "Круизер", True)
    print(moto2.info(), moto2.vypolnit_truk(), sep="\n")
    
    print("=== Все транспортные средства ===")
    for t in [avto1, avto2, moto1, moto2]:
        print(t.info())