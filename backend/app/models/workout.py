from datetime import date

from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class Workout(Base):
    __tablename__ = "workouts"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    workout_date: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    name: Mapped[str] = mapped_column(
    String(100),
    nullable=False
    )