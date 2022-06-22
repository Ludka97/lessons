"""Создать программу позволяющую осуществлять поиск по имени или возрасту, оба параметра вводятся с клавиатуры."""

import sqlite3


def select_user(age: int, name: str):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE age = ? or firstname = ?;
            """,
            (age, name)
        )
        session.commit()
        return cursor.fetchall()

if __name__ == "__main__":
    print(select_user(24, "Nikolai"))