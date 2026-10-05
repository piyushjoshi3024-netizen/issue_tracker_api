from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.issue import Issue
from app.schemas.issue import IssueCreate, IssueUpdate

router = APIRouter()


# =========================
# GET ALL ISSUES
# =========================

@router.get("/")
def get_issues(
    db: Session = Depends(get_db)
):
    result = db.execute(select(Issue))
    issues = result.scalars().all()

    return {
        "issues": issues
    }


# =========================
# GET ONE ISSUE
# =========================

@router.get("/{issue_id}")
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

@router.post("/")
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

@router.put("/{issue_id}")
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

    update_data = issue_data.model_dump(exclude_unset=True)

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

@router.delete("/{issue_id}")
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

    deleted_issue = {
        "id": issue.id,
        "title": issue.title,
        "description": issue.description,
        "status": issue.status,
        "priority": issue.priority
    }

    db.delete(issue)
    db.commit()

    return {
        "message": "Issue deleted successfully",
        "issue": deleted_issue
    }