# ***Patrones y Variables Automáticas en Makefile***

*Las reglas de patrones y las variables automáticas son características poderosas de Make que permiten escribir Makefiles más concisos y flexibles. Aquí tienes ejemplos que cubren patrones y variables automáticas.*

## ***Patrones***

1. **Cualquier fichero que termine en `.o`:**

    ```makefile
    # Regla para compilar cualquier fichero .c en un fichero .o con el mismo nombre base
    %.o: %.c
        gcc -c $(CFLAGS) -o $@ $<
    ```

2. **Ficheros en un subdirectorio:**

    ```makefile
    # Regla para compilar ficheros .c en el directorio 'Directory' a ficheros .o en el mismo directorio
    Directory/%.o: Directory/%.c
        gcc -c $(CFLAGS) -o $@ $<
    ```

## ***Variables Automáticas***

1. **Nombre del primer fichero de dependencia (`$<`):**

    ```makefile
    # Regla que utiliza $< para referirse al primer fichero de dependencia
    %.o: %.c
        @echo "Compilando $< a $@"
        gcc -c $(CFLAGS) -o $@ $<
    ```

2. **Lista de todos los ficheros modificados (`$?`):**

    ```makefile
    # Regla que muestra la lista de todos los ficheros modificados desde la última compilación
    programa: main.o calc.o
        @echo "Ficheros modificados: $?"
        gcc -o $@ $^
    ```

    *En un Makefile, la variable automática `$^` se utiliza para representar la lista completa de dependencias de una regla, excluyendo duplicados. Es muy útil cuando necesitas pasar todas las dependencias a un comando, como al enlazar ficheros objeto para crear un ejecutable.*

3. **Nombre del objetivo (`$@`):**

    ```makefile
    # Regla que utiliza $@ para referirse al nombre del fichero objetivo
    programa: main.o calc.o
        @echo "Creando el ejecutable: $@"
        gcc -o $@ $^
    ```

### ***Makefile Completo con Ejemplos***

**Aquí tienes un Makefile completo que utiliza patrones y variables automáticas:**

```makefile
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# objetivo: dependencias
# instrucciones

# Enlaces: https://www.gnu.org/software/make/
# Enlaces: https://www.gnu.org/software/make/manual/html_node/index.html

# Makefile con patrones y variables automáticas

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
```

### ***Explicación***

1. **Patrones:**
   - `%.o: %.c` *compila cualquier fichero `.c` en un fichero `.o` correspondiente.*
   - `Directory/%.o: Directory/%.c` *hace lo mismo pero en el subdirectorio `Directory`.*

2. **Variables Automáticas:**
   - *`$<` se refiere al primer fichero de dependencia.*
   - *`$?` lista todos los ficheros que han sido modificados desde la última compilación.*
   - *`$@` se refiere al nombre del fichero objetivo.*

### ***Uso del Makefile***

*Para compilar el proyecto, simplemente ejecuta:*

```bash
make
```

*Para limpiar los ficheros generados, ejecuta:*

```bash
make clean
```

*Este Makefile utiliza patrones para compilar ficheros `.c` en ficheros `.o` y aprovecha las variables automáticas para hacer el Makefile más dinámico y eficiente.*
