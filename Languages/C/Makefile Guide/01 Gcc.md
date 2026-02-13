<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***En el contexto de compilación con `gcc`, las opciones `-o` y `-c` tienen diferentes propósitos:***

1. **`-o` (Output File):**
   - *Esta opción se utiliza para especificar el nombre del fichero de salida ejecutable o de objeto generado por el compilador.*
   - *Ejemplo: `gcc fichero.c -o programa`*
   - *En este caso, `gcc` compilará `fichero.c` y generará un ejecutable llamado `programa`.*

2. **`-c` (Compile Only):**
   - *Esta opción indica a `gcc` que solo debe compilar el código fuente especificado en ficheros individuales (.c) en ficheros objeto (.o), sin intentar vincularlo en un ejecutable final.*
   - *Ejemplo: `gcc fichero.c -c`*
   - *Esto compila `fichero.c` y produce `fichero.o` como salida. No se genera un ejecutable final.*

## ***Diferencias Clave***

- **`-o`** *se utiliza para especificar el nombre del fichero de salida final generado por el compilador, ya sea un ejecutable o una biblioteca estática.*
- **`-c`** *se utiliza para compilar individualmente ficheros fuente (.c) en ficheros objeto (.o) sin vincularlos, permitiendo la creación posterior de un ejecutable combinando varios ficheros objeto.*

### ***Uso Combinado***

- *Si estás compilando un único fichero y deseas generar un ejecutable directamente, usarías `-o` para especificar el nombre del ejecutable.*
- *Si estás compilando varios ficheros y luego deseas vincularlos juntos para formar un ejecutable final, primero usarías `-c` para cada fichero individual y luego usarías `-o` para especificar el nombre del ejecutable final junto con los ficheros objeto generados.*

*En resumen, `-o` se usa para especificar el nombre del fichero de salida (ejecutable o biblioteca), mientras que `-c` se usa para compilar ficheros individuales en ficheros objeto sin vincularlos en un ejecutable final.*
