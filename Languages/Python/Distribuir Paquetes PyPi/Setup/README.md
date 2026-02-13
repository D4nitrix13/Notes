<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Setup.py***

```python
# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# Gitlab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from io import TextIOWrapper

from setuptools import find_packages, setup

f: TextIOWrapper

with open(file=r"README.md", mode="r", encoding="utf-8") as f:
    README: str = f.read()

setup(
    name="pycrypy",
    version="1.0.0.dev0",
    author="Daniel Benjamin Perez Morales",
    author_email="danielperezdev@proton.me",
    description="This utility, developed in Python3, significantly simplifies the configuration process of Alacritty, allowing easy adjustments to font, theme, padding, cursors, and font styles.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/D4nitrix13/pycrypy.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # Indicates that packages are in "src"
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
    ],
    keywords="alacritty",
    python_requires=">=3.6",
    install_requires=[
        "altgraph >= 0.17.4",
        "certifi >= 2025.1.31",
        "cffi >= 1.17.1",
        "charset-normalizer >= 3.4.1",
        "colored >= 2.3.0",
        "cryptography >= 44.0.2",
        "docutils >= 0.21.2",
        "id >= 1.5.0",
        "idna >= 3.10",
        "jaraco.classes >= 3.4.0",
        "jaraco.context >= 6.0.1",
        "jaraco.functools >= 4.1.0",
        "jeepney >= 0.9.0",
        "keyring >= 25.6.0",
        "markdown-it-py >= 3.0.0",
        "mdurl >= 0.1.2",
        "more-itertools >= 10.6.0",
        "mypy >= 1.15.0",
        "mypy-extensions >= 1.0.0",
        "nh3 >= 0.2.21",
        "packaging >= 24.2",
        "prettytable >= 3.16.0",
        "pycparser >= 2.22",
        "Pygments >= 2.19.1",
        "pyinstaller >= 6.12.0",
        "pyinstaller-hooks-contrib >= 2025.2",
        "readme_renderer >= 44.0",
        "requests >= 2.32.3",
        "requests-toolbelt >= 1.0.0",
        "rfc3986 >= 2.0.0",
        "rich >= 14.0.0",
        "SecretStorage >= 3.3.3",
        "setuptools >= 78.1.0",
        "toml >= 0.10.2",
        "twine >= 6.1.0",
        "types-toml >= 0.10.8.20240310",
        "typing_extensions >= 4.13.2",
        "urllib3 >= 2.4.0",
        "wcwidth >= 0.2.13",
    ],
    include_package_data=True,
    entry_points=dict(console_scripts=["pycrypy = cli.main:main"]),
)
```

## ***1. Importaciones***

```python
from setuptools import setup, find_packages
from io import TextIOWrapper
```

### ***`from setuptools import setup, find_packages`***

`setuptools` *es una biblioteca que facilita la creación, distribución y gestión de paquetes Python. Importa dos funciones:*

- **`setup()`:** *Esta función es el corazón del fichero `setup.py`. Se usa para definir las metainformaciones y configuraciones del paquete.*
- **`find_packages()`:** *Esta función busca y devuelve una lista de paquetes en el proyecto, ayudando a incluir automáticamente todos los paquetes que están en el directorio especificado (generalmente `src`).*

#### ***`from io import TextIOWrapper`***

- *`TextIOWrapper` es una clase del módulo `io` que se usa para manejar ficheros de texto. En este contexto, se utiliza para indicar el tipo de la variable `f`, que se usa para leer el fichero `README.md`.*

### ***2. Abrir y Leer el Fichero `README.md`***

```python
f: TextIOWrapper

with open(file = r"README.md", mode = "r", encoding = "utf-8") as f:
    README: str = f.read()
```

#### ***`f: TextIOWrapper`***

*Aquí se define una variable `f` que puede ser de tipo `TextIOWrapper` o `None`. Inicialmente, `f` se establece en `None`. Esto es parte de la anotación de tipos, que ayuda a los desarrolladores y herramientas de análisis de código a entender qué tipo de datos se espera.*

#### ***`with open(file = r"README.md", mode = "r", encoding = "utf-8") as f:`***

*Esta línea abre el fichero `README.md` en modo lectura (`"r"`) con codificación UTF-8. La construcción `with` se usa para garantizar que el fichero se cierre automáticamente después de que el bloque de código se ejecute, incluso si ocurre una excepción.*

- **`file = r"README.md"`:** *Especifica el nombre del fichero a abrir. El prefijo `r` indica una cadena sin procesar (raw string), que evita problemas con los caracteres de escape en las rutas de fichero en sistemas Windows.*
- **`mode = "r"`:** *Establece el fichero en modo lectura.*
- **`encoding = "utf-8"`:** *Define la codificación del fichero como UTF-8.*

*Dentro del bloque `with`, `f` es un objeto de fichero que permite leer el contenido del fichero `README.md`.*

#### ***`README: str = f.read()`***

*Lee todo el contenido del fichero `README.md` y lo almacena en la variable `README`, que es de tipo `str` (cadena de texto).*

#### ***Parámetros de `setup()`***

```python
setup(
    name="pycrypy",
    version="1.0.0.dev0",
    author="Daniel Benjamin Perez Morales",
    author_email="danielperezdev@proton.me",
    description="This utility, developed in Python3, significantly simplifies the configuration process of Alacritty, allowing easy adjustments to font, theme, padding, cursors, and font styles.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/D4nitrix13/pycrypy.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},  # Indicates that packages are in "src"
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: POSIX :: Linux",
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
    ],
    keywords="alacritty",
    python_requires=">=3.6",
    install_requires=[
        "altgraph >= 0.17.4",
        "certifi >= 2025.1.31",
        "cffi >= 1.17.1",
        "charset-normalizer >= 3.4.1",
        "colored >= 2.3.0",
        "cryptography >= 44.0.2",
        "docutils >= 0.21.2",
        "id >= 1.5.0",
        "idna >= 3.10",
        "jaraco.classes >= 3.4.0",
        "jaraco.context >= 6.0.1",
        "jaraco.functools >= 4.1.0",
        "jeepney >= 0.9.0",
        "keyring >= 25.6.0",
        "markdown-it-py >= 3.0.0",
        "mdurl >= 0.1.2",
        "more-itertools >= 10.6.0",
        "mypy >= 1.15.0",
        "mypy-extensions >= 1.0.0",
        "nh3 >= 0.2.21",
        "packaging >= 24.2",
        "prettytable >= 3.16.0",
        "pycparser >= 2.22",
        "Pygments >= 2.19.1",
        "pyinstaller >= 6.12.0",
        "pyinstaller-hooks-contrib >= 2025.2",
        "readme_renderer >= 44.0",
        "requests >= 2.32.3",
        "requests-toolbelt >= 1.0.0",
        "rfc3986 >= 2.0.0",
        "rich >= 14.0.0",
        "SecretStorage >= 3.3.3",
        "setuptools >= 78.1.0",
        "toml >= 0.10.2",
        "twine >= 6.1.0",
        "types-toml >= 0.10.8.20240310",
        "typing_extensions >= 4.13.2",
        "urllib3 >= 2.4.0",
        "wcwidth >= 0.2.13",
    ],
    include_package_data=True,
    entry_points=dict(console_scripts=["pycrypy = cli.main:main"]),
)
```

### ***Descripción de cada parámetro***

- **`name`:** *`"pycrypy"`*
  - *Nombre del paquete. Es el nombre con el que se instalará y referenciará el paquete en PyPI y otros sistemas de gestión de paquetes.*

- **`version`:** *`"1.0.0.dev0"`*
  - *Versión del paquete. Sigue la convención de versión semántica (SemVer) para indicar la versión del software.*

- **`author`:** *`"Daniel Benjamin Perez Morales"`*
  - *El nombre del autor del paquete.*

- **`author_email`:** *`"danielperezdev@proton.me"`*
  - *El correo electrónico del autor del paquete.*

- **`description`:** *`"Esta utilidad, desarrollada en Python3, simplifica significativamente el proceso de configuracion de Alacritty, permitiendo ajustar de manera simple la fuente, el tema, el padding, los cursores y los estilos de la fuente."`*
  - *Una breve descripción de lo que hace el paquete. Este es el texto que se muestra en los índices de paquetes y en la documentación.*

- **`long_description`:** *`README`*
  - *La descripción larga del paquete. En este caso, el contenido del fichero `README.md` se utiliza para proporcionar una descripción detallada del paquete.*

- **`long_description_content_type`:** *`"text/markdown"`*
  - *El tipo de contenido de la descripción larga. Indica que la descripción larga está en formato Markdown.*

- **`url`:** *`"https://github.com/D4nitrix13/pycrypy.git"`*
  - *La URL del repositorio del paquete. Aquí se encuentra el código fuente del paquete.*

- **`packages`:** *`find_packages(where = "src")`*
  - *Una lista de paquetes incluidos en el proyecto. `find_packages(where = "src")` busca paquetes dentro del directorio `src`.*

- **`package_dir`:** *`{"": "src"}`*
  - *Un diccionario que indica que todos los paquetes están en el directorio `src`. El primer valor (`""`) representa el paquete raíz, y `src` es el directorio que contiene los paquetes.*

- **`license`:** *`"MIT"`*
  - *La licencia bajo la cual se distribuye el paquete. En este caso, es la Licencia MIT.*

- **`classifiers`:**

  ```python
  [
      "Programming Language :: Python :: 3",
      "Operating System :: POSIX :: Linux",
      "Topic :: Terminals :: Terminal Emulators/X Terminals"
  ]
  ```

  - *Una lista de clasificadores que proporcionan información adicional sobre el paquete, como el lenguaje de programación, la licencia, el sistema operativo compatible, y el tema.*

- **`keywords`:** *`"alacritty"`*
  - *Palabras clave relacionadas con el paquete. Ayudan a los usuarios a encontrar el paquete a través de búsquedas.*

- **`python_requires`:** *`">=3.6"`*
  - *La versión mínima de Python requerida para ejecutar el paquete. En este caso, es Python 3.6 o superior.*

- **`install_requires`:**

  ```python
  [
        "altgraph >= 0.17.4",
        "certifi >= 2025.1.31",
        "cffi >= 1.17.1",
        "charset-normalizer >= 3.4.1",
        "colored >= 2.3.0",
        "cryptography >= 44.0.2",
        "docutils >= 0.21.2",
        "id >= 1.5.0",
        "idna >= 3.10",
        "jaraco.classes >= 3.4.0",
        "jaraco.context >= 6.0.1",
        "jaraco.functools >= 4.1.0",
        "jeepney >= 0.9.0",
        "keyring >= 25.6.0",
        "markdown-it-py >= 3.0.0",
        "mdurl >= 0.1.2",
        "more-itertools >= 10.6.0",
        "mypy >= 1.15.0",
        "mypy-extensions >= 1.0.0",
        "nh3 >= 0.2.21",
        "packaging >= 24.2",
        "prettytable >= 3.16.0",
        "pycparser >= 2.22",
        "Pygments >= 2.19.1",
        "pyinstaller >= 6.12.0",
        "pyinstaller-hooks-contrib >= 2025.2",
        "readme_renderer >= 44.0",
        "requests >= 2.32.3",
        "requests-toolbelt >= 1.0.0",
        "rfc3986 >= 2.0.0",
        "rich >= 14.0.0",
        "SecretStorage >= 3.3.3",
        "setuptools >= 78.1.0",
        "toml >= 0.10.2",
        "twine >= 6.1.0",
        "types-toml >= 0.10.8.20240310",
        "typing_extensions >= 4.13.2",
        "urllib3 >= 2.4.0",
        "wcwidth >= 0.2.13",
  ]
  ```

  - *Una lista de dependencias que se instalarán automáticamente cuando se instale el paquete.*
    - *Aquí, el paquete requiere `altgraph` versión **0.17.4** o superior.*
    - *Aquí, el paquete requiere `certifi` versión **2025.1.31** o superior.*
    - *Aquí, el paquete requiere `cffi` versión **1.17.1** o superior.*
    - *Aquí, el paquete requiere `charset-normalizer` versión **3.4.1** o superior.*
    - *Aquí, el paquete requiere `colored` versión **2.3.0** o superior.*
    - *Aquí, el paquete requiere `cryptography` versión **44.0.2** o superior.*
    - *Aquí, el paquete requiere `docutils` versión **0.21.2** o superior.*
    - *Aquí, el paquete requiere `id` versión **1.5.0** o superior.*
    - *Aquí, el paquete requiere `idna` versión **3.10** o superior.*
    - *Aquí, el paquete requiere `jaraco.classes` versión **3.4.0** o superior.*
    - *Aquí, el paquete requiere `jaraco.context` versión **6.0.1** o superior.*
    - *Aquí, el paquete requiere `jaraco.functools` versión **4.1.0** o superior.*
    - *Aquí, el paquete requiere `jeepney` versión **0.9.0** o superior.*
    - *Aquí, el paquete requiere `keyring` versión **25.6.0** o superior.*
    - *Aquí, el paquete requiere `markdown-it-py` versión **3.0.0** o superior.*
    - *Aquí, el paquete requiere `mdurl` versión **0.1.2** o superior.*
    - *Aquí, el paquete requiere `more-itertools` versión **10.6.0** o superior.*
    - *Aquí, el paquete requiere `mypy` versión **1.15.0** o superior.*
    - *Aquí, el paquete requiere `mypy-extensions` versión **1.0.0** o superior.*
    - *Aquí, el paquete requiere `nh3` versión **0.2.21** o superior.*
    - *Aquí, el paquete requiere `packaging` versión **24.2** o superior.*
    - *Aquí, el paquete requiere `prettytable` versión **3.16.0** o superior.*
    - *Aquí, el paquete requiere `pycparser` versión **2.22** o superior.*
    - *Aquí, el paquete requiere `Pygments` versión **2.19.1** o superior.*
    - *Aquí, el paquete requiere `pyinstaller` versión **6.12.0** o superior.*
    - *Aquí, el paquete requiere `pyinstaller-hooks-contrib` versión **2025.2** o superior.*
    - *Aquí, el paquete requiere `readme_renderer` versión **44.0** o superior.*
    - *Aquí, el paquete requiere `requests` versión **2.32.3** o superior.*
    - *Aquí, el paquete requiere `requests-toolbelt` versión **1.0.0** o superior.*
    - *Aquí, el paquete requiere `rfc3986` versión **2.0.0** o superior.*
    - *Aquí, el paquete requiere `rich` versión **14.0.0** o superior.*
    - *Aquí, el paquete requiere `SecretStorage` versión **3.3.3** o superior.*
    - *Aquí, el paquete requiere `setuptools` versión **78.1.0** o superior.*
    - *Aquí, el paquete requiere `toml` versión **0.10.2** o superior.*
    - *Aquí, el paquete requiere `twine` versión **6.1.0** o superior.*
    - *Aquí, el paquete requiere `types-toml` versión **0.10.8.20240310** o superior.*
    - *Aquí, el paquete requiere `typing_extensions` versión **4.13.2** o superior.*
    - *Aquí, el paquete requiere `urllib3` versión **2.4.0** o superior.*
    - *Aquí, el paquete requiere `wcwidth` versión **0.2.13** o superior.*

- **`include_package_data`:** *`True`*
  - *Un booleano que indica si se deben incluir datos adicionales del paquete (como ficheros de datos) que no están especificados en `MANIFEST.in`.*

- **`entry_points`:**

  ```python
  dict(
    console_scripts = [ "pycrypy = cli.main:main" ]
  ),
  ```

- *Define los puntos de entrada del paquete, como los scripts de consola. Aquí, se especifica que el comando `pycrypy` en la línea de comandos ejecutará la función `main` del módulo `cli.main`.*

### ***Significado de los Símbolos***

- **`{}`:**
  - *Utilizados para definir diccionarios. En `package_dir`, `{"": "src"}` es un diccionario que mapea el paquete raíz a `src`.*

- **`[]`:**
  - *Utilizados para definir listas. En `classifiers`, `["Programming Language :: Python :: 3", ...]` es una lista de clasificadores.*

- **`::`:**
  - *Usado en los clasificadores para separar las categorías. Por ejemplo, `"Programming Language :: Python :: 3"` indica que el paquete está escrito en Python 3.*

- **`>=`:**
  - *Indica que la versión de un paquete debe ser igual o superior a la especificada. En `python_requires = ">=3.6"`, significa que se requiere Python 3.6 o superior.*

- **`/`:**
  - *En la URL `https://github.com/D4nitrix13/pycrypy.git`, el símbolo `/` se usa para separar partes de la URL.*

*Cada uno de estos elementos ayuda a definir y configurar el paquete de Python de manera que sea correctamente instalado, utilizado y distribuido.*
