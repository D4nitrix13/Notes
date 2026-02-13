#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from io import TextIOWrapper
from typing import Dict, Optional, Union
from toml import dump, dumps
from sys import stdout, exit
# Creamos un diccionario para ser guardado en formato TOML
data: Dict[str, Dict[str, Union[str, float]]] = {
    "settings": {
        "theme": "dark",
        "version": 1.0
    }
}

# Ejemplo de cómo escribir el diccionario en un fichero TOML
f: Optional[TextIOWrapper] = None
with open(file = r"new_config.toml", mode = "w") as f:
    dump(o = data, f = f)

# Ejemplo de cómo convertir el diccionario a una cadena TOML
tomlString: str = dumps(o = data)
print(tomlString, end="\n", file = stdout)  # Imprimirá el contenido TOML como una cadena
exit(1)