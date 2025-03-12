#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# Importamos la clase PrettyTable del módulo prettytable
from prettytable import PrettyTable
from sys import stdout, exit

# Creamos una instancia de PrettyTable
table: PrettyTable = PrettyTable()

# Definimos los nombres de las columnas de la tabla
table.field_names = ["Nombre", "Edad", "Ciudad"]

# Agregamos filas a la tabla
table.add_row(row = ["Danna", 30, "Nueva York"])
table.add_row(row = ["Benjamin", 25, "San Francisco"])
table.add_row(row = ["Charlie", 35, "Los Ángeles"])

# Imprimimos la tabla
print(table, end = "\n", file = stdout)
exit(0)