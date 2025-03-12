#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from typing import Callable, Union
from sys import stdout

def apply(number: Union[int, float], f: Callable[[Union[int, float]], Union[int, float]]) -> Union[int, float]:
    """
    Igual en Python3 se le puede pasar una funcion como argumento
    """
    return f(number)

if __name__ == "__main__":
    """
    funciones anonimas en python solo se pueden de una linea eso tengo entendido no se puede de multiple linea eso tengo entendido
    """
    print(apply(number = 15, f = lambda num: 2 * num),end="\n", file = stdout)