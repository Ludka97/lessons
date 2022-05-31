"""
Создайте функцию three_args(), которая принимает 1, 2 или 3 ключевых параметра.  В результате ее работы на печать
выводятся значения переданных переменных, но только если они не равны None. Получим, например, следующее сообщение:
Переданы аргументы: var1 = 2, var3 = 10
"""

def three_args(var1, var2, var3):
    if var1 is not None:
        print("var1 - ", var1)
    if var2 is not None:
        print("var2 - ", var2)
    if var3 is not None:
        print("var3 - ", var3)

three_args(1,3, None)