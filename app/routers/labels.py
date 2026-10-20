from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select
    
from app.database import get_db
from app.models.label import Label
from app.models.issue import Issue

from app.schemas.label import LabelCreate, LabelResponse
from app.utils.dependencies import get_current_user

router = APIRouter()

@router.post(
    "/",
    
    response_model=LabelResponse,
    status_code=status.HTTP_201_CREATED,
)

def create_label(
    label_data: LabelCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    # Check if the label name already exists
    existing_label = db.execute(
        select(Label).where(Label.name == label_data.name)
    ).scalar_one_or_none()

    if existing_label:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Label with this name already exists."
        )

    new_label = Label(
        name=label_data.name
    )
    
    db.add(new_label)
    db.commit()
    db.refresh(new_label)

    return new_label    

@router.get(
    "/",
    response_model=list[LabelResponse],
)
def get_labels(
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    
    result = db.execute(
        select(Label).order_by(Label.name)  
    )
    
    return result.scalars().all()

@router.post(
    "/issues/{issue_id}/labels/{label_id}",
    status_code=status.HTTP_200_OK
)
def attach_label_to_issue(
    issue_id: int,
    label_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )

    label = db.get(Label, label_id)

    if not label:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Label not found"
        )

    if label in issue.labels:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Label already attached to issue"
        )

    issue.labels.append(label)

    db.commit()

    return {
        "message": "Label attached successfully"
    }
    
@router.get(
    "/issues/{issue_id}/labels",
    response_model=list[LabelResponse]
)
def get_issue_labels(
    issue_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )

    return issue.labels


@router.get(
    "/issues/{issue_id}/labels",
    response_model=list[LabelResponse]
)
def get_issue_labels(
    issue_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )

    return issue.labels


@router.delete(
    "/issues/{issue_id}/labels/{label_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def detach_label_from_issue(
    issue_id: int,
    label_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    issue = db.get(Issue, issue_id)

    if not issue:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Issue not found"
        )

    label = db.get(Label, label_id)

    if not label:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Label not found"
        )

    if label not in issue.labels:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Label is not attached to this issue"
        )

    issue.labels.remove(label)

    db.commit()