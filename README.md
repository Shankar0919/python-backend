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
  - [Run app](-#run-app)
  - [Run tests](-#run-tests)
- [Update API Spec & Collections](-#update-api-spec-&-collections)
- [Render Deployment](-#render-deployment)
- [Architecture](-#architecture)

Python backend using Flask, pytest, Flasgger, and auto-generated OpenAPI spec.

## Project Structure

- `src/app.py` → Application entrypoint
- `src/routes/` → Route definitions
- `src/controllers/` → Request handlers
- `src/services/` → Business logic
- `src/validators/` → Input validators
- `test/` → Pytest tests
- `scripts/` → Automation scripts (API spec + collections)
- `docs/` → API spec + generated collections

## Endpoints

- `GET /healthcheck` → Health check
- `POST /api/users/create` → Create user
- `PUT /api/users/update/<user_id>` → Update user
- `DELETE /api/users/delete/<user_id>` → Delete user

## Development

### Install dependencies

```bash
pip install -e .
```

### Run app

```bash
python src/app.py
```

### Run tests

```bash
pytest -v
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
| Test        | <https://python-backend-test.onrender.com> | test       |

> Each service runs the same codebase with different `APP_ENV` values.

## 🖼 Architecture

![Architecture Diagram](./architecture.png)
