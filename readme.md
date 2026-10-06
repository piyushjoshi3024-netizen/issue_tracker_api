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

## Tech Stack

- **Python 3.14**
- **FastAPI** — REST API framework
- **Pydantic v2** — Request/response validation
- **SQLAlchemy 2.1** — ORM
- **PostgreSQL 18** — Relational database
- **Psycopg 3** — PostgreSQL driver
- **Alembic** — Database migrations
- **Uvicorn** — ASGI server
- **python-dotenv** — Environment variable management
- **DataGrip** — Database client

---
##🚧 Current Development Status

🚧 Project Under Active Development

This project is currently in the building phase and is not yet considered production-ready. Features, APIs, database integration, and project structure are actively being implemented and refined.

The planned completion target is October 12, 2026.

Once the project reaches its stable release, this README will be updated with:

Complete setup instructions
Required dependencies
Environment configuration
Database setup
Local development instructions
API documentation and usage examples
Complete project structure and configuration details

Please consider the current repository a work in progress until the final release.

> **Target completion:** October 12, 2026

> This project is currently in the building phase and is not yet production-ready. Core features, database integration, API functionality, and project structure are actively being implemented and refined.

> After completion, this README will be updated with the complete setup guide, dependencies, environment configuration, database setup, local development instructions, API documentation, and usage examples required to run the project locally.
>
> **The current repository should be considered a work in progress.**


## Architecture

```text
                    Client
                      │
                      ▼
                ┌───────────┐
                │  FastAPI  │
                └─────┬─────┘
                      │
                      ▼
              ┌───────────────┐
              │    Pydantic   │
              │   Validation  │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   SQLAlchemy  │
              │      ORM      │
              └───────┬───────┘
                      │
                      ▼
                ┌───────────┐
                │  psycopg  │
                └─────┬─────┘
                      │
                      ▼
                ┌───────────┐
                │ PostgreSQL│
                └───────────┘


📌 Current Development Status
Completed
 FastAPI project setup
 PostgreSQL integration
 SQLAlchemy ORM
 Pydantic request schemas
 Pydantic response schemas
 Issue CRUD
 Modular API router
 HTTP status codes
 Database session management
 Transaction handling
 Global SQLAlchemy exception handling
 Issue timestamps
 Alembic setup
 First database migration
 PostgreSQL schema migration


🚧 Upcoming
 Database constraints
 Indexes
 Filtering by status and priority
 Pagination
 Search
 Sorting
 User model
 Issue-user relationships
 Authentication
 JWT
 Role-based access control
 Testing with Pytest
 Docker
 Production deployment
 CI/CD



