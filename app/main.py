from fastapi import FastAPI, HTTPException
from app.schemas.issue import IssueCreate, IssueUpdate




app = FastAPI(
    title="Issue Tracker API",
    description="Backend API for managing software issues"
)

# Temporary in-memory storage
issues = []
next_issue_id = 1


# -------------------------
# ROOT
# -------------------------

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Issue Tracker API!"
    }


# -------------------------
# CREATE ISSUE
# POST /issues
# -------------------------

@app.post("/issues")
async def create_issue(issue: IssueCreate):
    global next_issue_id

    new_issue = {
        "id": next_issue_id,
        **issue.model_dump()
    }

    issues.append(new_issue)

    next_issue_id += 1

    return {
        "message": "Issue created successfully",
        "issue": new_issue
    }


# -------------------------
# GET ALL ISSUES
# GET /issues
# -------------------------

@app.get("/issues")
async def get_issues():
    return {
        "issues": issues
    }


# -------------------------
# GET SINGLE ISSUE
# GET /issues/{issue_id}
# -------------------------

@app.get("/issues/{issue_id}")
async def get_issue(issue_id: int):

    for issue in issues:

        if issue["id"] == issue_id:
            return issue

    raise HTTPException(
        status_code=404,
        detail="Issue not found"
    )
    

@app.put("/issues/{issue_id}")
async def update_issue(issue_id: int, issue: IssueUpdate):

    # Find the issue
    for existing_issue in issues:

        if existing_issue["id"] == issue_id:

            # Get only the fields sent by the user
            update_data = issue.model_dump(exclude_unset=True)

            # Update those fields
            existing_issue.update(update_data)

            return {
                "message": "Issue updated successfully",
                "issue": existing_issue
            }

    # If issue doesn't exist
    raise HTTPException(
        status_code=404,
        detail="Issue not found"
    )
    

@app.delete("/issues/{issue_id}")
async def delete_issue(issue_id: int):

    for index, issue in enumerate(issues):

        if issue["id"] == issue_id:
            deleted_issue = issues.pop(index)

            return {
                "message": "Issue deleted successfully",
                "issue": deleted_issue
            }

    raise HTTPException(
        status_code=404,
        detail="Issue not found"
    )

