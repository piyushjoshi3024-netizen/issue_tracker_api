from datetime import datetime

from sqlalchemy import String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class User(Base):
    __tablename__ = "users"
    
    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )
    
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False
    )
    
    email: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )
    
    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )
    
    role: Mapped[str] = mapped_column(
        String(20),   #max 20 characters for role
        nullable=False,
        default="user"
    )
    
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False
    )
    
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,   
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )