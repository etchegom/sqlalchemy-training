from datetime import datetime
from typing import List

from sqlalchemy import DateTime, ForeignKey, String, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils import StringEncryptedType
from sqlalchemy_utils.types.encrypted.encrypted_type import AesEngine

Base = declarative_base()

secret = "you_shall_not_pass"


class PkModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)


class TimeStampedPkModel(PkModel):
    __abstract__ = True

    created = mapped_column(DateTime, nullable=False, server_default=func.now())
    modified = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=datetime.utcnow
    )


class User(TimeStampedPkModel):
    __tablename__ = "user"

    firstname: Mapped[str] = mapped_column(String(50))
    lastname: Mapped[str] = mapped_column(String(50))

    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )

    phone_number: Mapped[str]

    personal_info: Mapped[str] = mapped_column(
        StringEncryptedType(String, key=secret, engine=AesEngine, padding="pkcs5")
    )

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.firstname!r}, fullname={self.lastname!r})"


class Address(TimeStampedPkModel):
    __tablename__ = "address"

    email_address: Mapped[str]

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
