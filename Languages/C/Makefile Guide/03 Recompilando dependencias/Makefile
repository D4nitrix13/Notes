# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# objetivo: dependencias
#	instrucciones

# Enlaces: https://www.gnu.org/software/make/
# Enlaces: https://www.gnu.org/software/make/manual/html_node/index.html

# Recompilando dependencias

# Variables de compilación
CC = gcc
CFLAGS = -std=c99 -Wall -Wextra -Werror -pedantic
LDFLAGS = -lSDL2

# Objetivo por defecto
all: programa

# Enlazar los ficheros objeto para crear el ejecutable
programa: main.o calc.o
	$(CC) -o programa main.o calc.o $(LDFLAGS)

# Regla de limpieza
clean:
	rm -f *.o programa

# Dependencias explícitas
main.o: main.c libcalc.h
calc.o: calc.c libcalc.h

# Make es una herramienta inteligente que sabe cuándo hay un cambio en uno de nuestros ficheros.
# Esto se debe a que Make utiliza las fechas de modificación de los ficheros para determinar
# qué ficheros necesitan ser recompilados.

# Ejemplo de ejecución de Make:

# Directorio actual: C-Guide/Makefile
# Branch: master
# Versión de gcc: 11.4.0

# Primera ejecución de `make`:
# make
# gcc -std=c99 -Wall -Wextra -Werror -pedantic -c -o main.o main.c
# gcc -std=c99 -Wall -Wextra -Werror -pedantic -c -o calc.o calc.c
# gcc -o programa main.o calc.o -lSDL2

# En la primera ejecución, Make compila `main.c` y `calc.c` en `main.o` y `calc.o` respectivamente,
# y luego enlaza los ficheros objeto para crear el ejecutable `programa`.

# Segunda ejecución de `make`:
# make
# make: Nothing to be done for 'all'.

# En la segunda ejecución, si no ha habido cambios en `main.c`, `calc.c` o `libcalc.h`,
# Make detecta que no hay nada que hacer porque los ficheros objeto ya están actualizados.

# Esto demuestra cómo Make utiliza las fechas de modificación de los ficheros para evitar
# recompilaciones innecesarias y ahorrar tiempo.
