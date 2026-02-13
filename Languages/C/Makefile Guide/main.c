// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// main.c

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
