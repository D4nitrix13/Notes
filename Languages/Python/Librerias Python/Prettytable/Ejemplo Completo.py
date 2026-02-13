#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stdout, exit
from prettytable import PrettyTable

# Creamos una instancia de PrettyTable
table: PrettyTable = PrettyTable()

# Definimos los nombres de las columnas
table.field_names = ["Nombre", "Edad", "Ciudad"]

# Agregamos filas a la tabla
table.add_row(row = ["Danna", 30, "Nueva York"])
table.add_row(row = ["Benjamin", 25, "San Francisco"])
table.add_row(row = ["Charlie", 35, "Los Ángeles"])

# Configuramos el ancho máximo de las columnas
table.max_width = 20

# Cambiamos el alineamiento de las columnas
table.align["Nombre"] = "l"
table.align["Edad"] = "r"
table.align["Ciudad"] = "c"

# Habilitamos el borde y el encabezado
table.border = True
table.header = True

# Imprimimos la tabla
print(table, end="\n", file=stdout)

# Salimos del programa con código de estado 0 (éxito)
exit(0)