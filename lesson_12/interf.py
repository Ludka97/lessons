"""
Создать программу с пользовательским интерфейсом позволяющим выбирать определенную функцию и вводить необходимые данные.
"""

from main import create_product, get_product, update_product, delete_product, buy_purchase, show_user_purchase, \
    filter_purchase, current_session


TEMPLANE = """
    Choose an option:
    1. Create new product.
    2. Get products list.
    3. Update information for product.
    4. Delete product.
    5. Get purchase.
    6. Show purchase list for user.
    7. Purchase status.
    """


def main():
    while True:
        try:
            user_choice = int(input(TEMPLANE))
        except ValueError:
            user_choice = None

        if user_choice == 1:
            print("Write name, price, amount and comment for new product")
            name, price, amount, comment = input().split(',')
            create_product(current_session, name, int(price), int(amount), comment)
            print("New product has been created")
        elif user_choice == 2:
            for product in get_product(current_session):
                print(product)
            else:
                print("product list is empty")
        elif user_choice == 3:
            print("Write id, name, price, amount and comment for existed product")
            id, name, price, amount, comment = input().split(',')
            update_product(current_session, int(id), name, int(price), int(amount), comment)
            print("Information for product has been updated")
        elif user_choice == 4:
            print("Write product_id for delete")
            product_id = int(input())
            delete_product(current_session, product_id)
        elif user_choice == 5:
            print("Write user_id, product_id, amount")
            user_id, product_id, amount = input().split(',')
            buy_purchase(current_session, int(user_id), int(product_id), int(amount))
        elif user_choice == 6:
            print("Write user_id")
            user_id = int(input())
            show_user_purchase(current_session, user_id)
        elif user_choice == 7:
            print("Write amount")
            amount = input()
            filter_purchase(current_session, int(amount))
        else:
            print("Bye")


if __name__ == "__main__":
    main()


