<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Qué es un callback y cómo funciona en el contexto de las operaciones asíncronas en Node.js**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Importación del módulo 'fs' para operaciones de sistema de ficheros
const fs = require('node:fs');

console.log('Leyendo el primer fichero...');

// Operación asíncrona para leer el contenido del primer fichero './fichero.txt'
fs.readFile('./fichero.txt', 'utf-8', (err, text) => {
    // Callback: una función que se ejecuta después de que se completa una tarea asíncrona
    // 'err' es el posible error que ocurrió durante la operación
    // 'text' es el contenido del fichero leído, en formato UTF-8
    if (err) {
        console.error('Error al leer el primer fichero:', err);
        return;
    }
    console.log('Primer texto:', text);
});

console.log('--> Haciendo cosas mientras lee el fichero...');

console.log('Leyendo el segundo fichero...');
// Operación asíncrona para leer el contenido del segundo fichero './fichero2.txt'
fs.readFile('./fichero2.txt', 'utf-8', (err, text) => {
    // Callback: una función que se ejecuta después de que se completa una tarea asíncrona
    // 'err' es el posible error que ocurrió durante la operación
    // 'text' es el contenido del fichero leído, en formato UTF-8
    if (err) {
        console.error('Error al leer el segundo fichero:', err);
        return;
    }
    console.log('Segundo texto:', text);
});

/*
Lo bueno de esto es que no sabes qué tarea terminará primero.
Salida esperada podría ser en cualquier orden:
node "fs readFile Asyncrono.cjs"
Leyendo el primer fichero...
--> Haciendo cosas mientras lee el fichero...
Leyendo el segundo fichero...
Primer texto: Hola Mundo

Segundo texto:
Nombre: Daniel
Apellido: Perez
Edad: 18 años
Profesión: Programador

o también podría ser:

node "fs readFile Asyncrono.cjs"
Leyendo el primer fichero...
--> Haciendo cosas mientras lee el fichero...
Leyendo el segundo fichero...
Segundo texto:
Nombre: Daniel
Apellido: Perez
Edad: 18 años
Profesión: Programador

Primer texto: Hola Mundo
*/
```

## ***Explicación y Comentarios***

1. **Uso de `require('node:fs')`:**
   - **`const fs = require('node:fs');`:** *Importa el módulo `'fs'` de Node.js para realizar operaciones de sistema de ficheros. Se usa `'node:'` antes del nombre del módulo para versiones de Node.js 16 y superiores.*

2. **Operaciones Asíncronas (`fs.readFile()`):**
   - **`fs.readFile('./fichero.txt', 'utf-8', (err, text) => { ... });`:** *`fs.readFile()` es una función asíncrona que toma un callback como tercer parámetro. Este callback se ejecuta cuando se completa la operación de lectura del fichero. `err` es el posible error que puede ocurrir durante la lectura, y `text` es el contenido del fichero leído en formato UTF-8.*

3. **Callback:**
   - **Definición:** *Un callback es una función que se pasa como argumento a otra función (en este caso, `fs.readFile()`). Se ejecuta después de que se completa una tarea asíncrona para manejar el resultado o el error de la operación.*
   - **Función en el Ejemplo:** *El callback en este caso maneja la lectura del fichero y muestra el contenido (`text`) o maneja errores (`err`) si ocurren.*

4. **Ejecución Secuencial vs No Determinística:**
   - **Comentario:** *`--> Haciendo cosas mientras lee el fichero...`. Esto indica que otras operaciones pueden continuar mientras se espera la respuesta de la lectura del fichero. En el caso de operaciones asíncronas, como `fs.readFile()`, no se puede determinar qué operación se completará primero debido a su naturaleza no determinística.*

5. **Manejo de Errores:**
   - **Comprobación de `err`:** *Antes de usar el resultado (`text`), es importante verificar si `err` existe para manejar posibles errores que puedan ocurrir durante la lectura del fichero.*

### ***Importancia de las Operaciones Asíncronas***

- **Mejora de la Eficiencia:** *Las operaciones asíncronas permiten que el programa continúe ejecutándose sin bloquearse mientras espera que se completen tareas de E/S, como la lectura de ficheros.*
  
- **Manejo de Múltiples Tareas:** *Son ideales para entornos donde se deben manejar múltiples solicitudes simultáneamente, ya que permiten que el programa maneje otras tareas mientras espera las operaciones de E/S.*
