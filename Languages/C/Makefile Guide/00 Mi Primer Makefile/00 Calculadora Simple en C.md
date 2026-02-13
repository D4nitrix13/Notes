<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Calculadora Simple en C***

*Este proyecto implementa una calculadora básica en C, dividida en varios ficheros para una estructura modular. Aquí se explica cada fichero y su función en el proyecto.*

## ***ficheros del Proyecto***

### ***`main.c`***

*Este fichero contiene la función principal `main()` que interactúa con el usuario para realizar cálculos básicos utilizando las funciones definidas en `libcalc.h`.*

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include <stdio.h>
#include "libcalc.h"

int main(void)
{
    double num1, num2;
    char op;

    printf("Ingrese operando 1: ");
    scanf("%lf", &num1);
    printf("Ingrese operando 2: ");
    scanf("%lf", &num2);
    printf("Ingrese operador (+, -, *, /): ");
    scanf(" %c", &op);

    switch (op)
    {
    case '+':
        printf("Resultado de la suma: %.2lf\n", sum(num1, num2));
        break;
    case '-':
        printf("Resultado: %.2lf\n", subtract(num1, num2));
        break;
    case '*':
        printf("Resultado: %.2lf\n", multiply(num1, num2));
        break;
    case '/':
        printf("Resultado: %.2lf\n", divide(num1, num2));
        break;
    default:
        printf("Operador no válido.\n");
    }

    return 0;
}
```

### ***`calc.c`***

*En este fichero se encuentran las implementaciones de las funciones de operaciones matemáticas (`sum()`, `subtract()`, `multiply()`, `divide()`) declaradas en `libcalc.h`.*

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#include "libcalc.h"

double sum(double a, double b)
{
    return a + b;
}

double subtract(double a, double b)
{
    return a - b;
}

double multiply(double a, double b)
{
    return a * b;
}

double divide(double a, double b)
{
    if (b != 0)
    {
        return a / b;
    }
    else
    {
        return 0; // Manejo básico de división por cero
    }
}
```

### ***`libcalc.h`***

*Este fichero de cabecera (`libcalc.h`) contiene las declaraciones de las funciones y la estructura de datos utilizadas en el proyecto.*

```c
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

#ifndef CALC_H
#define CALC_H

// Estructura para los operandos de la calculadora
typedef struct {
    double operand1;
    double operand2;
} Operands;

// Funciones declaradas
extern double sum(double a, double b);
extern double subtract(double a, double b);
extern double multiply(double a, double b);
extern double divide(double a, double b);

#endif // CALC_H
```

## ***Compilación y Ejecución***

**Para compilar y ejecutar el proyecto de la calculadora en C utilizando diferentes métodos (directamente con `gcc -o`, con `gcc -c`) aquí tienes los pasos detallados:**

### **Compilar y Ejecutar Utilizando `gcc -o`**

1. **Compilación:**

   **Para compilar directamente con `gcc -o` y generar el ejecutable `programa`:**

   ```bash
   gcc -o programa main.c calc.c
   ```

   **Este comando compila `main.c` y `calc.c` en ficheros objeto y luego los vincula en un ejecutable llamado `programa`.**

2. **Ejecución:**

   **Para ejecutar el programa compilado:**

   ```bash
   ./programa
   ```

### ***Compilar y Vincular con `gcc -c` y luego Vincular Manualmente***

1. **Compilación por Pasos:**

   **Primero, compilamos cada fichero fuente en ficheros objeto separados usando `gcc -c`:**

   ```bash
   gcc -c main.c
   gcc -c calc.c
   ```

   **Esto generará `main.o` y `calc.o`.**

2. **Vinculación:**

   **Luego, vinculamos los ficheros objeto para crear el ejecutable `programa`:**

   ```bash
   gcc -o programa main.o calc.o
   ```

   **Este comando vincula `main.o` y `calc.o` en el ejecutable `programa`.**

3. **Ejecución:**

   **Para ejecutar el programa compilado:**

   ```bash
   ./programa
   ```

- *Con estos métodos, puedes compilar y ejecutar tu proyecto de calculadora en C de manera eficiente y organizada, ya sea manualmente con `gcc`, por pasos con `gcc -c`, o mediante un Makefile para automatizar el proceso.*

## ***Notas Adicionales***

- *Asegúrate de tener el compilador GCC instalado en tu sistema para poder compilar el proyecto.*
