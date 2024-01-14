from datetime import datetime
from typing import TYPE_CHECKING
from uuid import UUID

from fastapi_users_db_sqlalchemy import GUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql.functions import func
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime, String, Boolean, Integer

from app.db import Base

if TYPE_CHECKING:
    from app.models.user import User  # noqa: F401


class Posts(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[UUID] = mapped_column(GUID, ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="posts")

    created: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )
    updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    title: Mapped[str] = mapped_column(String(400), nullable=False, index=True)
    content: Mapped[str] = mapped_column(String, nullable=False)
    published: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    image: Mapped[str] = mapped_column(String, nullable=True)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Likes(Base):
    __tablename__ = "likes"
    post_id: Mapped[int] = mapped_column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)
    user_id: Mapped[UUID] = mapped_column(GUID, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    user: Mapped["User"] = relationship(back_populates="likes")