from pydantic import BaseModel
from datetime import date


class WorkoutExerciseCreate(BaseModel):
    exercise_id: int
    sets: int
    reps: int
    weight: float



class WorkoutCreate(BaseModel):
    name: str
    workout_date: date
    exercises: list[WorkoutExerciseCreate]