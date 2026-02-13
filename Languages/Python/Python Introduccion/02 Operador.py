"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Operadores Aritmeticos

# Operaciones con enteros
# Suma
from sys import stdout


print(3 + 4, end = "\n", file = stdout)
# Resta
print(3 - 4, end = "\n", file = stdout)
# Multiplicación
print(3 * 4, end = "\n", file = stdout)
# División
print(3 / 4, end = "\n", file = stdout)
# Módulo
print(10 % 3, end = "\n", file = stdout)
# División entera
print(10 // 3, end = "\n", file = stdout)
# Potencia el primer número es la base y el segundo el exponente
print(2**3, end = "\n", file = stdout)
# Jerarquía de operaciones
print(2**3 + 3 - 7 / 1 // 4, end = "\n", file = stdout)

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?", end = "\n", file = stdout)
# str() convierte un número a cadena de texto
print("Hola " + str(5), end = "\n", file = stdout)

# Operaciones mixtas
# En Python las operaciones se realizan de izquierda a derecha
"""
la multiplicación de cadenas de texto por un número entero
genera una nueva cadena de texto con el contenido repetido
En este caso "Hola " se repite 5 veces
"""
print("Hola " * 5, end = "\n", file = stdout)

"""
En este caso "Hola " se repite 2 elevado a 3 veces que es 8
"""
print("Hola " * (2**3), end = "\n", file = stdout)

flotante: float = 2.5 * 2
"""
En python no se puede multiplicar una cadena de texto por un número flotante
por eso se convierte a entero
En este caso "Hola " se repite 5 veces
"""
print("Hola " * int(flotante), end = "\n", file = stdout)


# Operadores Comparativos

# Operaciones con enteros
"""
El operador de comparación devuelve un booleano
True si la comparación es cierta
False si la comparación es falsa
"""
# > significa mayor que
print(3 > 4, end = "\n", file = stdout)  # False
# < significa menor que
print(3 < 4, end = "\n", file = stdout)  # True
# >= significa mayor o igual que
print(3 >= 4, end = "\n", file = stdout)  # False
# <= significa menor o igual que
print(4 <= 4, end = "\n", file = stdout)  # True
# == significa igual que
print(3 == 4, end = "\n", file = stdout)  # False
# != significa distinto que
print(3 != 4, end = "\n", file = stdout)  # True

# Operaciones con cadenas de texto
"""
En python se pueden comparar cadenas de texto
por orden alfabético por ASCII 
"""

print("Hola" > "Python", end = "\n", file = stdout)  # False
print("Hola" < "Python", end = "\n", file = stdout)  # True
print("aaaa" >= "abaa", end = "\n", file = stdout)  # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa"), end = "\n", file = stdout)  # Cuenta caracteres
print("Hola" <= "Python", end = "\n", file = stdout)  # False
print("Hola" == "Hola", end = "\n", file = stdout)  # True
print("Hola" != "Python", end = "\n", file = stdout)  # True

# Operadores Lógicos

# Basada en el Álgebra de Boole https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
"""
Los operadores lógicos devuelven un booleano
>>> Los operadores lógicos son and, or, not
>>> and significa y
>>> or significa o
>>> not significa no o negación
"""

# Al usar el operador and si una de las comparaciones es falsa devuelve False
print(3 > 4 and "Hola" > "Python", end = "\n", file = stdout)
# Al usar el operador or si una de las comparaciones es verdadera devuelve True
print(3 > 4 or "Hola" > "Python", end = "\n", file = stdout)
print(3 < 4 and "Hola" < "Python", end = "\n", file = stdout)
print(3 < 4 or "Hola" > "Python", end = "\n", file = stdout)
print(3 < 4 or ("Hola" > "Python" and 4 == 4), end = "\n", file = stdout)
# Al usar el operador not niega el resultado de la comparación y devuelve el contrario
# True se convierte en False y False se convierte en True
print(not (3 > 4), end = "\n", file = stdout)
