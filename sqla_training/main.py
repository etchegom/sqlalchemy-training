from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("postgresql://postgres:postgres@localhost:5432/sqlatraining", echo=True)
conn = engine.connect()
# metadata = MetaData()


def create_user():
    with Session(engine) as session:
        anakin = User(
            firstname="Anakin",
            lastname="Shywalker",
            personal_info="I am a Jedi",
            phone_number="123456789",
        )
        session.add(anakin)
        session.commit()


def list_users():
    with Session(engine) as session:
        for user in session.query(User).all():
            print(f"user {user} => {user.personal_info}")


if __name__ == "__main__":
    # create_user()
    list_users()
