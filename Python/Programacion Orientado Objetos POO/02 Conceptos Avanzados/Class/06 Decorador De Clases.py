#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
Al decorar una Clase, se crea una nueva Clase que hereda de la Clase original.
Esto significa que la nueva Clase tiene todos los atributos y métodos de la Clase original.
Por lo tanto, podemos agregar nuevos métodos y atributos a la Clase decorada. Pero cabe recalcar que si verificamos si la Clase decorada es una instancia de la Clase original, el resultado será False.
"""


"""
>>> En algunos casos mypy esta utilidad dara muchos problemas para estos casos la solucion es tiparlo con Any
"""
from typing import Any, Type

def decoradorClases(Clase: Type[Any]) -> Type[Any]:
    class NuevaClase(Clase):
        def __init__(self: "NuevaClase", nombre: str = "Daniel") -> None:
            self.nombre: str = nombre
            super().__init__()
            return None

        def nueva_funcion(self: 'NuevaClase') -> str: return "Esta es una nueva función en la Clase decorada"
    return NuevaClase
@decoradorClases
class MiClase:
    def __init__(self: 'MiClase') -> None: return None

    def funcion_original(self: 'MiClase') -> str: return "Esta es la función original de la Clase"

# Crear una instancia de la Clase decorada
objeto: Any = MiClase()

# Llamar a las funciones
print(objeto.funcion_original(), end="\n")  # Imprime "Esta es la función original de la Clase"
print(objeto.nueva_funcion(), end="\n")  # Imprime "Esta es una nueva función en la Clase decorada"  # type: ignore
