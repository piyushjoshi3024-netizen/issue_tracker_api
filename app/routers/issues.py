from fastapi import APIRouter, Depends, HTTPException, status , Query

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.issue import Issue
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
    status_filter: str | None = Query(default=None, alias="status"),
    priority_filter: str | None = Query(default=None, alias="priority"),
    skip: int = Query(default = 0, ge = 0),
    limit: int = Query(default = 10 , ge = 1 , le = 100),
    db: Session = Depends(get_db)
):
    
    query = select(Issue)
    if status_filter:
        query = query.where(Issue.status == status_filter)
        
    if priority_filter:
        query = query.where(Issue.priority == priority_filter)
            
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