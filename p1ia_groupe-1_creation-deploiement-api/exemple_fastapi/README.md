# Exemple FastAPI — API Tâches (Groupe 1)

Exemple minimal et exécutable accompagnant le document de synthèse.

## Lancer en local

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
pip install -r requirements.txt
fastapi dev main.py
```

- Documentation interactive : <http://127.0.0.1:8000/docs>
- Documentation ReDoc : <http://127.0.0.1:8000/redoc>
- Schéma OpenAPI : <http://127.0.0.1:8000/openapi.json>
- Santé : <http://127.0.0.1:8000/health>

## Endpoints

| Méthode | URI | Description |
|---|---|---|
| GET | `/api/v1/tasks?done=false&limit=20&offset=0` | Lister / filtrer / paginer |
| GET | `/api/v1/tasks/{id}` | Lire une tâche |
| POST | `/api/v1/tasks` | Créer (201) |
| PUT | `/api/v1/tasks/{id}` | Remplacer |
| PATCH | `/api/v1/tasks/{id}` | Modifier partiellement |
| DELETE | `/api/v1/tasks/{id}` | Supprimer (204) |
| GET | `/health` | Health check |

## Exemples cURL

```bash
curl http://127.0.0.1:8000/api/v1/tasks

curl -X POST http://127.0.0.1:8000/api/v1/tasks \
  -H "Content-Type: application/json" \
  -d '{"title":"Réviser HTTP","due_date":"2026-11-05"}'

curl -X PATCH http://127.0.0.1:8000/api/v1/tasks/1 \
  -H "Content-Type: application/json" \
  -d '{"done":true}'
```

## Tests

```bash
pytest -q
```

## Docker

```bash
docker compose up -d --build
# puis http://127.0.0.1:8000/docs
```

## Limites volontaires

- Stockage en mémoire : les données sont perdues au redémarrage.
- Pas d'authentification : voir le chapitre XI du document de synthèse
  (OAuth2/JWT) et le cheatSheet `auth_jwt_oauth2` pour l'ajouter.
- Exemple pédagogique : pour la production, ajouter une base de données,
  des migrations, des logs, du rate limiting et une CI/CD.
