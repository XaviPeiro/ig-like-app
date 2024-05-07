from sqlalchemy import Column, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    images: Mapped[list["Image"]] = relationship()


# TODO: Probar sqlalchemy-utils with new typing mapping and uuid.
class Image(Base):
    __tablename__ = "images"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    url: Mapped[str] = mapped_column(unique=True)
    owner_id: Mapped[User] = mapped_column(ForeignKey("users.id"))
    # owner: Mapped[User] = relationship(back_populates="images")
