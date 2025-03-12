// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Compilacion: gcc -o "00 Matematicas" "00 Matematicas.c" -lm
// Ejecucion: ./"00 Matematicas"
/*
La opción `-lm` en el comando de compilación con `gcc` se utiliza para indicar que se debe enlazar la biblioteca matemática estándar, `libm`. Aquí tienes una explicación detallada:

### Qué hace la opción `-lm`

Cuando se compila un programa en C que utiliza funciones matemáticas avanzadas, como las que se encuentran en el fichero `<math.h>`, el compilador necesita enlazar la biblioteca matemática estándar (`libm`). Esta biblioteca contiene implementaciones de funciones matemáticas como `sqrt`, `exp`, `log`, `log10`, `fmax`, `fmin`, entre otras.

### Significado de `-lm`

- `-l` es una opción del compilador que indica que se debe enlazar una biblioteca.
- `m` es el nombre de la biblioteca matemática estándar.

En conjunto, `-lm` le dice al compilador que debe buscar y enlazar la biblioteca `libm` durante el proceso de enlace (linking).

### Ejemplo del proceso de compilación

Cuando se compila y enlaza un programa en C que utiliza funciones de `math.h`, se siguen generalmente dos pasos:

1. **Compilación:** El código fuente de C se convierte en código objeto (fichero `.o`).
2. **Enlace:** El código objeto se enlaza con las bibliotecas necesarias para crear el ejecutable final.

Durante el segundo paso, si el programa utiliza funciones matemáticas, se debe incluir la biblioteca `libm`. Si no se especifica `-lm`, el enlazador no encontrará las definiciones de las funciones matemáticas, lo que resulta en errores de referencia indefinida.

*/
#include <stdio.h>
#include <math.h>

int main(void)
{
    // Función para calcular el valor absoluto de un número
    double numero = -5.5;
    double valorAbsoluto = fabs(numero);
    printf("Valor absoluto de %.2f: %.2f\n", numero, valorAbsoluto);

    // Función para calcular la raíz cuadrada de un número
    double radicando = 25.0;
    double raizCuadrada = sqrt(radicando);
    printf("Raíz cuadrada de %.2f: %.2f\n", radicando, raizCuadrada);

    // Función para calcular el valor de e elevado a la potencia x
    double x = 2.0;
    double exponencial = exp(x);
    printf("e elevado a %.2f: %.2f\n", x, exponencial);

    // Función para calcular el logaritmo natural de un número
    double logaritmoNatural = log(x);
    printf("Logaritmo natural de %.2f: %.2f\n", x, logaritmoNatural);

    // Función para calcular el logaritmo en base 10 de un número
    double logaritmoBase10 = log10(x);
    printf("Logaritmo base 10 de %.2f: %.2f\n", x, logaritmoBase10);

    // Función para calcular el valor máximo entre dos números
    double numero1 = 10.5, numero2 = 20.7;
    double maximo = fmax(numero1, numero2);
    printf("El máximo entre %.2f y %.2f es: %.2f\n", numero1, numero2, maximo);

    // Función para calcular el valor mínimo entre dos números
    double minimo = fmin(numero1, numero2);
    printf("El mínimo entre %.2f y %.2f es: %.2f\n", numero1, numero2, minimo);

    return 0;
}

/*
*Este código muestra cómo usar algunas de las funciones matemáticas más comunes disponibles en C a través de la biblioteca `math.h`. Las funciones incluidas son:*

- **`fabs()`:** *Calcula el valor absoluto de un número.*

- **`sqrt()`:** *Calcula la raíz cuadrada de un número.*

- **`exp()`:** *Calcula el valor de e elevado a la potencia x.*

- **`log()`:** *Calcula el logaritmo natural de un número.*

- **`log10()`:** *Calcula el logaritmo en base 10 de un número.*

- **`fmax()`:** *Calcula el valor máximo entre dos números.*

- **`fmin()`:** *Calcula el valor mínimo entre dos números.*

*Estas son solo algunas de las funciones matemáticas disponibles en C; la biblioteca `math.h` ofrece muchas más para realizar una variedad de operaciones matemáticas.*
*/