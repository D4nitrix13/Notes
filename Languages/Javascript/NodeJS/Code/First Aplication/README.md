<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Index***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Importamos el módulo 'fs/promises' para trabajar con el sistema de ficheros usando Promesas
const fs = require('node:fs/promises');

// Utilizamos 'fs.readdir' para leer el contenido del directorio actual ('.')
// Este método devuelve una Promesa, por lo que usamos '.then' y '.catch' para manejar el resultado y los errores
fs.readdir('.')
    .then(files => {
        // 'files' es un array con los nombres de los ficheros y directorios en el directorio actual
        // Usamos 'forEach' para iterar sobre cada fichero/directorio y lo imprimimos en la consola
        files.forEach(file => {
            console.log(file);
        });
    })
    .catch(err => {
        // Si ocurre un error al leer el directorio, se captura en este bloque '.catch'
        // Verificamos si 'err' existe y, si es así, imprimimos un mensaje de error en la consola
        if (err) {
            console.error('Error al leer el directorio:', err);
            return;
        }
    });

// Forma con callbacks
// Importamos el módulo 'fs' para trabajar con el sistema de ficheros usando callbacks
// const fs = require('node:fs')

// Usamos 'fs.readdir' para leer el contenido del directorio actual ('./')
// Este método toma un callback que maneja el error (si ocurre) y el resultado
// fs.readdir("./", (err, files) => {
//     // Si ocurre un error, 'err' contendrá la información sobre el error
//     if (err) {
//         // Imprimimos un mensaje de error en la consola
//         console.error("Error al leer el directorio:", err);
//     }
//     // 'files' es un array con los nombres de los ficheros y directorios en el directorio actual
//     // Usamos 'forEach' para iterar sobre cada fichero/directorio y lo imprimimos en la consola
//     files.forEach(file => {
//         console.log(file);
//     });
// })
```

## ***Explicación***

1. **Uso de Promesas con `fs/promises`:**
    - ***Importación del Módulo:** Se importa `fs/promises` para usar las funciones de sistema de ficheros basadas en Promesas.*
    - ***Lectura de Directorio:** `fs.readdir('.')` lee el contenido del directorio actual y devuelve una Promesa.*
    - ***Manejo de Resultados con `.then`:** Si la operación es exitosa, `.then` recibe un array `files` que contiene los nombres de los ficheros y directorios. Usamos `forEach` para imprimir cada nombre en la consola.*
    - ***Manejo de Errores con `.catch`:** Si ocurre un error, se captura en `.catch`, donde se verifica y se imprime un mensaje de error.*

2. **Uso de Callbacks con `fs`:**
    - ***Importación del Módulo:** Se importa `fs` para usar las funciones de sistema de ficheros basadas en callbacks.*
    - ***Lectura de Directorio:** `fs.readdir('./', (err, files)` lee el contenido del directorio actual. Este método toma un callback con dos parámetros: `err` y `files`.*
    - ***Manejo de Errores:** Si `err` contiene un error, se imprime un mensaje de error.*
    - ***Procesamiento de Resultados:** Si no hay error, `files` contiene los nombres de los ficheros y directorios. Usamos `forEach` para imprimir cada nombre en la consola.*

### ***Diferencias Entre Promesas y Callbacks***

- ***Promesas:***
  - *Permiten un manejo más claro y estructurado de operaciones asincrónicas.*
  - *Facilitan el encadenamiento de operaciones asincrónicas y el manejo de errores.*

- ***Callbacks:***
  - *Son la forma tradicional de manejar operaciones asincrónicas en Node.js.*
  - *Pueden llevar a anidamientos complicados y dificultar la lectura del código (conocido como "callback hell").*

- *Ambas técnicas son útiles y válidas en diferentes contextos, y el uso de una sobre otra puede depender de las preferencias del desarrollador y de la complejidad de la aplicación.*
