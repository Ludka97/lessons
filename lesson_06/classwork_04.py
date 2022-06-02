"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек, т.е. реализовать цикл в котором на каждом
ходу у игрока спрашивается, достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
"""

from classwork_03 import get_random_card

d = {
    "6":6, "7":7, "8":8, "9":9, "10":10, "J":2, "D":3, "K":4, "A":1
}

def nom_to_value(nominal):
    return d[nominal]

n, _ = get_random_card()
value = nom_to_value(n)

current_sum = value
while True:
    choice = input("Card [Y/n]: ")
    if choice == "n":
        break

    n, _ = get_random_card()
    value = nom_to_value(n)
    current_sum += value

    if current_sum > 21:
        print ("You loose", current_sum)
        break

    if current_sum == 21:
        print ("You win")
        break

    if current_sum < 21:
        print ("Your score", current_sum)

