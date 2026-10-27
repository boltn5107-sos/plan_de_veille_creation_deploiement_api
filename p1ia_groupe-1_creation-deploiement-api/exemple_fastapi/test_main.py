from fastapi.testclient import TestClient

import main

client = TestClient(main.app)


def setup_function() -> None:
    main.tasks.clear()
    main.next_id = 1


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_create_and_get_task() -> None:
    response = client.post(
        "/api/v1/tasks",
        json={"title": "Réviser HTTP", "due_date": "2026-11-05"},
    )
    assert response.status_code == 201
    task_id = response.json()["id"]

    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Réviser HTTP"


def test_create_validation_error() -> None:
    response = client.post("/api/v1/tasks", json={"title": ""})
    assert response.status_code == 422


def test_patch_task() -> None:
    created = client.post("/api/v1/tasks", json={"title": "Test"}).json()
    response = client.patch(
        f"/api/v1/tasks/{created['id']}", json={"done": True}
    )
    assert response.status_code == 200
    assert response.json()["done"] is True
    assert response.json()["title"] == "Test"


def test_delete_task() -> None:
    created = client.post("/api/v1/tasks", json={"title": "À supprimer"}).json()
    response = client.delete(f"/api/v1/tasks/{created['id']}")
    assert response.status_code == 204

    response = client.get(f"/api/v1/tasks/{created['id']}")
    assert response.status_code == 404
