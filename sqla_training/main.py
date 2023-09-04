from models import Address, User
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql://postgres:postgres@localhost:5432/sqlatraining", echo=True)
conn = engine.connect()
metadata = MetaData()


if __name__ == "__main__":
    metadata.create_all(engine)

    with Session(engine) as session:
        anakin = User(
            firstname="Anakin",
            lastname="Shywalker",
            addresses=[Address(email_address="anakin.skywalker@test.org")],
        )
