# ***Fichero `module.mjs`***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// module.mjs
// Forma moderna de exportar módulos utilizando ECMAScript Modules (ESM)

// Definición de la función 'suma'
// Esta función recibe dos argumentos y devuelve su suma
export function suma(a, b) {
    return a + b;
}

// Definición de la función 'restar'
// Esta función recibe dos argumentos y devuelve la resta del segundo argumento al primero
export function restar(a, b) {
    return a - b;
}

// Definición de la función 'multiplicacion'
// Esta función recibe dos argumentos y devuelve su producto
export function multiplicacion(a, b) {
    return a * b;
}
```

## ***Explicación Detallada***

1. **Uso de ECMAScript Modules (ESM):**
   - *ECMAScript Modules es la especificación moderna para manejar módulos en JavaScript, introducida en ES6.*
   - *A diferencia de CommonJS (`module.exports` y `require`), ESM utiliza `export` y `import` para definir y utilizar módulos.*

2. **Exportación de Funciones:**
   - *`export function suma(a, b) { ... }`*
     - *Exporta la función `suma` para que pueda ser importada en otros módulos.*
   - *`export function restar(a, b) { ... }`*
     - *Exporta la función `restar` para que pueda ser importada en otros módulos.*
   - *`export function multiplicacion(a, b) { ... }`*
     - *Exporta la función `multiplicacion` para que pueda ser importada en otros módulos.*

3. **Beneficios de Exportar Funciones por Separado:**
   - **Modularidad:** *Cada función puede ser importada individualmente en otros ficheros, permitiendo un uso más modular y específico de las funciones.*
   - **Optimización:** *Los módulos ESM permiten optimizaciones de tiempo de compilación, como la eliminación de código muerto (tree-shaking) en herramientas de construcción como Webpack.*
   - **Sintaxis Clara y Concisa:** *La sintaxis de `export` es clara y directa, facilitando la lectura y mantenimiento del código.*

### ***Uso de las Funciones Exportadas***

Pa*ra usar las funciones exportadas en otro módulo, puedes importarlas usando la sintaxis de ESM, como se muestra en el fichero `index.mjs`:*

```javascript
// index.mjs
// Forma recomendada de utilizar módulos con ECMAScript Modules (ESM)

// Importación de funciones desde el módulo 'module.mjs'
import { multiplicacion, restar, suma } from './module.mjs';

// Uso de las funciones importadas
console.log('Suma (2 + 3):', suma(2, 3));                 // Imprime el resultado de la suma de 2 y 3
console.log('Resta (2 - 3):', restar(2, 3));              // Imprime el resultado de la resta de 2 y 3
console.log('Multiplicación (2 * 3):', multiplicacion(2, 3));  // Imprime el resultado de la multiplicación de 2 y 3
```

### ***Ventajas de Usar ECMAScript Modules***

1. **Compatibilidad Estándar:**
   - *ESM es parte del estándar ECMAScript (ES6 y posteriores), lo que lo hace compatible con todos los navegadores modernos y entornos JavaScript.*

2. **Sintaxis Más Clara:**
   - *La sintaxis de `import` y `export` es más clara y fácil de entender en comparación con `require` y `module.exports` de CommonJS.*

3. **Carga Asíncrona:**
   - *ESM soporta la carga asíncrona de módulos, lo que puede mejorar el rendimiento en aplicaciones web.*

4. **Ámbito Léxico:**
   - *Las importaciones en ESM tienen un ámbito léxico, lo que significa que son constantes y no se pueden reasignar, lo que ayuda a prevenir errores.*

*Esta explicación proporciona una comprensión clara de cómo definir y exportar funciones usando ECMAScript Modules, destacando las ventajas y la sintaxis moderna recomendada.*
