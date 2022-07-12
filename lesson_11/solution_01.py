"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий. Реализовать следующие
функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""

import sqlite3


def create_product_table(database_name: str):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                price FLOAT,
                ammount INTEGER,
                comment TEXT
            );
            """
        )
        session.commit()


def create_product(name: str, price: int, ammount: int, comment: str):
    with sqlite3.connect("my_products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO products (name, price, ammount, comment)
            VALUES (?, ?, ?, ?);
            """,
            (name, price, ammount, comment),
        )
        session.commit()


def read_product(database_name: str):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT * FROM products;
            """
        )
        session.commit()
        return cursor.fetchall()


def update_product(id: int):
    with sqlite3.connect("my_products.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE products
            SET price = 20
            WHERE id = ?;
            """,
            (id,)
        )
        session.commit()
        return cursor.fetchone()


def delete_product(database_name: str, product_id: int):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM product WHERE id = ?;
            """,
            (product_id,)
        )
        session.commit()





"""if __name__ == "__main__":
    print(read_product(1, 10))
    print(update_product(2))
    print(delete_product(4))"""