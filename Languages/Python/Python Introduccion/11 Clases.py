"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Clases

# Definición
"""
Paradigma: orientado a objetos es un paradigma de programación que se basa en objetos
"""


from sys import stdout
from typing import Union


class PersonaVacia:
    # constructor
    def __init__(self: "PersonaVacia") -> None:
        # pass  # Para poder dejar la clase vacía
        return None


print(PersonaVacia, end = "\n", file = stdout)  # Nos imprime el tipo de dato de la clase
print(PersonaVacia(), end = "\n", file = stdout)  # Nos imprime el objeto de la clase

# Clase con constructor, funciones y popiedades privadas y públicas


class Persona:
    # Constructor
    def __init__(self: "Persona", nombre: str, segundoNombre: str, alias: str = "Sin alias") -> None:
        self.full_nombre: Union[str, int] = (
            f"{nombre} {segundoNombre} ({alias})"  # Propiedad pública
        )
        self.__nombre: str = nombre  # Propiedad privada
        return None

    def get_nombre(self: "Persona") -> str: return self.__nombre

    def caminar(self: "Persona") -> None:
        print(f"{self.full_nombre} está caminando", end = "\n", file = stdout)
        return None


persona: Persona = Persona(nombre="Daniel", segundoNombre="Benjamin")
print(persona.full_nombre, end = "\n", file = stdout)
print(persona.get_nombre(), end = "\n", file = stdout)
persona.caminar()

otraPersona: Persona = Persona(
    nombre="Daniel", segundoNombre="Benajamin", alias="DanielDev"
)
print(otraPersona.full_nombre, end = "\n", file = stdout)
otraPersona.caminar()
# sobreescribimos la propiedad full_nombre
otraPersona.full_nombre = "Daniel Benjamin Perez Morales"
print(otraPersona.full_nombre, end = "\n", file = stdout)

otraPersona.full_nombre = 100
print(otraPersona.full_nombre, end = "\n", file = stdout)
