<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Fichero `index.cjs`***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// index.cjs
// Este fichero utiliza el sistema de módulos CommonJS (cjs) para importar y utilizar módulos.

// Importación de funciones desde el módulo 'module.cjs'.
// La variable que contiene las funciones importadas puede tener cualquier nombre, 
// pero es recomendable utilizar un nombre descriptivo relacionado con el módulo.
const { suma, restar, multiplicacion } = require('./module.cjs');

// Uso de las funciones importadas
console.log('Suma (2 + 3):', suma(2, 3));                 // Imprime el resultado de la suma de 2 y 3
console.log('Resta (2 - 3):', restar(2, 3));              // Imprime el resultado de la resta de 2 y 3
console.log('Multiplicación (2 * 3):', multiplicacion(2, 3));  // Imprime el resultado de la multiplicación de 2 y 3

// Notas sobre los sistemas de módulos en Node.js:
// - Los ficheros con extensión .js usan por defecto el sistema de módulos CommonJS.
// - Los ficheros con extensión .mjs usan el sistema de módulos ECMAScript (ES Module).
// - Los ficheros con extensión .cjs usan explícitamente el sistema de módulos CommonJS.
```

## ***Explicación Detallada***

1. **Importación de Módulos:**
   - `const { suma, restar, multiplicacion } = require('./module.cjs');`
     - *Utiliza la sintaxis `require` de CommonJS para importar las funciones `suma`, `restar`, y `multiplicacion` desde el módulo `module.cjs`.*
     - *Se recomienda usar nombres descriptivos que reflejen las funciones o variables que estás importando para mejorar la legibilidad del código.*

2. **Uso de las Funciones Importadas:**
   - *`console.log('Suma (2 + 3):', suma(2, 3));`*
     - *Imprime el resultado de la función `suma` al sumar 2 y 3.*
   - *`console.log('Resta (2 - 3):', restar(2, 3));`*
     - *Imprime el resultado de la función `restar` al restar 3 de 2.*
   - *`console.log('Multiplicación (2 * 3):', multiplicacion(2, 3));`*
     - *Imprime el resultado de la función `multiplicacion` al multiplicar 2 por 3.*

3. **Notas sobre los Sistemas de Módulos:**
   - **CommonJS (.js y .cjs):**
     - *Por defecto, los ficheros con extensión `.js` utilizan el sistema de módulos CommonJS.*
     - *Los ficheros con extensión `.cjs` indican explícitamente que se debe usar el sistema de módulos CommonJS.*
   - **ES Modules (.mjs):**
     - *Los ficheros con extensión `.mjs` utilizan el sistema de módulos ECMAScript, que es el estándar moderno de JavaScript para módulos.*

*Este formato mejora la claridad y la comprensión del código, proporcionando comentarios detallados y explicaciones de cada parte importante del fichero `index.cjs`.*
