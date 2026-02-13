<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***`mypy` es una herramienta de verificación de tipos para Python que ayuda a detectar errores en tiempo de desarrollo al analizar el código con base en las anotaciones de tipo. A continuación, te explico cómo instalar, configurar y usar `mypy`, así como algunos conceptos clave relacionados.***

> [!NOTE]
> **[Recurso](https://mypy.readthedocs.io/en/stable/getting_started.html "https://mypy.readthedocs.io/en/stable/getting_started.html")**

## ***Instalación de `mypy`***

**Puedes instalar `mypy` utilizando `pip`, el gestor de paquetes para Python. Aquí está el comando para hacerlo:**

```bash
pip install mypy
```

```bash
mypy --version
mypy 1.10.0 (compiled: yes)
```

### ***Configuración de `mypy`***

```bash
touch pyproject.toml
```

```bash
touch mypy.ini
```

**`mypy` puede ser configurado a través de un fichero de configuración llamado `mypy.ini` o `pyproject.toml`. Aquí tienes un ejemplo básico de configuración en un fichero `mypy.ini`:**

```ini
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

[mypy]
# Ignorar módulos sin información de tipos
ignore_missing_imports = True

# Establecer el nivel de severidad para errores de tipo
disallow_untyped_calls = True
disallow_untyped_defs = True
```

**Y aquí un ejemplo en `pyproject.toml`:**

```toml
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

[tool.mypy]
ignore_missing_imports = true
disallow_untyped_calls = true
disallow_untyped_defs = true
```

### ***Uso Básico de `mypy`***

**Para verificar un fichero Python con `mypy`, simplemente ejecuta:**

```bash
mypy nombre_del_fichero.py
```

### ***Ejemplos de Análisis de Tipo con `mypy`***

#### ***1. Código con Tipos Anotados***

```python
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from sys import stdout, exit
def greet(*, name: str) -> str:
    return f"Hello, {name}"

# Llamada correcta
print(greet(name = "Danna"), end = "\n", file = stdout)
exit(0)

# Llamada incorrecta que generará un error en `mypy`
# print(greet(name = 123), end = "\n", file = stdout)  # Error: Argument 1 to "greet" has incompatible type "int"; expected "str"
```

#### ***2. Uso de `# type: ignore`***

**Si `mypy` lanza un error que deseas ignorar, puedes usar `# type: ignore` en la línea problemática:**

```python
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from colored import fore  # type: ignore
```

#### ***3. Configuración Avanzada***

**Puedes especificar reglas adicionales, como evitar el uso de tipos no anotados, configurando `mypy` en `mypy.ini` o `pyproject.toml`.**

**Ejemplo en `mypy.ini`:**

```ini
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

[mypy]
disallow_untyped_calls = True
disallow_untyped_defs = True
```

**Ejemplo en `pyproject.toml`:**

```toml
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

[tool.mypy]
disallow_untyped_calls = true
disallow_untyped_defs = true
```

### ***Errores Comunes y Cómo Solucionarlos***

#### ***1. Módulos Sin Información de Tipos***

**Si `mypy` no puede encontrar información de tipos para un módulo, puedes recibir un error como:**

```bash
error: Skipping analyzing "module_name": module is installed, but missing library stubs or py.typed marker
```

**En este caso, puedes usar `# type: ignore` para suprimir el error, o configurar `mypy` para ignorar módulos sin tipos.**

#### ***2. Errores de Tipo en las Anotaciones***

**Si `mypy` encuentra un error en las anotaciones de tipo, verifica que todos los tipos especificados sean correctos y consistentes.**

```python
def add(* , a: int, b: int) -> int:
    return a + b

# Error si se pasa un tipo incorrecto
# add(a = "a", b = "b")  # Error: Argument 1 to "add" has incompatible type "str"; expected "int"
```

> [!IMPORTAN]
> *El comando `mypy --install-types` se utiliza para instalar automáticamente las dependencias de tipo requeridas por los módulos que estás usando en tu código Python. Esto es especialmente útil cuando estás trabajando con módulos que no tienen información de tipos incorporada y quieres asegurarte de que `mypy` pueda realizar una verificación de tipos completa.*

### ***¿Qué Hace el Comando?***

1. **Instalación de Stubs de Tipos:** *`mypy` puede utilizar ficheros de tipos (conocidos como "type stubs") para proporcionar información de tipos para módulos que no tienen anotaciones de tipo nativas. Estos ficheros tienen la extensión `.pyi` y permiten a `mypy` realizar una verificación de tipos para módulos de terceros.*

2. **Automatización:** *Al ejecutar `mypy --install-types`, `mypy` verificará los módulos importados en tu código y, si detecta que algún módulo necesita ficheros de tipos adicionales que no están instalados, intentará instalar esos ficheros automáticamente.*

### ***¿Cómo Funciona?***

- **Verifica el Código:** *`mypy` analiza el código fuente de tu proyecto para identificar módulos que no tienen información de tipos o que podrían necesitar ficheros de tipos adicionales.*

- **Consulta y Descarga:** *Si `mypy` encuentra módulos que necesitan información de tipos y hay paquetes disponibles para esos módulos, descargará e instalará estos paquetes automáticamente desde el índice de paquetes de Python (PyPI).*

### ***Ejemplo de Uso***

*Supón que tienes un proyecto con dependencias externas que no tienen anotaciones de tipo, como una biblioteca que usas pero para la cual no tienes stubs instalados. Para asegurarte de que `mypy` pueda analizar estas dependencias correctamente, ejecutarías:*

```bash
mypy --install-types
```

### ***Beneficios***

- **Facilita la Configuración:** *Instalar automáticamente los stubs de tipos necesarios asegura que tu entorno de desarrollo esté completamente configurado para la verificación de tipos sin tener que buscar e instalar manualmente cada paquete adicional.*

- **Mejora la Verificación de Tipos:** *Tener información de tipos para todos los módulos utilizados ayuda a `mypy` a detectar posibles errores de tipo y proporciona una verificación más exhaustiva.*

### ***Consideraciones***

- **Compatibilidad:** *No todos los módulos tienen stubs de tipos disponibles. En algunos casos, es posible que necesites proporcionar tus propias anotaciones de tipo o usar `# type: ignore` para suprimir errores específicos.*

- **Dependencias Adicionales:** *Asegúrate de que tu entorno de Python tenga acceso a internet para descargar e instalar los paquetes necesarios.*

### ***Documentación y Recursos***

- **[Documentación Oficial de `mypy`](https://mypy.readthedocs.io/en/stable/ "https://mypy.readthedocs.io/en/stable/"):** *Información detallada sobre cómo usar y configurar `mypy`.*

- **[mypy – Install Types](https://mypy.readthedocs.io/en/stable/running_mypy.html#installing-types "https://mypy.readthedocs.io/en/stable/running_mypy.html#installing-types"):** Sección específica sobre cómo usar `mypy --install-types`.

**En resumen, `mypy --install-types` automatiza la instalación de stubs de tipos para módulos de terceros, lo que ayuda a asegurar que la verificación de tipos de `mypy` sea lo más completa posible.**

- **[PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/ "https://www.python.org/dev/peps/pep-0484/"):** *La propuesta que introdujo las anotaciones de tipo en Python.*

**En resumen, `mypy` es una herramienta poderosa para la verificación estática de tipos en Python. Ayuda a detectar errores en el código al analizar las anotaciones de tipo, y se puede configurar para adaptarse a las necesidades específicas del proyecto.**
