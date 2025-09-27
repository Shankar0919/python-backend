# Python Backend

Python backend using Flask, pytest, Flasgger, and auto-generated OpenAPI spec.

## 📂 Project Structure

- `src/app.py` → Application entrypoint
- `src/routes/` → Route definitions
- `src/controllers/` → Request handlers
- `src/services/` → Business logic
- `src/validators/` → Input validators
- `test/` → Pytest tests
- `scripts/` → Automation scripts (API spec + collections)
- `docs/` → API spec + generated collections

## 🚀 Endpoints

- `GET /healthcheck` → Health check  
- `POST /api/users/create` → Create user  
- `PUT /api/users/update/<user_id>` → Update user  
- `DELETE /api/users/delete/<user_id>` → Delete user  

## 🔧 Development

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

## 🔄 Update API Spec & Collections

Whenever you add or modify an endpoint, regenerate spec & collections:

```bash
python scripts/generate_apispec.py
python scripts/update_collections.py
```

This updates:
- `docs/api_spec.yaml`
- `docs/postman_collection.json`
- `docs/python-backend.bru`
