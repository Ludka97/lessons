"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure. Создать три дочерних класса Circle
(атрибуты: координаты центра, длина радиуса; методы: нахождение периметра и площади окружности), Triangle (атрибуты:
три точки, методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и
периметра). При потребности создавать все необходимые методы не описанные в задании
"""
import math


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def location(self):
        return self.x, self.y


class Figure:

    def area(self):
        raise NotImplementedError

    def perimetr(self):
        raise NotImplementedError


class Circle(Point, Figure):

    def __init__(self, x: int, y: int, r: int):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def perimetr(self):
        return 2 * math.pi * self.r


class Triangle(Point, Figure):

    def __init__(self, x: int, y: int, x2: int, y2: int, x3: int, y3: int):
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def area(self):
        side_a: int = 0
        side_a = math.sqrt(abs(self.x - self.x2) ** 2 + abs(self.y - self.y2) ** 2)
        side_b: int = 0
        side_b = math.sqrt(abs(self.x2 - self.x3) ** 2 + abs(self.y2 - self.y3) ** 2)
        side_c: int = 0
        side_c = math.sqrt(abs(self.x3 - self.x) ** 2 + abs(self.y3 - self.y) ** 2)
        p = (side_a + side_b + side_c) / 2
        return math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))

    def perimetr(self):
        side_a: int = 0
        side_a = math.sqrt(abs(self.x - self.x2) ** 2 + abs(self.y - self.y2) ** 2)
        side_b: int = 0
        side_b = math.sqrt(abs(self.x2 - self.x3) ** 2 + abs(self.y2 - self.y3) ** 2)
        side_c: int = 0
        side_c = math.sqrt(abs(self.x3 - self.x) ** 2 + abs(self.y3 - self.y) ** 2)
        return side_a + side_b + side_c

class Square(Point, Figure):

        def __init__(self, x: int, y: int, x2: int, y2: int):
            self.x = x
            self.y = y
            self.x2 = x2
            self.y2 = y2

        def area(self):
            side_s: int = 0
            side_s = math.sqrt(abs(self.x - self.x2) ** 2 + abs(self.y - self.y2) ** 2)
            return side_s * side_s

        def perimetr(self):
            side_s: int = 0
            side_s = math.sqrt(abs(self.x - self.x2) ** 2 + abs(self.y - self.y2) ** 2)
            return 4 * side_s




if __name__ == "__main__":
    circle_res = Circle(2, 4, 5)
    circle_res.area()
    circle_res.perimetr()
    circle_res.location()
    print("Area C - ", circle_res.area(), "Perimetr C - ", circle_res.perimetr(), "Location C - ", circle_res.location())

    triangle_res = Triangle(2, 4, 2, 9, 4, 7)
    triangle_res.area()
    triangle_res.perimetr()
    triangle_res.location()
    print("Area Tr - ", triangle_res.area(), "Perimetr Tr - ", triangle_res.perimetr())

    square_res = Square(2, 4, 2, 9)
    square_res.area()
    square_res.perimetr()
    square_res.location()
    print("Area S - ", square_res.area(), "Perimetr S - ", square_res.perimetr())

