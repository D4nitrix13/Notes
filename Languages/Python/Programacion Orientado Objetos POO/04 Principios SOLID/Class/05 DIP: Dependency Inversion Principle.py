#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
"DIP": "Dependency Inversion Principle" Significa en español Principio de inversion de dependencias.

La idea de este principio es que los modulos de alto nivel no deben depender de los modulos de bajo nivel. Ambos deben depender de abstracciones. Las abstracciones no deben depender de los detalles. Los detalles deben depender de las abstracciones. 
"""

"""
class Dictionario:
    def __init__(self: 'Dictionario', palabra: str) -> None:
        self.palabra: str = palabra
        return None

    def verificar_palabra(self: 'Dictionario') -> None:
        # logica para verificar si la palabra existe en el diccionario
        return None


class CorrectorOrtografico:
    def __init__(self: 'CorrectorOrtografico') -> None:
        # A esto se le llama
        self.diccionario: 'Dictionario' = Dictionario(palabra = "Data Science")
        return None

    def corregir_texto(self: 'CorrectorOrtografico', texto: str) -> None:
        # usamos el diccionario para corregir el texto
        return None

"""

"""
En este ejemplo la clase CorrectorOrtografico depende de la clase Dictionario
y esto no es bueno porque si queremos cambiar la clase Dictionario tendriamos que cambiar la clase CorrectorOrtografico y esto no es bueno porque no se cumple el principio de inversion de dependencias.
"""


from abc import ABC, abstractmethod
from typing import Union

class VerificadorOrtografico(ABC):
    @abstractmethod
    def __init__(self: 'VerificadorOrtografico') -> None:
        # A esto se le llama
        self.diccionario: 'Dictionario' = Dictionario(palabra = "Data Science")
        return None

    @abstractmethod
    def verificar_palabra(self: 'VerificadorOrtografico', palabra: str) -> None:
        # Logica para verificar si la palabra existe en el diccionario
        return None


class Dictionario(VerificadorOrtografico):
    def __init__(self: 'Dictionario', palabra: str) -> None:
        self.palabra: str = palabra
        super().__init__()
        return None

    def verificar_palabra(self: 'Dictionario', palabra: str) -> None:
        # logica para verificar si la palabra existe en el diccionario
        return None

class ServicioOnline(VerificadorOrtografico):
    def __init__(self: 'ServicioOnline', palabra: str) -> None:
        self.palabra: str = palabra
        super().__init__()
        return None

    def verificar_palabra(self: 'ServicioOnline', palabra: str) -> None:
        # logica para verificar desde el servicio online
        return None

class CorrectorOrtografico:
    def __init__(self: 'CorrectorOrtografico', verificador: Union['ServicioOnline', 'Dictionario']) -> None:
        # A esto se le llama
        self.verificador: Union['ServicioOnline', 'Dictionario'] = verificador
        return None

    def corregir_texto(self: 'CorrectorOrtografico', texto: str) -> None:
        # usamos el diccionario para corregir el texto
        return None

correctorOne: CorrectorOrtografico = CorrectorOrtografico(verificador = ServicioOnline(palabra = "Dev Web FullStack"))
correctorDos: CorrectorOrtografico = CorrectorOrtografico(verificador = Dictionario(palabra = "Pentesting"))

"""
Ahora la clase CorrectorOrtografico no depende de la clase Dictionario, ahora depende de la clase VerificadorOrtografico y esto es bueno porque si queremos cambiar la clase Dictionario por otra clase que tenga la misma funcionalidad no tendriamos que cambiar la clase CorrectorOrtografico y esto es bueno porque se cumple el principio de inversion de dependencias. 

Tambien la clase CorrectorOrtografico depende de la abstraccion VerificadorOrtografico y esto es bueno porque si queremos cambiar la clase Dictionario por otra clase que tenga la misma funcionalidad no tendriamos que cambiar la clase CorrectorOrtografico y esto es bueno porque se cumple el principio de inversion de dependencias.
"""
