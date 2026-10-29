from fastapi import HTTPException


def or_404(x):
    """
    Si no existe, lanza un HTTPException con código 404 y mensaje "No existe".
    """
    if x is None:
        raise HTTPException(404, "No existe")
    return x
