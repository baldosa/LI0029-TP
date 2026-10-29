# Controlador (MVC): endpoints de /libros. Pydantic valida la entrada (422 si es inválida).
from typing import Literal

from fastapi import APIRouter
from pydantic import BaseModel, Field

from models import libros
from routes import or_404

router = APIRouter(prefix="/libros")
Estado = Literal["por_leer", "leyendo", "leido"]


class LibroIn(BaseModel):
    titulo: str = Field(min_length=1, max_length=255)
    autor: str | None = None
    anio: int | None = None
    ol_key: str | None = Field(None, max_length=32)
    estado: Estado = "por_leer"
    puntaje: int | None = Field(None, ge=1, le=5)
    notas: str | None = None


# Todos los campos opcionales: PATCH solo cambia los que se envían
class LibroPatch(BaseModel):
    titulo: str | None = Field(None, min_length=1, max_length=255)
    autor: str | None = None
    anio: int | None = None
    estado: Estado | None = None
    puntaje: int | None = Field(None, ge=1, le=5)
    notas: str | None = None


@router.get("")
def listar(estado: Estado | None = None):
    return libros.listar(estado)


@router.post("", status_code=201)
def crear(b: LibroIn):
    return libros.crear(b.model_dump())


@router.get("/{id}")
def obtener(id: int):
    return or_404(libros.obtener(id))


@router.patch("/{id}")
def editar(id: int, b: LibroPatch):
    or_404(libros.obtener(id))
    return libros.editar(id, b.model_dump(exclude_unset=True))


@router.delete("/{id}", status_code=204)
def borrar(id: int):
    or_404(libros.obtener(id))
    libros.borrar(id)
