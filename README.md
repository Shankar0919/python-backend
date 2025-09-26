# Python Backend (Flask + Pytest)

This is a Python 3.13 backend using **Flask** for APIs and **pytest** for testing.  
It mirrors the structure of the [nodejs-backend](https://github.com/Shankar0919/nodejs-backend).

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
5. [Run Tests](#-run-tests)

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
```

---

## 🚀 Setup

### Create Virtual Environment

**Windows (using py launcher):**
```bash
py -3.13 -m venv venv
```

**Windows (full path if needed):**
```bash
"C:\Program Files\Python313\python.exe" -m venv venv
```

**Linux/Mac:**
```bash
python3.13 -m venv venv
```

### Activate Virtual Environment

| Shell        | Command |
|--------------|---------|
| **Git Bash** | `source venv/Scripts/activate` |
| **Command Prompt (cmd.exe)** | `venv\Scripts\activate` |
| **PowerShell** | `.env\Scripts\Activate.ps1` |
| **Linux/Mac (bash/zsh)** | `source venv/bin/activate` |

### Install Dependencies

```bash
pip install -r requirements.txt
```

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

### **GET /**

```json
{
  "status": "ok",
  "env": "local",
  "message": "Python Backend Running"
}
```

### **POST /api/users/create**

**Request:**
```json
{
  "name": "shankar",
  "active": "true",
  "dob": "2000-01-01"
}
```

**Response:**
```json
{
  "message": "User created",
  "data": {
    "id": "1",
    "name": "Shankar",
    "active": "true",
    "dob": "2000-01-01"
  }
}
```

### **PUT /api/users/update/<id>**

**Request:**
```json
{
  "name": "Shankar N",
  "active": "false"
}
```

**Response:**
```json
{
  "message": "User updated",
  "data": {
    "id": "1",
    "name": "Shankar N",
    "active": "false",
    "dob": "2000-01-01"
  }
}
```

---

## 🧪 Run Tests

```bash
pytest -v
```

Example output:

```
test/test_user_controller.py::test_create_user_success PASSED
test/test_user_controller.py::test_create_user_invalid_date PASSED
test/test_validators.py::test_boolean_validator PASSED
...
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
