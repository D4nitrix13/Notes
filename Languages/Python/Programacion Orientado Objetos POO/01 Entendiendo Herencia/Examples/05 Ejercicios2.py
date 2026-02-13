#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
Herencias - Ejercicio 2

Ejercicio de herencia y uso de super:

Crear un sistema para una escuela. En este sistema, vamos a tener dos clases principales: Persona y Estudiante. La clase Persona tendrá los atributos de nombre y edad y un método que imprima el nombre y la edad de la persona. La clase Estudiante heredará de la clase Persona y también tendrá un atributo adicional: grado y un método que imprima el grado del estudiante.
Deberás utilizar super en el método de inicialización (init) para reutilizar el código de la clase padre (Persona). Luego crea una instancia de la clase Estudiante e imprime sus atributos y utiliza sus métodos para asegurarte de que todo funciona correctamente.
"""

class Persona:
    def __init__(self: 'Persona', nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        return None

    def datos_persona(self: 'Persona') -> str: return f"Nombre: {self.nombre}\nEdad: {self.edad}"


class Estudiante(Persona):
    def __init__(self: 'Estudiante', nombre: str, edad: int, grado: str) -> None:
        super().__init__(nombre = nombre, edad = edad)
        self.grado: str = grado
        return None

    def grado_estudiante(self: 'Estudiante') -> str:
        # return "Grado: {grado_actual}".format(grado_actual=self.grado)  formato de impresion con .format y asignacion de variables 
        
        # return "Grado: {}".format(self.grado) formato de impresion con .format 
        
        # return "Grado: {0}".format(self.grado) formato de impresion con .format y asignacion de orden de impresion con {0} {1} {2} etc
        
        # return "Grado: %s" % (self.grado) formato de impresion con %s 
        
        return f"Grado: {self.grado}" # formato de impresion con f-string


daniel: Estudiante = Estudiante(nombre = "Daniel", edad = 20, grado = "10mo grado")
print(daniel.nombre, end="\n")
print(daniel.edad, end="\n")
print(daniel.datos_persona(), end="\n")
print(daniel.grado_estudiante(), end="\n")