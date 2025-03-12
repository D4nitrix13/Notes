#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# Importamos el módulo toml
from sys import stdout, exit
from typing import Any, Dict
from toml import load

# Ejemplo de cómo cargar un fichero TOML
# Supongamos que tenemos un fichero llamado 'config.toml' con el siguiente contenido:
# [settings]
# theme = "dark"
# version = 1.0

# Abrimos y leemos el fichero TOML
config: Dict[str, Any] = load(f = r"config.toml")

# Imprimimos el contenido cargado
print(config, end = "\n", file = stdout)
# Output
# {'settings': {'theme': 'dark', 'version': 1.0}}

# Ejemplo de cómo acceder a los datos cargados
print(config['settings']['theme'], end = "\n", file = stdout)  # Debería imprimir 'dark'
exit(1)