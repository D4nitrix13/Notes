#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import exit
from argparse import ArgumentParser

parser: ArgumentParser = ArgumentParser(
    prog = "Mi_Programa",
    description = "Este es un programa de ejemplo.",
    epilog = "Texto adicional al final de la ayuda.",
    exit_on_error = True,
    add_help = True
)

exit(0)