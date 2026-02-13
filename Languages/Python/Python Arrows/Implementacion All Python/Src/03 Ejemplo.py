#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout
from typing import List

dollars: List[str] = ['32$', '15$', '12$', '17$', '20$']

# Implementacion de todos
print(sum(filter(lambda dollar: dollar >= 20, map(lambda dollar: int(dollar[0:-1:1]), dollars))),end="\n", file = stdout)