<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Los tres casos de importación en Node.js usando los diferentes tipos de ficheros y sus extensiones correspondientes: `.js`, `.cjs`, y `.mjs`.***

## ***Caso 1: Importación desde un fichero `index.js` (CommonJS)***

### ***Mejora y Explicación***

**Cuando estás trabajando con ficheros `index.js` en Node.js, puedes importar el fichero de las siguientes maneras:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// index.js

// Definición de una función para exportar
function funcion() {
  console.log("Función ejecutada desde index.js");
}

// Exportación de la función
module.exports = { funcion };
```

#### ***Importación en otro fichero***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// Otro fichero que importa desde index.js

// Importación del módulo desde index.js (CommonJS)
const { funcion } = require("./index");
// o const { funcion } = require("./index.js");

// Uso de la función importada
funcion();
```

- **Explicación:**
  - *En ficheros `index.js` en Node.js (formato CommonJS), puedes importar el fichero tanto con `require("./index")` como con `require("./index.js")`. Ambas formas son válidas y funcionan de la misma manera debido a que Node.js asume automáticamente la extensión `.js` para ficheros CommonJS.*

## ***Caso 2: Importación desde un fichero `index.cjs` (CommonJS explícito)***

## ***Mejora y Explicación:***

**Cuando el fichero tiene explícitamente la extensión `.cjs`, la importación es ligeramente diferente:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// index.cjs

// Definición de una función para exportar
function funcion() {
  console.log("Función ejecutada desde index.cjs");
}

// Exportación de la función
module.exports = { funcion };
```

### ***Importación en otro fichero:***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// Otro fichero que importa desde index.cjs

// Importación del módulo desde index.cjs (CommonJS explícito)
const { funcion } = require("./index.cjs");

// Uso de la función importada
funcion();
```

- **Explicación:**
  - *Cuando el fichero tiene la extensión `.cjs`, en Node.js debes importarlo especificando la extensión completa en `require("./index.cjs")`. Node.js necesita esta especificación explícita para diferenciarlo de otros tipos de ficheros.*

### ***Caso 3: Importación desde un fichero `index.mjs` (ES Modules)***

### ***`Mejora y Explicación`***

**Cuando estás utilizando ficheros `.mjs` en Node.js, que son módulos de ECMAScript, la sintaxis de importación es diferente:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// index.mjs

// Definición de una función para exportar
function funcion() {
  console.log("Función ejecutada desde index.mjs");
}

// Exportación de la función
export { funcion };
```

### ***`Importación en otro fichero`***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// Otro fichero que importa desde index.mjs

// Importación del módulo desde index.mjs (ES Modules)
import { funcion } from "./index.mjs";

// Uso de la función importada
funcion();
```

- **Explicación:**
  - *En ficheros `.mjs` (ES Modules), se utiliza la palabra clave `import` para importar funciones o variables exportadas desde otros módulos. La extensión `.mjs` es necesaria para que Node.js reconozca el fichero como un módulo de ECMAScript.*
  - *No se puede omitir la extensión `.mjs` al importar, ya que Node.js requiere la especificación completa (`import { funcion } from "./index.mjs"`).*

### ***Resumen***

- **CommonJS (`index.js` y `index.cjs`):** *Se puede importar con o sin la extensión `.js`, pero en ficheros explícitamente `.cjs`, se debe usar la extensión completa en `require`.*
- **ES Modules (`index.mjs`):** *Se debe importar usando la palabra clave `import` y la extensión `.mjs` completa.*

- *Esta estructura te permite manejar de manera efectiva los diferentes tipos de ficheros y sus respectivas importaciones en Node.js, asegurando la compatibilidad y el correcto funcionamiento del código en el entorno de desarrollo.*
