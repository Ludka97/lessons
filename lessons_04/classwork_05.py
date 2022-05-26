"""Получить сумму кубов натуральных чисел от n до m используя цикл for, числа n и m вводятся с клавиатуры."""

n = abs(int(input("Введите n - ")))

m = abs(int(input("Введите m - ")))

result = 0

for element in range (n, m + 1):
    result += element ** 3

print(result)

