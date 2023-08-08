from abc import ABC


class Car(ABC):
    def __init__(self):
        print("Вызван метод конструктора класса Car")

    def maxSpeed(self):
        pass

    def drive(self):
        print("Едем")



class Tesla(Car):
    def maxSpeed(self):
        print("Максимальная скорость 200 км/ч")


class Mercedes(Car):
    def maxSpeed(self):
        print("Максимальная скорость 300 км/ч")


class Renault(Car):
    def maxSpeed(self):
        print("Максимальная скорость 180 км/ч")


class Motorcycle:
    def __init__(self, speed):
        self.speed = speed

    def drive(self):
        self.__turnOnLight()
        print("Едем")

    def __turnOnLight(self):
        print("Включаем фары")

class Honda(Motorcycle):
    def brake(self):
        print("Тормозим")


motorcycle1 = Motorcycle("90 км/ч")
motorcycle2 = Motorcycle("150 км/ч")
print(motorcycle1.speed)
print(motorcycle2.speed)

honda = Honda(20)
honda.drive()
honda.brake()
honda.__turnOnLight()


mercedes = Mercedes()
mercedes.drive()
mercedes.maxSpeed()

tesla = Tesla()
tesla.drive()
tesla.maxSpeed()


print(1 + 1)
print("1" + "1")

print(len("строку"))