<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***`PyInstaller` es una herramienta popular para convertir aplicaciones Python en ejecutables independientes que se pueden ejecutar en sistemas sin necesidad de tener Python instalado. Es útil para distribuir aplicaciones Python como ficheros ejecutables (.exe en Windows, binarios en Linux y macOS) que incluyen todas las dependencias necesarias.***

## ***Instalación de PyInstaller***

***Puedes instalar `PyInstaller` utilizando `pip`:***

```bash
pip install pyinstaller
```

### ***Uso Básico de PyInstaller***

**Para crear un ejecutable a partir de un script Python, usa el siguiente comando:**

```bash
pyinstaller nombre_del_script.py
```

**Esto generará varios ficheros y directorios en el directorio, incluyendo:**

- **`dist/`:** *Contiene el ejecutable generado.*
- **`build/`:** *Contiene ficheros temporales usados durante la construcción.*
- **`nombre_del_script.spec`:** *Fichero de especificación que PyInstaller usa para recordar cómo construyó el ejecutable.*

### ***Opciones Comunes de PyInstaller***

**Aquí hay algunas opciones útiles que puedes usar con `pyinstaller`:**

- **`--onefile`:** *Genera un solo fichero ejecutable en lugar de una directorio con múltiples ficheros.*

    ```bash
    pyinstaller --onefile nombre_del_script.py
    ```

- **`--noconsole`:** *Oculta la consola de comandos (útil para aplicaciones GUI).*

    ```bash
    pyinstaller --onefile --noconsole nombre_del_script.py
    ```

- **`--add-data`:** *Incluye ficheros adicionales o directorios en el ejecutable.*

    ```bash
    pyinstaller --onefile --add-data "SOURCE;DEST" nombre_del_script.py
    ```

    ```bash
    pyinstaller --onefile --add-data "SOURCE:DEST" nombre_del_script.py
    ```

    **Nota:** **En Windows, usa `;` para separar la ruta fuente y destino; en Linux/macOS, usa `:`.**

- **`--icon`:** *Especifica un icono para el ejecutable (solo para Windows).*

    ```bash
    pyinstaller --onefile --icon=icono.ico nombre_del_script.py
    ```

### ***Ejemplo Completo***

*Aquí tienes un ejemplo de cómo usar `PyInstaller` para crear un ejecutable de un script llamado `mi_script.py` que incluye un icono y oculta la consola:*

```bash
pyinstaller --onefile --noconsole --icon=mi_icono.ico mi_script.py
```

### ***Especificación Avanzada con `.spec`***

**`PyInstaller` genera un fichero `.spec` que puedes editar para personalizar el proceso de creación del ejecutable. Aquí hay un ejemplo de cómo se puede usar el fichero `.spec` para personalizar la construcción:**

```python
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

# mi_script.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['mi_script.py'],
    pathex=['/ruta/a/tu/script'],
    binaries=[],
    datas=[('data_folder', 'data_folder')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name='mi_script',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon='mi_icono.ico',
)
```

**Puedes ejecutar el fichero `.spec` con:**

```bash
pyinstaller mi_script.spec
```

### **Errores Comunes y Soluciones**

- **Errores de Importación:** *Si `PyInstaller` no incluye algunas dependencias, puedes agregarlas manualmente usando `--hidden-import` o editando el fichero `.spec`.*

    ```bash
    pyinstaller --onefile --hidden-import=module_name nombre_del_script.py
    ```

- **Ficheros Faltantes:** *Usa `--add-data` para incluir ficheros adicionales necesarios para la ejecución de tu aplicación.*

### ***Documentación y Recursos***

- **[Documentación Oficial de PyInstaller](https://pyinstaller.org/ "https://pyinstaller.org/"):** *Información detallada sobre cómo usar y configurar `PyInstaller`.*
- **[Ejemplos y Tutoriales](https://pyinstaller.org/en/stable/usage.html "https://pyinstaller.org/en/stable/usage.html"):** *Ejemplos prácticos de uso de `PyInstaller`.*

*En resumen, `PyInstaller` es una herramienta poderosa para crear ejecutables a partir de scripts Python, simplificando la distribución de aplicaciones y asegurando que todos los requisitos estén empaquetados en un solo fichero o en una directorio organizada.*
