# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# objetivo: dependencias
#	instrucciones

# Enlaces: https://www.gnu.org/software/make/
# Enlaces: https://www.gnu.org/software/make/manual/html_node/index.html

# Makefile
# Regla principal: compilación del programa
all: programa

# Regla `all`: define el objetivo principal del Makefile, que es `programa`.

programa: main.o calc.o
	gcc -o programa main.o calc.o

# Regla `programa`: compila el programa final. Depende de `main.o` y `calc.o`.
# Utiliza `gcc -o programa` para vincular los ficheros objeto `main.o` y `calc.o` en un ejecutable llamado `programa`.

# Regla para compilar `main.o`
main.o: main.c libcalc.h
	gcc -c main.c

# Regla `main.o`: compila `main.c` en `main.o`. Depende de `main.c` y `libcalc.h`.
# Utiliza `gcc -c main.c` para compilar `main.c` y generar el fichero objeto `main.o`.

# Regla para compilar `calc.o`
calc.o: calc.c libcalc.h
	gcc -c calc.c

# Regla `calc.o`: compila `calc.c` en `calc.o`. Depende de `calc.c` y `libcalc.h`.
# Utiliza `gcc -c calc.c` para compilar `calc.c` y generar el fichero objeto `calc.o`.

# Regla para limpiar ficheros objeto y el ejecutable
clean:
	rm -f *.o programa

# Regla `clean`: elimina todos los ficheros objeto (`*.o`) y el ejecutable `programa`.
