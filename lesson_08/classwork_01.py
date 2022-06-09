"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс имеет три метода: jump, run, bark.
Каждый метод выводит сообщение на экран. Создать объект класса Dog, вызвать все методы объекта и вывести на экран все
его атрибуты.
"""

class Animal:
    height: int = None
    weight: int = None
    name: str = None
    age: int = 10

    def __init__(self, *args, **kwargs):...

    def talk(self):
        raise NotImplementedError

class Dog(Animal):
    def sound(self):
        print(f"{self.name} is barking")

if __name__ == "__main__":
    dog1 = Dog(height = 10, weight = 5, name = "test", age =  5)
    dog1.sound()
