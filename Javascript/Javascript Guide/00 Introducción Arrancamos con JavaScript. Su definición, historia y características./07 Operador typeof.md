<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Operador typeof***

**El operador `typeof` en JavaScript es una herramienta fundamental para conocer el tipo de dato de una variable o valor específico. Aquí tienes un resumen detallado sobre su uso y funcionalidades:**

## ***Uso del operador typeof***

### ***Ejemplos básicos***

1. **Con una variable:**

   ```javascript
   const MAGIC_NUMBER = 7;
   typeof MAGIC_NUMBER; // "number"
   ```

   - *En este caso, `typeof` devuelve `"number"` porque `MAGIC_NUMBER` es un número.*

2. **Con valores directos:**

   ```javascript
   typeof undefined; // "undefined"
   typeof true; // "boolean"
   typeof 42; // "number"
   typeof "Hola mundo"; // "string"
   ```

   *Aquí vemos ejemplos de diferentes tipos de datos y cómo `typeof` devuelve la cadena correspondiente al tipo de cada valor.*

### ***Manejo de null***

- *JavaScript tiene un error histórico donde `typeof null` devuelve `"object"`, a pesar de que `null` no es realmente un objeto. Esto es una anomalía que existe desde las primeras versiones de JavaScript y no puede corregirse para no romper código existente:*

- *[Recurso](https://2ality.com/2013/10/typeof-null.html "https://2ality.com/2013/10/typeof-null.html")*

```javascript
typeof null; // "object"
```

**Para verificar si una variable es `null`, debes usar una comparación estricta (`===`):**

```javascript
const foo = null;
foo === null; // true
```

### ***Usando typeof con operadores de comparación***

**El operador `typeof` es útil en combinación con operadores de comparación para verificar el tipo de una variable antes de realizar operaciones específicas:**

```javascript
const age = 42;
typeof age === "number"; // true
```

**También se puede combinar con expresiones lógicas para realizar validaciones más complejas:**

```javascript
const age = 42;
typeof age === "number" && age > 18; // true
```

### ***Ejercicios interactivos***

1. **Verificar si una variable `userName` es de tipo `string`:**

   ```javascript
   typeof userName === "string";
   ```

2. **Asegurar que una variable `dogId` es de tipo `string`:**

   ```javascript
   typeof dogId === "string";
   ```

## ***Examen interactivo***

1. **¿Para qué sirve el operador typeof en JavaScript?**
   - *Respuesta correcta: Nos da el tipo de dato de una variable.*

2. **¿Qué devuelve `typeof null` en JavaScript?**
   - *Respuesta correcta: "object".*

3. **¿El operador typeof siempre devuelve una cadena de texto con el tipo del operando?**
   - *Respuesta correcta: Sí, siempre devuelve una cadena de texto.*

- *El operador `typeof` es esencial para la programación en JavaScript, permitiendo determinar dinámicamente el tipo de datos y facilitando la escritura de código robusto y eficiente.*

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/introduccion/operador-typeof "https://www.aprendejavascript.dev/clase/introduccion/operador-typeof")*
