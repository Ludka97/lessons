"""
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""
from solution_01 import Circle, Triangle, Square

FIGURES = ["Circle", "Triangle", "Square"]

if __name__ == "__main__":
    circle_res = Circle(2, 4, 5)
    circle_res.area()
    triangle_res = Triangle(2, 4, 2, 9, 4, 7)
    triangle_res.area()

    square_res = Square(2, 4, 2, 9)
    square_res.area()

squares = [circle_res.area(), triangle_res.area(), square_res.area()]

for key, value in zip(FIGURES, squares):
        print(key, value)

