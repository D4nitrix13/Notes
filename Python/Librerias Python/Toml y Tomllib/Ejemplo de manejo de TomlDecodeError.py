#!/usr/bin/env python3

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stderr, exit, stdout
from typing import Any, Dict
from toml import load
from toml.decoder import TomlDecodeError

try:
    # Intentamos cargar un fichero TOML malformado
    config: Dict[str, Any] = load(f = r"malformed_config.toml")
except TomlDecodeError as e:
    # Capturamos y mostramos el error de decodificación
    print(f'Error al decodificar el fichero TOML: {e}', end = "\n", file = stderr)
    exit(1)

print(config, end = "\n", file = stdout)
exit(0)
