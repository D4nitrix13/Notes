# ***Explicación detallada del Makefile***

## ***Explicación del Makefile***

```makefile
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# objetivo: dependencias
# instrucciones

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
```

### ***Explicación detallada***

1. **`all: programa`:**
   - *Define el objetivo principal del Makefile como `all`, que depende de `programa`.*
   - *Esto significa que al ejecutar `make all` o simplemente `make`, se construirá el `programa`.*

2. **`programa: main.o calc.o`:**
   - *Define la regla para construir el ejecutable `programa`.*
   - *Depende de `main.o` y `calc.o`, lo que significa que antes de ejecutar esta regla, Make verificará si `main.o` y `calc.o` están actualizados.*

3. **`main.o: main.c libcalc.h`** y **`calc.o: calc.c libcalc.h`:**
   - *Son reglas individuales para compilar `main.c` y `calc.c` respectivamente.*
   - *Cada una depende de su fichero fuente correspondiente (`main.c` y `calc.c`) y del fichero de cabecera `libcalc.h`.*
   - *Utilizan `gcc -c` para compilar los ficheros fuente en ficheros objeto (`main.o` y `calc.o`) sin intentar vincularlos en un ejecutable final.*

4. **`clean:`:**
   - *Define una regla para limpiar el directorio.*
   - *`rm -f *.o programa` elimina todos los ficheros objeto (`*.o`) y el ejecutable `programa`.*
   - *Esta regla es útil para mantener el directorio limpio de ficheros generados durante el proceso de compilación.*

### ***Uso del Makefile***

- **Compilar el programa:** *Ejecuta `make` para compilar `main.c` y `calc.c`, generar los ficheros objeto y construir el ejecutable `programa`.*
  
  ```bash
  make
  ```

- **Limpiar el directorio:** *Ejecuta `make clean` para eliminar todos los ficheros objeto y el ejecutable generado.*
  
  ```bash
  make clean
  ```

*Este Makefile te permite manejar eficientemente la compilación de tu programa de calculadora, asegurando que solo se recompilen los ficheros que han cambiado y facilitando la limpieza del entorno después de la compilación. Los enlaces proporcionados dirigen a recursos adicionales sobre GNU Make para más detalles y opciones avanzadas.*
