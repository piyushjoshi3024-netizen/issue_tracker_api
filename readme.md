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

| Technology | Purpose |
|------------|---------|
| Python | Backend programming language |
| FastAPI | REST API framework |
| Pydantic | Data validation and schemas |
| SQLAlchemy | ORM and database interaction |
| PostgreSQL | Relational database |
| psycopg | PostgreSQL driver |
| Uvicorn | ASGI server |
| python-dotenv | Environment configuration |

---

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



