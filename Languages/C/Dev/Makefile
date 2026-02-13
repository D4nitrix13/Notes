# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# Variables
CC = gcc                                # Compilador a utilizar
CFLAGS = -I "Lista Dinamica Int/lib" -Wall # Flags de compilación

# Objetivos
run: all

# Objetivos
all: programa
	./main

programa: main.o
	$(CC) -o main main.o  # Enlaza el objeto para crear el ejecutable

main.o: Lista\ Dinamica\ Int/src/main.c
	$(CC) $(CFLAGS) -c "Lista Dinamica Int/src/main.c"  # Compila el código fuente a objeto

# Regla para limpiar ficheros generados
clean:
	rm -f *.o main


# ```makefile
# programa: main.o
# 	$(CC) -o main main.o  # Enlaza el objeto para crear el ejecutable
# ```

# Desglose de la Sintaxis

# 1. `programa: main.o`:
#    - `programa`: Este es el objetivo (o "target") que estás tratando de construir. En este caso, se llama `programa` y es el nombre que le estás dando al ejecutable final.
#    - `main.o`: Esto es una dependencia del objetivo `programa`. Significa que para construir `programa`, necesitas tener `main.o` (el fichero objeto) ya creado. Si `main.o` no existe o ha sido modificado más recientemente que `programa`, entonces se ejecutará la línea que sigue.

# 2. `$(CC) -o main main.o`:
#    - `$(CC)`: Esta es una variable que representa el compilador que estás utilizando. En el `Makefile` anterior, se define como `gcc`, así que esta línea se convierte en `gcc -o main main.o` cuando se ejecuta.
#    - `-o main`: Este es un argumento que le dice al compilador que el nombre del fichero de salida (el ejecutable que se generará) debe ser `main`. 
#    - `main.o`: Este es el fichero objeto que se va a enlazar. Es el resultado de la compilación de `main.c`. El compilador toma este fichero objeto y lo enlaza para crear el ejecutable final.

# 3. `# Enlaza el objeto para crear el ejecutable`:
#    - Este es un comentario. En un `Makefile`, cualquier texto que siga a un `#` se considera un comentario y no se ejecuta. Aquí se usa para explicar lo que hace la línea anterior, en este caso, que está enlazando el fichero objeto para crear el ejecutable.

# Resumen Completo

# Cuando ejecutas `make programa`, el proceso que sigue es el siguiente:

# 1. Verifica Dependencias: 
#    - Comprueba si `main.o` está actualizado. Si no existe o es más reciente que `programa`, se procede a la siguiente regla para crear `main.o`.

# 2. Compilación:
#    - Una vez que `main.o` está disponible, el comando `$(CC) -o main main.o` se ejecuta. Esto enlaza el fichero objeto `main.o` y crea un ejecutable llamado `main`.

# 3. Resultado:
#    - El resultado final es que tendrás un ejecutable llamado `main` en tu directorio actual.

# Ejemplo Visual

# Imagina que tienes un fichero de código fuente `main.c` que define tu programa. Cuando haces `make`, el flujo es:

# - `main.c` → `main.o` (compilación)
# - `main.o` → `main` (enlazado)