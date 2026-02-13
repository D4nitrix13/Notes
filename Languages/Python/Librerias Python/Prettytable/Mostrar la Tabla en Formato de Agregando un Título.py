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

# Exportamos la tabla en formato deseado, agregando un título
# El formato por defecto es 'grid', que muestra la tabla con bordes
formatTable: str = table.get_string(title="Australian cities")

# Imprimimos la tabla formateada con el título en la salida estándar
# El parámetro end="\n" asegura que haya una nueva línea después de la tabla
print(formatTable, end="\n", file=stdout)

# Salimos del programa con código de estado 0 (éxito)
exit(0)