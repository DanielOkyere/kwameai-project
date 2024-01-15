from datetime import datetime
from typing import TYPE_CHECKING

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.types import String

from app.db import Base

if TYPE_CHECKING:
    from app.models.posts import Posts, Likes


class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"

    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )
    username: Mapped[str] = mapped_column(String(250), nullable=False, index=True)
    image: Mapped[str] = mapped_column(String(300), nullable=True)
    posts: Mapped["Posts"] = relationship(back_populates="user", cascade="all, delete")
    likes: Mapped["Likes"] = relationship(back_populates="user", cascade="all, delete")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.email!r})"

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


