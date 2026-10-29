# Modelo (MVC): consultas SQL de listas y de la tabla intermedia lista_libros.
from db import fetch, run

COLS = ("nombre", "descripcion")


def obtener(id):
    # Devuelve la lista con sus libros adentro (JOIN por la tabla intermedia)
    rows = fetch("SELECT * FROM listas WHERE id=%s", (id,))
    if not rows:
        return None
    lista = rows[0]
    lista["libros"] = fetch(
        "SELECT l.* FROM libros l JOIN lista_libros ll ON ll.libro_id=l.id "
        "WHERE ll.lista_id=%s ORDER BY l.titulo",
        (id,),
    )
    return lista


def listar():
    return fetch("SELECT * FROM listas ORDER BY nombre")


def crear(d):
    id, _ = run("INSERT INTO listas (nombre, descripcion) VALUES (%s,%s)", (d["nombre"], d.get("descripcion")))
    return obtener(id)


def editar(id, d):
    campos = {k: v for k, v in d.items() if k in COLS}
    if campos:
        sets = ",".join(f"{k}=%s" for k in campos)
        run(f"UPDATE listas SET {sets} WHERE id=%s", [*campos.values(), id])
    return obtener(id)


def borrar(id):
    run("DELETE FROM listas WHERE id=%s", (id,))


def agregar(lista_id, libro_id):
    # IGNORE: agregar dos veces el mismo libro no es error
    run("INSERT IGNORE INTO lista_libros (lista_id, libro_id) VALUES (%s,%s)", (lista_id, libro_id))


def quitar(lista_id, libro_id):
    run("DELETE FROM lista_libros WHERE lista_id=%s AND libro_id=%s", (lista_id, libro_id))
