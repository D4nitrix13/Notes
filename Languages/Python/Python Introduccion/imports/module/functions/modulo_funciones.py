"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
from typing import Union, Dict, Set, Tuple, List, Type

def tipo_dato(* , dato: Union[str, int, float , bool , List , Tuple , Dict , Set]) -> Type:
    return type(dato)