"""
Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное,
в идеале не использовать библиотечные функции.
"""
text = (input("text massage"))
text = text.split()

print(max(text, key = len))

#Работает некорректно: выводит первое слово, которок длинее предыдущего
def the_longest(word2):
    for i in text:
        a = len(text[0])
        if len(i) > a:
            a = len(i)
            return i

print(the_longest(text))

