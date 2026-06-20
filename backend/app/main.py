from fastapi import FastAPI

from app.api.routes.workout import router as workout_router
from app.api.routes.exercise import router as exercise_router

app = FastAPI(
    title="Mosh Fit API",
    version="0.1.0"
)

app.include_router(exercise_router)
app.include_router(workout_router)


@app.get("/")
def root():
    return {
        "message": "Mosh Fit API is running"
    }