#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me 

# para crear una clase en python se utiliza la palabra reservada class, seguido del nombre de la clase, y dentro de la clase se pueden crear los atributos y metodos que se deseen.

"""
En python utilizamos:
>>> 1. snake_case: para nombrar las clases, es decir, se utiliza la primera letra en minuscula y las demas en mayuscula, y si el nombre de la clase esta compuesto por mas de una palabra, se separan con un guion bajo.
    Ejemplo: class Celular_Samsung:

>>> 2. camel_case: se utiliza la primera letra en minuscula, y si el nombre de la clase esta compuesto por mas de una palabra, se separan con una mayuscula.
    Ejemplo: class celularSamsung:

>>> 3. PascalCase: se utiliza la primera letra en mayuscula y las demas en minuscula, y si el nombre de la clase esta compuesto por mas de una palabra, se separan con una mayuscula.
    Ejemplo: class CelularSamsung:

>>> 4. kebab-case: se utiliza la primera letra en minuscula y las demas en minuscula, y si el nombre de la clase esta compuesto por mas de una palabra, se separan con un guion medio.
    Ejemplo: class celular-samsung:

"""


from sys import stdout


class Celular:
    # cada clase puede tener uno o mas atributos, y estos atributos pueden ser de cualquier tipo de dato, incluso pueden ser de otro tipo de dato compuesto, como por ejemplo una lista, un diccionario, una tupla, etc.

    # atributos de la clase celular
    # atributos estaticos: son aquellos atributos que no cambian su valor, es decir, que siempre van a tener el mismo valor.
    marca: str = "samsung"
    modelo: str = "S23"
    camara: str = "48MP"


# esto se llama instanciar una clase o crear un objeto, y para instanciar una clase se utiliza la siguiente sintaxis:

celular1: Celular = Celular()

print(celular1,end="\n", file = stdout)
# nos imprime la direccion de memoria donde se encuentra el objeto celular1

# para acceder a los atributos de un objeto, se utiliza la siguiente sintaxis:
print(celular1.marca,end="\n", file = stdout)
print(celular1.modelo,end="\n", file = stdout)
print(celular1.camara,end="\n", file = stdout)

# tambien podemos crear mas objetos de la misma clase, y cada objeto puede tener valores diferentes en sus atributos.

celular2: Celular = Celular()
celular3: Celular = Celular()
celular4: Celular = Celular()

print(celular4.marca,end="\n", file = stdout)

# tambien podemos modificar los valores de los atributos de un objeto, de la siguiente manera:
celular4.marca = "Xiaomi"

print(celular4.marca,end="\n", file = stdout)

print(celular4,end="\n", file = stdout)
# <__main__.Celular object at 0x7f4fa2f03f10> ese __main__ es el nombre del fichero donde se encuentra la clase, y el 0x7f4fa2f03f10 es la direccion de memoria donde se encuentra el objeto celular4
