# Consume la API pública de Open Library (sin API key) para buscar libros.
import httpx
from fastapi import APIRouter, HTTPException, Query

router = APIRouter()


@router.get("/buscar")
def buscar(q: str = Query(min_length=2)):
    try:
        r = httpx.get(
            "https://openlibrary.org/search.json",
            params={"q": q, "limit": 10, "fields": "key,title,author_name,first_publish_year"},
            timeout=5,
        )
        r.raise_for_status()
    except httpx.HTTPError:
        raise HTTPException(502, "Open Library no disponible")
    # Se devuelve en el mismo formato que espera POST /libros
    return [
        {
            "ol_key": d["key"],
            "titulo": d.get("title"),
            "autor": ", ".join(d.get("author_name", [])[:2]) or None,
            "anio": d.get("first_publish_year"),
        }
        for d in r.json()["docs"]
    ]
