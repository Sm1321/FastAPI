# ⚡ FastAPI 

FastAPI is a modern, high-performance web framework for building APIs with Python 3.7+ using standard type hints.

---

## 🚀 Why Use FastAPI?

- ✅ **Fast** – very high performance (on par with Node.js and Go)
- 🧠 **Smart** – uses Python type hints for validation and IDE support
- 📚 **Auto Docs** – Swagger & ReDoc generated automatically
- 🔁 **Async Ready** – supports async/await out of the box
- 🧩 **Built-in Dependency Injection** – cleaner and modular code
- 📦 **Great for APIs** – REST, WebSockets, background tasks supported
- ✅ **Validation** – automatic with Pydantic (JSON, forms, etc.)

---

## ⚖️ FastAPI vs Flask

| Feature              | FastAPI                    | Flask                       |
|----------------------|----------------------------|-----------------------------|
| Speed                | ⚡ Very Fast (ASGI)         | 🐢 Slower (WSGI)            |
| Async Support        | ✅ Built-in                 | ⚠️ Not native                |
| Type Hints           | ✅ Enforced                 | ⚠️ Optional                  |
| Validation           | ✅ Automatic (Pydantic)     | ❌ Manual or plugins         |
| Auto Docs            | ✅ Swagger & ReDoc built-in | ❌ Requires plugins          |
| WebSockets           | ✅ Supported                | ❌ Not built-in              |
| Ideal For            | Modern APIs, ML, async apps | Simple/sync apps             |

---

## 🧰 Installation & Setup


```
pip install fastapi uvicorn
- fastapi: The core web framework.
- uvicorn: A lightweight, fast ASGI server that runs your FastAPI app. 
```
```
uvicorn main:app --reload
```
#### Open in browser:
- 🌐 http://127.0.0.1:8000 → Home

- 📘 http://127.0.0.1:8000/docs → Swagger UI

- 📙 http://127.0.0.1:8000/redoc → ReDoc UI

### 🧠 Core Features to Learn
- @app.get(), @app.post() – Define endpoints
- Query, path, and body parameters
- Request validation using Pydantic models
- Handling form data and file uploads
- Async routes (async def)
- Dependency Injection
- Background tasks
- WebSockets
- Middleware
- Authentication (JWT/OAuth2)
- Using databases (e.g., SQLModel, Tortoise, SQLAlchemy)

### 💡 Ideal For
- APIs for Machine Learning models
- Backend for Web/Mobile Apps
- Real-time apps (chat, notifications)
- Fast Prototyping

### ✅ Summary
FastAPI is a modern Python framework ideal for building high-performance APIs, with great developer experience, built-in async support, and automatic documentation. It's faster and more feature-rich than Flask, and perfect for modern backend needs.
