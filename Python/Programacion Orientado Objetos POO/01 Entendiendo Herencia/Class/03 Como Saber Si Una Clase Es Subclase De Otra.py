#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout


class Persona:
    def __init__(self: 'Persona', nombre: str, edad: int, nacionalidad: str) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        self.nacionalidad: str = nacionalidad
        return None

    def hablar(self: 'Persona') -> str: return f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años y soy {self.nacionalidad}"

class Artista:
    def __init__(self: 'Artista', habilidad: str) -> None:
        self.habilidad: str = habilidad
        return None

    def mostrar_habilidad(self: 'Artista') -> str: return f"Mi habilidad es {self.habilidad}"

class EmpleadoArtista(Persona, Artista):
    def __init__(
        self: 'EmpleadoArtista',
        nombre: str,
        edad: int,
        nacionalidad: str,
        habilidad: str,
        salario: float,
        empresa: str,
    ) -> None:
        # En este caso, la clase EmpleadoArtista hereda los atributos de las clases Persona y Artista.

        # pero no podemos usar super().__init__() tenemos que usar el nombre de la clase y pasar los atributos de las clases padre y pasarle el self.

        Persona.__init__(self = self, nombre = nombre, edad = edad, nacionalidad = nacionalidad)
        Artista.__init__(self = self, habilidad = habilidad)
        self.salario: float = salario
        self.empresa: str = empresa
        return None


    def presentarse_super(self: 'EmpleadoArtista') -> str: return f"{super().mostrar_habilidad()}"

    # al hacer super().hablar() estamos accediendo al metodo hablar de la clase padre no de la clase hija.

    def presentarse_self(self: 'EmpleadoArtista') -> str: return f"{self.mostrar_habilidad()}"

    # y cuando hacemos self.mostrar_habilidad() estamos accediendo al metodo mostrar_habilidad de la clase hija no de la clase padre.

    def mostrar_habilidad(self: 'EmpleadoArtista') -> str: return "No tengo habilidad"

    # si nosotros creamos un metodo con el mismo nombre de un metodo de una clase padre, el metodo de la clase hija va a tener prioridad.
    def presentarse_one(self: 'EmpleadoArtista') -> str: return f"Hola, mi nombre es {self.nombre} y mi habilidad es {self.mostrar_habilidad()} y tengo {self.edad} años y soy {self.nacionalidad} y trabajo en {self.empresa} y gano {self.salario}"

    def presentarse_two(self: 'EmpleadoArtista') -> str: return f"Hola, mi nombre es {self.nombre} y {super().mostrar_habilidad()} y tengo {self.edad} años y soy {self.nacionalidad} y trabajo en {self.empresa} y gano {self.salario} dolares al mes"


daniel: EmpleadoArtista = EmpleadoArtista(
    nombre = "Daniel",
    edad = 20,
    nacionalidad = "Nicaraguense",
    habilidad = "Cantar",
    salario = 1000000,
    empresa = "Google",
)

danna: Artista = Artista(habilidad = "Programar")

# Para saber si una clase es subclase de otra, podemos usar la funcion issubclass() y pasarle como primer argumento la clase que queremos saber si es subclase de otra y como segundo argumento la clase de la cual queremos saber si es subclase.
"""

>>> herencia = issubclass(clase, clase_de_la_cual_queremos_saber_si_es_subclase)

el valor que nos va a retornar es un booleano, True si es subclase y False si no lo es.
"""

herencia: bool = issubclass(EmpleadoArtista, Persona)
print(f"¿Es EmpleadoArtista subclase de Persona?: {'Si' if herencia == True else 'No'}",end = "\n", file = stdout)

herencia = issubclass(Artista, Persona)
print(f"¿Es Artista subclase de Persona?: {'Si' if herencia == True else 'No'}",end = "\n", file = stdout)

# para saber si un objeto es una instancia de una clase, podemos usar la funcion isinstance() y pasarle como primer argumento el objeto que queremos saber si es instancia de una clase y como segundo argumento la clase de la cual queremos saber si es instancia.

"""
ejemplo:
instancia = isinstance(objeto, clase_de_la_cual_queremos_saber_si_es_instancia)
"""

instancia: bool = isinstance(daniel, EmpleadoArtista)
print(f"¿Es Daniel una instancia de EmpleadoArtista?: {'Si' if instancia == True else 'No'}",end = "\n", file = stdout)
# la razon por la cual Daniel es una instancia de EmpleadoArtista es porque Daniel es un objeto de la clase EmpleadoArtista.

instancia = isinstance(daniel, Artista)
print(f"¿Es Daniel una instancia de Artista?: {'Si' if (instancia == True) else 'No'}",end = "\n", file = stdout)
# la razon por la cual Daniel es una instancia de Artista es porque la clase EmpleadoArtista hereda los atributos de la clase Artista.

instancia = isinstance(daniel, Persona)
print(f"¿Es Daniel una instancia de Persona?: {'Si' if (instancia == True) else 'No'}",end = "\n", file = stdout)
# la razon por la cual Daniel es una instancia de Persona es porque la clase EmpleadoArtista hereda los atributos de la clase Persona.

instancia = isinstance(danna, EmpleadoArtista)
print(f"¿Es Danna una instancia de EmpleadoArtista?: {'Si' if (instancia == True) else 'No'}",end = "\n", file = stdout)
# la razon por la cual Danna no es una instancia de EmpleadoArtista es porque Danna es un objeto de la clase Artista y la clase Artista no hereda los atributos de la clase EmpleadoArtista.

instancia = isinstance(danna, Persona)
print(f"¿Es Danna una instancia de Persona?: {'Si' if (instancia == True) else 'No'}",end = "\n", file = stdout)

instancia = isinstance(danna, Artista)
print(f"¿Es Danna una instancia de Artista?: {'Si' if (instancia == True) else 'No'}",end = "\n", file = stdout)
