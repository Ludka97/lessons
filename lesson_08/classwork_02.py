"""
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и меняет атрибут имени у объекта.
Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.
"""

# second solution
from classwork_01 import Dog

class NewDog(Dog):

    def change_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    dog1 = Dog(height = 10, weight = 5, name = "test")
    print("Old name:", dog1.name)
    dog1.change_name("New name")
    print("New name:", dog1.name)




"""   
import random


class Dog:
    height: int = None
    weight: int = None
    name: str = None
    age: int = 10

    def __init__(self, height: int, weight: int, name: str, age: int = None):
        self.height = height
        self.weight = weight
        self.name = name
        if age is not None:
            self.age = age

    def jump(self):
        print(f"{self.name} is jumping")

    def run(self):
        print(f"{self.name} is running")

    def bark(self):
        print(f"{self.name} is barking")

    def change_name(self):
        names = ["tuzik", "lord", "ballon"]
        self.name = random.choice(names)
        print("New name is", self.name)

if __name__ == "__main__":
    dog = Dog(10, 5, "test", 5)
    dog.change_name()
    """