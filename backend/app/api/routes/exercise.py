from fastapi import APIRouter
from app.schemas.exercise import ExerciseCreate
from app.services.exercise_service import ExerciseService


router = APIRouter(
    prefix="/exercises",
    tags=["Exercises"]
)


@router.post("")
def create_exercise(exercise: ExerciseCreate):
    return ExerciseService.create(exercise)