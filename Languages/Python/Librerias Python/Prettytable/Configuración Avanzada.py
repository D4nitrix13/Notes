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
table.field_names = ["Producto", "Cantidad", "Precio Unitario"]

# Agregamos filas a la tabla
table.add_row(row = ["Manzanas", 10, "$1.00"])
table.add_row(row = ["Naranjas", 5, "$0.80"])
table.add_row(row = ["Plátanos", 7, "$1.20"])

# Configuramos el ancho de las columnas
table.max_width = 20

# Cambiamos el alineamiento de las columnas
table.align["Producto"] = "l"  # Alineación a la izquierda
table.align["Cantidad"] = "r"  # Alineación a la derecha
table.align["Precio Unitario"] = "c"  # Alineación al centro

# Establecemos un borde para la tabla
table.border = True

# Establecemos el borde de las filas
table.header = True
table.header_style = "title"

# Imprimimos la tabla
print(table, end = "\n", file = stdout)
exit(0)