"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: fichero Handling o Manejo de ficheros

"""
io es un módulo de Python que proporciona una forma de utilizar las funciones dependientes del sistema operativo.
"""
import io
from typing import Dict, List, Union

"""
csv (Comma Separated Values) o valores separados por comas es un formato de fichero que se utiliza para almacenar datos tabulares, como una base de datos o una hoja de cálculo.
"""
import csv

"""
json (JavaScript Object Notation) o notación de objetos de JavaScript es un formato de fichero que se utiliza para almacenar y transmitir datos.
"""

import json

"""
os es un módulo de Python que proporciona una forma de utilizar las funciones dependientes del sistema operativo.
"""

import os

"""
xml (eXtensible Markup Language) o lenguaje de marcado extensible es un formato de fichero que se utiliza para almacenar y transmitir datos.
"""

import xml

# .txt fichero

# Leer, escribir y sobrescribir si ya existe
"""
open() es una función integrada de Python que se utiliza para abrir un fichero.

los argumentos de open() son:

>>> fichero: el nombre del fichero que se va a abrir

>>> mode: el modo en el que se va a abrir el fichero

>>> encoding: el tipo de codificación que se va a utilizar para abrir el fichero por defecto es utf-8

>>> buffering: el tamaño del buffer que se va a utilizar para leer y escribir el fichero por defecto es -1 que significa que se va a utilizar el buffer por defecto del sistema operativo. Si buffering es 0 no se va a utilizar buffer, si buffering es 1 se va a utilizar buffer de línea, si buffering es mayor que 1 se va a utilizar un buffer de ese tamaño.

>>> errors: el tipo de errores que se van a manejar por defecto es None que significa que se van a manejar todos los errores.

>>> newline: el tipo de nueva línea que se va a utilizar por defecto es None que significa que se va a utilizar el tipo de nueva línea que se utiliza por defecto en el sistema operativo.

>>> closefd: si se va a cerrar el descriptor de fichero después de abrir el fichero por defecto es True.

>>> opener: el tipo de objeto que se va a utilizar para abrir el fichero por defecto es None que significa que se va a utilizar el tipo de objeto que se utiliza por defecto en el sistema operativo.
"""

"""
Tipos de modos de apertura de ficheros:
w: write (sobrescribe el fichero si ya existe)
r: read (por defecto) (lee el fichero)
a: append (añade al final del fichero)
w+: write y read (sobrescribe el fichero si ya existe)
r+: read y write (lee y escribe el fichero)
a+: append y read (añade al final del fichero y lee el fichero)
"""


"""
ficheroTxt: io.TextIOWrapper = open(
    file="fichero.txt",
    mode="w+",
    encoding="utf-8",
    buffering=-1,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
)
"""


"""
ficheroTxt.write(
    "Mi nombre es Daniel\nMi apellido es Perez\n18 años\nY mi lenguaje preferido es Python"
)
"""


"""
Puedes usar el método seek() para mover el puntero de lectura al principio del fichero. 
El método seek() toma dos argumentos: el primer argumento es la posición del puntero de lectura y el segundo argumento es el punto de referencia.

Ejemplo:
el primer argumento es 0 que significa que el puntero de lectura se moverá al principio del fichero.
el segundo argumento es 0, que significa que el punto de referencia es el principio del fichero.

ficheroTxt.seek(0, 0)
"""


# * ficheroTxt.seek(0, 0)

"""
El método read() lee el contenido del fichero y lo devuelve como una cadena de texto.
El método read() toma un argumento opcional que es el número de caracteres que se van a leer del fichero.
Si no se especifica ningún argumento, el método read() lee todo el contenido del fichero. 
"""

# * print(ficheroTxt.read(), end ="\n", file = stdout)

# *print(ficheroTxt.read(10), end ="\n", file = stdout)

"""
El método readline() lee una línea del fichero y la devuelve como una cadena de texto.
El método readline() toma un argumento opcional que es el número de caracteres que se van a leer de la línea.
"""

# * print(ficheroTxt.readline(), end ="\n", file = stdout)
# * print(ficheroTxt.readline(10), end ="\n", file = stdout)

"""
el metodo readlines() lee todas las líneas del fichero y las devuelve como una lista de cadenas de texto.
"""
# * print(ficheroTxt.readlines(), end ="\n", file = stdout)

# * for linea in ficheroTxt.readlines():
# * print(linea, end ="\n", file = stdout)


"""
Añadir al final del fichero usamos el \n para que se añada en una nueva línea. 
si no se añade el \n se añadirá al final de la última línea.
"""

# * ficheroTxt.write("\nAunque también me gusta JavaScript")
# * print(ficheroTxt.readline(), end ="\n", file = stdout)


"""
Para cerrar el fichero usamos el método close().
"""

# * ficheroTxt.close()


"""
Otra forma de abrir un fichero es usando la declaración with.
y el fichero se cerrará automáticamente al finalizar el bloque de código o al salir de la identación.
"""

"""
with open(
    file="fichero.txt",
    mode="a",
    encoding="utf-8",
    buffering=-1,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
) as otroFichero:
    otroFichero.write("\nY C también")

"""

"""
El método remove() elimina el fichero especificado.
toma dos argumentos:
path: el nombre del fichero que se va a eliminar.
dir_fd: el descriptor de fichero del directorio que contiene el fichero que se va a eliminar. Por defecto es None. Lo que significa que el directorio que contiene el fichero es el directorio de trabajo actual.
"""
# * os.remove(path="fichero.txt", dir_fd=None)


# .json fichero


"""
jsonFichero: io.TextIOWrapper = open(
    file="fichero.json",
    mode="w+",
    encoding="utf-8",
    buffering=-1,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
)
"""

jsonTest: Dict[str, Union[str, int, List[str]]] = {
    "nombre": "Daniel",
    "apellido": "Perez",
    "edad": 18,
    "lenguages": ["Python", "C", "TypeScript"],
    "website": "https://daniel.dev",
}


"""
El método dump() es utilizado para escribir datos en un fichero en formato JSON.

Los metodos dump() y dumps() son utilizados para escribir datos en formato JSON.

dump() todos los argumentos que recibe son

>>> obj: el objeto que se va a escribir en el fichero. obj es una abreviatura de objeto.

>>> fp: el fichero en el que se va a escribir el objeto. fp es una abreviatura de fichero pointer o puntero de fichero.

>>> skipkeys: si es True, las claves que no son de tipo str serán omitidas. Por defecto es False.

>>> ensure_ascii: si es True, todos los caracteres no ASCII en el resultado serán escapados. Por defecto es True.

>>> check_circular: si es True, se lanzará un ValueError si se detecta una referencia circular. una referencia circular es una referencia a un objeto que ya ha sido referenciado. Por defecto es True.

>>> allow_nan: si es True, se permitirán los valores NaN, Los valores NaN son valores que no son números. Sus siglas en inglés son Not a Number que significa No es un número. Infinity e -Infinity son ejemplos de valores NaN. Por defecto es True.

>>> cls: la clase que se va a utilizar para codificar el objeto. Por defecto es None. Lo que significa que se va a utilizar la clase JSONEncoder.

>>> indent: el número de espacios que se van a utilizar para la indentación. Por defecto es None. Lo que significa que no se va a utilizar indentación. Si indent es un número mayor que 0, se va a utilizar indentación. Si indent es None, no se va a utilizar indentación.

>>> separators: una tupla que contiene los separadores que se van a utilizar para los elementos y los pares clave-valor. Por defecto es None. Lo que significa que se van a utilizar los separadores por defecto.

>>> default: una función que se va a utilizar para codificar objetos que no son de tipo JSON. Por defecto es None. Lo que significa que no se va a utilizar ninguna función para codificar objetos que no son de tipo JSON.

>>> sort_keys: si es True, las claves del objeto se van a ordenar alfabéticamente. Por defecto es False.
"""

"""
json.dump(
    obj=jsonTest: Dict[str, Union[str, int, List[str]]],
    fp=jsonFichero,
    skipkeys=False,
    ensure_ascii=True,
    check_circular=True,
    allow_nan=True,
    cls=None,
    indent=2,
    separators=None,
    default=None,
    sort_keys=False,
)
"""

"""
Para cerrar el fichero usamos el método close().
"""

# * jsonFichero.close()

"""
with open(
    file="fichero.json",
    mode="r",
    encoding="utf-8",
    buffering=-1,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
) as otrofichero:
    for linea in otrofichero.readlines():
        print(linea, end ="\n", file = stdout)
"""


"""
El método load() es utilizado para leer datos de un fichero en formato JSON.

Todos los argumentos que recibe son
>>> fp: el fichero del que se van a leer los datos. fp es una abreviatura de fichero pointer o puntero de fichero.

>>> cls: la clase que se va a utilizar para decodificar el objeto. Por defecto es None. Lo que significa que se va a utilizar la clase JSONDecoder.

>>> object_hook: una función que se va a utilizar para decodificar los objetos. Por defecto es None. Lo que significa que no se va a utilizar ninguna función para decodificar los objetos.

>>> parse_float: una función que se va a utilizar para decodificar los números de punto flotante. Por defecto es None. Lo que significa que no se va a utilizar ninguna función para decodificar los números de punto flotante.

>>> parse_int: una función que se va a utilizar para decodificar los números enteros. Por defecto es None. Lo que significa que no se va a utilizar ninguna función para decodificar los números enteros.

>>> parse_constant: una función que se va a utilizar para decodificar los valores especiales. Por defecto es None. Lo que significa que no se va a utilizar ninguna función para decodificar los valores especiales.

>>> object_pairs_hook: una función que se va a utilizar para decodificar los pares clave-valor. Por defecto es None. Lo que significa que no se va a utilizar ninguna función para decodificar los pares clave-valor.

"""

"""
diccionarioJson: Dict[str, Union[str, int]] = json.load(
    fp=open(
        file="fichero.json",
        mode="r",
        encoding="utf-8",
        buffering=-1,
        errors=None,
        newline=None,
        closefd=True,
        opener=None,
    ),
    cls=None,
    object_hook=None,
    parse_float=None,
    parse_int=None,
    parse_constant=None,
    object_pairs_hook=None,
)

"""

"""
Imprimir el diccionario 
"""
# * print(diccionarioJson, end ="\n", file = stdout)

"""
Imprimir el tipo de la variable diccionarioJson
"""
# * print(type(diccionarioJson), end ="\n", file = stdout)

"""
Acceder a un valor del diccionario
"""
# * print(diccionarioJson["nombre"], end ="\n", file = stdout)

# .csv fichero

# ficheroCsv: io.TextIOWrapper = open(
#     file="fichero.csv",
#     mode="w+",
#     encoding="utf-8",
#     buffering=-1,
#     errors=None,
#     newline=None,
#     closefd=True,
#     opener=None,
# )

"""
El método writer() es utilizado para escribir datos en un fichero en formato CSV.
todos los argumentos que recibe son

>>> como primer argumento se le pasa el fichero en el que se van a escribir los datos. csvfile es una abreviatura de CSV file.

>>> dialect: el dialecto que se va a utilizar para escribir los datos. Por defecto es excel. Los dialectos son un conjunto de reglas que definen el formato de un fichero CSV.

>>> delimiter: el delimitador que se va a utilizar para separar los campos. Por defecto es ",".

>>> quotechar: el carácter que se va a utilizar para citar los campos. Por defecto es '"'.

>>> quoting: el tipo de citado que se va a utilizar. Por defecto es QUOTE_MINIMAL.

>>> doublequote: si es True, los campos citados se van a citar con el mismo carácter que se utiliza para citar los campos. Por defecto es True.

>>> escapechar: el carácter que se va a utilizar para escapar los campos citados. Por defecto es None. Lo que significa que no se va a utilizar ningún carácter para escapar los campos citados.

>>> lineterminator: el carácter que se va a utilizar para terminar las líneas. Por defecto es "\r\n".

>>> skipinitialspace: si es True, se van a ignorar los espacios iniciales en los campos. Por defecto es False.

>>> strict: si es True, se va a lanzar un error si se detecta un formato CSV inválido. Por defecto es False.
"""

# csvEscribir: csv.writer = csv.writer(ficheroCsv)

"""
csvEscribir: csv.writer = csv.writer(
    ficheroCsv,
    dialect="excel",
    delimiter=",",
    quotechar='"',
    quoting=csv.QUOTE_MINIMAL,
    doublequote=True,
    escapechar=None,
    lineterminator="\r\n",
    skipinitialspace=False,
    strict=False,
)
"""

# * print(type(csvEscribir))

"""
El método writerow() es utilizado para escribir una fila en un fichero en formato CSV.

Recibe un argumento que es la fila que se va a escribir en el fichero. se le pasa una lista de valores que se van a escribir en la fila. Como lista de valores se puede utilizar una lista, una tupla o un conjunto.
"""

"""
csvEscribir.writerow(["nombre", "apellido", "edad", "lenguage", "website"])
csvEscribir.writerow(["Daniel", "Perez", 18, "Python", "https://daniel.dev"])
csvEscribir.writerow(["Benjamin", "Morales", 18, "COBOL", "https://python3.dev"])
"""

# * ficheroCsv.close()

"""
with open(
    file="fichero.csv",
    mode="w+",
    encoding="utf-8",
    buffering=-1,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
) as otrofichero:
    for linea in otrofichero.readlines():
        print(linea, end ="\n", file = stdout)
"""


# .xlsx fichero
# import xlrd # Debe instalarse el módulo

"""
xml.etree.ElementTree es un módulo de Python que proporciona una forma de trabajar con XML.
"""

import xml.etree.ElementTree as ET

# Crear el elemento raíz que es una etiqueta llamada root

"""
El metodo Element() es utilizado para crear un elemento XML.
todos los argumentos que recibe son
>>> como primer argumento: el nombre de la etiqueta que se va a crear. tag es una abreviatura de tag o etiqueta.

>>> attrib: un diccionario que contiene los atributos que se van a añadir a la etiqueta. Por defecto es None. Lo que significa que no se van a añadir atributos a la etiqueta.

>>> tag: el nombre de la etiqueta que se va a crear. Por defecto es None. Lo que significa que no se va a crear ninguna etiqueta.
"""
root: xml.etree.ElementTree.Element = ET.Element(
    "root", attrib = {"version": "1.0"}
)
# * print(type(root), end ="\n", file = stdout)

# Crear un elemento hijo que es una etiqueta llamada childs

"""
El metodo SubElement() es utilizado para crear un elemento hijo.
todos los argumentos que recibe son
>>> como primer argumento: el elemento padre al que se va a añadir el elemento hijo. parent es una abreviatura de parent o padre.

>>> como segundo argumento: el nombre de la etiqueta que se va a crear. tag es una abreviatura de tag o etiqueta.

>>> attrib: un diccionario que contiene los atributos que se van a añadir a la etiqueta. Por defecto es None. Lo que significa que no se van a añadir atributos a la etiqueta.
"""
child: ET.Element = ET.SubElement(root, "child", attrib={"version": "1.0"})


child.text = "Este es el texto del elemento hijo"

# Crear un fichero XML y escribir el árbol en él
"""
wb: write binary (sobrescribe el fichero si ya existe)
"""

"""
tree esta variable es de tipo xml.etree.ElementTree.ElementTree 
es utilizada para crear un árbol XML. A un árbol XML se le conoce como un árbol de elementos. Un árbol de elementos es una estructura de datos que se utiliza para representar un documento XML. Un árbol de elementos es un árbol en el que cada nodo es un elemento XML. Un elemento XML es una etiqueta que contiene un conjunto de atributos y un conjunto de nodos hijos. Un nodo hijo es un nodo que está conectado a otro nodo a través de una arista. Una arista es una línea que conecta dos nodos.
"""
tree: xml.etree.ElementTree.ElementTree = ET.ElementTree(
    element = root, file="fichero.xml"
)

with open(
    file="fichero.xml",
    mode="wb",
    encoding=None,
    buffering=-1,
    errors=None,
    newline=None,
    closefd=True,
    opener=None,
) as file:
    tree.write(file)
