"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Mis propios modulos
# Módulo para pruebas

from sys import stdout
from typing import Dict, List, Set, Tuple, Union


def sumar_valores(
    numeroUno: Union[str, int, float],
    numeroDos: Union[str, int, float],
    numeroTres: Union[str, int, float],
) -> None:
    if isinstance(numeroUno, (int, float)) and isinstance(numeroDos, (int, float)) and isinstance(numeroTres, (int, float)): print(numeroUno + numeroDos + numeroTres, end = "\n", file = stdout)
    if isinstance(numeroUno, str) and isinstance(numeroDos, str) and isinstance(numeroTres, str): print(numeroUno + numeroDos + numeroTres, end = "\n", file = stdout)
    
    return None


def imprimir_valor(valor: Union[str, int, float, bool, List, Tuple, Dict, Set]) -> None:
    print(valor, end = "\n", file = stdout)
    return None

