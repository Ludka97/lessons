"""
Доработать первое задание так, чтобы словарь читался из текстового CSV файла, где на каждой строке пары слов вида:
apple,яблоко
"""

import csv

#first_sol
d = {}
with open("dictionary.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        d[row[0]] = row[1]

#second_sol
with open("dictionary.csv", "r") as file:
    d = {row[0]: row[1] for row in csv.reader(file)}

def eng_to_rus(word):
    return d[word]

#first solution
def rus_to_eng(word):
    new_d = {
        value:key
    for key, value in d.items()
    }
    return key

#second solution
def rus_to_eng(word):
    for key, value in d.items():
        if value == word:
    return key

print(eng_to_rus("cat"))
print(eng_to_rus("mouse"))

print(rus_to_eng("лошадь"))
print(rus_to_eng("собака"))