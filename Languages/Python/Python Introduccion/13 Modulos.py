"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Modulos
# Modules

"""
los módulos son ficheros de python que contienen funciones, variables y clases que pueden ser importadas desde otros ficheros de python para ser usadas en el fichero que lo importa
"""

"""
Estructura de un modulo

>>> from es para importar un modulo 
>>> import es para importar un modulo y se puede usar para importar un modulo especifico de un paquete
>>> as es para renombrar un modulo el cual se puede usar para evitar conflictos de nombres de modulos
"""
import math

# Modulo de python 
from math import pi as PI_VALUE
from sys import stdout

import modulo

# Modulo propio
from modulo import imprimir_valor, sumar_valores

# Modulo propio dentro de un paquete o directorio o directorio
from imports.module import modulo_propio 

# importamos sin usar el from para importar un modulo especifico de un paquete o directorio o directorio. 
import imports.module.modulo_propio

# Usamos el as para renombrar el modulo porque si no lo renombramos tendremos que usar el nombre completo del modulo para usarlo y eso no es muy practico
import imports.module.modulo_propio as modulo_propio

# Importamos una funcion especifica de un modulo propio dentro de un paquete o directorio o directorio
from imports.module.modulo_propio import id_valor
from imports.module.modulo_propio import id_valor as id_valor_modulo_propio

from imports.module.functions import modulo_funciones
from imports.module.functions import modulo_funciones as modulo_funciones_renombrado
import imports.module.functions.modulo_funciones
import imports.module.functions.modulo_funciones as module_funciones
from imports.module.functions.modulo_funciones import tipo_dato
from imports.module.functions.modulo_funciones import tipo_dato as tipo_dato_modulo_funciones

modulo.sumar_valores(numeroUno=5, numeroDos=3, numeroTres=1)
modulo.imprimir_valor(valor="Hola Python!")

modulo.sumar_valores(numeroUno=5, numeroDos=3.2, numeroTres=11)
imprimir_valor(valor="Rust")

# El metodo pi() del modulo math nos retorna el valor de pi
print(math.pi, end = "\n", file = stdout)
# El metodo pow() del modulo math nos retorna el valor de 2 elevado a 8
print(math.pow(2, 8), end = "\n", file = stdout)


print(PI_VALUE, end = "\n", file = stdout)

edad: int = 18
# manera de importar un modulo propio dentro de un paquete o directorio o directorio.

print(id_valor(valor=edad), end = "\n", file = stdout)
print(id_valor_modulo_propio(valor=edad), end = "\n", file = stdout)

print(modulo_funciones.tipo_dato(dato=edad), end = "\n", file = stdout)
print(imports.module.functions.modulo_funciones.tipo_dato(dato=edad), end = "\n", file = stdout)
print(tipo_dato_modulo_funciones(dato=edad), end = "\n", file = stdout) 



# Cuando importamos un modulo propio y ejecutamos el fichero que lo  esta importando se crea un directorio __pycache__ la cual contiene un fichero .pyc el cual es un fichero compilado del modulo que importamos
