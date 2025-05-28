
# 🔐 FastAPI Auth API Boilerplate – Secure Backend Starter Kit

Launch your Python backend in minutes — with secure login, password hashing (Argon2), JWT token authentication, and SQLite3 database baked in.

---

## What Is This?

This is a **production-ready authentication API** built with **FastAPI + Argon2 + SQLite**, designed for developers who need a:
- Secure backend authentication system
- Plug-and-play login/signup API
- Fast MVP foundation
- Backend learning reference (FastAPI, DB, JWT)

---

## Features

-  Secure password hashing with **Argon2**
-  JWT-based login session (stateless auth)
-  SQLite3 lightweight DB (easy to deploy)
-  Swagger docs auto-generated (`/docs`)
-  Clean modular project structure
-  `GET /me` protected route (token required)
-  Easy to extend for production projects

---


## 🛠 Quickstart

1. **Clone the repo**
```bash
git clone https://github.com/NVLMND/auth_system.git
cd auth-system

Folder Structure
app/
├── main.py          # Entry point
├── auth.py          # Auth routes (login, signup)
├── models.py        # SQLAlchemy models
├── schemas.py       # Pydantic schemas
├── utils.py         # Password hashing (Argon2)
├── jwt_handler.py   # Token creation/validation
└── db.py            # DB connection


