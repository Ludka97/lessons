from sqlalchemy.orm import sessionmaker, Session

from models import Base, User, Profile, Address, Product
from utils import setup_db_engine, create_database_if_not_exists


def create_user(
        session: Session, email: str, password: str, phone: str, age: int, city: str, address: str
) -> User:
    user = User(email=email, password=password)
    profile = Profile(phone=phone, age=age)
    address = Address(city=city, address=address)

    session.add_all([user, profile, address])
    session.commit()

    return user


def update_or_create(session: Session, user: User, city: str, address: str) -> Address:
    if len(user.addresses):
        current_address = user.addresses[0]
        current_address.city = city
        current_address.address = address
    else:
        current_session = Address(user=user, city=city, address=address)

    session.add(address)
    session.commit()

    # return current_session


def create_product(
        session: Session, name: str, price: int, ammount: int, comment: str
) -> Product:
    product = Product(name=name, price=price, ammount=ammount, comment=comment)

    session.add(product)
    session.commit()

    return product


def get_product(
        session: Session, name: str, price: int, ammount: int, comment: str
) -> Product:
    product = Product(name=name, price=price, ammount=ammount, comment=comment)

    product_list = session.get(product)
    session.commit()

    return product_list


def update_or_create_product(session: Session, name: str, price: int, ammount: int, comment: str) -> Product:
    if len(product.id):
        current_product = product.addresses[0]
        current_product.name = name
        current_product.price = price
        current_product.ammount = ammount
        current_product.comment = comment
    else:
        current_session = Product(name=name, price=price, ammount=ammount, comment=comment)

    session.add(product)
    session.commit()

    return current_session


def delete_product(
        session: Session, name: str, price: int, ammount: int, comment: str
) -> Product:
    product = Product(name=name, price=price, ammount=ammount, comment=comment)

    session.delete(product)
    session.commit()

    return product



if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    # Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    # new_user = create_user(
    #     session=current_session,
    #     email="test@gmail.com",
    #     password="test0pass",
    #     phone="80295554433",
    #     age=25,
    #     city="NY",
    #     address="street_num"
    # )

    # user = current_session.query(User).filter_by(email="test@test.com").first()
    # update_or_create(
    #     session=current_session,
    #     user=user,
    #     city="Old city",
    #     address="Old_address"
    # )

    new_product = create_product(
        session=current_session,
        name="TV-set",
        price=1500,
        ammount=100,
        comment="25"
    )
