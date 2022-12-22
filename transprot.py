from abc import ABC, abstractmethod


class Transport_agency(ABC):
    EARNINGS = 0

    @abstractmethod
    def earnings(self, earnings):
        Transport_agency.EARNINGS += (earnings * 0.2)


class Car(Transport_agency):
    def __init__(self, distance):
        self.distance = distance

    def earnings(self, earnings):
        Transport_agency.EARNINGS += (earnings * 0.2)


class Train(Transport_agency):
    def __init__(self, distance):
        self.distance = distance

    def earnings(self, earnings):
        Transport_agency.EARNINGS += (earnings * 0.2)


class Airplane(Transport_agency):
    def __init__(self, distance):
        self.distance = distance

    def earnings(self, earnings):
        Transport_agency.EARNINGS += (earnings * 0.2)


i = 1
reg = {}
while True:
    distance = int(input("Введите расстояние в км:"))
    senders_city = input("Введите размер города отправителя: b - большой, s - средний, m -маленький: ")
    recipient_city = input("Введите размер города получателя: b - большой, s - средний, m -маленький: ")
    if senders_city == "b" and recipient_city == "b":
        print("Вид т/c: самолет, цена: 5$/км")
        load_size = int(input("Введите размер груза 3$/kg:"))
        summ = distance * 5 + load_size * 3
        print(f"Итог:{summ}$")
        ts = Airplane(distance)
        ts.earnings(summ)
        reg[i] = {
            f"город отправитель:{senders_city}, город получатель:{recipient_city}, Путь:{distance}км, вес груза:{load_size} кг, заработано:{summ}$"}
    elif senders_city != "m" and recipient_city != "m" and senders_city == "s" or recipient_city == "s":
        print("Вид т/c: Поезд, цена: 3.5$/км")
        load_size = int(input("Введите размер груза 1.25$/kг:"))
        summ = distance * 3.5 + load_size * 1.25
        print(f"Итог:{summ}$")
        ts = Train(distance)
        ts.earnings(summ)
        reg[i] = {
            f"Вид т/c: поезд, город отправитель:{senders_city}, город получатель:{recipient_city}, Путь:{distance}км, вес груза:{load_size} кг, заработано:{summ}$"}
    elif senders_city == "m" or recipient_city == "m":
        print("Вид т/c: Авто, цена: 1.5$/км")
        load_size = int(input("Введите размер груза 0.89$/kг:"))
        summ = distance * 1.5 + load_size * 0.89
        print(f"Итог:{summ}$")
        ts = Car(distance)
        ts.earnings(summ)
        reg[i] = {
            f"Вид т/c: авто, город отправитель:{senders_city}, город получатель:{recipient_city}, Путь:{distance}км, вес груза:{load_size} кг, заработано:{summ}$"}
    elif senders_city and recipient_city == "1":
        print(reg)
    elif senders_city and recipient_city == "end":
        break
    else:
        print("Введены неверные значения")
    i += 1
