#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from sys import stdout


class Persona:
    def __init__(self: 'Persona', nombre: str, edad: int) -> None:
        self.nombre: str = nombre
        self.edad: int = edad
        return None

    def __str__(self: 'Persona') -> str:
        return f"""Persona(
nombre: str ='{self.nombre}',
edad: int ={self.edad}
)"""

    # al usar repr() se puede usar eval() para crear un objeto
    # debe retornar un string que sea valido para crear un objeto el formato es el siguiente.

    # Clase(parametros) si el parametro es un string se debe usar comillas simples o dobles y si es un numero no se debe usar comillas
    def __repr__(self: 'Persona') -> str: return f"Persona('{self.nombre}', {self.edad})"


daniel: Persona = Persona(nombre="Daniel", edad=50)
print(daniel,end="\n", file = stdout)

# __str__ es para el usuario final
# __repr__ es para el programador

# print(daniel.__str__(),end="\n", file = stdout)
repre: str = repr(daniel)
print(repre,end="\n", file = stdout)
resultado: Persona = eval(repre)

print(resultado.nombre,end="\n", file = stdout)

"""
El código proporcionado muestra el uso de algunas funciones especiales en Python, como repr() y eval(), junto con la función print(),end="\n".

La función repr() se utiliza para obtener una representación en forma de cadena de un objeto. Toma un objeto como argumento y devuelve una cadena que representa ese objeto. En el código, se utiliza la función repr() para obtener la representación en forma de cadena del objeto daniel y se almacena en la variable repre.

La función eval() se utiliza para evaluar una expresión o un fragmento de código en forma de cadena. Toma una cadena como argumento y la evalúa como una expresión o un fragmento de código válido en Python. En el código, se utiliza la función eval() para evaluar la cadena almacenada en la variable repre y se guarda el resultado en la variable resultado.
"""

"""
Metodos de sobrecarga de operadores en python Progrmacion orientada a objetos
>>> 1. `__add__(self, other)`: Suma (`+`).
    def __add__(self: object, other: object) -> object:
        return self + other

>>> 2. `__sub__(self, other)`: Resta (`-`).
    def __sub__(self: object, other: object) -> object:
        return self - other

>>> 3. `__mul__(self, other)`: Multiplicación (`*`).
    def __mul__(self: object, other: object) -> object:
        return self * other

>>> 4. `__truediv__(self, other)`: División (`/`).
    def __div__ (self: object, other: object) -> object:
        return self / other
        
>>> 5. `__floordiv__(self, other)`: División entera (`//`).
    def __floordiv__ (self: object, other: object) -> object:
        return self // other
        
>>> 6. `__mod__(self, other)`: Módulo (`%`).
    def __mod__(self: object, other: object) -> object:
        return self % other
        
>>> 7. `__divmod__(self, other)`: División y módulo (`divmod()`).
    def __divmod__(self: object, other: object) -> object:
        return divmod(self, other)

>>> 8. `__pow__(self, other[, modulo])`: Potenciación (`**`).
    def __pow__(self: object, other: object) -> object:
        return self ** other

>>> 10. `__rshift__(self, other)`: Desplazamiento a la derecha (`>>`).
    def __rshift__(self: object, other: object) -> object:
        return self >> other

>>> 9. `__lshift__(self, other)`: Desplazamiento a la izquierda (`<<`).
    def __lshift__(self: object, other: object) -> object:
        return self << other

>>> 11. `__and__(self, other)`: Operador de bits AND (`&`).
    def __and__(self: object, other: object) -> object:
        return self & other

>>> 12. `__xor__(self, other)`: Operador de bits XOR (`^`).
    def __xor__(self: object, other: object) -> object:
        return self ^ other

>>> 13. `__or__(self, other)`: Operador de bits OR (`|`).
    def __or__(self: object, other: object) -> object:
        return self | other

>>> 14. `__neg__(self)`: Negación unaria (`-x`).
    def __neg__(self: object) -> object:
        return -self

>>> 15. `__pos__(self)`: Positivo unario (`+x`).
    def __pos__(self: object) -> object:
        return +self

>>> 16. `__abs__(self)`: Valor absoluto (`abs(x)`).
    def __abs__(self: object) -> object:
        return abs(self)

>>> 17. `__invert__(self)`: Invertir bits (`~x`).
    def __invert__(self: object) -> object:
        return ~self

>>> 18. `__complex__(self)`: Conversión a número complejo (`complex(x)`).
    def __complex__(self: object) -> object:
        return complex(self)

>>> 19. `__int__(self)`: Conversión a entero (`int(x)`).
    def __int__(self: object) -> object:
        return int(self)

>>> 20. `__float__(self)`: Conversión a punto flotante (`float(x)`).
    def __float__(self: object) -> object:
        return float(self)

>>> 21. `__round__(self[, ndigits])`: Redondeo (`round(x[, ndigits])`).
    def __round__(self: object, ndigits: int = 0) -> object:
        return round(self, ndigits)

>>> 22. `__trunc__(self)`: Truncamiento (`math.trunc(x)`).
    def __trunc__(self: object) -> object:
        return math.trunc(self)

>>> 23. `__floor__(self)`: Parte entera hacia abajo (`math.floor(x)`).
    def __floor__(self: object) -> object:
        return math.floor(self)

>>> 24. `__ceil__(self)`: Parte entera hacia arriba (`math.ceil(x)`).
    def __ceil__(self: object) -> object:
        return math.ceil(self)

>>> 25. `__eq__(self, other)`: Igualdad (`==`).
    def __eq__(self: object, other: object) -> object:
        return self == other

>>> 26. `__ne__(self, other)`: Desigualdad (`!=`).
    def __ne__(self: object, other: object) -> object:
        return self != other

>>> 27. `__lt__(self, other)`: Menor que (`<`).
    def __lt__(self: object, other: object) -> object:
        return self < other

>>> 28. `__le__(self, other)`: Menor o igual que (`<=`).
    def __le__(self: object, other: object) -> object:
        return self <= other

>>> 29. `__gt__(self, other)`: Mayor que (`>`).
    def __gt__(self: object, other: object) -> object:
        return self > other

>>> 30. `__ge__(self, other)`: Mayor o igual que (`>=`).
    def __ge__(self: object, other: object) -> object:
        return self >= other

>>> 31. `__contains__(self, item)`: Verifica si un elemento está en el objeto (`in`).
    def __contains__(self: object, item: object) -> object:
        return item in self

>>> 32. `__len__(self)`: Longitud del objeto (`len()`).
    def __len__(self: object) -> object:
        return len(self)

>>> 33. `__getitem__(self, key)`: Acceso a elementos mediante índices (`[]`).
    def __getitem__(self: object, key: object) -> object:
        return self[key]

>>> 34. `__setitem__(self, key, value)`: Asignación de elementos mediante índices (`obj[key] = value`).
    def __setitem__(self: object, key: object, value: object) -> object:
        self[key] = value

>>> 35. `__delitem__(self, key)`: Eliminación de elementos mediante índices (`del obj[key]`).
    def __delitem__(self: object, key: object) -> object:
        del self[key]

>>> 36. `__iter__(self)`: Iterador para bucles (`iter()`).
    def __iter__(self: object) -> object:
        return iter(self)

>>> 37. `__next__(self)`: Obtener el próximo elemento de un iterador (`next()`).
    def __next__(self: object) -> object:
        return next(self)

>>> 38. `__reversed__(self)`: Iterador para reversa (`reversed()`).
    def __reversed__(self: object) -> object:
        return reversed(self)

>>> 39. `__call__(self[, args[, kwargs]])`: Llamada de objeto como función (`obj()`).
    def __call__(self: object, *args: object, **kwargs: object) -> object:
        return self(*args, **kwargs)

>>> 40. `__enter__(self)`: Contexto de entrada para el uso de `with`.
    def __enter__(self: object) -> object:
        return self

>>> 41. `__exit__(self, exc_type, exc_value, traceback)`: Contexto de salida para el uso de `with`.
    def __exit__(self: object, exc_type: object, exc_value: object, traceback: object) -> object:
        pass

>>> 42. `__str__(self)`: Representación de cadena amigable para humanos (`str()`).
    def __str__(self: object) -> object:
        return str(self)

>>> 43. `__repr__(self)`: Representación de cadena detallada para desarrolladores (`repr()`).
    def __repr__(self: object) -> object:
        return repr(self)
    
>>> 44. `__hash__(self)`: Valor hash para el objeto (`hash()`).
    def __hash__(self: object) -> object:
        return hash(self)
    
>>> 45. `__bool__(self)`: Evaluación booleana (`bool()`).
    def __bool__(self: object) -> object:
        return bool(self)

>>> 46. `__iadd__(self, other)`: Sobrecarga del operador de suma y asignación (`+=`).
    def __iadd__(self: object, other: object) -> object:
        return self += other

>>> 47. `__isub__(self, other)`: Sobrecarga del operador de resta y asignación (`-=`).
    def __isub__(self: object, other: object) -> object:
        return self -= other

>>> 48. `__imul__(self, other)`: Sobrecarga del operador de multiplicación y asignación (`*=`).
    def __imul__(self: object, other: object) -> object:
        return self *= other

>>> 49. `__itruediv__(self, other)`: Sobrecarga del operador de división y asignación (`/=`).
    def __itruediv__(self: object, other: object) -> object:
        return self /= other

>>> 50. `__ifloordiv__(self, other)`: Sobrecarga del operador de división entera y asignación (`//=`).
    def __ifloordiv__(self: object, other: object) -> object:
        return self //= other

>>> 51. `__imod__(self, other)`: Sobrecarga del operador de módulo y asignación (`%=`).
    def __imod__(self: object, other: object) -> object:
        return self %= other

>>> 52. `__ipow__(self, other[, modulo])`: Sobrecarga del operador de potenciación y asignación (`**=`).
    def __ipow__(self: object, other: object) -> object:
        return self **= other

>>> 53. `__ilshift__(self, other)`: Sobrecarga del operador de desplazamiento a la izquierda y asignación (`<<=`).
    def __ilshift__(self: object, other: object) -> object:
        return self <<= other

>>> 54. `__irshift__(self, other)`: Sobrecarga del operador de desplazamiento a la derecha y asignación (`>>=`).
    def __irshift__(self: object, other: object) -> object:
        return self >>= other

>>> 55. `__iand__(self, other)`: Sobrecarga del operador de bits AND y asignación (`&=`).
    def __iand__(self: object, other: object) -> object:
        return self &= other

>>> 56. `__ixor__(self, other)`: Sobrecarga del operador de bits XOR y asignación (`^=`).
    def __ixor__(self: object, other: object) -> object:
        return self ^= other

>>> 57. `__ior__(self, other)`: Sobrecarga del operador de bits OR y asignación (`|=`).
    def __ior__(self: object, other: object) -> object:
        return self |= other

>>> 58. `__dir__(self)`: Sobrecarga del operador dir(), que se llama para obtener la lista de nombres de atributos válidos del objeto.
    def __dir__(self: object) -> object:
        return ['atributo1', 'atributo2']

>>> 59. `__sizeof__(self)`: Sobrecarga del operador sys.getsizeof(), que devuelve el tamaño en bytes del objeto.
    def __sizeof__(self: object) -> object:
        return sys.getsizeof(self.atributo)


>>> 60. `__format__(self, format_spec)`: Sobrecarga del operador format(), utilizado para personalizar la representación de cadena del objeto.
    def __format__(self: object, format_spec: object) -> object:
        return f'Objeto formateado según {format_spec}'

>>> 61. `__del__(self)`: Sobrecarga del operador de eliminación (del), llamado cuando el objeto va a ser eliminado.
    def __del__(self: object) -> object:
        pass
"""
