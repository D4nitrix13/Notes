// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "10 Input" "10 Input.c"
// Ejecucion: ./"10 Input"
/*
*******************************************
*     Tema: Entrada y Salida de Datos en C *
*     Nivel: Basico                       *
*******************************************
*/

// ***Instrucción del preprocesador*:** Incluye el fichero de cabecera estándar para entrada y salida (stdio.h).
#include <stdio.h>      // stdio.h contiene funciones para operaciones de entrada y salida, como printf y scanf.

// ***Función principal*:** Todo programa en C debe tener una función principal llamada `main`.
int main(void) {
    // Declaración de variables
    int num;
    float num_float;
    double num_double;
    char caracter;
    char cadena[100];

    // Solicitar y leer un número entero
    printf("Ingrese un número entero: ");
    scanf("%d", &num);
    printf("El número ingresado es: %d\n", num);

    // Solicitar y leer un número decimal (float)
    printf("Ingrese un número decimal (float): ");
    scanf("%f", &num_float);
    printf("El número ingresado es: %f\n", num_float);

    // Solicitar y leer un número decimal (double)
    printf("Ingrese un número decimal (double): ");
    scanf("%lf", &num_double);
    printf("El número ingresado es: %lf\n", num_double);

    // Solicitar y leer un carácter
    printf("Ingrese un carácter: ");
    scanf(" %c", &caracter); // Espacio antes de %c para ignorar espacios en blanco
    printf("El carácter ingresado es: %c\n", caracter);

    // Solicitar y leer una cadena de caracteres (sin espacios)
    printf("Ingrese una cadena de caracteres sin espacios: ");
    scanf("%s", cadena); // Lee hasta encontrar un espacio
    printf("La cadena ingresada es: %s\n", cadena);

    // Limpiar el buffer de entrada
    fflush(stdin);

    // Solicitar y leer una cadena de caracteres (incluyendo espacios)
    printf("Ingrese una cadena de caracteres: ");
    fgets(cadena, sizeof(cadena), stdin);
    printf("La cadena ingresada es: %s\n", cadena);

    // Solicitar y leer un solo carácter
    printf("Ingrese un carácter: ");
    caracter = getchar();
    printf("El carácter ingresado es: %c\n", caracter);

    // Limpiar el buffer de entrada
    fflush(stdin);

    // Solicitar y leer una cadena de caracteres (incluyendo espacios) - ADVERTENCIA: Uso de gets, no es seguro
    printf("Ingrese una cadena de caracteres: ");
    gets(cadena); // Advertencia: gets no es seguro, podría causar desbordamiento de búfer
    printf("La cadena ingresada es: %s\n", cadena);
    
    return 0;
}

/*
** Ilustración ASCII de Entrada y Salida de Datos en C :**

1. *Entrada y Salida de Datos en C*:
   +------------------------------------------------------------+
   | int num;                                                   |
   | float num_float;                                           |
   | double num_double;                                         |
   | char caracter;                                             |
   | char cadena[100];                                          |
   |                                                            |
   | printf("Ingrese un número entero: ");                      |
   | scanf("%d", &num);                                         |
   | printf("El número ingresado es: %d\n", num);               |
   |                                                            |
   | printf("Ingrese un número decimal (float): ");             |
   | scanf("%f", &num_float);                                   |
   | printf("El número ingresado es: %f\n", num_float);         |
   |                                                            |
   | printf("Ingrese un número decimal (double): ");            |
   | scanf("%lf", &num_double);                                 |
   | printf("El número ingresado es: %lf\n", num_double);       |
   |                                                            |
   | printf("Ingrese un carácter: ");                           |
   | scanf(" %c", &caracter);                                   |
   | printf("El carácter ingresado es: %c\n", caracter);        |
   |                                                            |
   | printf("Ingrese una cadena de caracteres sin espacios: "); |
   | scanf("%s", cadena);                                       |
   | printf("La cadena ingresada es: %s\n", cadena);            |
   |                                                            |
   | fflush(stdin);                                             |
   | printf("Ingrese una cadena de caracteres: ");              |
   | fgets(cadena, sizeof(cadena), stdin);                      |
   | printf("La cadena ingresada es: %s\n", cadena);            |
   |                                                            |
   | printf("Ingrese un carácter: ");                           |
   | caracter = getchar();                                      |
   | printf("El carácter ingresado es: %c\n", caracter);        |
   |                                                            |
   | fflush(stdin);                                             |
   | printf("Ingrese una cadena de caracteres: ");              |
   | gets(cadena);  // Advertencia: gets no es seguro           |
   | printf("La cadena ingresada es: %s\n", cadena);            |
   +------------------------------------------------------------+
*/

/*
### Buffer y Limpiar el Buffer de Entrada en C

En programación, un **buffer** se refiere a una región de memoria temporal utilizada para almacenar datos mientras se transfieren de un lugar a otro. En el contexto de entrada y salida (I/O) en C:

- **Buffer de Entrada (stdin):** Cuando se lee entrada desde el teclado (stdin) usando funciones como `scanf` o `fgets`, los datos se almacenan temporalmente en un buffer interno antes de ser procesados por el programa. Este buffer permite que el programa maneje eficientemente la entrada y realice operaciones con ella.

- **Limpiar el Buffer de Entrada:** A veces es necesario limpiar o vaciar el buffer de entrada para evitar que datos adicionales (como saltos de línea o caracteres inesperados) interfieran con las próximas operaciones de entrada. Esto es especialmente útil cuando se alternan entre leer diferentes tipos de datos o se desea asegurar que no queden caracteres no deseados en el buffer.

### Uso de `fflush(stdin)` en C

`fflush(stdin)` es una técnica que se utiliza comúnmente para limpiar el buffer de entrada (`stdin`). Sin embargo, es importante destacar que según el estándar de C, `fflush` está destinado a ser utilizado con streams de salida, no con streams de entrada. Por lo tanto, `fflush(stdin)` puede no ser portátil y puede comportarse de manera inconsistente en diferentes sistemas.

**Alternativas Recomendadas:**
- **Para limpiar el buffer de entrada** de manera segura y portátil, se pueden utilizar métodos alternativos como leer y descartar los caracteres no deseados del buffer con un bucle o consumir el buffer hasta el próximo salto de línea después de una lectura.

**Ejemplo de limpieza de buffer de entrada sin `fflush(stdin)`:**

```c
int c;
while ((c = getchar()) != '\n' && c != EOF); // Leer y descartar caracteres hasta encontrar nueva línea o EOF
```

**Conclusión:**
Es recomendable evitar `fflush(stdin)` para limpiar el buffer de entrada debido a su comportamiento no definido según el estándar. En su lugar, se debe manejar cuidadosamente la entrada y descartar los caracteres no deseados de manera explícita y segura para garantizar la consistencia y portabilidad del código.
*/