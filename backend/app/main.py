from fastapi import FastAPI

app = FastAPI(
    title="Mosh Fit API",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Mosh Fit API is running"
    }