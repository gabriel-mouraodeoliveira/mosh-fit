from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base import Base


class WorkoutExercise(Base):
    __tablename__ = "workout_exercises"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True
    )

    workout_id: Mapped[int] = mapped_column(
        ForeignKey("workouts.id")
    )

    exercise_id: Mapped[int] = mapped_column(
        ForeignKey("exercises.id")
    )

    sets: Mapped[int] = mapped_column(
        Integer
    )

    reps: Mapped[int] = mapped_column(
        Integer
    )

    weight: Mapped[float] = mapped_column(
        Float
    )