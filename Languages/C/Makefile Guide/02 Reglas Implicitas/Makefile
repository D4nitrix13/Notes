# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# objetivo: dependencias
#	instrucciones

# Enlaces: https://www.gnu.org/software/make/
# Enlaces: https://www.gnu.org/software/make/manual/html_node/index.html

# Makefile con reglas implícitas

# Variables de compilación
CC = gcc
CFLAGS = -std=c99 -Wall -Wextra -Werror -pedantic
LDFLAGS = -lSDL2

# Objetivo por defecto
all: programa

# Reglas implícitas:
# Make tiene reglas implícitas que sabe cómo compilar ficheros .c a .o:
# `$(CC) $(CFLAGS) -c` se usa para compilar .c a .o

# Enlazar los ficheros objeto para crear el ejecutable
programa: main.o calc.o
	$(CC) -o programa main.o calc.o $(LDFLAGS)

# Regla de limpieza
clean:
	rm -f *.o programa

# Dependencias explícitas
main.o: main.c libcalc.h
calc.o: calc.c libcalc.h
