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
from app.utils.dependencies import (
    get_current_user,
    get_user_comment
)


router = APIRouter()


# CREATE COMMENT
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
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )

    new_comment = Comment(
        issue_id=issue_id,
        user_id=current_user.id,
        content=comment_data.content
    )

    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment


# GET COMMENTS FOR AN ISSUE
@router.get(
    "/issues/{issue_id}/comments",
    response_model=list[CommentResponse]
)
def get_issue_comments(
    issue_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )

    query = (
        select(Comment)
        .where(Comment.issue_id == issue_id)
        .order_by(Comment.created_at.desc())
    )

    result = db.execute(query)

    return result.scalars().all()


# UPDATE COMMENT
@router.put(
    "/comments/{comment_id}",
    response_model=CommentResponse
)
def update_comment(
    comment_data: CommentUpdate,
    comment: Comment = Depends(get_user_comment),
    db: Session = Depends(get_db)
):
    comment.content = comment_data.content

    db.commit()
    db.refresh(comment)

    return comment


# DELETE COMMENT
@router.delete(
    "/comments/{comment_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_comment(
    comment: Comment = Depends(get_user_comment),
    db: Session = Depends(get_db)
):
    db.delete(comment)
    db.commit()