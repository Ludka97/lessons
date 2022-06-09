"""
Создать программу, которая импортирует класс из предыдущей задачи, создает объект и при инициализации устанавливает
марку Mercedes, модель E500, год выпуска 2000. Далее “разгоняет” машину до 100 км/ч и выводит скорость на экран.
"""


from solution_01 import Car

class NewCar(Car):

    def speed_up_100(self):
        while self.speed < 100:
            self.speed += 5
            print(self.speed)


if __name__ == "__main__":
    car2 = NewCar("Mersedes", "E500", 2000, 0)
    car2.speed_up_100()
