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

@router.get("")
def list_workouts():
    return WorkoutService.list()   

@router.get("/{workout_id}")
def get_workout(workout_id: int):
    return WorkoutService.get_by_id(workout_id)

@router.patch("/{workout_id}/deactivate", status_code=204)
def deactivate(workout_id: int):
    WorkoutService.deactivate(workout_id) 

@router.patch("/{workout_id}/activate", status_code=204)
def activate(workout_id: int):
    WorkoutService.activate(workout_id)   