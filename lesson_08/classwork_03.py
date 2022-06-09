"""
Создать новый класс Cat, который имеет все те же атрибуты что и Dog, только заменить метод bark на meow.
"""

from classwork_01 import Animal, Dog

class Cat(Animal):

    def sound(self):
        print(f"{self.name} is meowing")

class CatAndDog(Cat, Dog):
    pass


if __name__ == "__main__":
    cat_and_dog = CatAndDog(height=10, weight=5, name="test", age=5)
    cat_and_dog.sound()
