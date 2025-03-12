"""
Autor: Daniel Benjamin Perez Morales
GitHub: https://github.com/D4nitrix13
Correo electrónico: danielperezdev@proton.me 
"""
from sys import stdout
from typing import List

from typing_extensions import Protocol

# Tipado de funciones lambda (funciones anónimas) en Python.
# Discusión en Stack Overflow:
# https://stackoverflow.com/questions/33833881/is-it-possible-to-type-hint-a-lambda-function

class SumarTresValoresFuncionLambda(Protocol):
    def __call__(self: "SumarTresValoresFuncionLambda", primerValor: int, segundoValor: int) -> int: return primerValor + segundoValor
class FuncionLambda(Protocol):
    def __call__(self: "FuncionLambda", x: int, y: int) -> int: return x + y

class ConvertirMayuscula(Protocol): 
    def __call__(self: "ConvertirMayuscula", palabra) -> str: return palabra.upper()

# Tema: Lambdas en Python

"""
Las funciones lambda son funciones anónimas que se pueden utilizar para realizar operaciones en una sola línea. 
Las funciones lambda se utilizan para realizar operaciones simples y no requieren un nombre para ser utilizadas.
"""


# Funcion normal
def sumar_dos_valores(*, primerValor: int, segundoValor: int) -> int: return primerValor + segundoValor


print(
    f"funcion normal sumar_dos_valores = {sumar_dos_valores(primerValor = 2, segundoValor = 4)}",
    end ="\n", file = stdout
)


# Funcion normal
def multiplicar_valor(*, primerValor: int, segundoValor: int) -> int: return primerValor * segundoValor


print(
    f"funcion normal multiplicar_valor = {multiplicar_valor(primerValor=2, segundoValor=4)}",
    end ="\n", file = stdout
)

def sumar_tres_valores(*, valor: int) -> SumarTresValoresFuncionLambda: 
    return lambda primerValor, segundoValor: primerValor + segundoValor + valor

print(
    f"funcion lambda sumar_tres_valores = {sumar_tres_valores(valor = 3)(primerValor = 2, segundoValor = 4)}",
    end ="\n", file = stdout
)

# Lambda
# * La función lambda se puede asignar a una variable

"""
Suma dos valores y retorna el resultado
>>> Suma dos valores y retorna el resultado
los valores son x e y
estos valores pueden ser de cualquier tipo de dato que se pueda sumar 
"""

"""
>>> Protocol Es una clase base de typing_extensions que se utiliza para definir tipos de protocolo en Python. Los protocolos permiten especificar interfaces esperadas por ciertos tipos, incluidas las funciones y métodos.

>>> FuncionLambda es un protocolo que define que cualquier objeto de este tipo debe ser invocable (__call__) con dos argumentos x y y, ambos enteros, y debe devolver un entero. Esencialmente, este protocolo indica que cualquier objeto que se comporte como una función que acepta dos enteros y devuelve un entero será compatible con este protocolo.

Aquí se define una función lambda llamada sumar que cumple con el protocolo FuncionLambda. La lambda toma dos argumentos x e y, ambos enteros, y devuelve la suma de estos dos valores.
"""


"""
>>> En Python, `__call__` es un método especial o mágico que se utiliza para hacer que un objeto sea callable, es decir, que se comporte como una función. Cuando un objeto define el método `__call__`, se puede invocar como si fuera una función.

### Funcionamiento de `__call__`:

- **Definición:** El método `__call__` permite que un objeto sea llamado como una función.

- **Implementación:** Se define dentro de una clase y toma al menos un argumento (`self`), que hace referencia al propio objeto.

- **Uso:** Cuando se invoca un objeto que implementa `__call__`, Python ejecuta automáticamente el código definido dentro de `__call__`.

### Ejemplo:

```python
class Sumador:
    def __call__(self: "Sumador", x: int, y: int):
        return x + y

sumar: Sumador = Sumador()
resultado: int = sumar(3, 5)  # Aquí se llama a sumar como si fuera una función
print(resultado)  # Output: 8
```

### Explicación del Ejemplo:

1. **Clase `Sumador`:** Define una clase `Sumador` que implementa el método `__call__`.

2. **Método `__call__`:** Dentro de `Sumador`, `__call__` toma dos parámetros (`x` e `y`) y devuelve la suma de estos dos valores.

3. **Creación de instancia:** Se crea una instancia `sumar` de la clase `Sumador`.

4. **Invocación como función:** `sumar(3, 5)` llama a `__call__` de la instancia `sumar`, pasando `3` y `5` como argumentos. Esto devuelve `8`, que se asigna a `resultado`.

5. **Impresión del resultado:** Se imprime el resultado de la suma, que es `8`.

### Significado:

En resumen, `__call__` en Python permite que los objetos definidos por el usuario se comporten como funciones cuando se les llama, proporcionando flexibilidad para implementar objetos que encapsulen comportamientos específicos de función o método.
"""


"""
El uso del protocolo (`Protocol` de `typing_extensions`) depende del contexto y de lo que necesites lograr en tu código

### Uso del Protocolo (`Protocol`):

1. **Definición de Interfaces:**
   - El protocolo (`Protocol`) te permite definir interfaces esperadas para tipos de datos en Python.
   - Es útil cuando necesitas especificar qué métodos o atributos debe tener un objeto para ser considerado compatible con cierto uso o contexto.

2. **Ejemplo de `FuncionLambda`:**
   - En el ejemplo anterior, `FuncionLambda` se utilizó para especificar que un objeto debe ser callable (como una función) y aceptar dos argumentos enteros (`x` e `y`) para sumarlos.

3. **Sin Necesidad del Protocolo:**
   - Si solo necesitas crear una función lambda o cualquier función que sume dos números enteros y devuelva un resultado, no es estrictamente necesario utilizar `Protocol`.
   - Puedes definir la función directamente sin especificar un tipo de protocolo. Python manejará dinámicamente el comportamiento de la función.

4. **Cuándo Usar Protocolo:**
   - Utiliza `Protocol` cuando necesites definir interfaces claras y esperadas para tipos personalizados o cuando necesites verificar la compatibilidad de objetos con ciertos métodos o atributos.
   - Es particularmente útil en entornos donde se espera polimorfismo basado en interfaces, como en sistemas de tipado estático (usando `mypy`, por ejemplo).

### Ejemplo sin Protocolo:

```python
# Definir una función simple para sumar dos números
sumar = lambda x, y: x + y

# Llamar a la función lambda y mostrar el resultado
print(f"sumar = {sumar(2, 4)}")
```

### Conclusión:

- Si tu objetivo es simplemente crear funciones o lambdas que realicen operaciones básicas, no necesitas usar `Protocol`.
- Utiliza `Protocol` cuando necesites definir y verificar interfaces específicas para tipos personalizados en tu código, especialmente en contextos donde el tipado estático o la verificación de tipos sea importante (como con `mypy`).

En resumen, el uso de `Protocol` depende de la necesidad de especificar interfaces y verificar comportamientos de objetos en tu código.
"""

sumar: FuncionLambda = lambda x, y: x + y
print(f"sumar = {sumar(x = 2, y = 4)}", end ="\n", file = stdout)

"""
>>> convertirMayusculas: callable = lambda palabra: palabra.upper()
>>> lo que hace esta función es convertir una palabra a mayúsculas
"""

convertirMayusculas: ConvertirMayuscula = lambda palabra: palabra.upper()
print(f"convertirMayusculas = {convertirMayusculas(palabra = 'hola')}", end ="\n", file = stdout)

"""
lambda iterable: iterable % 2 == 0, listaNumeros

La función filter() devuelve un iterador que filtra los elementos de una secuencia, para los que la función de filtro devuelve True.

La función filter() toma dos argumentos:
>>> Una función
>>> Una secuencia

Lo que hace internamente la función filter es recorrer la secuencia y aplicar la función a cada elemento.

Si la función devuelve True, el elemento se incluye en la secuencia de salida. Si la función devuelve False, el elemento se excluye de la secuencia de salida.

otra manera de enterderlo seria:

listaNumeros: List[int] = [1, 2, 3, 4, 5, 6]
listaFiltrada: List[int] = list()
for iterable in listaNumeros:
    if iterable % 2 == 0:
        print(iterable, end ="\n", file = stdout)
        listaFiltrada.append(iterable)
        # osea que es True
"""

listaNumeros: List[int] = [1, 2, 3, 4, 5, 6]
filtarLista: filter = filter(lambda iterable: iterable % 2 == 0, listaNumeros)
print(f"filtarLista = {list(filtarLista)}", end ="\n", file = stdout)


"""
map es una función que toma dos argumentos:
>>> Una función
>>> Una secuencia

La función map() aplica una función a todos los elementos de una secuencia dada.
>>> la diferencia entre map y filter es que map retorna un iterador con los resultados de aplicar la función a cada elemento de la secuencia. y filter retorna un iterador con los elementos de la secuencia que cumplen una condición.

otra manera de entenderlo seria:
listaNumeros: List[int] = [1, 2, 3, 4, 5]
listaMapeada: List[int] = []
for iterable in listaNumeros:
    print(iterable**2, end ="\n", file = stdout)
    listaMapeada.append(iterable**2)
    # osea que es True
"""
listaNumeros = [1, 2, 3, 4, 5]
listaMapeada: map = map(lambda x: x**2, listaNumeros)
print(f"listaMapeada = {list(listaMapeada)}", end ="\n", file = stdout)
