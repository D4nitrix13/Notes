// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// libcalc.h

#ifndef CALC_H
#define CALC_H true

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
