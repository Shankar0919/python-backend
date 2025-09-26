# Python Backend (Flask + Pytest)

This is a Python 3.13 backend using **Flask** for APIs, **pytest** for testing, and **Flasgger** for Swagger-UI.  
It also provides **Postman** and **Bruno** collections generated from the OpenAPI spec.

---

## 📑 Table of Contents
1. [Project Structure](#-project-structure)
2. [Setup](#-setup)
   - [Create Virtual Environment](#create-virtual-environment)
   - [Activate Virtual Environment](#activate-virtual-environment)
   - [Install Dependencies](#install-dependencies)
3. [Run the App](#-run-the-app)
   - [PowerShell](#powershell)
   - [Git Bash](#git-bash)
   - [Command Prompt](#command-prompt)
4. [API Endpoints](#-api-endpoints)
5. [API Documentation (Swagger-UI)](#-api-documentation-swagger-ui)
6. [Postman & Bruno Collections](#-postman--bruno-collections)
7. [Run Tests](#-run-tests)
8. [Contributor Workflow](#-contributor-workflow)

---

## 📂 Project Structure

```
src/
  ├── app.py                # Flask entrypoint
  ├── controllers/          # API controllers
  ├── services/             # Data transformations
  └── validators/           # Input validation modules
test/                       # pytest test cases
env/                        # environment variable files
docs/                       # API spec + collections
scripts/                    # scripts to update collections
```

---

## 🚀 Setup

### Create Virtual Environment

**Windows (using py launcher):**
```bash
py -3.13 -m venv venv
```

**Linux/Mac:**
```bash
python3.13 -m venv venv
```

### Activate Virtual Environment

| Shell        | Command |
|--------------|---------|
| **Git Bash** | `source venv/Scripts/activate` |
| **Command Prompt (cmd.exe)** | `venv\Scripts\activate.bat` |
| **PowerShell** | `.env\Scripts\Activate.ps1` |
| **Linux/Mac (bash/zsh)** | `source venv/bin/activate` |

### Install Dependencies

```bash
pip install -r requirements.txt
```

⚡ **Tip for existing venv users (don’t recreate it):**

If you already have a `venv/` folder from a previous setup, you don’t need to create it again.  
Just install or upgrade the dependencies into the existing venv:

**PowerShell / CMD**
```powershell
.env\Scripts\python.exe -m pip install -r requirements.txt
```

**Linux / Mac / Git Bash**
```bash
venv/bin/python -m pip install -r requirements.txt
```

This ensures packages are installed inside your existing venv without recreating it.

---

## ▶️ Run the App

### PowerShell
```powershell
$env:APP_ENV="local"; python src/app.py
```

### Git Bash (Linux/Mac too)
```bash
APP_ENV=local python src/app.py
```

### Command Prompt
```cmd
set APP_ENV=local && python src/app.py
```

Flask will start on **http://127.0.0.1:5000/**  

---

## 📡 API Endpoints

See `docs/api_spec.yaml` for the OpenAPI spec.  
Endpoints include:
- `GET /` → Health Check
- `POST /api/users/create` → Create User
- `PUT /api/users/update/{id}` → Update User

---

## 📖 API Documentation (Swagger-UI)

After running the app, open:  
👉 [http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/)  

This shows interactive Swagger-UI docs generated from `docs/api_spec.yaml`.

---

## 📦 Postman & Bruno Collections

Collections are generated from the OpenAPI spec.  

Run the script:

**PowerShell**
```powershell
python scripts/update_collections.py
```

**Git Bash/Linux/Mac**
```bash
python scripts/update_collections.py
```

**Command Prompt**
```cmd
python scripts\update_collections.py
```

This regenerates:
- `docs/postman_collection.json`
- `docs/python-backend.bru`

---

## 🧪 Run Tests

```bash
python -m pytest -v test
```

---

## 🆕 Contributor Workflow

When a collaborator **creates or modifies an endpoint**, the following steps **must be done before pushing code**:

1. **Update the API spec**  
   Edit `docs/api_spec.yaml` to include the new/changed endpoint.

2. **Regenerate collections**  
   Run the following command depending on your shell:

   **PowerShell**
   ```powershell
   python scripts/update_collections.py
   ```

   **Git Bash/Linux/Mac**
   ```bash
   python scripts/update_collections.py
   ```

   **Command Prompt**
   ```cmd
   python scripts\update_collections.py
   ```

   This will regenerate:
   - `docs/postman_collection.json`
   - `docs/python-backend.bru`

3. **Verify Swagger-UI**  
   Run the app and open [http://127.0.0.1:5000/apidocs/](http://127.0.0.1:5000/apidocs/) to confirm the new endpoint is visible in the documentation.

4. **Commit and push**  
   Now commit the updated code + docs together.

---

### 🔒 Pre-commit Hook

This repo enforces a **pre-commit Git hook** to ensure API docs and collections are always up to date.

1. Install the hook path (run once):
   ```bash
   git config core.hooksPath .githooks
   ```

2. Make it executable (Linux/Mac/Git Bash only):
   ```bash
   chmod +x .githooks/pre-commit
   ```

Now, every commit will:
- Run `python scripts/update_collections.py`
- Fail if `docs/api_spec.yaml` or collections are outdated
