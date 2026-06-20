from app.database.base import Base
from app.database.connection import engine

from app.models.exercise import Exercise

from app.models.exercise import Exercise
from app.models.workout import Workout
from app.models.workout_exercise import WorkoutExercise


Base.metadata.create_all(bind=engine)

print("Tabelas criadas com sucesso!")