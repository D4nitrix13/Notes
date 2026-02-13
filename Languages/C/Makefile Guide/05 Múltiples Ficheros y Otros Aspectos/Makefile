# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# objetivo: dependencias
#	instrucciones

# Enlaces: https://www.gnu.org/software/make/
# Enlaces: https://www.gnu.org/software/make/manual/html_node/index.html

# Makefile principal

# Directiva para incluir otros Makefile
include DirectoryMakefile/Makefile

# La directiva `include` se utiliza en Makefiles para incluir y procesar otro fichero Makefile,
# en este caso, el fichero ubicado en `DirectoryMakefile/Makefile`. Esto permite modularizar y
# reutilizar configuraciones comunes en diferentes partes del proyecto.

# Al importar un Makefile dentro de otro usando `include`, el contenido del Makefile
# importado (`DirectoryMakefile/Makefile` en este caso) se procesa junto con el Makefile
# actual. Esto significa que los objetivos definidos en `DirectoryMakefile/Makefile`
# pueden afectar el comportamiento de `make`, incluyendo cuál es el objetivo predeterminado
# que se ejecuta al invocar `make` en el directorio donde se encuentra este Makefile principal.

# Ejemplo de uso en el código:
# Supongamos que `DirectoryMakefile/Makefile` contiene reglas y variables específicas
# que son necesarias para la compilación de ciertos componentes del proyecto. Al utilizar
# `include`, se integra ese fichero en el Makefile actual, extendiendo así su funcionalidad
# con las reglas y variables definidas en `DirectoryMakefile/Makefile`.

# -------------------------------------------------------------------------------------------------

# Variables de compilación
CC = gcc
CFLAGS = -std=c99 \
-Wall \
-Wextra \
-Werror \
-pedantic

# Define el compilador como gcc
# Opciones de compilación:
#   -std=c99: Estándar C99
#   -Wall y -Wextra: Advertencias detalladas
#   -Werror: Tratar las advertencias como errores
#   -pedantic: Adherirse estrictamente al estándar

# Explicación:
# - La variable CC se establece como gcc, indicando que se usará el compilador GNU C.
# - CFLAGS se utiliza para especificar las opciones de compilación.
# - El uso del carácter '\' al final de cada línea excepto la última permite dividir
#   las opciones de compilación en varias líneas para mejorar la legibilidad del Makefile.
# - Esto no afecta cómo se interpretan las opciones por parte del compilador; simplemente
#   es una convención de Makefile para manejar líneas largas de forma más clara.

# -------------------------------------------------------------------------------------------------

# Objetivo por defecto
all: programa

# Patrón para compilar cualquier fichero .c en un fichero .o
%.o: %.c
	@echo "Compilando $< a $@"
	$(CC) -c $(CFLAGS) -o $@ $<

# Enlazar los ficheros objeto para crear el ejecutable
programa: main.o calc.o
	@echo "Ficheros de dependencias: $^"
	@echo "Creando el ejecutable: $@"
	$(CC) -o $@ $^

# Regla de limpieza
clean:
	rm -f *.o programa

# Dependencias explícitas
main.o: main.c libcalc.h
calc.o: calc.c libcalc.h

# -------------------------------------------------------------------------------------------------

# Directiva `.PHONY` para especificar objetivos que no son ficheros
.PHONY: all clean

# PHONY: all clean: Indica que all y clean son objetivos que no representan ficheros reales y deben ejecutarse siempre que se invoquen, independientemente de si hay ficheros con esos nombres.