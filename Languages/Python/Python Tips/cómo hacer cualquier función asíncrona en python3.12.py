#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# pip3 install requests
from sys import stdout
from typing import Dict, Union
from requests import Response, get

from asyncio import Task, create_task, to_thread, run

# Función asíncrona para obtener el estado de una URL
async def fetch_status(*, url: str) -> Dict[str, Union[int, str]]:
    # Imprimir el URL que se está consultando
    print(f"fetching status for: {url}", end = "\n", file = stdout)
    
    # Ejecutar la solicitud GET en un hilo separado y esperar su resultado
    response: Response = await to_thread(get, url, None)
    
    # Imprimir cuando la solicitud se haya completado
    print("Done!", end = "\n", file = stdout)

    # Retornar el estado y la URL en un diccionario
    return {"status": response.status_code, "url": url}

# Función principal asíncrona
async def main() -> None:
    # Crear tareas asíncronas para consultar dos URLs concurrentemente
    apple_task: Task[Dict[str, Union[int, str]]] = create_task(coro = fetch_status(url = "https://www.apple.com/"))
    google_task: Task[Dict[str, Union[int, str]]] = create_task(coro = fetch_status(url = "https://www.google.com"))

    # Esperar a que ambas tareas se completen y obtener los resultados
    apple_status: Dict[str, Union[int, str]] = await apple_task
    google_status: Dict[str, Union[int, str]] = await google_task

    # Imprimir los resultados de las consultas
    print(apple_status, end = "\n", file = stdout)
    print(google_status, end = "\n", file = stdout)

    return None

# Ejecutar la función principal asíncrona en el bucle de eventos
if __name__ == "__main__":
    run(main = main())

"""
Tu código en Python 3.12 está utilizando `asyncio` para realizar tareas asíncronas. Aquí hay una explicación detallada y algunos puntos clave sobre cómo hacer funciones asíncronas en Python, y una revisión del código proporcionado.

### Explicación de Funciones Asíncronas en Python

Las funciones asíncronas en Python se definen utilizando la palabra clave `async`. Estas funciones permiten realizar operaciones de manera no bloqueante, lo que es especialmente útil para operaciones de I/O (como solicitudes de red) que pueden llevar tiempo en completarse.

### Componentes Clave del Código

1. **Importaciones y Configuración:**
   - `to_thread`: Permite ejecutar funciones sincrónicas en un hilo separado y obtener sus resultados de manera asíncrona.
   - `create_task`: Crea una tarea asíncrona que se ejecutará concurrentemente.
   - `run`: Ejecuta la función principal asíncrona en el bucle de eventos de `asyncio`.

2. **Función `fetch_status`:**
   - Esta función asíncrona usa `await` para llamar a `to_thread`, que a su vez ejecuta la función `get` de la biblioteca `requests` en un hilo separado.
   - La función `fetch_status` realiza una solicitud HTTP GET para obtener el estado del URL proporcionado y devuelve un diccionario con el estado y la URL.

3. **Función `main`:**
   - Crea tareas asíncronas para consultar dos URLs (Apple y Google) de manera concurrente.
   - Usa `await` para esperar la finalización de ambas tareas y luego imprime los resultados.

4. **Ejecución del Programa:**
   - La función `main` es ejecutada por el bucle de eventos de `asyncio` usando `run(main())`.

### Código Mejorado con Comentarios

Aquí está tu código con comentarios detallados para explicar cada parte:

```python
#!/usr/bin/env python3

# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# pip3 install requests
from sys import stdout
from typing import Dict, Union
from requests import Response, get

from asyncio import Task, create_task, to_thread, run

# Función asíncrona para obtener el estado de una URL
async def fetch_status(*, url: str) -> Dict[str, Union[int, str]]:
    # Imprimir el URL que se está consultando
    print(f"fetching status for: {url}", end = "\n", file = stdout)
    
    # Ejecutar la solicitud GET en un hilo separado y esperar su resultado
    response: Response = await to_thread(get, url, None)
    
    # Imprimir cuando la solicitud se haya completado
    print("Done!", end = "\n", file = stdout)

    # Retornar el estado y la URL en un diccionario
    return {"status": response.status_code, "url": url}

# Función principal asíncrona
async def main() -> None:
    # Crear tareas asíncronas para consultar dos URLs concurrentemente
    apple_task: Task[Dict[str, Union[int, str]]] = create_task(coro = fetch_status(url = "https://www.apple.com/"))
    google_task: Task[Dict[str, Union[int, str]]] = create_task(coro = fetch_status(url = "https://www.google.com"))

    # Esperar a que ambas tareas se completen y obtener los resultados
    apple_status: Dict[str, Union[int, str]] = await apple_task
    google_status: Dict[str, Union[int, str]] = await google_task

    # Imprimir los resultados de las consultas
    print(apple_status, end = "\n", file = stdout)
    print(google_status, end = "\n", file = stdout)

    return None

# Ejecutar la función principal asíncrona en el bucle de eventos
if __name__ == "__main__":
    run(main)
```

### Explicación Adicional

- **`to_thread`:** Convierte una función sincrónica (como `get` de `requests`) en una función que se puede ejecutar de manera asíncrona en un hilo separado. Esto es útil porque `requests` no es asíncrono por sí mismo, y `to_thread` ayuda a evitar que el código bloquee el hilo principal.
  
- **`create_task`:** Permite que la función asíncrona `fetch_status` se ejecute en paralelo con otras tareas asíncronas. Esto permite que ambas solicitudes HTTP se realicen al mismo tiempo, en lugar de esperar a que una termine antes de comenzar la otra.

- **`run`:** Ejecuta la función asíncrona `main` en el bucle de eventos de `asyncio`. Esto es necesario para iniciar el procesamiento asíncrono.

Este enfoque permite realizar tareas de red o I/O de manera eficiente sin bloquear el hilo principal, mejorando la eficiencia y el rendimiento del programa.
"""

"""
En el contexto de la informática y la programación, **I/O** significa **Input/Output**. Se refiere a los mecanismos que permiten a un sistema o programa interactuar con el mundo exterior, intercambiando datos con otros sistemas, usuarios, dispositivos o ficheros. Aquí está una explicación más detallada:

### 1. **Input (Entrada)**

**Entrada** se refiere a cualquier dato o señal que un programa recibe de una fuente externa. Ejemplos de entrada incluyen:

- **Datos del Usuario:** Datos introducidos por el usuario a través de un teclado, ratón o interfaz gráfica.
- **Ficheros:** Datos leídos desde ficheros almacenados en un disco duro, SSD o en la nube.
- **Redes:** Datos recibidos a través de una red, como solicitudes HTTP desde un navegador web.
- **Sensores:** Datos provenientes de dispositivos de hardware como sensores en un dispositivo IoT (Internet de las cosas).

### 2. **Output (Salida)**

**Salida** se refiere a cualquier dato o señal que un programa envía a una fuente externa. Ejemplos de salida incluyen:

- **Pantalla:** Información mostrada en una pantalla o ventana gráfica.
- **Ficheros:** Datos escritos en ficheros en un disco o en la nube.
- **Redes:** Datos enviados a través de una red, como respuestas HTTP desde un servidor web.
- **Dispositivos:** Información enviada a dispositivos de hardware, como impresoras o altavoces.

### 3. **Ejemplos en Programación**

En programación, el manejo de I/O es crucial porque permite que los programas interactúen con el entorno. Ejemplos en diferentes contextos incluyen:

- **Lectura de Ficheros:** Leer datos de un fichero de texto o binario.
  ```python
  from io import TextIOWrapper
  from typing import Optional 
  file: Optional[TextIOWrapper] = None
  with open(file = r'file.txt', mode = 'r') as file:
      data = file.read()
  ```
  
- **Escritura de Ficheros:** Escribir datos en un fichero.
  ```python
  from io import TextIOWrapper
  from typing import Optional 
  
  file: Optional[TextIOWrapper] = None
  with open(file = r'file.txt', mode = 'w') as file:
      file.write('Hello, world!')
  ```

- **Interacción con el Usuario:** Leer entrada del usuario desde la consola.
  ```python
  userInput: str = str(input('Enter something: '))
  ```

- **Redes:** Hacer una solicitud HTTP para obtener datos de una página web.
  ```python
  from requests import Response, get
  response: Response = get(url = 'https://www.example.com')
  data: str = response.text
  ```

### 4. **I/O Bloqueante vs. No Bloqueante**

- **I/O Bloqueante:** El proceso se detiene mientras espera que la operación de I/O se complete. Por ejemplo, una lectura de fichero o una solicitud de red puede hacer que el programa se quede esperando hasta que la operación finalice.

- **I/O No Bloqueante:** El proceso puede continuar ejecutándose mientras se realiza la operación de I/O. Esto se logra a través de técnicas como la programación asíncrona o el uso de múltiples hilos. Permite que el programa realice otras tareas mientras espera que la operación de I/O se complete.

### 5. **Importancia en Programación**

El manejo eficiente de I/O es esencial para el rendimiento y la capacidad de respuesta de los programas, especialmente en aplicaciones que interactúan con usuarios, redes o sistemas de almacenamiento. La capacidad para manejar operaciones de I/O de manera asíncrona y concurrente puede mejorar significativamente la eficiencia y la experiencia del usuario en aplicaciones modernas.

En resumen, I/O es un concepto fundamental en programación que abarca cualquier tipo de operación que involucre la entrada y salida de datos entre un programa y su entorno.
"""
