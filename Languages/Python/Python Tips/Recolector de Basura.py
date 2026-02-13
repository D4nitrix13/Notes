#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

from gc import disable, collect, enable
from typing import Optional

# Desactiva el recolector de basura
disable()

# Crea algunos objetos y referencias circulares
class Node:
    def __init__(self: "Node") -> None:
        self.ref: Optional["Node"] = None
        return None

node1: Node = Node()
node2: Node = Node()
node1.ref = node2
node2.ref = node1

# Aquí, node1 y node2 forman un ciclo de referencia. 
# El recolector de basura puede limpiar esto cuando se vuelve a habilitar.

# Habilita el recolector de basura
enable()

# Fuerza la recolección de basura
collect()

"""
El recolector de basura (garbage collector) es una parte fundamental de la administración de memoria en lenguajes de programación que usan gestión automática de memoria, como Python. Su propósito principal es gestionar y liberar la memoria que ya no es utilizada por el programa, lo que ayuda a evitar fugas de memoria y optimizar el uso de recursos.

### Conceptos Básicos

1. **Gestión de Memoria:**
   - En los lenguajes de programación, la memoria se utiliza para almacenar datos y objetos creados durante la ejecución del programa. Esta memoria se asigna dinámicamente a medida que se crean nuevos objetos.

2. **Objetos No Referenciados:**
   - Los objetos en memoria pueden ser referenciados por otras partes del programa. Cuando ya no hay ninguna referencia a un objeto, se considera que es "no referenciado" y que el espacio de memoria que ocupaba puede ser reutilizado.

### ¿Cómo Funciona el Recolector de Basura?

El recolector de basura realiza varias tareas para gestionar la memoria:

1. **Detección de Objetos Inalcanzables:**
   - El recolector de basura identifica objetos que ya no están siendo referenciados por el programa. Estos objetos se consideran "inaccesibles" y, por lo tanto, pueden ser eliminados para liberar memoria.

2. **Estrategias de Recolección:**
   - Existen varias estrategias para la recolección de basura. Algunas de las más comunes incluyen:
     - **Recolección de Basura Basada en Contador de Referencias:** Cada objeto mantiene un contador que se incrementa cuando se crea una nueva referencia al objeto y se decrementa cuando se elimina una referencia. Cuando el contador llega a cero, el objeto se considera para la recolección.
     - **Recolección de Basura por Algoritmo de Marcado y Barrido:** Este algoritmo marca todos los objetos que están alcanzables desde las raíces del programa (por ejemplo, variables globales y locales) y luego barre (elimina) los objetos que no están marcados como alcanzables.

3. **Ciclo de Recolección:**
   - La recolección de basura puede ocurrir en diferentes momentos, como cuando el sistema detecta que se ha alcanzado un umbral de uso de memoria o en momentos específicos del ciclo de vida del programa.

### Ejemplo en Python

Python utiliza un recolector de basura basado en un conteo de referencias y un recolector de ciclos. Aquí está cómo funcionan:

1. **Conteo de Referencias:**
   - Python mantiene un contador de referencias para cada objeto. Cuando el contador llega a cero, el objeto se elimina automáticamente.

2. **Recolección de Ciclos:**
   - Además del conteo de referencias, Python incluye un recolector de ciclos que puede detectar y limpiar ciclos de referencia (situaciones en las que un grupo de objetos se refiere mutuamente y no son accesibles desde el programa).

### Ejemplo de Código en Python

```python
from gc import disable, collect, enable
from typing import Optional

# Desactiva el recolector de basura
disable()

# Crea algunos objetos y referencias circulares
class Node:
    def __init__(self: "Node") -> None:
        self.ref: Optional["Node"] = None
        return None

node1: Node = Node()
node2: Node = Node()
node1.ref = node2
node2.ref = node1

# Aquí, node1 y node2 forman un ciclo de referencia. 
# El recolector de basura puede limpiar esto cuando se vuelve a habilitar.

# Habilita el recolector de basura
enable()

# Fuerza la recolección de basura
collect()
```

### Ventajas del Recolector de Basura

- **Prevención de Fugas de Memoria:** Evita que la memoria se llene con objetos no utilizados.
- **Simplificación del Código:** Los programadores no tienen que gestionar manualmente la memoria.
- **Optimización Automática:** La recolección automática ayuda a mantener el rendimiento al liberar memoria no utilizada.

### Desventajas

- **Sobrecarga de Rendimiento:** El proceso de recolección de basura puede afectar el rendimiento del programa, especialmente si se realiza con frecuencia.
- **Incertidumbre en el Tiempo de Ejecución:** La recolección de basura puede ocurrir en momentos impredecibles, lo que puede afectar la consistencia del tiempo de ejecución en aplicaciones sensibles al tiempo.

En resumen, el recolector de basura es una herramienta crucial para la gestión automática de memoria en lenguajes de programación, que ayuda a mantener la eficiencia y evitar problemas relacionados con la memoria en el desarrollo de software.
"""