"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
# Strings

from sys import stdout


string: str = "Mi String"
otraString: str = "Mi otro String"

print(len(string), end = "\n", file = stdout)
print(len(otraString), end = "\n", file = stdout)
print(string + " " + otraString, end = "\n", file = stdout)


"""
En python existen caracteres especiales que empiezan por \
\n salto de línea
\t tabulación
\\ barra invertida
\r retorno de carro
\b retroceso
\f salto de página
\a beep
\v tabulación vertical

Tambien se pueden escapar caracteres especiales
\" comillas dobles
\' comillas simples
\\n
"""
nuevaLineaString: str = "Este es un String\ncon salto de línea"
print(nuevaLineaString, end = "\n", file = stdout)

stringTabulada: str = "\tEste es un String con tabulación"
print(stringTabulada, end = "\n", file = stdout)

escaparString: str = "\\tEste es un String \\n escapado"
print(escaparString, end = "\n", file = stdout)

# Formateo

nombre, segundo_nombre, edad = "Daniel", "Perez", 18

"""
existen muchos tipos de formateo
>>> .format() es el más usado 
1. {} para cadenas de texto
2. {} para enteros
3. {} para flotantes
4. {} para hexadecimales
5. {} para octales
6. {} para exponenciales
7. {} para caracteres
8. {} para representaciones de cadenas de texto
9. {} para enteros
10. {} para enteros sin signo
11. {} para punto flotante o exponencial
12. {:.2f} para flotantes con dos decimales el 2 dice cuantos decimales queremos mostrar

Dentro de los parentesis podemos poner el orden de los argumentos

ejemplo:

print("Mi nombre es {1} {0} y mi edad es {2}".format(nombre, segundo_nombre, edad), end = "\n", file = stdout)

Así se imprimiría:
>>> Mi nombre es Perez Daniel y mi edad es 18 
Eso es por que el ordenamiento empieza desde 0 osea que nombre es 0, segundo_nombre es 1 y edad es 2
y se sustituye en el orden que se le indique

Tambien podemos ponerle un nombre a los argumentos
print("Mi nombre es {nombre} {segundo_nombre} y mi edad es {edad}".format(nombre=nombre, segundo_nombre=segundo_nombre, edad=edad), end = "\n", file = stdout)

Así se imprimiría:
>>> Mi nombre es Daniel Perez y mi edad es 18

>>> f"" fstrings es el más moderno
1. {} para cadenas de texto
2. {} para enteros
3. {} para flotantes
4. {} para hexadecimales
5. {} para octales
6. {} para exponenciales
7. {} para caracteres
8. {} para representaciones de cadenas de texto
9. {} para enteros
10. {} para enteros sin signo
11. {} para punto flotante o exponencial
12. {:.2f} para flotantes con dos decimales el 2 dice cuantos decimales queremos mostrar

ejemplo:

print(f"Mi nombre es {nombre} {segundo_nombre} y mi edad es {edad}", end = "\n", file = stdout)

Así se imprimiría:
>>> Mi nombre es Daniel Perez y mi edad es 18



>>> % es el más antiguo
1. %s para cadenas de texto
2. %d para enteros
3. %f para flotantes
4. %x para hexadecimales
5. %o para octales
6. %e para exponenciales
7. %c para caracteres
8. %r para representaciones de cadenas de texto
9. %i para enteros
10. %u para enteros sin signo
11. %g para punto flotante o exponencial
12. %.2f para flotantes con dos decimales el 2 dice cuantos decimales queremos mostrar
"""
print(
    "Mi nombre es {} {} y mi edad es {}".format(nombre, segundo_nombre, edad), end = "\n", file = stdout
)
print("Mi nombre es %s %s y mi edad es %d" % (nombre, segundo_nombre, edad), end = "\n", file = stdout)
print(
    "Mi nombre es " + nombre + " " + segundo_nombre + " y mi edad es " + str(edad),
    end = "\n", file = stdout,
)
print(f"Mi nombre es {nombre} {segundo_nombre} y mi edad es {edad}", end = "\n", file = stdout)

# Desempaqueado de caracteres

"""
El desempaqueado de caracteres es una forma de asignar variables a cada caracter de un string

En este caso
a = p
b = y
c = t
d = h
e = o
f = n
"""

a: str = ""
b: str = ""
c: str = ""
d: str = ""
e: str = ""
f: str = ""

lenguage: str = "python"

# error: Unpacking a string is disallowed  [misc]
a, b, c, d, e, f = lenguage # type: ignore

print(a, end = "\n", file = stdout)
print(e, end = "\n", file = stdout)


# Slicing
"""
El slicing es una forma de obtener un caracter de un string o una parte de un string o un string completo de una forma más sencilla

El formato es el siguiente
>>> [inicio:]
>>> [:fin]
>>> [inicio:fin]
>>> [inicio:fin:salto]


>>> inicio es el caracter desde donde se va a empezar a obtener el string (se incluye)

>>> fin es el caracter donde se va a terminar de obtener el string (no se incluye)

>>> salto es el salto que se va a dar entre cada caracter (se incluye)


"""

# Recordemos que python empieza a contar desde 0

# El contenido de la variable lenguage es "python"

# El resultado de lenguageSlice es "yt"
"""
strings p y t h o n
indice  0 1 2 3 4 5
"""
lenguageSlice = lenguage[1:3]

print(lenguageSlice, end = "\n", file = stdout)

"""
Cuando se pone [1:] se empieza desde el caracter 1 hasta el final
Lo mismo ----> [1:len(lenguageSlice):1]
"""
lenguageSlice = lenguage[1:]
print(lenguageSlice, end = "\n", file = stdout)

"""
Esta forma es para obtener el caracter antepenultimo

strings             p  y  t  h  o  n
indice  positivo    0  1  2  3  4  5
indice negativo    -6 -5 -4 -3 -2 -1

-1 es el ultimo caracter
-2 es el penultimo caracter
-3 es el antepenultimo caracter
etc.

poner [-0] 

"""
lenguageSlice = lenguage[-2]
print(lenguageSlice, end = "\n", file = stdout)

lenguageSlice = lenguage[0:5:2]
print(lenguageSlice, end = "\n", file = stdout)

"""
strings             p  y  t  h  o  n
indice  positivo    0  1  2  3  4  5
indice negativo    -6 -5 -4 -3 -2 -1

lenguageSlice = lenguage[0:5:2]
empiezamos desde el caracter 0 hasta el caracter 6 con un salto de 2 en 2
asi que el resultado seria
inicio = p
salta en p t o
fin = 5
"""

"""
strings             p  y  t  h  o  n
indice  positivo    0  1  2  3  4  5
indice negativo    -6 -5 -4 -3 -2 -1

Para darle la vuelta a un string se puede hacer de la siguiente forma
[::-1] es el string completo
los dos puntos indican que se va a empezar desde el principio hasta el final
el -1 indica que se va a dar un salto de -1 en -1
Lo mismo --> [-1: -len(a) - 1: -1]
"""

lenguageReversa = lenguage[::-1]
print(lenguageReversa, end = "\n", file = stdout)

lenguageReversa = lenguage[::-2]
print(lenguageReversa, end = "\n", file = stdout)

# En python todo es un objeto
# Metodos de strings

# .capitalize() convierte la primera letra en mayuscula y el resto en minuscula y si ya esta en mayuscula la deja igual
print(lenguage.capitalize(), end = "\n", file = stdout)

# .upper() convierte todo el string en mayuscula y si ya esta en mayuscula la deja igual
print(lenguage.upper(), end = "\n", file = stdout)

# .count() cuenta cuantas veces se repite un caracter en un string recibe un argumento y es el caracter que se va a contar retorna un entero y si no encuentra el caracter retorna 0

print(lenguage.count("t"), end = "\n", file = stdout)

# .isalnum() retorna un booleano si el string es alfanumerico si tiene espacios retorna False
print(lenguage.isnumeric(), end = "\n", file = stdout)
print("1".isnumeric(), end = "\n", file = stdout)

# .lower() convierte todo el string en minuscula y si ya esta en minuscula la deja igual
print(lenguage.lower(), end = "\n", file = stdout)

# se puede encadenar metodos
# .isupper() retorna un booleano si el string esta en mayuscula
# Entonces .lower().isupper() retorna un booleano si el string esta en minuscula y si esta en minuscula retorna True
# lo mismo pasa con .islower()

print(lenguage.lower().isupper(), end = "\n", file = stdout)
# .startswith() retorna un booleano si el string empieza con el argumento que se le pasa
print(lenguage.startswith("Py"), end = "\n", file = stdout)
# .endswith() retorna un booleano si el string termina con el argumento que se le pasa
print(lenguage.startswith("on"), end = "\n", file = stdout)

# python es case sensitive ose es sensible a mayusculas y minusculas
print("Py" == "py")  # No es lo mismo

"""
[:] retorna el string completo y es lo mismo que poner [::] Y [::1]
"""
print(lenguage[:], end = "\n", file = stdout)
print(lenguage[::], end = "\n", file = stdout)
print(lenguage[::1], end = "\n", file = stdout)
