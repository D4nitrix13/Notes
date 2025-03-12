"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Tema: Ejercicios

from os import system, name
from sys import stdout
from typing import Union

def borrar() -> None:
    system(command = "clear" if name == "posix" else "cls")
    return None


def main() -> None:
    borrar()
    print("""\
        {r}Ejericios:
        {r}1. EL FAMOSO "FIZZ BUZZ”
        {r}2. ¿ES UN ANAGRAMA?
        {r}3. LA SUCESIÓN DE FIBONACCI
        {r}4. ¿ES UN NÚMERO PRIMO?
        {r}5. INVIRTIENDO CADENAS
        {r}6. Salir
        """.format(r = '\b' * 8), end = "\n", file = stdout
    )
    index: Union[int, None] = None
    
    eleccion: str = str(input("Elige un ejercicio: "))
    match eleccion:
        case "1":
            """
            >>> EL FAMOSO "FIZZ BUZZ”:
            >>> Escribe un programa que muestre por consola (con un print) los
            >>> números de 1 a 100 (ambos incluidos y con un salto de línea entre
            >>> cada impresión), sustituyendo los siguientes:
            >>> - Múltiplos de 3 por la palabra "fizz".
            >>> - Múltiplos de 5 por la palabra "buzz".
            >>> - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
            """

            for index in range(1, 101, 1):
                if index % 3 == 0 and index % 5 == 0: print("fizzbuz", end ="\n", file = stdout)
                elif index % 3 == 0: print("fizz", end ="\n", file = stdout)
                elif index % 5 == 0: print("buzz", end ="\n", file = stdout)
                else: print(index, end ="\n", file = stdout)

        case "2":
            """
            >>> ¿ES UN ANAGRAMA?
            >>> Escribe una función que reciba dos palabras (String) y retorne
            >>> verdadero o falso (Bool) según sean o no anagramas.
            >>> - Un Anagrama consiste en formar una palabra reordenando TODAS
            >>> las letras de otra palabra inicial.
            >>> - NO hace falta comprobar que ambas palabras existan.
            >>> - Dos palabras exactamente iguales no son anagrama.
            """

            palabraOne: str = str(input("ingrese la primera palabra: "))
            palabraTwo: str = str(input("ingrese la palabra dos: "))

            if palabraOne.lower() == palabraTwo.lower(): print("No son anagramas")
            print(
                "Es anagrama"
                if sorted(palabraOne.lower(), reverse=False)
                == sorted(palabraTwo.lower(), reverse=False)
                else "No es anagrama", end = "\n", file = stdout
            )

        case "3":
            """
            >>> LA SUCESIÓN DE FIBONACCI
            >>> Escribe un programa que imprima los 50 primeros números de la sucesión
            >>> de Fibonacci empezando en 0.
            >>> - La serie Fibonacci se compone por una sucesión de números en
            >>> la que el siguiente siempre es la suma de los dos anteriores.
            >>> 0, 1, 1, 2, 3, 5, 8, 13...
            """

            inicio: int = 0
            siguiente: int = 1
            
            for index in range(0, 50, 1):
                print(inicio, end ="\n", file = stdout)
                fibonacciNum = inicio + siguiente
                inicio = siguiente
                siguiente = fibonacciNum

        case "4":
            """
            >>> ¿ES UN NÚMERO PRIMO?
            >>> Escribe un programa que se encargue de comprobar si un número es o no primo.
            >>> Hecho esto, imprime los números primos entre 1 y 100.
            """

            for numero in range(1, 101, 1):
                if numero >= 2:
                    es_divisible: bool = False
                    for index in range(2, numero, 1):
                        if numero % index == 0:
                            es_divisible = True
                            break
                    if not es_divisible: print(numero, end ="\n", file = stdout)

        case "5":
            """
            >>> INVIRTIENDO CADENAS
            >>> Crea un programa que invierta el orden de una cadena de texto
            >>> Sin usar funciones propias del lenguaje que lo hagan de forma automática.
            >>> - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
            """

            texto: str = str(input("Ingrese el texto: "))
            textoLen: int = len(texto)
            textoReversa: str = ""

            for index in range(0, textoLen, 1): textoReversa += texto[textoLen - index - 1]
            print(textoReversa, end ="\n", file = stdout)

        case "6":
            """
            >>> Salir
            """
            print("Saliendo...", end = "\n", file = stdout)
            exit(0)
        case _:
            print("Opción no valida", end ="\n", file = stdout)

    str(input("Presione una tecla para continuar..."))
    main()


if __name__ == "__main__": main()
