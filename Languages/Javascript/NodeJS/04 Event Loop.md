# ***Event loop***

*El **event loop** en JavaScript es un mecanismo fundamental que permite a JavaScript realizar operaciones no bloqueantes, a pesar de ser un lenguaje de un solo hilo. Esto es crucial para manejar tareas asincrónicas como IO (input/output) de ficheros, peticiones de red, timers, etc., sin bloquear la ejecución del código. A continuación, se explica detalladamente cómo funciona el event loop a bajo nivel.*

## ***Conceptos Básicos***

1. **Single-threaded:**
   - *JavaScript en el navegador y Node.js se ejecuta en un solo hilo. Esto significa que en cualquier momento dado, solo una instrucción puede ser ejecutada.*

2. **Call Stack (Pila de Llamadas):**
   - *Es una estructura de datos que registra las funciones que se están ejecutando en el momento, siguiendo la regla de `LIFO` (Last In, First Out).*

3. **Heap:**
   - *Es un área de memoria donde se almacenan objetos y variables dinámicos.*

4. **Queue (Cola):**
   - *Es una lista de mensajes o tareas que están esperando para ser procesadas. Cada mensaje tiene una función asociada que debe ejecutarse.*

### ***Funcionamiento del Event Loop***

1. **Inicio:**
   - *Cuando ejecutas un programa en JavaScript, todas las funciones se colocan en la **call stack** y se ejecutan secuencialmente.*

2. **Ejecutando Código Sincrónico:**
   - *El código sincrónico se ejecuta de arriba hacia abajo, agregando y quitando funciones de la call stack.*

3. **Manejo de Código Asincrónico:**
   - *Cuando se encuentra una operación asincrónica (como una solicitud HTTP o una lectura de fichero), el motor de JavaScript delega esta tarea al entorno (como el navegador o Node.js), que maneja estas operaciones en segundo plano.*

4. **Callback Queue (Cola de Tareas):**
   - *Una vez que las operaciones asincrónicas completan su tarea, las funciones de callback asociadas se colocan en la callback queue.*

5. **El Event Loop:**
   - *El event loop es un proceso continuo que monitorea tanto la call stack como la callback queue.*
   - *Si la call stack está vacía, el event loop toma la primera función de la callback queue y la empuja a la call stack para ser ejecutada.*
   - *Este proceso continúa indefinidamente, asegurando que todas las tareas asincrónicas se manejen sin bloquear el hilo principal.*

### ***Pasos Detallados del Event Loop***

1. **Call Stack Inicial:**
   - *La ejecución comienza con el código principal, que se coloca en la call stack.*
   - *Se ejecutan todas las instrucciones sincrónicas.*

2. **Operaciones Asincrónicas:**
   - *Cuando se encuentra una operación asincrónica, como `setTimeout`, `fetch`, `readFile`, etc., esta se delega al entorno del navegador o Node.js.*
   - *La función principal continúa ejecutándose sin esperar a que estas operaciones terminen.*

3. **Cola de Tareas (Task Queue):**
   - *Una vez que una operación asincrónica completa su tarea, el callback correspondiente se coloca en la task queue.*
   - *Las operaciones asincrónicas no interrumpen el flujo principal del programa.*

4. **Event Loop en Acción:**
   - *El event loop verifica constantemente la call stack y la task queue.*
   - *Si la call stack está vacía (es decir, todas las funciones sincrónicas han terminado), el event loop toma la primera tarea de la task queue y la coloca en la call stack.*
   - *La tarea se ejecuta y este ciclo se repite.*

5. **Repetición del Ciclo:**
   - *Este proceso se repite continuamente, lo que permite que el código JavaScript maneje múltiples tareas de manera eficiente sin bloquear el hilo principal.*

### ***Ejemplo Ilustrativo***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@pro

console.log('Inicio');

setTimeout(() => {
    console.log('Tarea Asincrónica');
}, 2000);

console.log('Fin');
```

#### ***Proceso de Ejecución***

1. **Call Stack:**
   - *`console.log('Inicio')` se coloca en la call stack y se ejecuta, imprimiendo `Inicio`.*
   - *`setTimeout` se coloca en la call stack. El navegador gestiona el temporizador y la función de callback asociada se coloca en la task queue después de 2000 ms.*
   - *`console.log('Fin')` se coloca en la call stack y se ejecuta, imprimiendo `Fin`.*

2. **Event Loop:**
   - *El event loop observa que la call stack está vacía después de que `console.log('Fin')` se ejecuta.*
   - *Después de 2000 ms, la función de callback de `setTimeout` se coloca en la task queue.*
   - *El event loop mueve la función de callback de la task queue a la call stack.*
   - *La función de callback se ejecuta, imprimiendo `Tarea Asincrónica`.*

### ***Importancia del Event Loop***

- ***No Bloqueo:***
  - *Permite que JavaScript maneje operaciones de larga duración como IO sin bloquear el hilo principal.*
- ***Interactividad:***
  - *Mantiene la UI receptiva en aplicaciones web, permitiendo que se respondan eventos de usuario mientras se ejecutan tareas en segundo plano.*
- ***Eficiencia:***
  - *Mejora el rendimiento general de las aplicaciones al permitir la ejecución paralela de múltiples tareas asincrónicas.*

El event loop es esencial para entender cómo JavaScript maneja la concurrencia y la asincronía, lo que es crucial para escribir aplicaciones eficientes y receptivas.
