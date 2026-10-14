from datetime import datetime

from sqlalchemy import Text, DateTime , ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Comment(Base):
    __tablename__ = "comments"
    
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    
    issue_id: Mapped[int] = mapped_column(
        ForeignKey("issues.id", ondelete="CASCADE"),
        nullable=False
    )
    
    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False
    )
    
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        nullable=False 
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )
    
    issue: Mapped["Issue"] = relationship(
        back_populates="comments",
    )
    
    user: Mapped["User"] = relationship(
        back_populates="comments",
    )
    
