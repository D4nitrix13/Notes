#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import NoReturn, Never, Optional, assert_never
from enum import Enum

# Definición de la función que usa NoReturn y Never
def manejar_error(*, msg: str) -> NoReturn:
    """
    Lanza una excepción y nunca retorna.
    
    :param msg: Mensaje de error para la excepción.
    :raises Exception: Siempre lanza una excepción.
    """
    raise Exception(msg)

def estado_proceso(*, state: 'State') -> Never:
    """
    Función que debería manejar todos los estados posibles.
    Nunca debería retornar normalmente si todos los estados están cubiertos.
    
    :param state: Estado actual del sistema.
    :raises AssertionError: Si un estado no es manejado, se lanza una excepción.
    """
    if state == State.ON:
        print("The system is turned on!", end="\n", file=stdout)
    elif state == State.OFF:
        print("The system is turned off!", end="\n", file=stdout)
    elif state == State.LIMBO:
        print("The system is in limbo!", end="\n", file=stdout)
    else:
        # Si el estado no está manejado, assert_never ayuda a asegurar que
        # todos los casos están cubiertos en tiempo de compilación.
        assert_never(state)  # Esto lanza un error si `state` es de un valor inesperado.

# Definición del Enum para representar los estados posibles
class State(Enum):
    OFF: int = 0
    ON: int = 1
    LIMBO: int = 2

def main() -> None:
    """
    # Función principal para demostrar el uso de `Never` y `NoReturn`.
    """
    state: State = State.ON  # Establece el estado actual del sistema.
    
    # Muestra cómo manejar el estado usando la función que puede lanzar excepciones.
    e: Optional[Exception] = None
    try:
        manejar_error(msg = "An error occurred")  # Esta llamada no retorna nunca.
    except Exception as e:
        print(f"Exception caught: {e}", end="\n", file=stdout)

    # Procesa el estado usando la función que debería manejar todos los casos.
    estado_proceso(state = state)

if __name__ == "__main__":
    main()

"""
Explicación:

    manejar_error:
        Tipo de Retorno: NoReturn
        Propósito: Esta función siempre lanza una excepción y nunca retorna. El tipo NoReturn indica que la función no debería retornar normalmente; en su lugar, lanzará una excepción que termina la ejecución del programa o función que la llama.

    estado_proceso:
        Tipo de Retorno: Never
        Propósito: Esta función debería manejar todos los casos posibles de State. El tipo Never es utilizado aquí para indicar que la función nunca debería retornar bajo condiciones normales si todos los casos están cubiertos. Si hay un caso que no está manejado, assert_never ayudará a identificarlo en tiempo de compilación.

    State:
        Enum: Enum usado para representar diferentes estados posibles del sistema.

    assert_never:
        Uso: Se utiliza para asegurarse de que todos los casos posibles del Enum están cubiertos en una función. Si se encuentra un valor inesperado, assert_never generará un error en tiempo de compilación.

Esta mejora proporciona un uso claro y práctico de Never y NoReturn en un contexto realista con enumeraciones y manejo de errores en Python.
"""