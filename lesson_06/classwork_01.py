"""
Дан словарь, где в качестве ключей английские слова, а значений - их перевод на русский язык. Написать две функции,
одна переводит слово с английского на русский, где слово - это входной параметр, вторая функция - с русского
на английский.
"""

d = {
    "cat":"кошка",
    "dog":"собака",
    "cow":"корова",
    "horse":"лошадь",
    "mouse":"мышь"
}
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