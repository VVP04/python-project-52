# 📝 Task Manager

### Hexlet tests and linter status:
[![Actions Status](https://github.com/VVP04/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/VVP04/python-project-52/actions)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=VVP04_python-project-52&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=VVP04_python-project-52)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=VVP04_python-project-52&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=VVP04_python-project-52)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=VVP04_python-project-52&metric=coverage)](https://sonarcloud.io/summary/new_code?id=VVP04_python-project-52)

### 🌐 Demo
👉 [Task Manager on Render](https://python-project-52-tae0.onrender.com)

---

## 📖 About the project

**Task Manager** is a web—based task management application.  
The application is implemented on **Django** and allows you to organize the workflow for creating, distributing and controlling tasks.

---

## 🚀 Features

- User registration and authentication  
- CRUD operations for:
  - **Tasks** (creation, editing, deletion, assignment of performers)  
  - **Statuses** (task statuses: new, in progress, done, etc.)
  - **Labels** (tags for tasks)  
- Restrictions on deleting entities if they are used  
- Authorization:
- Tasks can only be deleted by their author  
  - Unauthorized actions are blocked  
- Interface based on Django templates  
- Multilingual support (i18n) 

---

## 🛠 Installation (for developers)

### 1. Clone repository
```bash
git clone https://github.com/VVP04/python-project-52.git
cd python-project-52
```
### 2. Install dependencies
We use uv for package management:
```bash
make install
```
For development:
```bash
make dev-install
```
### 3. Setup environment
Create a .env file in the project root and configure it (example):
```bash
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3
ROLLBAR_ACCESS_TOKEN=your-rollbar-token
ROLLBAR_ENV=development/production
```
### 4. Run migrations
```bash
make migrate
```
### 5. Run local server
```bash
make run
```

---

## Dependencies
- Python 3.12+
- Django — web framework
- dj-database-url — database configuration from DATABASE_URL
- psycopg2-binary — PostgreSQL driver
- django-bootstrap5 — UI integration
- rollbar — error tracking
- pytest / pytest-django — testing
- coverage — test coverage
- ruff — linter

## Testing
Run linter:
```bash
make lint
```
Run tests:
```bash
make test
```
Run tests with coverage:
```bash
make coverage
```
## Author
Project developed by Plesovskikh Vladimir

## Additional information
- Continuous Integration via GitHub Actions
- Code quality monitoring with SonarCloud
- Deployment on Render
- Error monitoring via Rollbar