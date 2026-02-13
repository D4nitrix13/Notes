#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from argparse import ArgumentParser, Namespace
from sys import stdout, exit

parser: ArgumentParser = ArgumentParser(description = "Programa de ejemplo")
parser.add_argument("-i", "--input", required = True, help = "Fichero de entrada")
args: Namespace = parser.parse_args()

print(args.input, end = "\n", file = stdout)  # Imprime el valor del argumento --input
exit(0)