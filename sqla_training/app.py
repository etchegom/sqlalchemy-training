from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from sqla_training.factories import UserFactory
from sqla_training.models import User

engine = create_engine("postgresql://postgres:postgres@localhost:5432/sqlatraining", echo=True)
# conn = engine.connect()


def create_session():
    session = scoped_session(sessionmaker(engine))

    for factory_class in (UserFactory,):
        factory_class._meta.sqlalchemy_session = session

    return session


def populate(session):
    UserFactory.create_batch(10)
    # anakin = User(
    #     firstname="Anakin",
    #     lastname="Shywalker",
    #     personal_info="I am a Jedi",
    #     phone_number="123456789",
    # )
    # session.add(anakin)
    session.commit()


def run_queries(session):
    for user in session.query(User).all():
        print(f"user {user} => {user.personal_info}")
