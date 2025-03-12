<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Variables en JavaScript***

- **En JavaScript, las variables son contenedores que utilizamos para almacenar y manipular datos dentro de un programa. Aquí te explico cómo funcionan y las diferentes formas de declararlas:**

## ***Declaración de variables con `let`***

- *Para crear una variable mutable (que puede cambiar de valor), usamos la palabra clave `let`.*

```javascript
let numero // Declaración de variable sin inicializar
numero = 1 // Asignación de valor
console.log(numero + 1) // → 2
numero = 5 // Reasignación de valor
console.log(numero + 1) // → 6
```

También podemos inicializar y asignar el valor al mismo tiempo:

```javascript
let welcomeText = 'Hola' // Variable de texto
let isCool = true // Variable booleana
```

### ***Ejercicios interactivos***

1. **Crear una variable `mensaje` y asignarle el valor "Hola JavaScript":**

   ```javascript
   let mensaje = "Hola JavaScript"
   ```

2. **Crear una variable `resultado` y asignarle la suma de 2 y 3:**

   ```javascript
   let resultado = 2 + 3
   ```

## ***Constantes con `const`***

- *Las constantes se declaran con la palabra clave `const` y no pueden ser reasignadas después de su inicialización.*

```javascript
const PI = 3.1415
```

**Intentar reasignar una constante generará un error:**

```javascript
PI = 3 // Error: Assignment to constant variable.
```

**Las constantes deben inicializarse con un valor al momento de la declaración:**

```javascript
const RADIUS // Error: Missing initializer in const declaration.
```

### ***Ejercicio interactivo***

1. **Crear una constante `IS_DISABLED` y asignarle el booleano `true`:**

   ```javascript
   const IS_DISABLED = true
   ```

## ***Variables con `var`***

*Aunque menos común hoy en día, `var` es otra forma de declarar variables en JavaScript. Sin embargo, tiene comportamientos que pueden ser problemáticos y es recomendable evitar su uso.*

## ***Convenciones y nomenclatura***

*Es importante nombrar las variables de manera descriptiva y seguir convenciones de nomenclatura para mejorar la legibilidad del código.*

- **camelCase:** *Primera palabra en minúscula y las siguientes con mayúscula al inicio.*

  ```javascript
  let camelCase = 1
  let camelCaseIsCool = 2
  let userName = 'DanielDev'
  ```

- **snake_case:** *Todas las palabras en minúscula y separadas por guiones bajos.*

  ```javascript
  let snake_case = 1
  let snake_case_is_cool = 2
  let user_name = 'DanielDev'
  ```

- **SCREAMING_CASE:** *Todas las palabras en mayúsculas y separadas por guiones bajos, comúnmente usado para constantes.*

  ```javascript
  const SCREAMING_CASE = 1
  const SCREAMING_CASE_IS_COOL = 2
  const USER_NAME = 'DanielDev'
  ```

*Recuerda que JavaScript distingue entre mayúsculas y minúsculas en los nombres de las variables.*

## ***Examen interactivo***

1. **¿Qué es una variable en JavaScript?**
   - *Respuesta: Una variable es un contenedor de información que se utiliza para almacenar datos en un programa.*

2. **¿Qué peculiaridad tienen las variables `const` en JavaScript?**
   - *Respuesta: No se pueden reasignar después de su inicialización.*

*Con estos conceptos, podrás manejar eficazmente las variables en JavaScript y escribir código más claro y mantenible.*

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/introduccion/variables "https://www.aprendejavascript.dev/clase/introduccion/variables")*
