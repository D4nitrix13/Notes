#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me 

"""
El polimorfismo de coerción, también conocido como polimorfismo ad hoc o polimorfismo de sobrecarga de operadores, es un tipo de polimorfismo donde los operadores o funciones pueden tener diferentes comportamientos dependiendo del tipo de sus argumentos.
"""


from sys import stdout

def main() -> None:
    num1: int = 5
    num2: float = 6.5
    print(f"Type: {type(num1)}",end="\n", file = stdout)
    print(f"Type: {type(num2)}",end="\n", file = stdout)

    resultado: float = num1 + num2
    print(resultado,end="\n", file = stdout)
    print(f"Type: {type(resultado)}",end="\n", file = stdout)
    # En este caso resultado es un float porque el operador + esta sobrecargado para que cuando se le pase un int y un float el resultado sea un float
    return None


if __name__ == "__main__":
    main()
