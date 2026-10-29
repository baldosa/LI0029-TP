# Controlador (MVC): endpoints de /listas y del vínculo lista-libro.
from fastapi import APIRouter
from pydantic import BaseModel, Field

from models import libros, listas
from routes import or_404

router = APIRouter(prefix="/listas")


class ListaIn(BaseModel):
    nombre: str = Field(min_length=1, max_length=100)
    descripcion: str | None = Field(None, max_length=255)


class ListaPatch(BaseModel):
    nombre: str | None = Field(None, min_length=1, max_length=100)
    descripcion: str | None = Field(None, max_length=255)


@router.get("")
def listar():
    return listas.listar()


@router.post("", status_code=201)
def crear(l: ListaIn):
    return listas.crear(l.model_dump())


@router.get("/{id}")
def obtener(id: int):
    return or_404(listas.obtener(id))


@router.patch("/{id}")
def editar(id: int, l: ListaPatch):
    or_404(listas.obtener(id))
    return listas.editar(id, l.model_dump(exclude_unset=True))


@router.delete("/{id}", status_code=204)
def borrar(id: int):
    or_404(listas.obtener(id))
    listas.borrar(id)


@router.put("/{id}/libros/{libro_id}", status_code=204)
def agregar(id: int, libro_id: int):
    or_404(listas.obtener(id))
    or_404(libros.obtener(libro_id))
    listas.agregar(id, libro_id)


@router.delete("/{id}/libros/{libro_id}", status_code=204)
def quitar(id: int, libro_id: int):
    or_404(listas.obtener(id))
    listas.quitar(id, libro_id)
