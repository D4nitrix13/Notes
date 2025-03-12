<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***console.log()***

**En JavaScript, `console.log()` es una función fundamental para imprimir mensajes en la consola del navegador o en el entorno de desarrollo. Aquí te explico más sobre su uso y otros métodos relacionados:**

## ***Uso básico de `console.log()`***

**La sintaxis básica para imprimir un mensaje en la consola es:**

```javascript
console.log("Hola, JavaScript");
// -> Hola, JavaScript
```

**También puedes imprimir el valor de una variable:**

```javascript
const nombre = 'JavaScript';
console.log(nombre);
// -> JavaScript
```

## ***Imprimir varios valores o variables***

- *Para imprimir múltiples valores o variables en una sola línea de código, simplemente sepáralos por comas dentro del `console.log()`:*

```javascript
const nombre = 'JavaScript';
const version = 2023;
console.log(nombre, version);
// -> JavaScript 2023
```

## ***Otros métodos de `console`***

**Además de `console.log()`, existen otros métodos que puedes usar para imprimir mensajes en la consola:**

- **`console.error()`:** *Para imprimir mensajes de error.*
- **`console.warn()`:** *Para imprimir mensajes de advertencia.*
- **`console.info()`:** *Para imprimir mensajes de información.*

- **Estos métodos tienen un formato especial que ayuda a identificar rápidamente el tipo de mensaje:**

```javascript
console.error('Error');
// ❌ Error

console.warn('Advertencia');
// ⚠️ Advertencia

console.info('Información');
// ℹ️ Información
```

## ***Diferencia entre `console.log()` y `console.error()`***

**La diferencia principal entre `console.log()` y `console.error()` es su propósito:**

- **`console.log()`:** *Se utiliza para imprimir cualquier tipo de mensaje en la consola.*
- **`console.error()`:** *Se utiliza específicamente para imprimir mensajes que indican un error.*

- *Además, `console.error()` suele mostrar el mensaje con un estilo visual diferente, como un icono de advertencia o error, para facilitar su identificación.*

- *En resumen, `console.log()` es la función principal para imprimir mensajes en la consola de JavaScript, mientras que los métodos `console.error()`, `console.warn()` y `console.info()` están diseñados para situaciones específicas como errores, advertencias y mensajes informativos respectivamente. Utilizar estos métodos adecuadamente ayuda a mantener el código organizado y facilita el proceso de depuración y desarrollo.*

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/introduccion/console-log "https://www.aprendejavascript.dev/clase/introduccion/console-log")*
