#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
MRO (Metodo Resolucion De Orden) o (Method Resolution Order)
Es el orden en el que se van a ejecutar los metodos y atributos de las clases
que estan involucradas en la herencia multiple (cuando una clase hereda de mas de una clase)
"""


from sys import stdout


class A:
    def hablar(self: 'A') -> str: return "Hola soy la clase A"

class F:
    """def hablar(self: object) -> str:
    return "Hola soy la clase F"
    """
    pass

class B(A):
    def hablar(self: object) -> str: return "Hola soy la clase B"
class C(F):
    def hablar(self: object) -> str: return "Hola soy la clase C"
class D(B, C):
    def hablar(self: object) -> str: return "Hola soy la clase D"

letra: D = D()
print(letra.hablar(),end="\n", file = stdout)
print(D.__mro__,end="\n", file = stdout)
# el metodo mro nos dice el orden en el que se van a ejecutar los metodos y atributos de las clases que estan involucradas en la herencia multiple

# la salida es: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class '__main__.C'>, <class '__main__.F'>, <class 'object'>) object es la clase padre de todas las clases por eso aparece al final en python todo es un objeto

print(letra.__class__,end="\n", file = stdout)
# el metodo __class__ nos dice la clase a la que pertenece el objeto


# Si queremos llamar un metodo de una clase especifica podemos hacerlo de esta manera
print(B.hablar(self=letra),end="\n", file = stdout)
# la salida es: Hola soy la clase B porque estamos llamando el metodo de la clase B pasandole como parametro el objeto letra que es de la clase D. No es necesario que la clase del objeto tenga heredada la clase B para poder llamar el metodo de la clase B

"""
Primero se ejecuta el metodo de la clase D, si no lo encuentra se va ala clase B y si el metodo no esta en la clase B se va a la clase C y si el metodo no esta en la clase C se va a la clase A 
"""

"""
      --A--
     /     \ 
    /       \ 
   /         \ 
  B           C
   \         /
    \       /
     \     /
      --D--

D esta heredando de B y C 
y B y C que son las clase padre de D estan heredando de A que es la clase padre de B y C

D -> B -> C -> A
"""

"""
    A      F
    |      |
    |      |
    B      C
    \      /
     \    /
        D
        
En este ejemplo B y C no estan hereando de A por eso el orden cambia

Primero se ejecuta el metodo de la clase D, si no lo encuentra se va ala clase B y si el metodo no esta en la clase B se va a la clase A no a la clase C porque C no esta heredando de A si no esta en la clase A se va a la clase C y si el metodo no esta en la clase C se va a la clase F

D -> B -> A -> C -> F
"""
