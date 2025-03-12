#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
La abstaccion es un concepto que nos permite ocultar detalles de implementacion y solo mostrar los detalles que sean necesarios para el usuario. Por ejemplo, cuando enviamos un mensaje de texto no nos importa como funciona el servicio de telefonia, solo queremos enviar el mensaje. 

En python, la abstraccion se logra a traves de clases abstractas y metodos abstractos. Una clase abstracta es aquella que no se puede instanciar, es decir, no se puede crear objetos de esa clase. Por lo general, las clases abstractas sirven como base para que las clases hijas hereden metodos y atributos. 

Un metodo abstracto es un metodo que se declara pero no se implementa, es decir, solo se define la firma del metodo, pero no su implementacion. Las clases abstractas pueden tener metodos abstractos, y las clases hijas de estas clases deben implementar los metodos abstractos de la clase padre.

Para crear una clase abstracta en python, se debe importar el modulo abc (Abstract Base Class) y heredar de la clase ABC. Para crear un metodo abstracto, se debe importar el decorador abstractmethod del modulo abc y decorar el metodo con este decorador.
"""

from sys import stdout


class Auto:
    def __init__(self: 'Auto') -> None:
        self._estado: str = "apagado"
        return None
    
    def encender(self: 'Auto') -> None:
        self._estado = "encendido"
        print("El auto esta encendido",end="\n", file = stdout)
        return None
    
    def conducir(self: 'Auto') -> None:
        if self._estado == "apagado":
            self.encender()
        print("Conduciendo el auto",end="\n", file = stdout)

miAuto: Auto = Auto()
miAuto.conducir()