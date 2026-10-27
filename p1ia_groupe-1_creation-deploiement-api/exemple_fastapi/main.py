"""API Tâches — exemple pédagogique FastAPI (Groupe 1).

Lancement :
    pip install -r requirements.txt
    fastapi dev main.py
    # ou : uvicorn main:app --reload

Documentation :
    http://127.0.0.1:8000/docs
    http://127.0.0.1:8000/redoc
"""

from datetime import date, datetime, timezone
from typing import Annotated

from fastapi import FastAPI, HTTPException, Path, Query, status
from pydantic import BaseModel, ConfigDict, Field

app = FastAPI(
    title="API Tâches",
    version="1.0.0",
    description="API de démonstration REST — Groupe 1 (veille API/FastAPI).",
)


class TaskBase(BaseModel):
    title: str = Field(min_length=1, max_length=200, examples=["Réviser HTTP"])
    due_date: date | None = Field(default=None, examples=["2026-11-05"])


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    done: bool | None = None
    due_date: date | None = None


class Task(TaskBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
    done: bool = False
    created_at: date


class TaskList(BaseModel):
    items: list[Task]
    total: int
    limit: int
    offset: int


# Stockage en mémoire : à remplacer par une base (SQLAlchemy, SQLModel...).
tasks: dict[int, Task] = {}
next_id = 1


@app.get("/health", tags=["ops"])
def health() -> dict[str, str]:
    return {"status": "ok", "version": app.version}


@app.get("/api/v1/tasks", response_model=TaskList, tags=["tasks"])
def list_tasks(
    done: Annotated[bool | None, Query(description="Filtrer par état")] = None,
    limit: Annotated[int, Query(ge=1, le=100)] = 20,
    offset: Annotated[int, Query(ge=0)] = 0,
) -> TaskList:
    items = sorted(tasks.values(), key=lambda t: t.id)
    if done is not None:
        items = [t for t in items if t.done == done]
    total = len(items)
    page = items[offset : offset + limit]
    return TaskList(items=page, total=total, limit=limit, offset=offset)


@app.get("/api/v1/tasks/{task_id}", response_model=Task, tags=["tasks"])
def get_task(task_id: Annotated[int, Path(ge=1)]) -> Task:
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    return task


@app.post(
    "/api/v1/tasks",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    tags=["tasks"],
)
def create_task(payload: TaskCreate) -> Task:
    global next_id
    task = Task(
        id=next_id,
        created_at=datetime.now(timezone.utc).date(),
        **payload.model_dump(),
    )
    tasks[next_id] = task
    next_id += 1
    return task


@app.put("/api/v1/tasks/{task_id}", response_model=Task, tags=["tasks"])
def replace_task(task_id: int, payload: TaskCreate) -> Task:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    current = tasks[task_id]
    updated = Task(
        id=current.id,
        created_at=current.created_at,
        **payload.model_dump(),
    )
    tasks[task_id] = updated
    return updated


@app.patch("/api/v1/tasks/{task_id}", response_model=Task, tags=["tasks"])
def update_task(task_id: int, payload: TaskUpdate) -> Task:
    task = tasks.get(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    updated = task.model_copy(update=payload.model_dump(exclude_unset=True))
    tasks[task_id] = updated
    return updated


@app.delete(
    "/api/v1/tasks/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["tasks"],
)
def delete_task(task_id: int) -> None:
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Tâche introuvable")
    del tasks[task_id]
