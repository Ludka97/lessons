from sqlalchemy.orm import sessionmaker, Session

from models import Base, User, Profile, Address, Product, Shoplist
from utils import setup_db_engine, create_database_if_not_exists

engine = setup_db_engine()
create_database_if_not_exists(engine=engine)

Base.metadata.create_all(engine)
CurrentSession = sessionmaker(bind=engine)
current_session = CurrentSession()

def create_user(
    session: Session, email: str, password: str, phone: str, age: int, city: str, address: str
) -> User:
    user = User(email=email, password=password)
    profile = Profile(user=user, phone=phone, age=age)
    address = Address(user=user, city=city, address=address)

    session.add_all([user, profile, address])
    session.commit()

    return user


def update_or_create_address(session: Session, user: User, city: str, address: str) -> Address:
    if len(user.addresses):
        current_address = user.addresses[0]
        current_address.city = city
        current_address.address = address
    else:
        current_address = Address(user=user, city=city, address=address)

    session.add(current_address)
    session.commit()

    return current_address


def create_product(
    session: Session, name: str, price: int, ammount: int, comment: str
) -> Product:
    product = Product(name=name, price=price, ammount=ammount, comment=comment)

    session.add(product)
    session.commit()

    return product


def get_product(session: Session):
    result = session.query(Product.id, Product.name, Product.price, Product.ammount, Product.comment).all()
    print(result)


def update_product(session: Session, id: int, name: str, price: int, ammount: int, comment: str):
    session.query(Product).filter_by(id=id).update({"name": name, "price": price, "ammount": ammount, "comment": comment})
    session.commit()


def delete_product(session: Session, id: int):
    session.query(Product).filter_by(id=id).delete()
    session.commit()


def buy_purchase(session: Session, user_id: int, product_id: int, ammount: int):
    purchase = Shoplist(user_id=user_id, product_id=product_id, ammount=ammount)
    session.add(purchase)
    session.commit()

    return purchase


def show_user_purchase(session: Session, user_id: int):
    shoplist = session.query(Shoplist).filter_by(user_id=user_id).all
    return shoplist


def filter_purchase(session: Session, amount: int):
    if session.query(Shoplist).filter(amount > 0):
        print("Available")
    else:
        print("Not available")


# if __name__ == "__main__":
#     engine = setup_db_engine()
#     create_database_if_not_exists(engine=engine)
#
#     Base.metadata.create_all(engine)
#     CurrentSession = sessionmaker(bind=engine)
#     current_session = CurrentSession()


    # read = get_product(
    #     session=current_session)


    # delete = delete_product(
    #     session=current_session,
    #     id=2)


    # update_pr = update_product(
    #     session=current_session,
    #     id= 2,
    #     name= "notebook",
    #     price= 700,
    #     ammount= 3,
    #     comment= "test"
    # )


    # new_user = create_user(
    #     session=current_session,
    #     email="test@test.com",
    #     password="password",
    #     phone="+375292992929",
    #     age=20,
    #     city="City",
    #     address="Address 123",
    # )

    # user = current_session.query(User).filter_by(email="test@test.com").first()
    # update_or_create_address(
    #     session=current_session,
    #     user=user,
    #     city="Old City",
    #     address="Old Address 123"
    # )
    #
    #
    # new_product = create_product(
    #     session=current_session,
    #     name="PS5",
    #     price=3500,
    #     ammount=20,
    #     comment="5"
    # )
