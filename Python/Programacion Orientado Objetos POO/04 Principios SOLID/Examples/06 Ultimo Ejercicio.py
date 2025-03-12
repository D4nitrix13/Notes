#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
Chatbot analizador de sentimientos

En este proyecto, podrias desarrollar un chatbot en python, que nos pida que le digamos algo y tome eso que le decimos, analice el sentimiento y no responda cual es el sentimiento.
Este proyecto te daria la oportunidad de trabajar con varios aspectos de la Programacion Orientada a Objetos, modulos, API, analisis de datos, etc.
"""

from types import FrameType
from typing import NoReturn, Optional, Any, List, Union
import signal, pdb
from subprocess import check_call, CalledProcessError
from os import name, system
from sys import platform, executable, exit, stdout

def install_dependency(*, packageName: str) -> Union[NoReturn, None]:
    try:
        if platform.startswith('linux') or platform == 'darwin': check_call(args = [executable, '-m', 'pip', 'install', packageName])
        elif platform == 'win32': check_call(args=[executable, '-m', 'pip', 'install', packageName])
        else: raise OSError("Sistema operativo no soportado para la instalación automática.")
    
    except CalledProcessError as e: 
        print(f"Error al intentar instalar {packageName}: {e}", end = "\n", file = stdout)
        exit(1)
    return None

try: import textblob
except ImportError:
    print("textblob no está instalado. Instalando ahora...", end = "\n", file = stdout)
    install_dependency(packageName = "textblob")

try: from deep_translator import GoogleTranslator
except ImportError:
    print("deep_translator no está instalado. Instalando ahora...", end = "\n", file = stdout)
    install_dependency(packageName = "deep_translator")

try: from pwn import *
except ImportError:
    print("pwn no está instalado. Instalando ahora...", end = "\n", file = stdout)
    install_dependency(packageName = "pwn")

try: from termcolor import colored
except ImportError:
    print("termcolor no está instalado. Instalando ahora...", end = "\n", file = stdout)
    install_dependency(packageName = "colored")

try: from langdetect import detect, DetectorFactory
except ImportError:
    print("langdetect no está instalado. Instalando ahora...", end = "\n", file = stdout)
    install_dependency(packageName = "langdetect")

import time
from pwn import log
from termcolor import colored
import textblob
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

ESPAÑOL: str = "es"
ENGLISH: str = "en"

def borrar() -> None:
    system(command = "cls" if name == "nt" else "clear")
    return None

def salir_programa(sig: int ,frame: Optional[FrameType]) -> NoReturn:
    log.failure(message = f"{colored(text = 'Saliendo!', color = 'light_red')}")
    exit(1)

signal.signal(signalnum = signal.SIGINT, handler = salir_programa)


# ! en-English
# ! es-Spanish

class Español:
    def __init__(self: "Español") -> None:
        self._traductorEspañol: GoogleTranslator = GoogleTranslator(source = 'auto', target = ESPAÑOL)
        # self._traductorEspañol: GoogleTranslator: Define un atributo de instancia _traductor_español que es de tipo GoogleTranslator.

        # GoogleTranslator(source = ENGLISH, target = ESPAÑOL): Crea una instancia de GoogleTranslator configurada para traducir del inglés al español.

        # source = ENGLISH: Especifica el idioma de origen como inglés ('en').
        # target = ESPAÑOL: Especifica el idioma de destino como español ('es').
        return None
    def _traducir_texto_español(self:"Español", texto: str) -> str:
        # self._traductorEspañol.translate(text=texto): Llama al método translate de la instancia GoogleTranslator para traducir el texto.
        # text = texto: Especifica el texto que se va a traducir.
        return self._traductorEspañol.translate(text = texto)


class Ingles:
    def __init__(self: 'Ingles') -> None:
        self._traductor_ingles: GoogleTranslator = GoogleTranslator(source = 'auto', target = ENGLISH)
        return None

    def _traducir_texto_ingles(self: 'Ingles', texto: str) -> str:
        return self._traductor_ingles.translate(text = texto)

DetectorFactory.seed = 0

class Traductor(Ingles, Español):
    def __init__(self: 'Traductor') -> None:
        Ingles.__init__(self = self)
        Español.__init__(self = self)
        return None

    def _ver_idioma(self: 'Traductor', texto: str) -> Union[str, NoReturn]:
        try:
            idioma: str = detect(text = texto)
            return idioma
        except LangDetectException: raise LangDetectException(message = f"{colored(text = 'No se pudo detectar el idioma', color = 'light_red')}", code = 1)

class AnalizadorSentimientos(Traductor):
    def __init__(self: 'AnalizadorSentimientos') -> None:
        super().__init__()
        return None

    def _analizador_sentimientos(self: 'AnalizadorSentimientos', texto: str) -> str:
        # idioma: str = self._ver_idioma(texto = texto)
        
        analisis: textblob.TextBlob = textblob.TextBlob(text = self._traducir_texto_ingles(texto = texto))
        if analisis.sentiment.polarity > 0: return f"{colored(text = 'El comentario que hiciste indica que tu estado de animo es positivo',color = 'light_green')}"
        elif analisis.sentiment.polarity == 0: return f"{colored(text = 'El comentario que hiciste indica que tu estado de animo es neutral',color = 'light_yellow')}"
        else: return f"{colored(text = 'El comentario que hiciste indica que te sientes mal',color = 'light_red')}"

if __name__ == "__main__":
    borrar()
    daniel: AnalizadorSentimientos = AnalizadorSentimientos()
    
    print(f"{colored(text = 'Analizador De Sentimiento Hechos En Python3',color = 'light_grey')}" , end = "\n", file = stdout)
    while True:
        log.info(message = f"{colored(text = 'Ingrese Un Texto De Tu Estado De Animo (Salir -> Ctrl + C): ', color = 'light_cyan')}")
        textoUsuario: str = str(input('')).lower()


        # Actualizar el estado
        emociones: List[str] = [
                "Felicidad", "Tristeza", "Ira", "Miedo", "Sorpresa", "Asco", "Amor", "Odio", "Alegría", "Depresión",
                "Ansiedad", "Esperanza", "Paz", "Euforia", "Desesperación", "Culpa", "Vergüenza", "Orgullo", "Cansancio",
                "Satisfacción", "Desagrado", "Enojo", "Desilusión", "Excitación", "Preocupación", "Aburrimiento",
                "Inseguridad", "Compasión", "Empatía", "Admiración", "Envidia", "Arrepentimiento", "Remordimiento",
                "Desamparo", "Resignación", "Enamoramiento", "Desdén", "Hostilidad", "Resentimiento", "Indignación",
                "Desesperanza", "Despreocupación", "Placer", "Tranquilidad", "Nostalgia", "Incredulidad", "Sorpresa",
                "Incredulidad", "Desesperación", "Curiosidad", "Satisfacción", "Escepticismo", "Euforia", "Compasión",
                "Ira", "Vergüenza", "Emoción", "Agobio", "Desprecio", "Asombro", "Sorpresa", "Desconsuelo", "Frustración",
                "Comprensión", "Perplejidad", "Despreocupación", "Respeto", "Inseguridad", "Resentimiento", "Remordimiento",
                "Desesperanza", "Desesperación", "Aburrimiento", "Cautela", "Pena", "Esperanza", "Miedo", "Desagrado",
                "Plenitud", "Arrepentimiento", "Desilusión", "Optimismo", "Incertidumbre", "Soledad", "Soledad", "Satisfacción",
                "Serenidad", "Admiración", "Envidia", "Esperanza", "Hostilidad", "Indiferencia", "Tranquilidad", "Felicidad",
                "Preocupación", "Alivio", "Compasión", "Ira", "Compasión"
            ]
        i: Optional[str] = None
        p1: Any = log.progress(message = f"{colored(text = 'Analizando Estado de Animo', color = 'light_blue')}")
        
        for i in emociones:
            p1.status(f"{colored(text = i, color = 'light_magenta')}")
            time.sleep(0.1)

        # Indicar éxito
        p1.success(f"{colored(text = '¡El anilisis ha sido completado con Exito!', color = 'light_magenta')}")
        

        time.sleep(1.0)
        print(daniel._analizador_sentimientos(texto = textoUsuario),end = "\n", file = stdout)
        
        # Volviendo a preguntar
        log.info(message = f"{colored(text = 'Ingrese Un Texto De Tu Estado De Animo (Salir -> Ctrl + C): ', color = 'light_cyan')}")
        continue