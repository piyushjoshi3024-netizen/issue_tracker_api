from datetime import datetime

from pydantic import BaseModel, Field


class CommentCreate(BaseModel):
    content: str = Field(
        min_length=1,
        max_length=1000
    )


class CommentUpdate(BaseModel):
    content: str = Field(
        min_length=1,
        max_length=1000
    )


class CommentResponse(BaseModel):
    id: int
    issue_id: int
    user_id: int
    content: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }