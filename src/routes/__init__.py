from fastapi import HTTPException


def or_404(x):
    if x is None:
        raise HTTPException(404, "No existe")
    return x
