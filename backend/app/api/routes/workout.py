from fastapi import APIRouter

from app.schemas.workout import WorkoutCreate
from app.services.workout_service import WorkoutService

router = APIRouter(
    prefix="/workouts",
    tags=["Workouts"]
)

@router.post("")
def create_workout(workout: WorkoutCreate):
    return WorkoutService.create(workout)