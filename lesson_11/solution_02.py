from solution_01 import create_product_table, create_product, read_product, update_product, delete_product

DB_NAME = "my_products.sqlite3"

TEMPLATE = """
    Выберите один из вариантов:
    1. Создать таблицу продуктов
    2. Напечатать все продукты
    3. Создать новый продукт
    4. Обновить продукт по ID
    5. Удалить продукт по ID
"""

def main():
    while True:
        try:
            user_choice = int(input(TEMPLATE))
        except ValueError:
            user_choice = None

        if user_choice == 1:
            create_product_table(DB_NAME)
            print("Таблица продуктов создана")
        elif user_choice == 2:
            for product in read_product(DB_NAME):
                print(product)
            else:
                print("Не найдено ни одного продукта")
        elif user_choice == 3:
            print("Введите name, price, ammount и comment через запятую: ")
            name, price, ammount, comment = input().split(',')
            create_product(DB_NAME, name, float(price), int(ammount), comment)
        elif user_choice == 4:
            print("Введите product_id, name, price, ammount и comment через запятую: ")
            product_id, name, price, ammount, comment = input().split(',')
            update_product(DB_NAME, int(product_id), name, float(price), int(ammount), comment)
        elif user_choice == 5:
            print("Введите product_id для удаления: ")
            product_id = int(input())
            delete_product(DB_NAME, product_id)
        else:
            return print("Пока!")


if __name__ == "__main__":
    main()