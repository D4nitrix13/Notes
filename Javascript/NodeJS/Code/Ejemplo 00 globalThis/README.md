<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me 

// Ejemplo básico de uso de `console` en Node.js

// Imprime un saludo en la consola
console.log("Saludo")

// Imprime un mensaje informativo en la consola
console.info("Mensaje")

// Imprime un mensaje de error en la consola
console.error("Mensaje Error")

// Intento de acceder al objeto `window`, que no está definido en Node.js
// Esto causará un error porque `window` es específico de los navegadores web
// Node.js utiliza `global` o `globalThis` en lugar de `window`

/*
El siguiente bloque de código está comentado porque causará un error si se ejecuta:
    ReferenceError: window is not defined
Esto sucede porque `window` es un objeto global en el entorno del navegador, pero no en Node.js.
*/

// console.log(window)

// Para demostrar que `window` no está definido en Node.js, imprimimos su tipo
// Debería ser 'undefined'
console.log(typeof window)  // 'undefined'

// `globalThis` es una variable global que se refiere al contexto global en cualquier entorno

/*
En el navegador, `globalThis` apunta a `window`.
En Node.js, `globalThis` apunta a `global`.
De hecho, `console.log()` es una propiedad de `globalThis`.
*/

// Imprime el objeto `globalThis`, mostrando todas las propiedades globales disponibles en Node.js
globalThis.console.log(globalThis)
```

## **Explicación Detallada**

1. **Uso de `console`:**
   - **`console.log("Saludo")`:** *Imprime "Saludo" en la consola.*
   - **`console.info("Mensaje")`:** *Imprime "Mensaje" en la consola, generalmente utilizado para mensajes informativos.*
   - **`console.error("Mensaje Error")`:** *Imprime "Mensaje Error" en la consola, generalmente utilizado para errores.*

2. **Error al acceder a `window`:**
   - *Intentar usar `window` en Node.js resultará en un error porque `window` es un objeto específico del entorno del navegador.*
   - *En Node.js, el equivalente a `window` es `global` o `globalThis`.*

3. **Uso de `globalThis`:**
   - *`globalThis` es una variable global que proporciona una forma estándar de acceder al objeto global en diferentes entornos (navegador, Node.js, etc.).*
   - *En el navegador, `globalThis` se refiere a `window`.*
   - *En Node.js, `globalThis` se refiere a `global`.*

4. **Demostración del uso de `globalThis`:**
   - *`console.log(typeof window)`: Muestra 'undefined', indicando que `window` no está definido en Node.js.*
   - *`globalThis.console.log(globalThis)`: Imprime el objeto `globalThis`, mostrando todas las propiedades y métodos globales disponibles en el entorno de Node.js.*

### ***Notas Adicionales***

- *Usar `globalThis` es una buena práctica para escribir código que sea compatible entre diferentes entornos.*
- *`console` es una de las muchas propiedades disponibles en `globalThis`, lo que permite su uso en cualquier parte de la aplicación sin necesidad de importar módulos adicionales.*
