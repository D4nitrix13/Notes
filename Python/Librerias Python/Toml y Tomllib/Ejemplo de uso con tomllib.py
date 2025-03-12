#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# Importamos el módulo tomllib que está disponible en Python `3.11` y versiones posteriores
from io import BufferedReader
from sys import stdout
from tomllib import load # type: ignore
from typing import Any, Dict, Optional

# Ejemplo de cómo cargar un fichero TOML
# Supongamos que tenemos un fichero llamado 'config.toml' con el siguiente contenido:
# [settings]
# theme = "dark"
# version = 1.0

# Abrimos y leemos el fichero TOML
f: Optional[BufferedReader] = None

with open(file = r'config.toml', mode = 'rb') as f:
    # Usamos tomllib.load para cargar el contenido del fichero en un diccionario
    config: Dict[str, Any] = load(f)

# Imprimimos el contenido cargado
print(config, end = "\n", file = stdout)

# Ejemplo de cómo acceder a los datos cargados
print(config['settings']['theme'], end = "\n", file = stdout)  # Debería imprimir 'dark'

# Output
# {'settings': {'theme': 'dark', 'version': 1.0}}
exit(0)
