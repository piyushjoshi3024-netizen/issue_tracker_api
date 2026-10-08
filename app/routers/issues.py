from fastapi import APIRouter, Depends, HTTPException, status , Query

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.issue import Issue
from app.schemas import issue
from app.schemas.issue import (
    IssueCreate,
    IssueUpdate,
    IssueResponse,
    IssueMessageResponse,
    IssueStatus,
    IssuePriority
)

router = APIRouter()


# =========================
# GET ALL ISSUES
# =========================

@router.get("/", response_model=list[IssueResponse])
def get_issues(
    status_filter: IssueStatus | None = Query(default=None),
    priority_filter: IssuePriority | None = Query(default=None),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    sort_by: str = Query(default="created_at"),
    order: str = Query(default="desc"),
    db: Session = Depends(get_db)
):
    query = select(Issue)

    # Filtering
    if status_filter:
        query = query.where(Issue.status == status_filter.value)

    if priority_filter:
        query = query.where(Issue.priority == priority_filter.value)

    # Sorting
    if sort_by == "created_at":
        column = Issue.created_at
    elif sort_by == "updated_at":
        column = Issue.updated_at
    elif sort_by == "priority":
        column = Issue.priority
    else:
        column = Issue.created_at

    if order == "asc":
        query = query.order_by(column.asc())
    else:
        query = query.order_by(column.desc())

    # Pagination
    query = query.offset(skip).limit(limit)

    result = db.execute(query)

    return result.scalars().all()


# =========================
# GET ONE ISSUE
# =========================

@router.get("/{issue_id}", response_model=IssueResponse)
def get_issue(
    issue_id: int,
    db: Session = Depends(get_db)
):
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Issue not found"
        )

    return issue


# =========================
# CREATE ISSUE
# =========================

@router.post(
    "/",
    response_model=IssueMessageResponse,
    status_code=status.HTTP_201_CREATED
)
def create_issue(
    issue_data: IssueCreate,
    db: Session = Depends(get_db)
):
    new_issue = Issue(
        title=issue_data.title,
        description=issue_data.description,
        status=issue_data.status.value,
        priority=issue_data.priority.value
    )

    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)

    return {
        "message": "Issue created successfully",
        "issue": new_issue
    }


# =========================
# UPDATE ISSUE
# =========================

@router.put(
    "/{issue_id}",
    response_model=IssueMessageResponse
)
def update_issue(
    issue_id: int,
    issue_data: IssueUpdate,
    db: Session = Depends(get_db)
):
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Issue not found"
        )

    update_data = issue_data.model_dump(
        exclude_unset=True
    )

    if "status" in update_data:
        update_data["status"] = update_data["status"].value

    if "priority" in update_data:
        update_data["priority"] = update_data["priority"].value

    for field, value in update_data.items():
        setattr(issue, field, value)

    db.commit()
    db.refresh(issue)

    return {
        "message": "Issue updated successfully",
        "issue": issue
    }


# =========================
# DELETE ISSUE
# =========================

@router.delete(
    "/{issue_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_issue(
    issue_id: int,
    db: Session = Depends(get_db)
):
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=404,
            detail="Issue not found"
        )

    db.delete(issue)
    db.commit();