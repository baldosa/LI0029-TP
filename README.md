# TP Final

Alumno: Ema Guillén

Biblioteca de lectura: CRUD de libros (por leer / leyendo / leído) y listas de libros.
Busca libros en la API pública de Open Library y expone una API propia (FastAPI) sobre MariaDB.
MVC: `src/models` (datos), `src/routes` (controladores), `src/static/index.html` (vista).

## Correr
    docker compose up --build    # base + API + web en http://localhost:8000 (con --reload sobre src/)


Variables opcionales: DB_HOST, DB_PORT, DB_USER, DB_PASS, DB_NAME.
