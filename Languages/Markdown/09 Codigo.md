<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# Codigo

```python
# Ejemplo python
"""
>>> Ejemplo
"""
import os

def borrar() -> None: 
    os.system(command="cls" if os.name == "nt" else "clear")
    return None

class Autor():
    def __init__(self: 'Autor') -> None:
        self.__nombre: str = "Daniel Perez"
        self.__edad: int = 18
        self.__nacionalidad: str = "Nicaraguense"
        self.__habilidad: str "Programar"

    @property
    def habilidad(self: 'Autor') -> str: return self.__habilidad

    @habilidad.setter
    def habilidad(self: 'Autor', nueva_habilidad: str) -> None: self.__habilidad = nueva_habilidad

    @habilidad.deleter
    def habilidad(self: 'Autor') -> None: del self.__habilidad

if __name__ == "__main__":
    borrar()
    Danitrix: Autor = Autor()
    Danitrix.habilidad = "Musico"
    print(Danitrix.habilidad, end = "\n")
```

```Java
// Ejemplo Java
Package Directorio.Mardown;
public class Ejemplo{
    public Ejemplo(){

    }public static void main(String[] args){
        System.out.println("Hola esto es un ejemplo");
    }
}
```

```Javascript
// Ejemplo Javascript
console.log("Ejemplo javascript");
```

```Typescript
// Ejemplo Typescript
console.log("Ejemplo Typescript");
```

```C
/* Ejemplo en c*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define NUMERO 13

int main(int argc, char *argv[]) {
    printf("Hola Mundo\n");

    printf("Número de argumentos: %d\n", argc);
    for (short int i = 0; i < argc; i++) {
        printf("Argumento %d: %s\n", i, argv[i]);
    }

    return 0;
}
```
