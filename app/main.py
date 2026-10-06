from fastapi import FastAPI

from app.database import engine, Base
from app.models.issue import Issue
from app.routers.issues import router as issues_router

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError

# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Issue Tracker API",
    description="Backend API for managing software development issues"
)


@app.exception_handler(SQLAlchemyError)
async def sqlalchemy_exception_handler(
    request: Request,
    exc: SQLAlchemyError
):
    return JSONResponse(
        status_code=500,
        content={
            "detail": "A database error occurred"
        }
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