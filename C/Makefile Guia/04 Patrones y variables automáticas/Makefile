# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# objetivo: dependencias
#	instrucciones

# Enlaces: https://www.gnu.org/software/make/
# Enlaces: https://www.gnu.org/software/make/manual/html_node/index.html

# Múltiples ficheros y otros aspectos finales

# Variables de compilación
CC = gcc
CFLAGS = -std=c99 -Wall -Wextra -Werror -pedantic
LDFLAGS = -lSDL2

# Objetivo por defecto
all: programa

# Patrón para compilar cualquier fichero .c en un fichero .o
%.o: %.c
	@echo "Compilando $< a $@"
	$(CC) -c $(CFLAGS) -o $@ $<

# Patrón para compilar ficheros en un subdirectorio
Directory/%.o: Directory/%.c
	@echo "Compilando $< a $@ en el directorio Directory"
	$(CC) -c $(CFLAGS) -o $@ $<

# Enlazar los ficheros objeto para crear el ejecutable
programa: main.o calc.o
	@echo "Ficheros modificados: $?"
	@echo "Creando el ejecutable: $@"
	$(CC) -o $@ $^ $(LDFLAGS)

# Regla de limpieza
clean:
	rm -f *.o programa

# Dependencias explícitas
main.o: main.c libcalc.h
calc.o: calc.c libcalc.h
