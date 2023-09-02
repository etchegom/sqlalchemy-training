from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self):
        return f"<Student(name={self.name})>"
