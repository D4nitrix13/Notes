#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me 
from typing import List
from sys import exit, stdout

def main() -> None:
    celular1_marca: str = "huawei"
    celular2_marca: str = "Samsung"
    celular3_marca: str = "apple"

    # Modelo del celular
    celular1_modelo: str = "S23"
    celular2_modelo: str = "Iphone 15 pro"
    celular3_modelo: str = "P20 pro"

    celular1_camara_trasera: str = "48mp"
    celular2_camara_trasera: str = "48mp"
    celular3_camara_trasera: str = "12mp"

    celular1_camara_frontal: str = "24mp"
    celular2_camara_frontal: str = "24mp"
    celular3_camara_frontal: str = "8mp"

    print(celular1_camara_frontal,end="\n", file = stdout)

    # Es imposible manejar los datos de esta manera, ya que si se quiere agregar un nuevo celular, se tendria que crear una nueva variable para cada uno de los atributos del celular, y esto se vuelve muy tedioso y dificil de manejar, por eso es que se utiliza la POO, para poder manejar los datos de una manera mas facil y ordenada.


    celulares: List[str] = list()
    celulares.extend(["Samsung", "S23", "48mp", "24mp"])

    return None

if __name__ == "__main__":
    main()
    exit(0)
