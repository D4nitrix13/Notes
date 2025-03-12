"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""

# Tema: Python Package Manager (PIP) o Gestor de Paquetes de Python

# Dependencias necesarias
# python3 -m pip install pandas-stubs
# mypy --install-types
# python3 -m pip install types-requests

"""
Es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. 

>>> PIP es el gestor de paquetes por defecto para Python. 

>>> Es una herramienta que permite instalar y desinstalar paquetes de software escritos en Python que se encuentran en el Python Package Index (PyPI).

>>> Existen otros gestores de paquetes como conda, easy_install, entre otros.

>>> PyPI es el repositorio de software oficial para paquetes de software de Python.

>>> Para instalar un paquete se utiliza el comando pip install nombre_del_paquete.

>>> Se puede instalar una versión específica de un paquete con el comando pip install nombre_del_paquete==versión.

>>> Para desinstalar un paquete se utiliza el comando pip uninstall nombre_del_paquete.

>>> Para listar los paquetes instalados se utiliza el comando pip list.

>>> Para mostrar información de un paquete instalado se utiliza el comando pip show nombre_del_paquete.

>>> Para actualizar un paquete se utiliza el comando pip install --upgrade nombre_del_paquete.

>>> Para instalar un paquete desde un fichero se utiliza el comando pip install nombre_del_paquete-1.0.tar.gz.

>>> Si no tienes pip instalado, puedes instalarlo con el comando python get-pip.py en sistemas Unix o python get-pip.py --user en sistemas Windows.

>>> Si no te deja instalar pip, puedes instalarlo con el comando sudo apt install python3-pip en sistemas Unix o python get-pip.py --user en sistemas Windows.

>>> Igualmente, puedes instalar paquetes usando esta sintaxis: python -m pip install nombre_del_paquete. donde -m que es --module, es una forma de ejecutar un módulo como un script.
"""

# * PIP https://pypi.org

# * pip install pip
# * pip --version

"""
Parece que PyPI ya no admite la función de búsqueda a través de XML-RPC, que es lo que `pip search` solía utilizar. Ahora, para buscar paquetes en PyPI, te recomendaría usar el sitio web oficial de PyPI o la interfaz de búsqueda en línea en lugar del comando `pip search`.

Puedes visitar [https://pypi.org/search](https://pypi.org/search) para buscar paquetes directamente desde tu navegador web. Esto te proporcionará la información más actualizada sobre los paquetes disponibles en PyPI.
"""

from sys import stdout
import numpy
import requests
import pandas

# * pip install numpy
# pip list | grep -iE "numpy"


"""
Para ver la version de numpy se puede usar el siguiente comando:

print(numpy.__version__)

Para obtener la versión mayor de numpy se puede usar el siguiente comando:

print(numpy.version.version)
"""
print(numpy.__version__, end ="\n", file = stdout)

numpyLista: numpy.ndarray = numpy.array(object=[35, 24, 62, 52, 30, 30, 17])
print(type(numpyLista), end ="\n", file = stdout)

print(numpyLista * 2, end ="\n", file = stdout)

# * pip install pandas

# * pip list
# * pip uninstall pandas
# * pip show numpy
# * pip install six

# * pip install requests

response: requests.models.Response = requests.get(
    url="https://pokeapi.co/api/v2/pokemon?limit=151"
)
print(response, end ="\n", file = stdout)
print(response.status_code, end ="\n", file = stdout)
print(
    response.json(
        cls=None,
        object_hook=None,
        parse_float=None,
        parse_int=None,
        parse_constant=None,
        object_pairs_hook=None,
    ),
    end="\n", file = stdout
)

# Arithmetics Package o Módulo

from Module.aritmeticos import sumar_dos_valores

print(sumar_dos_valores(primerValor = 5, segundoValor = 10), end ="\n", file = stdout)
