# Issue Tracker API

A production-oriented REST API for managing software development issues such as bugs, feature requests, development tasks, critical problems, and improvements.

The project provides a backend system similar to the issue-tracking functionality found in platforms such as GitHub Issues and Jira. It allows development teams to create, organize, prioritize, update, and track issues throughout their lifecycle.

Built with **FastAPI, PostgreSQL, SQLAlchemy, and Pydantic**, the project focuses on clean API design, reliable data persistence, validation, and maintainable backend architecture.

---

## Overview

The Issue Tracker API provides the core backend functionality required by a software development team to manage development issues.

An issue can represent:

- 🐛 Bug reports
- ✨ Feature requests
- 📋 Development tasks
- 🚨 Critical problems
- 🔧 Improvements
- 🛠️ Maintenance work

Each issue can be assigned a priority and tracked through different stages of its lifecycle.

The API is designed as a standalone backend service that can be consumed by web applications, mobile applications, internal tools, or other services.

---

## Features

### Issue Management

- Create new issues
- Retrieve all issues
- Retrieve a specific issue
- Update existing issues
- Delete issues
- Track issue status
- Assign issue priority

### Validation

- Request body validation using Pydantic
- Required field validation
- String length validation
- Enum-based status validation
- Enum-based priority validation

### Database

- PostgreSQL database
- SQLAlchemy ORM
- Persistent issue storage
- Automatic database model mapping
- Environment-based database configuration

### API

- RESTful API architecture
- HTTP status codes
- Structured JSON responses
- Error handling
- Interactive Swagger documentation
- ReDoc documentation

---

Please consider the current repository a work in progress until the final release.

> **The current repository should be considered a work in progress.**


###Tech Stack

| Technology          | Purpose                     |
| ------------------- | --------------------------- |
| **Python 3.14**     | Programming language        |
| **FastAPI**         | REST API framework          |
| **Pydantic v2**     | Request/response validation |
| **SQLAlchemy 2.1**  | ORM                         |
| **PostgreSQL 18**   | Relational database         |
| **Psycopg 3**       | PostgreSQL driver           |
| **Alembic**         | Database migrations         |
| **Uvicorn**         | ASGI server                 |
| **PyJWT**           | JWT authentication          |
| **pwdlib + Argon2** | Password hashing            |
| **python-dotenv**   | Environment configuration   |
| **DataGrip**        | Database management         |


## Architecture

```text
                         Client
                           │
                           ▼
                    ┌─────────────┐
                    │   FastAPI   │
                    └──────┬──────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ Authentication & │
                 │  Authorization   │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    Pydantic      │
                 │   Validation     │
                 └────────┬─────────┘
                          │
                          ▼
                 ┌──────────────────┐
                 │    SQLAlchemy    │
                 │       ORM        │
                 └────────┬─────────┘
                          │
                          ▼
                    ┌───────────┐
                    │  Psycopg  │
                    └─────┬─────┘
                          │
                          ▼
                    ┌───────────┐
                    │ PostgreSQL│
                    └───────────┘


📌 Current Development Status

##Completed

 FastAPI project setup
 PostgreSQL integration
 SQLAlchemy ORM
 Psycopg 3 integration
 Database session management
 Transaction handling
 Pydantic request schemas
 Pydantic response schemas
 Issue CRUD
 Modular API routers
 Proper HTTP status codes
 Error handling
 Global SQLAlchemy exception handling
 Issue timestamps
 Filtering
 Pagination
 Sorting
 Alembic setup
 Database migrations
 User model
 User registration
 Password hashing
 Login
 JWT authentication
 Current-user authentication
 Protected routes
 User ↔ Issue relationship
 Issue ownership authorization
 Role-based access control
 Admin role
 Admin authorization dependency
 Admin issue listing
 Admin issue updating
 Admin issue deletion....

🚧In Development

 Issue comments
 Comment-user relationship
 Comment-issue relationship
 Comment authorization
 Labels / tags
 Advanced search
 Issue assignment
 Activity / audit logs
 Automated testing with Pytest
 Database constraints and indexes
 Docker
 CI/CD
 Production deployment



🗓️ Project Completion Target

🎯 Target Completion Date: October 18, 2026

The project is currently in active development.

The core backend architecture, database integration, authentication, authorization, issue management, filtering, pagination, sorting, migrations, and administrator functionality have been implemented.

The remaining development focuses on completing advanced issue-management features, automated testing, containerization, deployment, and final production-oriented improvements.


he final version aims to provide:


##FastAPI Backend
       │
       ├── Authentication
       ├── Authorization
       ├── RBAC
       ├── Issue Management
       ├── Comments
       ├── Labels
       ├── Search
       ├── Filtering
       ├── Pagination
       ├── Audit Logs
       ├── Automated Testing
       ├── Docker
       ├── CI/CD
       └── Cloud Deployment


📌 Project Status

🚧 Active Development

Target completion: October 18, 2026

The repository will continue receiving incremental feature, architecture, testing, and deployment improvements until the planned completion date.