<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# *Cómo convertir las funciones de callback de Node.js a funciones que devuelven promesas usando `util.promisify`, y cómo usar esas promesas para realizar operaciones asíncronas de lectura de ficheros:*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Esto sólo en los módulos nativos
// que no tienen promesas nativas

// Importación del módulo 'fs' para operaciones de sistema de ficheros
const fs = require('node:fs');

// Importación del módulo 'util' para promisificar funciones
const { promisify } = require('node:util');

// Promisificar la función fs.readFile
const readFilePromise = promisify(fs.readFile);

console.log('Leyendo el primer fichero...');

// Utilizando la función promisificada para leer el primer fichero './fichero.txt'
readFilePromise('./fichero.txt', 'utf-8')
    .then((text) => {
        console.log('Primer texto:', text);
    })
    .catch((err) => {
        console.error('Error al leer el primer fichero:', err);
    });

console.log('--> Haciendo cosas mientras lee el fichero...');

console.log('Leyendo el segundo fichero...');

// Utilizando la función promisificada para leer el segundo fichero './fichero2.txt'
readFilePromise('./fichero2.txt', 'utf-8')
    .then((text) => {
        console.log('Segundo texto:', text);
    })
    .catch((err) => {
        console.error('Error al leer el segundo fichero:', err);
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

1. **Promisificación con `promisify`:**
   - **`const { promisify } = require('node:util');`:** *Importa la función `promisify` del módulo `util` de Node.js. Esta función convierte funciones de estilo callback en funciones que devuelven promesas.*

2. **Promisificación de `fs.readFile`:**
   - **`const readFilePromise = promisify(fs.readFile);`:** *Usa `promisify` para convertir la función de callback `fs.readFile` en una función que devuelve una promesa, llamada `readFilePromise`.*

3. **Uso de Promesas en Lugar de Callbacks:**
   - **`readFilePromise('./fichero.txt', 'utf-8').then((text) => { ... })`:** *Utiliza `readFilePromise` para leer el contenido del fichero `./fichero.txt`. La promesa se resuelve con el texto del fichero, que se maneja dentro del `.then()`.*

4. **Manejo de Errores con `.catch()`:**
   - **`.catch((err) => { ... })`:** *Maneja cualquier error que ocurra durante la lectura del fichero utilizando `.catch()` después de `.then()` para capturar y manejar errores de manera efectiva.*

5. **Ejecución No Determinística:**
   - **Comentario:** *`Lo bueno de esto es que no sabes qué tarea terminará primero.`. Este comentario resalta que las operaciones asíncronas pueden completarse en cualquier orden, lo que es beneficioso para la eficiencia y paralelización en aplicaciones Node.js.*

### ***Ventajas de Promisificar Operaciones***

- **Manejo más limpio de errores:** *El uso de promesas y `async/await` simplifica la gestión de errores en comparación con los callbacks anidados.*
  
- **Compatibilidad con Estructuras de Control Modernas:** *Facilita el uso de estructuras de control modernas como `async/await`, lo que mejora la legibilidad y mantenibilidad del código.*

- **Mejora en la Organización del Código:** *Permite una organización más clara y modular del código, al evitar la pirámide de la muerte (callback hell) que puede ocurrir con múltiples callbacks anidados.*

- *Esta conversión a promesas con `util.promisify` es una práctica común en Node.js para mejorar la legibilidad y el manejo de errores en operaciones asíncronas, manteniendo un código más limpio y estructurado.*
