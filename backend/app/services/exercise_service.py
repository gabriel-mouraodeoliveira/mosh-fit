from app.database.connection import SessionLocal
from app.models.exercise import Exercise
from app.schemas.exercise import ExerciseCreate


class ExerciseService:

    @staticmethod
    def create(exercise: ExerciseCreate):

        db = SessionLocal()

        try:

            exercise_db = Exercise(
                name=exercise.name,
                muscle_group=exercise.muscle_group
            )

            db.add(exercise_db)

            db.commit()

            db.refresh(exercise_db)

            return {
                "id": exercise_db.id,
                "name": exercise_db.name,
                "muscle_group": exercise_db.muscle_group
            }

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()