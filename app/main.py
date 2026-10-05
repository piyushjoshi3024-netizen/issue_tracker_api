from fastapi import FastAPI

from app.database import engine, Base
from app.models.issue import Issue
from app.routers.issues import router as issues_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Issue Tracker API",
    description="Backend API for managing software development issues"
)


# Register routers
app.include_router(
    issues_router,
    prefix="/issues",
    tags=["Issues"]
)


@app.get("/")
async def root():
    return {
        "message": "Welcome to the Issue Tracker API!"
    }