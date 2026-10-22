# 🚀 Issue Tracker API

A production-oriented REST API for managing software development issues such as bugs, feature requests, development tasks, critical problems, improvements, and maintenance work.

The project is designed around the core backend architecture of modern issue-tracking platforms such as GitHub Issues and Jira, with a focus on **authentication, authorization, issue ownership, role-based access control, relational data modeling, database migrations, comments, labels, and containerization**.

Built with **FastAPI, PostgreSQL, SQLAlchemy, Pydantic, Alembic, JWT, and Docker**.

> 🚧 **Status: Active Development**
>
> The core backend architecture is implemented. Advanced features, automated testing, optimization, CI/CD, and production deployment are still in development.

---

## 📌 Overview

The Issue Tracker API provides backend functionality required by development teams to create, organize, prioritize, assign, update, and track software development issues.

An issue can represent:

* 🐛 Bug reports
* ✨ Feature requests
* 📋 Development tasks
* 🚨 Critical problems
* 🔧 Improvements
* 🛠️ Maintenance work

The API supports:

* User authentication
* JWT-based authorization
* Role-based access control
* Issue ownership
* Admin operations
* Issue filtering, pagination, and sorting
* Comments
* Labels / tags
* PostgreSQL persistence
* Database migrations
* Dockerized execution
* Interactive API documentation

The API is designed as a standalone backend service that can be consumed by web applications, mobile applications, internal tools, or other services.

---

# ✨ Features

## 🐛 Issue Management

* Create issues
* Retrieve issues
* Retrieve individual issues
* Update issues
* Delete issues
* Track issue status
* Assign issue priority
* Issue timestamps
* Issue ownership

### Supported Issue Statuses

* `open`
* `in_progress`
* `resolved`
* `closed`

### Supported Priorities

* `low`
* `medium`
* `high`
* `critical`

---

## 🔐 Authentication & Security

* User registration
* Secure password hashing using **Argon2**
* User login
* JWT access tokens
* Protected API routes
* Current-user authentication
* Token validation
* Environment-based secret configuration

Passwords are never stored in plaintext.

---

## 👤 Authorization & RBAC

The API implements ownership-based authorization and role-based access control.

### User Roles

* `user`
* `admin`

### Authorization capabilities

* Users can manage their own issues
* Users can manage their own comments
* Admins can manage issues across the system
* Admin-only routes
* Reusable authorization dependencies

This separates:

**Authentication**

> Who are you?

from:

**Authorization**

> What are you allowed to do?

---

## 💬 Comments

Issues support comments for development discussions and collaboration.

Implemented functionality includes:

* Create comments
* Retrieve issue comments
* Update comments
* Delete comments
* Comment ownership
* User ↔ Comment relationship
* Issue ↔ Comment relationship
* Comment timestamps
* Sorted comment retrieval

---

## 🏷️ Labels / Tags

Issues can be organized using labels.

Implemented functionality includes:

* Create labels
* Retrieve labels
* Attach labels to issues
* Remove labels from issues
* Retrieve labels attached to an issue
* Many-to-many Issue ↔ Label relationship
* Duplicate label prevention

The relationship is implemented using an association table.

---

## 🔎 Filtering, Pagination & Sorting

Issue listing supports backend-side:

* Filtering
* Pagination
* Sorting

This allows the API to handle larger datasets without returning the entire issue collection in a single response.

Advanced search is planned for a future phase.

---

# 🗄️ Database

The project uses **PostgreSQL** as the primary relational database.

### Database capabilities

* Persistent data storage
* SQLAlchemy ORM
* PostgreSQL relationships
* Foreign keys
* Many-to-many relationships
* Database sessions
* Transaction handling
* Database migrations
* Environment-based database configuration

### ORM

SQLAlchemy 2.x is used for:

* Models
* Relationships
* Queries
* Sessions
* Database interaction

### PostgreSQL Driver

The project uses **Psycopg 3** for PostgreSQL connectivity.

---

# 🔄 Database Migrations

Database schema changes are managed using **Alembic**.

Migrations have been implemented for:

* Issue timestamps
* Users
* User ↔ Issue relationship
* Comments
* Labels
* Issue ↔ Label relationship

Example commands:

```bash
alembic revision --autogenerate -m "migration message"
```

```bash
alembic upgrade head
```

---

# 🐳 Docker

The API is containerized using Docker.

The Docker image:

* Uses Python 3.14
* Installs dependencies from `requirements.txt`
* Runs FastAPI using Uvicorn
* Exposes port `8001`
* Supports environment-based configuration
* Connects to the PostgreSQL database

### Build Docker Image

```bash
docker build -t issue-tracker-api .
```

### Run Container

```bash
docker run --name issue-tracker-api -p 8001:8001 --env-file .env.docker issue-tracker-api
```

### Start Existing Container

```bash
docker start issue-tracker-api
```

### Stop Container

```bash
docker stop issue-tracker-api
```

### View Container Logs

```bash
docker logs issue-tracker-api
```

The Docker configuration is currently designed for development and local containerized execution.

---

# 📚 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8001/docs
```

### ReDoc

```text
http://127.0.0.1:8001/redoc
```

These interfaces can be used to explore and test the API endpoints.

---

# 🏗️ Architecture

```text
                         Client
                           │
                           ▼
                    ┌─────────────┐
                    │   FastAPI   │
                    └──────┬──────┘
                           │
                           ▼
              ┌────────────────────────┐
              │ Authentication &       │
              │ Authorization / RBAC   │
              └───────────┬────────────┘
                          │
                          ▼
                ┌──────────────────┐
                │     Pydantic     │
                │    Validation    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │    API Routers   │
                │ Issues / Auth /  │
                │ Comments / Labels│
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
```

---

# 📁 Project Structure

```text
FAST_PROJECT/
│
├── app/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── issue.py
│   │   ├── user.py
│   │   ├── comment.py
│   │   └── label.py
│   │
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── issue.py
│   │   ├── user.py
│   │   ├── comment.py
│   │   └── label.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── issues.py
│   │   ├── auth.py
│   │   ├── comments.py
│   │   └── labels.py
│   │
│   ├── utils/
│   │   ├── security.py
│   │   ├── jwt.py
│   │   └── dependencies.py
│   │
│   ├── database.py
│   ├── main.py
│   └── __init__.py
│
├── alembic/
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── README
│
├── .dockerignore
├── .gitignore
├── .env
├── .env.docker
├── Dockerfile
├── alembic.ini
├── requirements.txt
└── README.md
```

> Environment files containing credentials and secrets should not be committed to version control.

---

# 🛠️ Tech Stack

| Technology          | Purpose                            |
| ------------------- | ---------------------------------- |
| **Python 3.14**     | Programming language               |
| **FastAPI**         | REST API framework                 |
| **Pydantic v2**     | Request/response validation        |
| **SQLAlchemy 2.x**  | ORM and database interaction       |
| **PostgreSQL 18**   | Relational database                |
| **Psycopg 3**       | PostgreSQL driver                  |
| **Alembic**         | Database migrations                |
| **Uvicorn**         | ASGI server                        |
| **PyJWT**           | JWT authentication                 |
| **pwdlib + Argon2** | Password hashing                   |
| **python-dotenv**   | Environment configuration          |
| **Docker**          | Application containerization       |
| **DataGrip**        | Database management and inspection |

---

# 🚧 Development Status

## ✅ Completed

### Core API

* FastAPI project setup
* REST API architecture
* Modular API routers
* Pydantic request schemas
* Pydantic response schemas
* HTTP status codes
* Error handling
* Global SQLAlchemy exception handling

### Issue Management

* Issue CRUD
* Issue status
* Issue priority
* Issue timestamps
* Issue ownership
* Filtering
* Pagination
* Sorting

### Database

* PostgreSQL integration
* SQLAlchemy ORM
* Psycopg 3 integration
* Database sessions
* Transaction handling
* Foreign key relationships
* Alembic setup
* Database migrations

### Authentication

* User model
* User registration
* Password hashing
* Login
* JWT authentication
* Current-user authentication
* Protected routes

### Authorization

* User ↔ Issue relationship
* Issue ownership authorization
* Role-based access control
* Admin role
* Admin authorization dependency
* Admin issue listing
* Admin issue updating
* Admin issue deletion

### Comments

* Comment model
* Comment creation
* Comment retrieval
* Comment updating
* Comment deletion
* Comment ownership
* User ↔ Comment relationship
* Issue ↔ Comment relationship
* Comment authorization
* Comment sorting

### Labels

* Label model
* Label creation
* Label retrieval
* Issue ↔ Label many-to-many relationship
* Attach labels to issues
* Detach labels from issues
* Retrieve issue labels
* Duplicate label prevention

### Containerization

* Dockerfile
* Docker image
* Dockerized FastAPI application
* Docker environment configuration
* `.dockerignore`
* Local container execution
* Docker ↔ PostgreSQL connectivity

---

# 🚧 In Development

The following features are planned or currently under development:

* 🔍 Advanced issue search
* 👤 Issue assignment
* 📜 Activity / audit logs
* 🧪 Automated testing with Pytest
* ⚡ Database constraints and indexes
* 🐳 Docker Compose
* 🔄 CI/CD pipeline
* ☁️ Production deployment
* 🔐 Production security hardening
* 📊 Performance optimization
* 🏭 Production-ready configuration

---

# 🗓️ Project Completion Target

🎯 **Target Completion Date: October 24, 2026**

The project is currently under active development.

The core backend architecture, database integration, authentication, authorization, issue management, filtering, pagination, sorting, migrations, comments, labels, and containerization have been implemented.

The remaining development focuses on advanced issue-management features, automated testing, database optimization, orchestration, CI/CD, deployment, and final production-oriented improvements.

---

# 🎯 Final Project Vision

The final version aims to provide a complete production-oriented issue management backend:

```text
FastAPI Backend
│
├── Authentication
├── JWT Security
├── Authorization
├── RBAC
├── Issue Management
├── Issue Assignment
├── Comments
├── Labels
├── Search
├── Filtering
├── Pagination
├── Sorting
├── Activity / Audit Logs
├── Automated Testing
├── Database Optimization
├── Docker
├── Docker Compose
├── CI/CD
└── Cloud Deployment
```

---

# 🚀 Running Locally

## 1. Clone the repository

```bash
git clone <repository-url>
cd FAST_PROJECT
```

## 2. Create virtual environment

```bash
python -m venv myenv
```

### Windows

```powershell
myenv\Scripts\activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Configure environment variables

Create a `.env` file:

```env
DATABASE_URL=postgresql+psycopg://postgres:<password>@localhost:5432/issue_tracker
JWT_SECRET_KEY=<your-secret-key>
```

Never commit secrets or passwords to Git.

## 5. Apply database migrations

```bash
alembic upgrade head
```

## 6. Start the API

```bash
python -m uvicorn app.main:app --reload --port 8001
```

The API will be available at:

```text
http://127.0.0.1:8001
```

Swagger:

```text
http://127.0.0.1:8001/docs
```

ReDoc:

```text
http://127.0.0.1:8001/redoc
```

---

# 🐳 Running with Docker

Build:

```bash
docker build -t issue-tracker-api .
```

Run:

```bash
docker run --name issue-tracker-api -p 8001:8001 --env-file .env.docker issue-tracker-api
```

Start an existing container:

```bash
docker start issue-tracker-api
```

Stop:

```bash
docker stop issue-tracker-api
```

Logs:

```bash
docker logs issue-tracker-api
```

Swagger:

```text
http://127.0.0.1:8001/docs
```

---

# 📌 Project Status

🚧 **Active Development**

The project has progressed from a basic FastAPI CRUD application into a structured backend system with:

* Relational database architecture
* ORM-based persistence
* Authentication
* JWT security
* Authorization
* RBAC
* Ownership enforcement
* Comments
* Labels
* Filtering
* Pagination
* Sorting
* Database migrations
* Docker containerization

The repository will continue receiving incremental feature, architecture, testing, optimization, and deployment improvements until the planned final release.

---

## 📄 License

This project is licensed under the **MIT License**.

Copyright © 2026 Piyush Joshi
