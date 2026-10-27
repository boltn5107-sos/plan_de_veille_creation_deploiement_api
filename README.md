# p1ia_groupe-1_creation-deploiement-api

Dossier de livrables — veille « Introduction aux API et à l'architecture REST avec FastAPI ».

## Contenu

| Élément | Fichier | Description |
|---|---|---|
| Document de synthèse | `document_synthese.pdf` | Document détaillé de 44 pages (13 chapitres, tableaux, exemples de code). |
| Version web | `document_synthese.html` | Source HTML du document (impression / modification). |
| Diapositives | `diapositives.pptx` | 55 diapositives : pourquoi / comment / exemple pour chaque concept. |
| CheatSheets | `cheatsheets/cheatsheet_http.pdf` | Méthodes, statuts, en-têtes, cache, cURL. |
| | `cheatsheets/cheatsheet_rest.pdf` | Contraintes, URIs, CRUD, pagination, versioning, erreurs. |
| | `cheatsheets/cheatsheet_fastapi.pdf` | Installation, routes, Pydantic, dépendances, tests, async. |
| | `cheatsheets/cheatsheet_auth_jwt_oauth2.pdf` | AuthN/AuthZ, OAuth2, PKCE, JWT, OWASP. |
| Exemple exécutable | `exemple_fastapi/` | API CRUD FastAPI + tests + Dockerfile + docker-compose. |
| Sources | `sources/sources_cheatsheets.md` | Liens Internet utilisés pour les cheatSheets et références. |

## Vérifications rapides

```bash
cd exemple_fastapi
pip install -r requirements.txt
pytest -q
fastapi dev main.py
```

Documentation générée : <http://127.0.0.1:8000/docs>.

## Modalités de livraison

1. Vérifier que le dossier porte exactement le nom `p1ia_groupe-1_creation-deploiement-api`.
2. Uploader le dossier complet sur Google Drive.
3. Partager le lien du dossier dans le groupe WhatsApp de la classe.

## Outils demandés

- **VSCode** : éditeur de code (extension Python, Pylance, Ruff).
- **Postman** : tester les endpoints (importer `http://127.0.0.1:8000/openapi.json`).

## Remarques

- Les PDF ont été générés à partir des sources HTML avec Chrome (impression A4).
- Les cheatSheets sont des synthèses originales ; les sources sont citées dans chaque PDF et dans `sources/`.
- Les numéros de page des PDF sont ajoutés en pied de page.
