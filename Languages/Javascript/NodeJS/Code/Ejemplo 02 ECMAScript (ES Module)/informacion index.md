# ***Fichero `index.mjs`:***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// index.mjs
// Forma recomendada de utilizar módulos con ECMAScript Modules (ESM)

// Importación de funciones desde el módulo 'module.mjs'.
// Utilizamos la sintaxis de importación de ESM para traer las funciones necesarias.
import { multiplicacion, restar, suma } from './module.mjs';

// Uso de las funciones importadas
console.log('Suma (2 + 3):', suma(2, 3));                 // Imprime el resultado de la suma de 2 y 3
console.log('Resta (2 - 3):', restar(2, 3));              // Imprime el resultado de la resta de 2 y 3
console.log('Multiplicación (2 * 3):', multiplicacion(2, 3));  // Imprime el resultado de la multiplicación de 2 y 3
```

## ***Explicación Detallada***

1. **Uso de ECMAScript Modules (ESM):**
   - *ECMAScript Modules es la forma moderna y recomendada de trabajar con módulos en JavaScript.*
   - *A diferencia de CommonJS, que usa `require` y `module.exports`, ESM utiliza `import` y `export`.*

2. **Importación de Funciones:**
   - *`import { multiplicacion, restar, suma } from './module.mjs';`*
     - *Esta línea importa las funciones `multiplicacion`, `restar`, y `suma` desde el fichero `module.mjs`.*
     - *La sintaxis de importación de ESM permite importar múltiples exportaciones nombradas de un módulo de una manera clara y concisa.*

3. **Uso de las Funciones Importadas:**
   - *`console.log('Suma (2 + 3):', suma(2, 3));`*
     - *Imprime el resultado de la función `suma` al sumar 2 y 3.*
   - *`console.log('Resta (2 - 3):', restar(2, 3));`*
     - *Imprime el resultado de la función `restar` al restar 3 de 2.*
   - *`console.log('Multiplicación (2 * 3):', multiplicacion(2, 3));`*
     - *Imprime el resultado de la función `multiplicacion` al multiplicar 2 por 3.*

### ***Ventajas de Usar ECMAScript Modules***

1. **Compatibilidad Estándar:**
   - *ESM es parte del estándar ECMAScript (ES6 y posteriores), lo que lo hace compatible con todos los navegadores modernos y entornos JavaScript.*

2. **Sintaxis Más Clara:**
   - *La sintaxis de `import` y `export` es más clara y fácil de entender en comparación con `require` y `module.exports` de CommonJS.*

3. **Carga Asíncrona:**
   - *ESM soporta la carga asíncrona de módulos, lo que puede mejorar el rendimiento en aplicaciones web.*

4. **Ámbito Léxico:**
   - *Las importaciones en ESM tienen un ámbito léxico, lo que significa que son constantes y no se pueden reasignar, lo que ayuda a prevenir errores.*

### ***Notas Adicionales***

- *Los ficheros con extensión `.mjs` indican que deben ser tratados como módulos ECMAScript.*
- *En entornos donde el soporte para ESM está habilitado (como Node.js a partir de la versión 12 con ciertas configuraciones), se pueden usar ficheros `.mjs` para aprovechar estas ventajas.*
- *En Node.js, también se puede habilitar ESM en ficheros `.js` añadiendo `"type": "module"` en el `package.json`.*

*Este formato proporciona una explicación detallada y clara sobre cómo trabajar con ECMAScript Modules, destacando sus ventajas y la sintaxis moderna que se recomienda utilizar.*
