#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from typing import Dict

lista: Dict[str, str] = {
    "Mantenibilidad": "El software debe ser mantenible teniendo en cuenta que el software cambia constantemente que sea facil de mantener y de cambiar",
    
    "Reusabilidad": "El software debe ser reutilizable en diferentes partes del sistema todos los modulos, componentes, clases, etc deben ser reutilizables",

    "Legibilidad": "El software debe ser legible para que sea facil de entender y de mantener que lo entienda cualquier programador con comentarios, nombres de variables, etc",

    "Extensibilidad": "El software debe ser extensible para que sea facil de extender y de mantener sin afectar el funcionamiento del sistema"
}

# SOLID Estos principios se crearon para que el codigo sea mantenible, reutilizable, legible y extensible
solid: Dict[str, str] = {
    "SRP": "Single Responsability Principle",
    "OCP": "Open Closed Principle",
    "LSP": "Liskov Substitution Principle",
    "ISP": "Interface Segregation Principle",
    "DIP": "Dependency Inversion Principle"
}
