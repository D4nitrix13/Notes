#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

"""
En la programación orientada a objetos, los enlaces dinámicos y estáticos se refieren a cuándo se resuelve el método o la función que se debe llamar.

El enlace estático, también conocido como enlace temprano, se resuelve en tiempo de compilación. Esto significa que el método que se va a llamar se decide en el momento de la compilación. En Python, que es un lenguaje interpretado, este concepto no se aplica de la misma manera que en los lenguajes compilados.

El enlace dinámico, también conocido como enlace tardío, se resuelve en tiempo de ejecución. Esto significa que el método que se va a llamar se decide en el momento de la ejecución. Python utiliza enlace dinámico.
"""


from sys import stdout
from typing import Optional, Union

class Animal:
    def hablar(self: 'Animal') -> Optional[str]: return None

class Pato(Animal):
    def hablar(self: 'Pato') -> str: return "¡Cuac!"
class Perro(Animal):
    def hablar(self: 'Perro') -> str: return "¡Guau!"

def hacer_hablar(animal: Union[Pato, Perro]) -> None:
    # No importa el tipo de 'animal' mientras tenga un método 'hablar'
    print(animal.hablar(),end="\n", file = stdout)
    return None

pato: Pato = Pato()
perro: Perro = Perro()

# Aunque 'pato' y 'perro' son de diferentes tipos,
# ambos tienen un método 'hablar', por lo que podemos usarlos
# de manera intercambiable en la función 'hacer_hablar'
hacer_hablar(animal = pato)  # Imprime: ¡Cuac!
hacer_hablar(animal = perro)  # Imprime: ¡Guau!

"""
En este ejemplo, la función hacer_hablar puede tomar cualquier objeto que tenga un método hablar. No importa si el objeto es un Pato o un Perro, siempre que tenga un método hablar, se puede usar en hacer_hablar. Esto es un ejemplo de enlace dinámico, ya que el método específico hablar que se llama se decide en tiempo de ejecución.
"""


"""
Python es un lenguaje de programación de tipado dinámico, lo que significa que el tipo de una variable se conoce solo en tiempo de ejecución y, por lo tanto, solo utiliza enlace dinámico. Sin embargo, para ilustrar el concepto de enlace estático, podemos usar un ejemplo en un lenguaje de programación de tipado estático como Java.

public class Main 
{
    public static void main(String[] args) 
    {
        Main.hola();
    }

    public static void hola() 
    {
        System.out.println("¡Hola, mundo!"),end="\n";
    }
}

"""

# En este ejemplo, el método hola es un método estático. Cuando se llama a Main.hola() en el método main, el compilador de Java sabe exactamente qué método se va a llamar en tiempo de compilación. Esto es un ejemplo de enlace estático.
