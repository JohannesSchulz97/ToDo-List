from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

app = FastAPI()

# In-memory task list (resets when server restarts)
tasks = ['Walk the dogs', 'Cook Food', 'Study Maths']

class Task(BaseModel):
    task: str

@app.get("/tasks")
def get_tasks():
    return {"tasks": tasks}

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task.task)
    return {"message": "Task added!"}

@app.delete("/tasks")
def complete_task(task: Task): 
    tasks.remove(task.task)
    return {"message": "Task added!"}


app.mount("/", StaticFiles(directory="static", html=True), name="static")