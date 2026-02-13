<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***FileSystem Asyn await cjs***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

// Fichero con extensión .cjs

// Aquí estamos importando la función `readFile` del módulo 'fs/promises' de Node.js, 
// que nos permite trabajar con operaciones de ficheros de manera asincrónica usando Promesas.
const { readFile } = require('node:fs/promises');

// Top-level await es una característica que permite usar 'await' en el nivel superior 
// de un módulo sin necesidad de envolverlo en una función asíncrona.
// Sin embargo, esta característica sólo está disponible en los módulos ECMAScript (ESM).
// En CommonJS (CJS), debemos usar una IIFE (Immediately Invoked Function Expression) para utilizar 'await'.

// IIFE (Immediately Invoked Function Expression) es una función que se ejecuta inmediatamente después de su creación.
// Aquí usamos una IIFE para poder utilizar 'await' dentro de un módulo CommonJS.
(async () => {
    console.log('Leyendo el primer fichero...');
    const text = await readFile('./fichero.txt', 'utf-8');
    console.log('primer texto:', text);

    console.log('--> Hacer cosas mientras lee el fichero...');

    console.log('Leyendo el segundo fichero...');
    const second_text = await readFile('./fichero2.txt', 'utf-8');
    console.log('segundo texto:', second_text);
})();

/*
Nota importante sobre el uso de punto y coma en JavaScript:
En JavaScript, es una buena práctica usar punto y coma al final de las declaraciones, especialmente antes de un IIFE.
Si no usamos el punto y coma, JavaScript podría interpretar el código de manera incorrecta, 
como si estuviéramos intentando ejecutar la IIFE inmediatamente después de la declaración del 'require', 
lo que resultaría en un error.

Ejemplo de lo que podría suceder sin punto y coma:
JavaScript podría pensar que estamos tratando de ejecutar el resultado del 'require' como una función, 
lo cual no es lo que queremos:

const { readFile } = require('node:fs/promises')(
   async () => {
      console.log('Leyendo el primer fichero...');
      const text = await readFile('./fichero.txt', 'utf-8');
      console.log('primer texto:', text);

      console.log('--> Hacer cosas mientras lee el fichero...');

      console.log('Leyendo el segundo fichero...');
      const second_text = await readFile('./fichero2.txt', 'utf-8');
      console.log('segundo texto:', second_text);
   }
)()

Para evitar esto, siempre debemos usar un punto y coma antes de una IIFE cuando no está separada por un bloque o declaración diferente.
*/
```

## ***Explicación y Mejora de Comentarios***

1. **Top-level await:**
   - *En módulos ECMAScript (ESM), se puede usar `await` directamente en el nivel superior del código, conocido como "top-level await".*
   - *En módulos CommonJS (CJS), esto no es posible. Para usar `await` en CJS, es necesario envolver el código en una función asíncrona o una IIFE (Immediately Invoked Function Expression).*

2. **IIFE (Immediately Invoked Function Expression):**
   - *Es una función que se ejecuta inmediatamente después de su creación.*
   - *Se usa comúnmente para crear un ámbito local y ejecutar código asincrónico en módulos CJS.*

3. **Punto y coma (`;`) en JavaScript:**
   - *Es importante usar punto y coma al final de las declaraciones, especialmente antes de una IIFE.*
   - *Si no se usa, JavaScript podría interpretar el código de manera incorrecta, pensando que la IIFE es una llamada de función inmediata del resultado del `require`, lo que causaría errores.*
