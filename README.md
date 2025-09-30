# Python Backend

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.x-green.svg)
![License](https://img.shields.io/badge/license-MIT-yellow.svg)
[![CI](https://github.com/your-username/your-repo/actions/workflows/CI.yml/badge.svg)](https://github.com/your-username/your-repo/actions)
[![Render](https://img.shields.io/badge/deploy-Render-blueviolet)](https://render.com)

## Table of Contents

- [Project Structure](-#project-structure)
- [Endpoints](-#endpoints)
- [Development](-#development)
  - [Install dependencies](-#install-dependencies)
  - [Run tests](-#run-tests)
  - [Run app](-#run-app)
- [Update API Spec & Collections](-#update-api-spec-&-collections)
- [Render Deployment](-#render-deployment)
- [Architecture](-#architecture)

Python backend using Flask, pytest, Flasgger, and auto-generated OpenAPI spec.

## Project Structure

- `src/app.py` → Application entrypoint
- `src/app_routes.py` → Central router (includes all controllers, no prefixes)
- `src/controllers/` → Request handlers  
  - `user_controller.py` (CRUD endpoints: `/users`, `/users/create`, `/users/update/{id}`, `/users/delete/{id}`)  
  - `health_controller.py` (`/healthcheck`)  
- `src/services/` → Business logic (`user_service.py`)
- `src/validators/` → Input validators
- `test/` → Pytest tests (100% coverage for updated endpoints)
- `scripts/` → Automation scripts (API spec + collections)
- `docs/` → API spec + generated collections

## Endpoints

- **GET `/healthcheck`**
  - Returns:
    ```json
    {
      "message": "Shankar Python Backend Application is Up and Running successfully"
    }
    ```

- **GET `/users`**
  - Returns:
    ```json
    []
    ```

- **POST `/users/create`**
  - Returns:
    ```json
    {
      "message": "User created successfully"
    }
    ```

- **PUT `/users/update/{id}`**
  - Returns:
    ```json
    {
      "message": "User {id} updated successfully"
    }
    ```

- **DELETE `/users/delete/{id}`**
  - Returns:
    ```json
    {
      "message": "User {id} deleted successfully"
    }
    ```

## Development

### Install dependencies

```bash
  pip install -r requirements-test.txt .
```

### Run tests

#### Unit Test

```bash
  pytest -v
```

#### Unit Test Coverage

These commands create coverage reports in HTML showing covered/uncovered lines.  
Coverage will also be displayed in the terminal.

- For All Files:
  ```bash
    pytest --cov=src --cov-report=term-missing --cov-report=html --cov-report=annotate:coverage/annotate
  ```
- For Individual File:
  ```bash
    pytest --cov=`File-Path` --cov-report=term-missing --cov-report=html:coverage/html --cov-report=annotate:coverage/annotate
  ```

#### Run Lint

```bash
  python -m flake8 src
```

### Run app

```bash
  python src/app.py
```

## Update API Spec & Collections

Whenever you add or modify an endpoint, regenerate spec & collections:

```bash
  python scripts/generate_apispec.py
  python scripts/update_collections.py
```

This updates:

- `docs/api_spec.yaml`
- `docs/postman_collection.json`
- `docs/python-backend.bru`

## Render Deployment

This application is deployed on Render with the following environments:

| Environment | URL                                        | APP_ENV    |
| ----------- | ------------------------------------------ | ---------- |
| Production  | <https://python-backend-prod.onrender.com> | production |
| Engineering | <https://python-backend-eng.onrender.com>  | eng        |

> Each service runs the same codebase with different `APP_ENV` values.

## 🖼 Architecture

![Architecture Diagram](./architecture.png)
