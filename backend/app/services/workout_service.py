from fastapi import HTTPException

from sqlalchemy import select

from app.database.connection import SessionLocal
from app.models.exercise import Exercise
from app.models.workout import Workout
from app.models.workout_exercise import WorkoutExercise
from app.schemas.workout import WorkoutCreate


class WorkoutService:

    @staticmethod
    def create(workout: WorkoutCreate):
        db = SessionLocal()

        try:
            exercise_ids = [
                exercise.exercise_id
                for exercise in workout.exercises
            ]

            stmt = select(Exercise).where(
                Exercise.id.in_(exercise_ids)
            )


            existing_exercises = (
                db.execute(stmt)
                .scalars()
                .all()
            )

            if len(existing_exercises) != len(exercise_ids):
                raise HTTPException(
                    status_code=404,
                    detail="One or more exercises do not exist"
                )

            workout_db = Workout(
                name=workout.name,
                workout_date=workout.workout_date
            )

            db.add(workout_db)

            # Obtém o ID sem finalizar a transação
            db.flush()

            workout_exercises = [
                WorkoutExercise(
                    workout_id=workout_db.id,
                    exercise_id=exercise.exercise_id,
                    sets=exercise.sets,
                    reps=exercise.reps,
                    weight=exercise.weight
                )
                for exercise in workout.exercises
            ]

            db.add_all(workout_exercises)

            db.commit()

            return {
                "id": workout_db.id,
                "name": workout_db.name,
                "workout_date": workout_db.workout_date,
                "exercises": [
                    {
                        "exercise_id": exercise.exercise_id,
                        "sets": exercise.sets,
                        "reps": exercise.reps,
                        "weight": exercise.weight
                    }
                    for exercise in workout.exercises
                ]
            }

        except Exception:
            db.rollback()
            raise

        finally:
            db.close()

    @staticmethod
    def list():
        db = SessionLocal()

        try:
            stmt = select(Workout).where(Workout.is_active).order_by(Workout.workout_date.desc())

            workouts = db.execute(stmt).scalars().all()

            return [
                    {
                        "id": workout.id,
                        "workout_date": workout.workout_date,
                        "name": workout.name
                    }    
                    for workout in workouts           
            ]

        finally:
            db.close()    


    @staticmethod
    def get_by_id(workout_id: int):
        db = SessionLocal()

        try:
            stmt = select(Workout).where(Workout.id == workout_id)

            workout = (
                db.execute(stmt).scalars().first()               
            )

            if not workout:
                raise HTTPException(
                    status_code=404,
                    detail="Workout not found"
                )

            stmt = select(WorkoutExercise).where(WorkoutExercise.workout_id == workout.id)

            workout_exercises = (
                db.execute(stmt)
                .scalars()
                .all()
            )

            
            exercise_ids = [
                workout_exercise.exercise_id
                for workout_exercise in workout_exercises
            ]

            stmt = select(Exercise).where(
            Exercise.id.in_(exercise_ids)
            )

            exercises = (
                db.execute(stmt)
                .scalars()
                .all()
            )

            exercise_map = {
                exercise.id: exercise
                for exercise in exercises
            }

            exercise_data = [
                {
                    "exercise_id": workout_exercise.exercise_id,
                    "exercise_name": exercise_map[
                        workout_exercise.exercise_id
                    ].name,
                    "sets": workout_exercise.sets,
                    "reps": workout_exercise.reps,
                    "weight": workout_exercise.weight
                }
                for workout_exercise in workout_exercises
            ]

            return {
                "id": workout.id,
                "name": workout.name,
                "workout_date": workout.workout_date,
                "exercises": exercise_data
            }

            pass

        finally:
            db.close()        




