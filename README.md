# ⚡ FastAPI - Beginner Friendly Guide

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

## ⚙️ FastAPI vs Flask

| Feature              | FastAPI                    | Flask                       |
|----------------------|----------------------------|-----------------------------|
| Speed                | Very Fast (ASGI)           | Slower (WSGI)               |
| Async Support        | Built-in                   | Not native                  |
| Type Hints           | Enforced                   | Optional                    |
| Validation           | Automatic via Pydantic     | Manual or plugins           |
| Auto Docs            | Built-in Swagger / ReDoc   | Requires plugins            |
| WebSockets           | Supported                  | Not native                  |

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
