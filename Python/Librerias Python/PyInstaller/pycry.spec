# -*- mode: python ; coding: utf-8 -*-

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# Ruta al Fichero principal del script
scriptPath = "./src/cli/main.py"

# Crea la variable de análisis
a = Analysis([scriptPath],
    pathex=["./src"],
    binaries=[],
    datas=[
        ("./src/TemasClaros", "TemasClaros"),
        ("./src/TemasOscuros", "TemasOscuros"),
        ("./src/TemasRecomendados", "TemasRecomendados"),
        ("./src/cli", "cli"),
        ("./src/config", "config"),
        ("./src/lib", "lib"),
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    cipher=None,
    noarchive=False
)

# Configuración del ensamblaje
pyz = PYZ(a.pure, a.zipped_data, cipher=None)

# Configuración del ejecutable
exe = EXE(pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="pycrypy",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False
)  # Cambiar a True si necesitas la consola

# Eliminar la configuración de COLLECT
# La configuración anterior crea el ejecutable y maneja los recursos automáticamente.
