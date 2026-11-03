# FastAPI Demo API 🚀

A simple production-ready REST API built with **Python** and **FastAPI** to demonstrate backend development skills.

## Features
- RESTful endpoints.
- Data validation using Pydantic models.
- CRUD operations simulated with an in-memory database.
- Auto-generated interactive documentation (Swagger UI).

## Endpoints
- `GET /` - Returns a welcome message.
- `GET /tasks` - Returns a list of tasks.
- `POST /tasks` - Creates a new task.
- `GET /tasks/{task_id}` - Returns a specific task by ID.

## How to run locally
1. Install dependencies:
   ```bash
   pip install fastapi uvicorn