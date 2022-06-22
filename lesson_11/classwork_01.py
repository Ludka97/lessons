"""Создать функцию, которая позволяет добавлять данные в таблицу user. Добавить 5 различных записей."""

import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
           """
           INSERT INTO user (firstname, lastname, email, password, age)
           VALUES (?, ?, ?, ?, ?);
           """,
           (firstname, lastname, email, password, age),
        )
        session.commit()




if __name__ == "__main__":
    create_user("Daria", "Yurush", "dashkefedor@gmail.com", "Testpassword", 26)
    create_user("Lyudmila", "Kachan", "ludka@gmail.com", "password1", 24)
    create_user("Andrei", "Kachan", "andron@gmail.com", "wordpass", 30)
    create_user("Olga", "Kvach", "shpil@gmail.com", "Testword", 25)
    create_user("Nikolai", "Simak", "Nick@gmail.com", "Tpass", 25)