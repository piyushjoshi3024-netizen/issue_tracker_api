from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.comment import Comment
from app.models.issue import Issue
from app.models.user import User
from app.schemas.comment import (
    CommentCreate,
    CommentUpdate,
    CommentResponse
)
from app.utils.dependencies import get_current_user


router = APIRouter()


@router.post(
    "/issues/{issue_id}/comments",
    response_model=CommentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_comment(
    issue_id: int,
    comment_data: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check whether the issue exists
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )

    # Create the comment
    new_comment = Comment(
        issue_id=issue_id,
        user_id=current_user.id,
        content=comment_data.content
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


@router.get(
    "/issues/{issue_id}/comments",
    response_model=list[CommentResponse]
)
def get_issue_comments(
    issue_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check whether the issue exists
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )

    # Get comments belonging to this issue
    query = select(Comment).where(
        Comment.issue_id == issue_id
    )

    result = db.execute(query)

    return result.scalars().all()