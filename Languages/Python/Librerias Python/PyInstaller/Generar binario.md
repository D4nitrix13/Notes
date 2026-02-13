<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Explicación de cada parte del fichero `.spec` para PyInstaller***

<!-- mypy --install-types -->
<!-- python3 -m pip install types-pyinstaller -->

```python
# -*- mode: python ; coding: utf-8 -*-

# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me
```

```python
# Ruta al Fichero principal del script
scriptPath = "./src/cli/main.py"
```

*Define la ruta al Fichero principal del script que deseas convertir en un ejecutable. En este caso, `main.py` se encuentra en el directorio `./src/cli`.*

```python
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
```

## ***Explicación de la Sección `Analysis`:***

- **`[scriptPath]`:** *Una lista que contiene la ruta al Fichero principal del script. Aquí, se pasa `scriptPath` definido anteriormente.*
- **`pathex=["./src"]`:** *Lista de directorios que se añadirán a la ruta de búsqueda de PyInstaller. Aquí, se incluye el directorio `src`.*
- **`binaries=[]`:** *Lista de Ficheros binarios adicionales que se deben incluir en el ejecutable.*
- **`datas`:** *Lista de tuplas que especifican Ficheros de datos adicionales y sus ubicaciones en el ejecutable. Por ejemplo, `("./src/TemasClaros", "TemasClaros")` significa que el directorio `./src/TemasClaros` se incluirá en el ejecutable en una directorio llamada `TemasClaros`.*
- **`hiddenimports=[]`:** *Lista de módulos que no se detectan automáticamente pero que deben incluirse en el ejecutable.*
- **`hookspath=[]`:** *Lista de directorios que contienen ganchos personalizados.*
- **`hooksconfig={}`:** *Configuración de los ganchos.*
- **`runtime_hooks=[]`:** *Lista de scripts que deben ejecutarse antes del script principal.*
- **`excludes=[]`:** *Lista de módulos que deben excluirse del ejecutable.*
- **`cipher=None`:** *Objeto de cifrado utilizado para cifrar los Ficheros Python en el ejecutable.*
- **`noarchive=False`:** *Si se establece en `True`, no se agruparán los Ficheros Python en un Fichero `.pyz`.*

```python
# Configuración del ensamblaje
pyz = PYZ(a.pure, a.zipped_data, cipher=None)
```

### **Explicación de la Sección `PYZ`:**

- **`a.pure`:** *Ficheros Python puros (sin binarios) analizados en la etapa anterior.*
- **`a.zipped_data`:** *Ficheros comprimidos en un Fichero `.pyz`.*
- **`cipher=None`:** *Cifra utilizada para proteger el contenido del Fichero `.pyz`.*

```python
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
```

### ***Explicación de la Sección `EXE`:***

- **`pyz`:** *Objeto `PYZ` creado en la etapa anterior.*
- **`a.scripts`:** *Lista de scripts a ejecutar.*
- **`a.binaries`:** *Lista de Ficheros binarios a incluir.*
- **`a.zipfiles`:** *Lista de Ficheros zip a incluir.*
- **`a.datas`:** *Lista de Ficheros de datos a incluir.*
- **`name="pycrypy"`:** *Nombre del Fichero ejecutable resultante.*
- **`debug=False`:** *Si se establece en `True`, se incluirá información de depuración en el ejecutable.*
- **`bootloader_ignore_signals=False`:** *Si se establece en `True`, el bootloader ignorará las señales del sistema.*
- **`strip=False`:** *Si se establece en `True`, se eliminarán los símbolos de depuración de los binarios.*
- **`upx=True`:** *Si se establece en `True`, se comprimirán los binarios con UPX.*
- **`console=False`:** *Si se establece en `True`, se abrirá una consola al ejecutar el ejecutable (útil para aplicaciones GUI).*

```python
# Eliminar la configuración de COLLECT
# La configuración anterior crea el ejecutable y maneja los recursos automáticamente.
```

*Esta sección es un comentario indicando que la configuración anterior se encarga de crear el ejecutable y manejar los recursos necesarios. No se utiliza la función `COLLECT` porque los recursos ya están siendo manejados por las configuraciones previas.*

*En resumen, este Fichero de configuración de PyInstaller se encarga de tomar el script principal `main.py` ubicado en `src`, recopilar todos los Ficheros y datos necesarios, y generar un único Fichero ejecutable llamado `pycrypy`.*

---

### ***Para usar PyInstaller desde la línea de comandos y lograr lo mismo que el Fichero de configuración mencionado, puedes ejecutar el siguiente comando en el directorio donde se encuentra la directorio `src`***

```bash
pyinstaller --onefile \
            --noconfirm \
            --clean \
            --noconsole \
            --name pycrypy \
            --paths ./src \
            --add-data "./src/TemasClaros:TemasClaros" \
            --add-data "./src/TemasOscuros:TemasOscuros" \
            --add-data "./src/TemasRecomendados:TemasRecomendados" \
            --add-data "./src/cli:cli" \
            --add-data "./src/config:config" \
            --add-data "./src/lib:lib" \
            ./src/cli/main.py
```

### ***Explicación de cada opción***

- **`--onefile`:** *Crea un solo Fichero ejecutable.*
- **`--noconfirm`:** *No pide confirmación antes de sobrescribir Ficheros.*
- **`--clean`:** *Limpia los Ficheros temporales de compilación.*
- **`--noconsole`:** *No abre una ventana de consola al ejecutar el ejecutable (para aplicaciones GUI). Cambiar a `--console` si necesitas la consola.*
- **`--name pycrypy`:** *Define el nombre del Fichero ejecutable resultante.*
- **`--paths ./src`:** *Añade `./src` a la ruta de búsqueda de PyInstaller.*
- **`--add-data "./src/TemasClaros:TemasClaros"`:** *Incluye la directorio `./src/TemasClaros` en el ejecutable y la mapea a `TemasClaros`.*
- **`--add-data "./src/TemasOscuros:TemasOscuros"`:** *Incluye la directorio `./src/TemasOscuros` en el ejecutable y la mapea a `TemasOscuros`.*
- **`--add-data "./src/TemasRecomendados:TemasRecomendados"`:** *Incluye la directorio `./src/TemasRecomendados` en el ejecutable y la mapea a `TemasRecomendados`.*
- **`--add-data "./src/cli:cli"`:** *Incluye la directorio `./src/cli` en el ejecutable y la mapea a `cli`.*
- **`--add-data "./src/config:config"`:** *Incluye la directorio `./src/config` en el ejecutable y la mapea a `config`.*
- **`--add-data "./src/lib:lib"`:** *Incluye la directorio `./src/lib` en el ejecutable y la mapea a `lib`.*
- **`./src/cli/main.py`:** *Especifica el Fichero principal del script.*

*Este comando debería crear un único Fichero ejecutable que incluya todos los Ficheros de datos y recursos necesarios. Asegúrate de ejecutar este comando desde el directorio que contiene la directorio `./src`.*
