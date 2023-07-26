import sqlalchemy as db

from os import path as op
from pprint import pprint


engine = db.create_engine(f"sqlite:///{op.abspath(op.dirname(__file__))}/european_database.sqlite")
conn = engine.connect()

metadata = db.MetaData()

Division = db.Table("divisions", metadata, autoload_with=engine)

Student = db.Table(
    "Student",
    metadata,
    db.Column("Id", db.Integer(), primary_key=True),
    db.Column("Name", db.String(255), nullable=False),
    db.Column("Major", db.String(255), default="Math"),
    db.Column("Pass", db.Boolean(), default=True),
)

metadata.create_all(engine)


def select_divisions():
    query = Division.select().where(Division.columns.name == "Premier League")
    results = conn.execute(query).fetchmany(size=5)
    pprint(results)


def create_students():
    query = Student.insert()
    values_list = [
        {"Id": "2", "Name": "Nisha", "Major": "Science", "Pass": False},
        {"Id": "3", "Name": "Natasha", "Major": "Math", "Pass": True},
        {"Id": "4", "Name": "Ben", "Major": "English", "Pass": False},
    ]
    conn.execute(query, values_list)


def select_students():
    query = Student.select()
    # query = Student.select().where(Student.columns.Major == 'English')
    results = conn.execute(query).fetchall()
    pprint(results)


if __name__ == "__main__":
    # show_divisions()
    create_students()
    select_students()
