#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout, exit
from time import sleep

texto: str = "Hola,\nMundo!"
print(texto, end = "\n", file = stdout)
# Salida:
# Hola,
# Mundo!

for i in range(0, 10, 1):
    stdout.write(f"\rNúmero: {i}")
    stdout.flush()
    sleep(0.5)
print("", end = "\n", file = stdout)  # Para terminar la línea

texto: str = "Hola, Mundo!\b."
print(texto, end = "\n", file = stdout)
# Salida:
# Hola, Mundo!.

texto: str = "Columna1\tColumna2\tColumna3"
print(texto, end = "\n", file = stdout)
# Salida:
# Columna1    Columna2    Columna3

texto: str = "Ruta del fichero: C:\\\\Ficheros\\MiFichero.txt"
print(texto, end = "\n", file = stdout)
# Salida:
# Ruta del fichero: C:\\Ficheros\MiFichero.txt

texto: str = 'Aquí hay una comilla simple: \'\'.'
print(texto, end = "\n", file = stdout)
# Salida:
# Aquí hay una comilla simple: ''.

texto: str = "Aquí hay una comilla doble: \"\"."
print(texto, end = "\n", file = stdout)
# Salida:
# Aquí hay una comilla doble: "".

texto: str = "Emoji: \U0001F600"  # Código Unicode para 😀
print(texto, end = "\n", file = stdout)
# Salida:
# Emoji: 😀

texto: str = "Sonido de campana: \a"
print(texto, end = "\n", file = stdout)
# Nota: El efecto del sonido depende de la configuración del sistema y del terminal.

texto: str = "Primera página\fSegunda página"
print(texto, end = "\n", file = stdout)
# Nota: El efecto puede variar según el entorno donde se imprime.

texto: str = "Primera línea\vSegunda línea"
print(texto, end = "\n", file = stdout)
# Nota: El efecto puede variar según el entorno donde se imprime.

texto: str = """\
Este es un ejemplo
de una cadena multilínea
que usa el carácter de escape
para continuar en la siguiente línea
sin incluir un salto de línea.
"""
print(texto, end = "\n", file = stdout)

exit(0)
# Salida:
# Este es un ejemplo de una cadena multilínea que usa el carácter de escape para continuar en la siguiente línea sin incluir un salto de línea.


# Explicación:

#     """ con \: El uso de """ con \ permite definir cadenas multilínea sin incluir los saltos de línea en la cadena resultante. Esto es útil para cadenas largas o para mantener la legibilidad en el código.

#     Otros caracteres de escape:
#         \n: Nueva línea.
#         \r: Retorno de carro.
#         \b: Retroceso.
#         \t: Tabulación.
#         \\: Barra invertida literal.
#         \': Comillas simples.
#         \": Comillas dobles.
#         \u/\U: Caracteres Unicode.
#         \a: Campana.
#         \f: Salto de página.
#         \v: Tabulación vertical.

# Cada uno de estos caracteres de escape tiene un propósito específico y puede ser útil en diferentes contextos para manipular el formato y la presentación del texto.