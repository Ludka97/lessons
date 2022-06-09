"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0). Методы: увеличить скорости
(скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0), отображение скорости, задний ход
(изменение знака скорости).

"""

class Car:
    brand: str = None
    model: str = None
    year: int = None
    speed: int = 0

    def __init__(self,  brand: str, model: str, year: int, speed: int = 0):
        self.brand = brand
        self.model = model
        self.year = year
        if speed is not None:
            self.speed = speed

    def speed_up(self):
        self.speed += 5
        print(self.speed)

    def speed_down(self):
        self.speed -= 5
        print(self.speed)

    def stop(self):
        self.speed = 0
        print(self.speed)

    def speed_now(self):
        print(self.speed)

    def reverse(self):
        if self.speed < 0:
            print("R")


if __name__ == "__main__":
    car = Car("Audi", "TT", 2010, 0)
    car.speed_up()
    car.speed_down()
    car.stop()
    car.speed_now()
    car.reverse()