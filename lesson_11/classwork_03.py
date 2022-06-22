"""Создать функцию для поиска всех пользователей в возрасте от X до Y лет."""

import sqlite3


def select_user(from_age: int, to_age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE age >= ? and age <= ?;
            """,
            (from_age, to_age)
        )
        session.commit()
        return cursor.fetchall()

if __name__ == "__main__":
    print(select_user(4, 27))