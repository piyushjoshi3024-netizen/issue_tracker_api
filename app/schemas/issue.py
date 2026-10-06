from pydantic import BaseModel, Field
from enum import Enum


class IssueStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    CLOSED = "closed"


class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class IssueCreate(BaseModel):

    title: str = Field(
        min_length=3,
        max_length=100
    )

    description: str

    status: IssueStatus = IssueStatus.OPEN

    priority: IssuePriority = IssuePriority.MEDIUM


class IssueUpdate(BaseModel):
    
    title: str | None = Field(
        default=None,
        min_length=3,
        max_length=100
    )

    description: str | None = None

    status: IssueStatus | None = None

    priority: IssuePriority | None = None


class IssueResponse(BaseModel):

    id: int
    title: str
    description: str
    status: IssueStatus
    priority: IssuePriority

    model_config = {
        "from_attributes": True
    }
    
class IssueMessageResponse(BaseModel):
    
    message: str
    issue: IssueResponse