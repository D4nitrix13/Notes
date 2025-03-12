#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout

def primer_ejemplo() -> str:
    # Inicializa una variable 'text' con el valor "hello".
    text: str = "hello"
    
    # Concatena un signo de exclamación al final de 'text'.
    text = text + "!"
    
    # Devuelve la nueva cadena que ahora es "hello!".
    return text

def segundo_ejemplo() -> None:  # Cambiado de str a None porque no se devuelve nada
    # Inicializa una tupla 'coordinates' con dos valores flotantes.
    coordinates: tuple[float, ...] = (1.0, 2.5)
    
    # Intenta concatenar un entero a la tupla 'coordinates'.
    # Esto generará un error porque no se puede concatenar un entero a una tupla directamente.
    coordinates += (3.7,)  # Solución: usar una tupla para la concatenación
    
    # Imprime la tupla 'coordinates'.
    print(coordinates, end="\n", file=stdout)

    return None

def tercer_ejemplo() -> None:  # Cambiado de str a None porque no se devuelve nada
    # Inicializa una tupla 'coordinates' con dos valores flotantes.
    coordinates: tuple[float, ...] = (1, 2)
    
    # Imprime el identificador único (ID) de la tupla 'coordinates' antes de modificarla.
    print("Before:", id(coordinates), end="\n", file=stdout)

    # Intenta modificar un valor en la tupla.
    # Esto generará un error porque las tuplas son inmutables en Python y no soportan la asignación a un índice.
    # Dara error TypeError: 'tuple' object does not support item assignment
    # coordinates[0] = 10

    # Solución: usa el operador += para agregar un nuevo elemento a la tupla.
    coordinates += (3,)  # Se agrega una coma después del entero 3 para asegurar que se cree una nueva tupla con un solo elemento.
    
    # Imprime el identificador único (ID) de la tupla 'coordinates' después de modificarla.
    print("After:", id(coordinates), end="\n", file=stdout)
    
    # Imprime la nueva tupla 'coordinates' con el valor añadido.
    print(coordinates, end="\n", file=stdout)

    return None

def cuarto_ejemplo() -> str:
    # Inicializa una variable 'text' con el valor "hello".
    text: str = "hello"
    
    # Intenta modificar el primer carácter de la cadena 'text'.
    # Esto generará un error porque las cadenas en Python son inmutables y no soportan la asignación a un índice.
    # TypeError: 'str' object does not support item assignment
    # text[0] = "H"
    
    # Devuelve el texto modificado. El código anterior causará un error, por lo que esta línea no se ejecutará.
    return text

if __name__ == "__main__":
    # Ejecuta la función cuarto_ejemplo si el fichero es ejecutado como script principal.
    print(cuarto_ejemplo(), end = "\n", file = stdout)
