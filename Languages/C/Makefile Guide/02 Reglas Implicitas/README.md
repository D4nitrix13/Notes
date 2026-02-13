# ***Las reglas implícitas en Makefile son reglas predefinidas que Make utiliza para automatizar el proceso de compilación sin que se tengan que definir explícitamente. Aquí tienes un ejemplo de un Makefile para un proyecto en C que aprovecha las reglas implícitas:***

```makefile
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

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
```

## ***Explicación***

1. **Variables de compilación:**

    ```makefile
    CC = gcc
    CFLAGS = -std=c99 -Wall -Wextra -Werror -pedantic
    LDFLAGS = -lSDL2
    ```

   *Estas variables definen el compilador (`CC`), las opciones de compilación (`CFLAGS`) y las opciones de vinculación (`LDFLAGS`).*

2. **Objetivo por defecto:**

    ```makefile
    all: programa
    ```

   *El objetivo por defecto es `all`, que depende del objetivo `programa`.*

3. **Reglas implícitas:**

    ```makefile
    programa: main.o calc.o
     $(CC) -o programa main.o calc.o $(LDFLAGS)
    ```

   *Esta regla específica enlaza los ficheros objeto `main.o` y `calc.o` para crear el ejecutable `programa`. No es necesario definir cómo compilar los ficheros `.c` a `.o` porque Make tiene reglas implícitas para eso.*

4. **Regla de limpieza:**

    ```makefile
    clean:
     rm -f *.o programa
    ```

   *Esta regla elimina los ficheros objeto y el ejecutable generado.*

5. **Dependencias explícitas:**

    ```makefile
    main.o: main.c libcalc.h
    calc.o: calc.c libcalc.h
    ```

   *Estas reglas indican que `main.o` depende de `main.c` y `libcalc.h`, y `calc.o` depende de `calc.c` y `libcalc.h`. Esto asegura que los ficheros objeto se recompilan si cualquiera de sus dependencias cambia.*

### ***Uso del Makefile***

**Para compilar el proyecto, simplemente ejecuta:**

```bash
make
```

**Para limpiar los ficheros generados, ejecuta:**

```bash
make clean
```

*Este Makefile utiliza reglas implícitas para compilar los ficheros fuente en ficheros objeto y define explícitamente la vinculación de estos ficheros objeto en un ejecutable.*
