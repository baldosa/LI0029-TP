from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from mysql.connector import IntegrityError

from routes import libros

app = FastAPI(title="Biblioteca de lectura")
app.include_router(libros.router)


@app.exception_handler(IntegrityError)
def duplicado(request, exc):
    return JSONResponse({"detail": "Dato duplicado o referencia inválida"}, status_code=409)


# último: "/" captura todo lo que no matcheó antes
app.mount("/", StaticFiles(directory="static", html=True), name="static")
