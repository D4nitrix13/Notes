<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***null y undefined en JavaScript***

- *En JavaScript, los tipos de datos `null` y `undefined` son fundamentales para manejar valores que no están definidos o que indican la ausencia de valor. Aquí te explico sus características y cómo se utilizan:*

## ***null***

- *`null` es un valor que indica explícitamente la ausencia de valor. Es decir, se utiliza cuando queremos decir que una variable no contiene ningún valor válido.*

```javascript
let capacidad = null; // La variable capacidad tiene un valor null
```

## ***undefined***

- *`undefined` indica que una variable ha sido declarada pero no se le ha asignado ningún valor. También puede ser el valor por defecto de una variable recién declarada.*

```javascript
let dinero; // La variable dinero está declarada pero no tiene valor asignado, por lo que es undefined
```

**También podemos asignar directamente `undefined` a una variable:**

```javascript
let rolloDePapel = undefined; // La variable rolloDePapel tiene el valor undefined
```

## ***Diferencias entre null y undefined***

**La principal diferencia radica en su significado:**

- **null:** *Indica explícitamente la ausencia de valor.*
- **undefined:** *Indica que algo está declarado pero no tiene valor asignado.*

- *Por ejemplo, cuando creamos una variable sin asignarle un valor, su valor inicial será `undefined`.*

### ***Ejercicios interactivos***

1. **Crear una variable con `let` llamada `capacidad` y asignarle un valor `null`:**

   ```javascript
   let capacidad = null;
   ```

2. **Crear una variable con `let` llamada `dinero` y asegurarse de que tenga un valor de `undefined`:**

   ```javascript
   let dinero;
   ```

## ***Comparaciones con null y undefined***

**Cuando comparamos `null` y `undefined` con el operador de igualdad estricta (`===`), son considerados diferentes entre sí:**

```javascript
null === undefined // false
```

**Solo las comparaciones de `null` con `null` y `undefined` con `undefined` devolverán `true`:**

```javascript
null === null // true
undefined === undefined // true
```

## ***Examen interactivo***

1. **¿Qué valor tiene una variable a la que no se le ha asignado nada al declararla?**
   - *Respuesta: Un valor `undefined`.*

*Con estos conceptos claros, podrás manejar correctamente las situaciones donde necesitas representar la ausencia de valor en tu código JavaScript.*

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/introduccion/null-y-undefined "https://www.aprendejavascript.dev/clase/introduccion/null-y-undefined")*
