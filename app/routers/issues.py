from fastapi import APIRouter, Depends, HTTPException, status , Query

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.utils.dependencies import (
    get_current_user,
    get_user_issue,
    require_admin,
    get_admin_issue
)
from app.database import get_db
from app.models.issue import Issue
from app.schemas import issue
from app.models.user import User
from app.schemas.issue import (
    IssueCreate,
    IssueUpdate,
    IssueResponse,
    IssueMessageResponse,
    IssueStatus,
    IssuePriority
)
from app.utils.dependencies import get_current_user
router = APIRouter()

from sqlalchemy import select, or_


# =========================
# GET ALL ISSUES
# =========================

@router.get("/my", response_model=list[IssueResponse])
def get_my_issues(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = select(Issue).where(
        Issue.user_id == current_user.id
    )

    result = db.execute(query)

    return result.scalars().all()


@router.get("/", response_model=list[IssueResponse])
def get_issues(
    status_filter: IssueStatus | None = Query(default=None),
    priority_filter: IssuePriority | None = Query(default=None),
    skip: int = Query(default=0, ge=0),
    limit: int = Query(default=10, ge=1, le=100),
    sort_by: str = Query(default="created_at"),
    order: str = Query(default="desc"),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = select(Issue).where(
        Issue.user_id == current_user.id
        )

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

#===============================
# Admin getting the issues of all users
#==============================

@router.get("/admin", response_model=list[IssueResponse])
def get_all_issues_admin(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    query = select(Issue)
    
    result = db.execute(query)
    
    return result.scalars().all()

# =========================
# GET ONE ISSUE
# =========================


@router.get("/{issue_id}", response_model=IssueResponse)
def get_issue(
   issue: Issue = Depends(get_user_issue)
):
    issue = db.execute(
        select(Issue).where(
            Issue.id == issue_id,
            Issue.user_id == current_user.id
            )
        ).scalar_one_or_none()

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
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    new_issue = Issue(
    title=issue_data.title,
    description=issue_data.description,
    status=issue_data.status.value,
    priority=issue_data.priority.value,
    user_id=current_user.id
)

    db.add(new_issue)
    db.commit()
    db.refresh(new_issue)

    return {
        "message": "Issue created successfully",
        "issue": new_issue
    }

#=====================
# admin updating the issue
#====================

@router.put(
    "/admin/{issue_id}",
    response_model=IssueMessageResponse
)
def admin_update_issue(
    issue_data: IssueUpdate,
    issue: Issue = Depends(get_admin_issue),
    db: Session = Depends(get_db)
):
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
        "message": "Issue updated successfully by admin",
        "issue": issue
    }

# =========================
# UPDATE ISSUE
# =========================

@router.put("/{issue_id}", response_model=IssueMessageResponse)
def update_issue(
    issue_data: IssueUpdate,
    issue: Issue = Depends(get_user_issue),
    db: Session = Depends(get_db)
):
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


#=========================
# admin deleting the issue
#=======================

@router.delete(
    "/admin/{issue_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def admin_delete_issue(
    issue: Issue = Depends(get_admin_issue),
    db: Session = Depends(get_db)
):
    db.delete(issue)
    db.commit()



# =========================
# DELETE ISSUE
# =========================

@router.delete(
    "/{issue_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_issue(
    issue: Issue = Depends(get_user_issue),
    db: Session = Depends(get_db)
):
    db.delete(issue)
    db.commit()