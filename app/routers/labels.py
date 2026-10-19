from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select

from app.database import get_db
from app.models.label import Label
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