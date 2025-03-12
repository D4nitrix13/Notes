#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from argparse import ArgumentParser
from sys import exit

parser: ArgumentParser = ArgumentParser(description = "Programa de ejemplo")

parser.add_argument(
    "-i", "--input",            # Nombres del argumento
    dest = "input_file",          # Nombre del atributo en el Namespace
    nargs = 1,                    # Número de argumentos esperados
    type = str,                   # Tipo de dato del argumento
    required = True,              # Argumento obligatorio
    help = "Fichero de entrada",  # Descripción del argumento
    metavar = "FICHERO"           # Nombre en la ayuda
)

parser.add_argument(
    "--verbose",                # Nombres del argumento
    action = "store_true",        # Almacena True si el argumento está presente
    help = "Mostrar salida detallada"  # Descripción del argumento
)
exit(0)