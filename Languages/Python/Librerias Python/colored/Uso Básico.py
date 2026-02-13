#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stdout
from colored import Fore, Back, Style

# Definir colores y estilos
red: str  = Fore.RED
green: str  = Fore.GREEN
yellow: str  = Fore.YELLOW
blue: str  = Fore.BLUE
reset: str  = Style.reset

# Definir fondos
bgRed: str  = Back.RED
bgGreen: str  = Back.GREEN

# Estilos
bold: str = Style.bold
underline: str = Style.underline

# Crear mensajes con colores y estilos
message1: str = f"{red}Este texto es rojo{reset}"
message2: str = f"{green}{bold}Este texto es verde y negrita{reset}"
message3: str = f"{yellow}{underline}Este texto es amarillo y subrayado{reset}"
message4: str = f"{blue}{bgRed}Texto azul con fondo rojo{reset}"

# Imprimir los mensajes
print(message1, end = "\n", file = stdout)
print(message2, end = "\n", file = stdout)
print(message3, end = "\n", file = stdout)
print(message4, end = "\n", file = stdout)
exit(0)