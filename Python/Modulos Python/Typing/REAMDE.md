<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***El módulo `typing` en Python proporciona soporte para anotaciones de tipo, lo que ayuda a especificar qué tipo de datos se espera en las variables, parámetros y funciones. Esto mejora la legibilidad del código y facilita la detección de errores antes de la ejecución. A continuación, se detalla el propósito de varios tipos y herramientas del módulo `typing`, junto con ejemplos de su uso.***

## ***Documentación del Código Python***

*Este proyecto demuestra el uso de diferentes tipos de datos en Python, así como estructuras de datos avanzadas y ejemplos de manipulación de datos utilizando funciones integradas como `map` y `filter`. A continuación, se proporciona una descripción detallada del código y sus componentes.*

## ***Autor***

- **Nombre:** *Daniel Benjamin Perez Morales*
- **GitHub:** **[D4nitrix13](https://github.com/D4nitrix13 "https://github.com/D4nitrix13")**
- **Email:** *`danielperezdev@proton.me`*

## ***Descripción***

**Este script Python ilustra cómo trabajar con varios tipos de datos y estructuras en Python, incluyendo:**

- *Tipos de datos básicos.*
- *Estructuras de datos de un solo tipo.*
- *Estructuras de datos de múltiples tipos.*
- *Ejemplos de uso de funciones integradas como `map` y `filter`.*
- *Ejemplos de estructuras de datos anidadas y opcionales.*

## ***Tipos de Datos***

**El código incluye ejemplos de los siguientes tipos de datos básicos:**

- **Cadena de texto (`str`):** *Representa texto. Ejemplo: `"Daniel"`*
- **Entero (`int`):** *Representa números enteros. Ejemplo: `18`*
- **Número de punto flotante (`float`):** *Representa números con decimales. Ejemplo: `20.0`*
- **Número complejo (`complex`):** *Representa números con una parte real e imaginaria. Ejemplo: `10j`*
- **Booleano (`bool`):** *Representa valores `True` o `False`. Ejemplo: `True`*
- **Ningún valor (`None`):** *Representa la ausencia de un valor. Ejemplo: `None`*

## ***Estructuras De Datos De Un Solo Tipo***

**El código muestra cómo definir y usar listas, tuplas, conjuntos y diccionarios con un solo tipo de datos:**

- **Listas (`List`):** *Colecciones ordenadas y mutables. Ejemplos: `List[str]`, `List[int]`*
- **Tuplas (`Tuple`):** *Colecciones ordenadas e inmutables. Ejemplos: `Tuple[str, str]`, `Tuple[int, int]`*
- **Conjuntos (`Set`):** *Colecciones desordenadas y mutables de elementos únicos. Ejemplos: `Set[str]`, `Set[int]`*
- **Diccionarios (`Dict`):** *Colecciones desordenadas y mutables de pares clave-valor. Ejemplos: `Dict[str, str]`, `Dict[int, int]`*

## ***Estructuras De Datos De Múltiples Tipos***

**El código utiliza `Union` para permitir que una variable pueda ser de varios tipos. Ejemplos:**

- **Lista con múltiples tipos (`List[Union[str, int, float, complex, bool, None]]`):** *Puede contener elementos de diferentes tipos.*
- **Tupla con múltiples tipos (`Tuple[Union[str, int, float, complex, bool, None], ...]`):** *Puede contener elementos de diferentes tipos.*
- **Conjunto con múltiples tipos (`Set[Union[str, int, float, complex, bool, None]]`):** *Puede contener elementos de diferentes tipos.*
- **Diccionario con múltiples tipos (`Dict[Union[str, int, float, complex, bool, None], Union[str, int, float, complex, bool, None]]`):** *Puede contener claves y valores de diferentes tipos.*

## ***Ejemplos Adicionales***

- **Listas anidadas:** *Listas que pueden contener tuplas o conjuntos. Ejemplo: `listaAnidada`*
- **Tuplas anidadas:** *Tuplas que pueden contener otros tipos de colecciones. Ejemplo: `setAnidado`*
- **Diccionarios anidados:** *Diccionarios que contienen otros tipos de colecciones. Ejemplo: `diccionarioAnidado`*
- **Variables opcionales:** *Variables que pueden ser de un tipo específico o `None`. Ejemplos: `opcionalStr`, `opcionalInt`*

## ***Funciones Integradas***

- **`map`:** *Aplica una función a cada elemento de una lista y devuelve un iterador. Ejemplo: `variableMap`*
- **`filter`:** *Filtra los elementos de un iterador según una función de predicado. Ejemplo: `variableFilter`*

## ***Ejemplo de Función***

**La función `error` lanza una excepción con una descripción del error:**

```python
def error(*, descripcionError: str) -> NoReturn:
   """
   Función que lanza una excepción con la descripción del error.

   :param descripcionError: Descripción del error que se incluirá en la excepción.
   :raises ValueError: Siempre lanza una excepción con el mensaje proporcionado.
   """
   raise ValueError(descripcionError)
```

## ***Ejecución***

**El código final imprime listas mapeadas y filtradas en la salida estándar:**

```python
print(listaMapeada, end="\n", file=stdout)
print(listaFiltrada, end="\n", file=stdout)
```

*Este script ofrece una visión integral de cómo manejar tipos de datos, estructuras de datos y funciones en Python. Puedes modificar y expandir este código para adaptarlo a tus necesidades específicas.*
