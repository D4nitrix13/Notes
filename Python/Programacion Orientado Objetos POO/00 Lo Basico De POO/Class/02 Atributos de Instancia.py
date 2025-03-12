#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me 

from sys import stdout


class Celular:
    # atributos de instancia son aquellos atributos que se le asignan a cada objeto de la clase, es decir, cada objeto puede tener valores diferentes en sus atributos.

    # def __init__ es un metodo especial que se ejecuta al crear un objeto de la clase, es decir, al crear un objeto de la clase Celular, se ejecuta el metodo __init__ y se le pasan los parametros que se le pasen al crear el objeto. def __init__ tambien se le conoce como metodo constructor de la clase.

    def __init__(self: 'Celular', marca: str, modelo: str, camara: str) -> None:
        # self es un parametro especial que hace referencia al objeto que se esta creando, es decir, self es el objeto que se esta creando, y se le asigna los valores que se le pasan al crear el objeto.

        self.marca: str = marca

        # marca es un atributo de instancia, y self.marca es el atributo de la clase

        # por ejemplo self.xd = marca, xd es un atributo de la clase, y marca es un atributo de instancia

        self.modelo: str = modelo
        self.camara: str = camara
        return None


celular1: Celular = Celular(marca = "Xiaomi", modelo = "Redmi Note 9", camara = "64MP")

celular2: Celular = Celular(marca = "Samsung", modelo = "Galaxy A51", camara = "48MP")

print(celular1.marca,end = "\n", file = stdout)
