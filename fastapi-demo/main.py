from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Jhon's FastAPI Demo")

# Modelo de datos para una tarea
class Task(BaseModel):
    id: int
    title: str
    completed: bool = False

# Base de datos en memoria (simula una DB real)
tasks_db = [
    Task(id=1, title="Aprender FastAPI", completed=True),
    Task(id=2, title="Conseguir trabajo remoto", completed=False),
]

@app.get("/")
def read_root():
    return {"message": "Hola, soy Jhon. Este es mi demo de FastAPI."}

@app.get("/tasks")
def get_tasks():
    return tasks_db

@app.post("/tasks")
def create_task(task: Task):
    tasks_db.append(task)
    return {"message": "Tarea creada", "task": task}

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    return {"error": "Tarea no encontrada"}