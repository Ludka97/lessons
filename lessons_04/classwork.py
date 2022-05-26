"""Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел больше 10."""
import random

my_list = [1,3,5,7,10,12,14,2]

result =0

for item in my_list:
    if item > 10:
        result += item

print(result)
