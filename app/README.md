# AI Portfolio API 🚀

Una API RESTful construida con **FastAPI** y **PostgreSQL/SQLite** que simula el procesamiento de texto con Inteligencia Artificial y guarda un historial de las peticiones.

## 🛠️ Tecnologías utilizadas
*   **Python 3.11+**
*   **FastAPI** (Framework web moderno y rápido)
*   **SQLAlchemy** (ORM para base de datos)
*   **Pydantic** (Validación de datos)
*   **Uvicorn** (Servidor ASGI)

## 🚀 Características
*   Endpoint `POST /generate`: Recibe un texto y devuelve una respuesta "generada por IA".
*   Endpoint `GET /history`: Muestra el historial de todas las peticiones guardadas.
*   Documentación interactiva automática con Swagger UI (`/docs`).
*   Base de datos relacional (SQLite para desarrollo local, lista para migrar a PostgreSQL).

## ⚙️ Cómo ejecutarlo localmente

1. Clona este repositorio:
   ```bash
   git clone https://github.com/JHON12091986/fastapi-ai-portfolio.git
   cd fastapi-ai-portfolio