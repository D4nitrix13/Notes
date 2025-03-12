<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->
# ***Pasos para compilar el ejemplo que te proporcioné***

1. *Guarda el código en dos ficheros separados, uno para cada fichero fuente:*

    `main.c`:

    ```c
    // Autor: Daniel Benjamin Perez Morales
    // GitHub: https://github.com/D4nitrix13
    // Correo electrónico: danielperezdev@proton.me
    #include <stdio.h>

    extern int variable_externa;

    int main(void) {
        printf("El valor de la variable externa es: %d\n", variable_externa);
        return 0;
    }
    ```

    `extern.c`:

    ```c
    int variable_externa = 42;
    ```

2. *Abre una terminal en el directorio donde guardaste los ficheros.*

3. *Compila ambos ficheros fuente usando un comando de compilación:*

    ```bash
    gcc -o programa main.c extern.c 
    ```

    *Este comando le dice al compilador GCC que compile ambos ficheros fuente y los enlace en un programa llamado `programa`. `-o programa` especifica el nombre del fichero de salida.*

4. *Si no hay errores, se generará un fichero ejecutable llamado `programa` en el mismo directorio.*

5. *Ejecuta el programa:*

```bash
./programa
```

*Esto imprimirá el valor de la variable externa en la consola. En este caso, el resultado será:*

```txt
El valor de la variable externa es: 42
```
