"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы, которая считывает
название города и выводит на печать страну.

"""

def city_to_country(city):
    mapping = {
        "Belarus" : ["Minsk", "Grodno", "Ivye"],
        "Poland" : ["Poznan", "Belostok", "Wroclaw"],
        "Japan" : ["Tokyo", "Tsushima", "Toyota"],
    }
    for country, city_list in mapping.items():
        if city in city_list:
            return country

print(city_to_country("Tokyo"))
