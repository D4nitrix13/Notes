<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicaciones de los Ficheros***

---

## ***Explicacion Fichero Html `index.html`***

```html
<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
    <!-- Emmet Matching Pair -->
    <!-- Esta función te posiciona al principio o al final de una etiqueta HTML.
    Debes seleccionar la etiqueta o colocar el cursor dentro de ella para activarla. -->

    <!-- Selección de Elementos -->
    <!-- Usa `ctrl + shift + p` y escribe `seleccionar los elementos y` para ejecutar `Emmet: Balance In`. Esto seleccionará todos los elementos dentro de una etiqueta cuando el cursor está dentro de ella. -->

    <div>
        <!-- Emmet: Balance Outward -->
        <!-- Selecciona todos los elementos dentro de una etiqueta. Coloca el cursor dentro de la etiqueta y ejecuta el comando correspondiente. -->

        <!-- Emmet: Balance Inward -->
        <!-- Selecciona el contenido dentro de una etiqueta. Debes seleccionar toda la etiqueta para aplicarlo correctamente. -->

        <h2>Vscode</h2>

        <p>bla bla</p>
    </div>
</body>

</html>
```

**Explicación mejorada:**

- **Emmet Matching Pair:** *Esta función te permite colocar el cursor al principio o al final de una etiqueta HTML. Para usarla, selecciona la etiqueta o coloca el cursor dentro de ella.*

- **Selección de Elementos:** *Utiliza `ctrl + shift + p` y escribe `seleccionar los elementos y` para ejecutar `Emmet: Balance In`. Esto seleccionará todos los elementos dentro de una etiqueta cuando el cursor está dentro de ella.*

- **Emmet: Balance Outward:** *Selecciona todos los elementos dentro de una etiqueta. Coloca el cursor dentro de la etiqueta y ejecuta el comando correspondiente.*

- **Emmet: Balance Inward:** *Selecciona el contenido dentro de una etiqueta. Debes seleccionar toda la etiqueta para aplicarlo correctamente.*

---

## ***Expliacacion Fichero Javascript `index.js`***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: [D4nitrix13](https://github.com/D4nitrix13)
// Correo electrónico: danielperezdev@proton.me

import add from "./helpers/add";
import people from "./helpers/people";

/**
 * # **Función:** ~*Say a message*~
 * 
 * ```javascript
 * console.log("Daniel Perez")
 * ```
 * 
 * @param {string} message Mensaje a mostrar en el cuadro de alerta.
 * @return {void}
 */
function say(message) {
    alert(message);
}

// Al hacer clic en la función, se pueden configurar varias opciones.
// Activar las referencias del icono:
say("hello");

add(10, 15);
people;

// Para usar "Go to Symbol", presiona `Ctrl + Shift + P`, borra el `>`, y escribe `#<funcion>` o `@`.
```

**Explicación:**

- **Autor:** *Nombre completo del autor.*
- **GitHub:** *Enlace al perfil del autor en GitHub.*
- **Correo electrónico:** *Dirección de correo electrónico del autor.*

- **Función: "Say a message"**
  - *Ejemplo de uso en JavaScript.*
  - *Parámetro `message`: Cadena que se muestra en un cuadro de alerta.*
  - *Retorna `void` (ningún valor).*

- **Instrucciones adicionales:**
  - *Se pueden configurar varias opciones al hacer clic en la función.*
  - *Ejemplo de uso de otras funciones importadas (`add` y `people`).*
  
- **Uso de "Go to Symbol":**
  - *Para usar la función "Go to Symbol", presiona `Ctrl + Shift + P`, elimina `>`, y escribe `#<funcion>` o `@`.*

---

## ***Explicacion Fichero Javascript `add.js`***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: [D4nitrix13](https://github.com/D4nitrix13)
// Correo electrónico: danielperezdev@proton.me

/**
 * Función: **Add 2 numbers together**
 * 
 * @param {number} a El primer número a sumar.
 * @param {number} b El segundo número a sumar.
 * @returns La suma de `a` y `b`.
 */
export default function add(a, b) {
    return a + b;
}

// Para importar, es necesario utilizar `export default`, como se muestra aquí.
```

**Explicación mejorada:**

- **Autor:** *Nombre completo del autor.*
- **GitHub:** *Enlace al perfil del autor en GitHub.*
- **Correo electrónico:** *Dirección de correo electrónico del autor.*

- **Función: "Add 2 numbers together"**
  - **Descripción:** *Función que suma dos números.*
  - **Parámetros:**
    - **`a`:** *El primer número a sumar.*
    - **`b`:** *El segundo número a sumar.*
  - **Retorna:** *La suma de `a` y `b`.*

- **Notas sobre la exportación:**
  - *Para importar esta función en otros ficheros, se utiliza `export default`, como se muestra en el ejemplo.*

---

## ***Explicacion Fichero Javascript `people.js`***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: [D4nitrix13](https://github.com/D4nitrix13)
// Correo electrónico: danielperezdev@proton.me

/**
 * Array de personas.
 *
 * @type {Array<Object>} Un array que contiene objetos con nombres de personas.
 */
const people = [
    { name: "Daniel" }
];

export default people;
```

**Explicación mejorada:**

- **Autor:** *Nombre completo del autor.*
- **GitHub:** *Enlace al perfil del autor en GitHub.*
- **Correo electrónico:** *Dirección de correo electrónico del autor.*

- **Array de personas:**
  - **Descripción:** *Un array que contiene objetos con nombres de personas.*
  - **Tipo:** *`Array<Object>`*
  - **Estructura:** *Cada objeto tiene una propiedad `name` que representa el nombre de una persona.*
