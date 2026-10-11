# FastAPI

# FastAPI — Learning & Machine Learning APIs

A hands-on journey to learning **FastAPI**, building REST APIs with Python, and deploying machine learning models as API services.

This repository contains my practice code, examples, and projects as I learn backend API development and machine learning model serving.

## 🎯 Learning Objectives

- Understand APIs, REST architecture, HTTP methods, and JSON.
- Build REST APIs using FastAPI and Uvicorn.
- Validate request data using Pydantic.
- Work with path parameters, query parameters, and request bodies.
- Create CRUD APIs and organize backend projects.
- Integrate trained machine learning models into API endpoints.
- Learn database integration, authentication, and testing.
- Explore Docker and deployment for production-ready ML APIs.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | Building REST APIs |
| Uvicorn | Running the ASGI application server |
| Pydantic | Request validation and data schemas |
| Swagger UI | Interactive API testing |
| Scikit-learn | Machine learning model integration |
| PyTorch | Deep learning model integration |
| Git & GitHub | Version control |

*Some technologies are planned learning topics and may not yet be implemented in this repository.*

## 📁 Project Structure

The current practice project is organized around a Python application and a virtual environment.

```text
FastAPI/
├── FastAPI_ML/
│   └── Practise/
│       ├── main.py
│       └── README.md
├── myvenv/
└── README.md
```

- `main.py` — FastAPI application and API endpoints.
- `myvenv/` — Local Python virtual environment.
- `README.md` — Project documentation.

The exact folder structure may evolve as the project grows.

> **Note:** Do not commit your virtual environment (`myvenv/`) to GitHub. Create it locally and reinstall dependencies when needed.

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Naim-087/FastAPI.git
cd FastAPI
```

### 2. Create a virtual environment

On Windows PowerShell:

```powershell
py -m venv myvenv
```

If you use a specific Python installation, you can create the environment using that interpreter.

### 3. Activate the environment

```powershell
.\myvenv\Scripts\Activate.ps1
```

### 4. Install FastAPI and Uvicorn

```powershell
python -m pip install --upgrade pip
python -m pip install "fastapi[standard]"
```

## 🚀 Run the Application

Navigate to the directory containing `main.py`.

```powershell
cd FastAPI_ML\Practise
```

Start the development server:

```powershell
python -m uvicorn main:app --reload
```

**Command explanation:**

- `main` — the Python file `main.py`.
- `app` — the FastAPI application object defined in that file.
- `--reload` — automatically reloads the application when code changes.

The server will normally be available at:

`http://127.0.0.1:8000`

## 📚 API Documentation

FastAPI automatically generates interactive API documentation.

| Resource | URL |
|---|---|
| API homepage | http://127.0.0.1:8000/ |
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

Use Swagger UI to inspect endpoints, submit requests, and view responses directly in your browser.

## 💻 First API Example

```python
from fastapi import FastAPI

app = FastAPI(
    title="My FastAPI Learning Project",
    description="Learning REST API development with Python",
    version="0.1.0",
)

@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

@app.get("/about")
def about():
    return {
        "project": "FastAPI Learning",
        "goal": "Building APIs for machine learning",
    }
```

Run the application:

```powershell
python -m uvicorn main:app --reload
```

Example response from `/`:

```json
{
  "message": "Hello, FastAPI!"
}
```

## 🧠 Machine Learning API Roadmap

My goal is to learn how to serve machine learning models through REST APIs.

- [ ] Build basic GET and POST endpoints.
- [ ] Validate input using Pydantic.
- [ ] Create CRUD APIs.
- [ ] Load a trained Scikit-learn model.
- [ ] Build a classification and regression prediction API.
- [ ] Develop an image classification API using PyTorch.
- [ ] Integrate PostgreSQL for storing prediction history.
- [ ] Add automated tests and authentication.
- [ ] Containerize the application using Docker.
- [ ] Deploy an ML API.

## 📖 Learning Resources

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Pydantic Documentation](https://docs.pydantic.dev/latest/)
- [Uvicorn Documentation](https://www.uvicorn.org/)
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)
- [PyTorch Documentation](https://pytorch.org/docs/stable/index.html)

## 👨‍💻 Author

**Naim**

- GitHub: [@Naim-087](https://github.com/Naim-087)
- Repository: [FastAPI](https://github.com/Naim-087/FastAPI)

---

⭐ This repository documents my progress in learning FastAPI and building APIs for machine learning applications.
