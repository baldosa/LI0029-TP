# Modelo (MVC): consultas SQL de la tabla libros.
from db import fetch, run

# Columnas editables; también sirve de lista blanca en editar()
COLS =("titulo", "autor", "anio", "ol_key", "estado", "puntaje", "notas")


def obtener(id):
    rows = fetch("SELECT * FROM libros WHERE id=%s", (id,))
    return rows[0] if rows else None


def listar(estado=None):
    if estado:
        return fetch("SELECT * FROM libros WHERE estado=%s ORDER BY titulo", (estado,))
    return fetch("SELECT * FROM libros ORDER BY titulo")


def crear(d):
    marks = ",".join(["%s"] * len(COLS))
    id, _ = run(f"INSERT INTO libros ({','.join(COLS)}) VALUES ({marks})", [d.get(c) for c in COLS])
    return obtener(id)


def editar(id, d):
    campos = {k: v for k, v in d.items() if k in COLS}
    if campos:
        sets = ",".join(f"{k}=%s" for k in campos)
        run(f"UPDATE libros SET {sets} WHERE id=%s", [*campos.values(), id])
    return obtener(id)


def borrar(id):
    run("DELETE FROM libros WHERE id=%s", (id,))
