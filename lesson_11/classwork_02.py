"""Создать функцию, которая позволяет добавлять данные в таблицу user. Добавить 5 различных записей."""

import sqlite3


def select_user(name: str):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT *
            FROM user
            WHERE firstname = ?;
            """,
            (name,)
        )
        session.commit()
        return cursor.fetchone()

if __name__ == "__main__":
    print(select_user("Nikolai"))