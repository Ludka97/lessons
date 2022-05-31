"""
Написать функцию, которая получает на вход имя и выводит строку вида: f"Hello, {name}". Создать список из 5 имен.
Вызвать функцию для каждого элемента списка в цикле.
"""

def my_func(name):
    print(f"Hello, {name}")


my_names = ["Ludka", "Dasha", "Marina", "Yulia", "Olga"]

for name in my_names:
    my_func(name)