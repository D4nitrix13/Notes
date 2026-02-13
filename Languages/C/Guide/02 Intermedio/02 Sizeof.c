// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "02 Sizeof" "02 Sizeof.c"
// Ejecucion: ./"02 Sizeof"

#include <stdio.h>

int main(void)
{
    // Declaración de variables de diferentes tipos
    int entero;
    char caracter;
    float flotante;
    double doble;

    // Declaración de arreglos unidimensionales
    int arregloEnteros[10];
    char cadena[] = "Hola";
    float arregloFlotantes[5];
    double arregloDobles[3];

    // Declaración de arreglos bidimensionales
    int matrizEnteros[3][3];
    char matrizCaracteres[2][5] = {{'H', 'o', 'l', 'a', '\0'}, {'M', 'u', 'n', 'd', 'o'}};
    float matrizFlotantes[2][2];
    double matrizDobles[4][4];

    // Uso de sizeof para obtener tamaños
    printf("Tamaño de un entero: %zu bytes\n", sizeof(entero));
    printf("Tamaño de un caracter: %zu bytes\n", sizeof(caracter));
    printf("Tamaño de un flotante: %zu bytes\n", sizeof(flotante));
    printf("Tamaño de un doble: %zu bytes\n", sizeof(doble));

    printf("Tamaño de un arreglo unidimensional de enteros (10 elementos): %zu bytes\n", sizeof(arregloEnteros));
    printf("Tamaño de una cadena de caracteres (incluyendo el carácter nulo): %zu bytes\n", sizeof(cadena));
    printf("Tamaño de un arreglo unidimensional de flotantes (5 elementos): %zu bytes\n", sizeof(arregloFlotantes));
    printf("Tamaño de un arreglo unidimensional de dobles (3 elementos): %zu bytes\n", sizeof(arregloDobles));

    printf("Tamaño de un arreglo bidimensional de enteros (3x3 elementos): %zu bytes\n", sizeof(matrizEnteros));
    printf("Tamaño de un arreglo bidimensional de caracteres (2x5 elementos): %zu bytes\n", sizeof(matrizCaracteres));
    printf("Tamaño de un arreglo bidimensional de flotantes (2x2 elementos): %zu bytes\n", sizeof(matrizFlotantes));
    printf("Tamaño de un arreglo bidimensional de dobles (4x4 elementos): %zu bytes\n", sizeof(matrizDobles));

    return 0;
}

/*
sizeof es un operador que devuelve el tamaño en bytes del tipo de dato o variable.
Se utiliza sizeof para determinar y mostrar el tamaño en bytes de cada tipo de dato y arreglo.

sizeof es un operador en C que calcula el tamaño en bytes del tipo de dato, variable o expresión dada. Es evaluado en tiempo de compilación.

Funcionamiento a Bajo Nivel:
Internamente, sizeof consulta el tipo de dato en la tabla de tipos del compilador y devuelve el número de bytes requeridos para almacenar el tipo especificado.
*/

/*
Claro, vamos a explicar cada uno de los tamaños de los tipos de datos y arreglos en C, y por qué se calculan de esa manera.

### Tipos de Datos en C

1. **Entero (`int`):**
   ```c
   int entero;
   ```
   - Tamaño: 4 bytes.
   - Los enteros en la mayoría de las arquitecturas modernas de 32 y 64 bits suelen ocupar 4 bytes (32 bits).

2. **Caracter (`char`):**
   ```c
   char caracter;
   ```
   - Tamaño: 1 byte.
   - Un carácter en C ocupa 1 byte (8 bits), que es suficiente para almacenar cualquier valor de un carácter ASCII.

3. **Flotante (`float`):**
   ```c
   float flotante;
   ```
   - Tamaño: 4 bytes.
   - Un número flotante en C suele ocupar 4 bytes (32 bits), siguiendo el estándar IEEE 754.

4. **Doble (`double`):**
   ```c
   double doble;
   ```
   - Tamaño: 8 bytes.
   - Un número doble en C ocupa 8 bytes (64 bits), también siguiendo el estándar IEEE 754.

### Arreglos Unidimensionales

1. **Arreglo de Enteros:**
   ```c
   int arregloEnteros[10];
   ```
   - Tamaño: 10 elementos * 4 bytes = 40 bytes.

2. **Cadena de Caracteres:**
   ```c
   char cadena[] = "Hola";
   ```
   - Tamaño: 5 bytes (4 caracteres + 1 byte para el carácter nulo `\0`).

3. **Arreglo de Flotantes:**
   ```c
   float arregloFlotantes[5];
   ```
   - Tamaño: 5 elementos * 4 bytes = 20 bytes.

4. **Arreglo de Dobles:**
   ```c
   double arregloDobles[3];
   ```
   - Tamaño: 3 elementos * 8 bytes = 24 bytes.

### Arreglos Bidimensionales

1. **Arreglo Bidimensional de Enteros (3x3):**
   ```c
   int matrizEnteros[3][3];
   ```
   - Tamaño: 3 * 3 elementos * 4 bytes = 36 bytes.
   - Cada elemento del arreglo bidimensional es un entero, y hay 9 elementos en total (3 filas * 3 columnas).

2. **Arreglo Bidimensional de Caracteres (2x5):**
   ```c
   char matrizCaracteres[2][5];
   ```
   - Tamaño: 2 * 5 elementos * 1 byte = 10 bytes.
   - Cada elemento es un carácter, y hay 10 elementos en total (2 filas * 5 columnas).

3. **Arreglo Bidimensional de Flotantes (2x2):**
   ```c
   float matrizFlotantes[2][2];
   ```
   - Tamaño: 2 * 2 elementos * 4 bytes = 16 bytes.
   - Cada elemento es un flotante, y hay 4 elementos en total (2 filas * 2 columnas).

4. **Arreglo Bidimensional de Dobles (4x4):**
   ```c
   double matrizDobles[4][4];
   ```
   - Tamaño: 4 * 4 elementos * 8 bytes = 128 bytes.
   - Cada elemento es un doble, y hay 16 elementos en total (4 filas * 4 columnas).

### Explicación de `sizeof` a Bajo Nivel

- **Qué es `sizeof`:**
  `sizeof` es un operador en C que calcula el tamaño en bytes del tipo de dato, variable o expresión dada. Es evaluado en tiempo de compilación, no en tiempo de ejecución.

- **Funcionamiento a Bajo Nivel:**
  Internamente, `sizeof` consulta el tipo de dato en la tabla de tipos del compilador y devuelve el número de bytes requeridos para almacenar el tipo especificado. Esto incluye la suma de los tamaños de todos los elementos en caso de arreglos.

### Ejemplo Visual de Arreglo Bidimensional

- **Arreglo Bidimensional de Enteros (3x3):**
  ```c
  int matrizEnteros[3][3];
  ```
  - Visualización:
    ```plaintext
    [ [ 0, 1, 2 ],
      [ 3, 4, 5 ],
      [ 6, 7, 8 ] ]
    ```
  - Cada entero ocupa 4 bytes.
  - Total de elementos: 3 filas * 3 columnas = 9 elementos.
  - Tamaño total: 9 elementos * 4 bytes = 36 bytes.

Este mismo cálculo se aplica a otros arreglos bidimensionales, simplemente ajustando el tamaño del tipo de dato y el número de elementos en el arreglo.

### Resumen de Tamaños

- **Entero:** 4 bytes.
- **Caracter:** 1 byte.
- **Flotante:** 4 bytes.
- **Doble:** 8 bytes.
- **Arreglo Unidimensional de Enteros (10 elementos):** 40 bytes.
- **Cadena de Caracteres ("Hola"):** 5 bytes (incluyendo `\0`).
- **Arreglo Unidimensional de Flotantes (5 elementos):** 20 bytes.
- **Arreglo Unidimensional de Dobles (3 elementos):** 24 bytes.
- **Arreglo Bidimensional de Enteros (3x3):** 36 bytes.
- **Arreglo Bidimensional de Caracteres (2x5):** 10 bytes.
- **Arreglo Bidimensional de Flotantes (2x2):** 16 bytes.
- **Arreglo Bidimensional de Dobles (4x4):** 128 bytes.

Espero que esta explicación haya sido clara y útil para comprender cómo se calculan los tamaños de diferentes tipos de datos y arreglos en C.
*/