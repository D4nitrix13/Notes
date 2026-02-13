"""
El juego consiste en crear personajes en un juego y esos personajes se puedan fusionar para formar personajes mas poderosos que tenga mas poder...

Para ello debemos cambiar el comportamiento del operador + para que cuando los personajes se fusionen, salga un nuevo personaje con el nombre habilidades mejoradas.

una posible formula es: el promedio de las habilidades de ambos, al cuadrado!.
"""


class Sayayin:
    def __init__(self: object, nombre, poder: float, vida: int) -> None:
        self.nombre: str = nombre
        self.poder: float = poder
        self.vida: int = vida

    def __str__(self: object) -> str:
        return f"""Sayayin(nombre = '{self.nombre}', poder = {self.poder}, vida = {self.vida})"""

    def __repr__(self: object) -> str:
        return f"Sayayin('{self.nombre}',{self.poder},{self.vida})"

    def __add__(self: object, otro_sayayin: object) -> object:
        return Sayayin(
            nombre=f"{self.nombre}  {otro_sayayin.nombre}",
            poder=self.poder + otro_sayayin.poder,
            vida=self.vida + otro_sayayin.vida,
        )


goku: Sayayin = Sayayin(nombre="Goku", poder=1000.0, vida=100)
vegeta: Sayayin = Sayayin(nombre="Vegeta", poder=900.0, vida=100)
jiren: Sayayin = Sayayin(nombre="Jiren", poder=10000.0, vida=100)

nuevo_sayayin: Sayayin = goku.__add__(vegeta)

jireta: Sayayin = jiren.__add__(nuevo_sayayin)

print(goku.__str__())
print(vegeta.__str__())
print(jiren.__str__())
print(nuevo_sayayin.__str__())
print(jireta.__str__())
