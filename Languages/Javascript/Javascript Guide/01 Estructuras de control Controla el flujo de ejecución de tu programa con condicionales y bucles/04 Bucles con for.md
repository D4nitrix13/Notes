<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Bucles con for***

- *La estructura de control `for` en JavaScript es muy útil para ejecutar una serie de instrucciones un número determinado de veces. A diferencia de `while`, que usa una condición para determinar si se ejecuta o no el bloque de código, `for` usa un contador que se incrementa en cada iteración hasta que se cumple una condición.*

---

## ***Sintaxis de `for`***

**La sintaxis de `for` es la siguiente:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

for (inicialización; condición; actualización) {
  // código a ejecutar
}
```

**Importante: fíjate que `for` tiene tres partes separadas por `;`:**

1. **Inicialización:** *Se realiza antes de que se inicie el bucle y se utiliza para declarar variables y asignar valores iniciales.*
2. **Condición:** *Es una expresión booleana que se evalúa antes de cada iteración del bucle. Si la expresión se evalúa como `true`, se ejecuta el bloque de código dentro del bucle. Si la expresión se evalúa como `false`, el bucle termina.*
3. **Actualización:** *Se utiliza para actualizar el valor de la variable de control del bucle después de cada iteración. Normalmente, se incrementa o decrementa el valor de la variable de control del bucle.*

---

### ***Ejemplo de uso de `for`***

**El siguiente ejemplo muestra cómo se puede usar `for` para imprimir los números del 1 al 10:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

for (let number = 1; number <= 10; number++) {
  console.log(number);
}
```

- **Inicialización:** *Se declara la variable `number` y se le asigna el valor 1.*
- **Condición:** *Mientras `number <= 10`, se itera el bucle.*
- **Actualización:** *`number++` incrementa el valor de `number` en 1 después de cada iteración.*

---

#### ***Incrementando números con `++`***

- *El operador `++` nos permite incrementar el valor de una variable número en 1. Por ejemplo, si tenemos la variable `i` con el valor 5, `i++` incrementaría el valor de `i` en 1, es decir, `i` pasaría a valer 6.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let i = 5;
i++;
console.log(i); // -> 6
```

- *Es una forma abreviada de escribir `i = i + 1`. Y, como ves, es la forma más típica de usar en bucles como `for` para no tener que escribir `i = i + 1` cada vez.*

---

#### ***Iterando al revés***

- *El método `for` en JavaScript también se puede utilizar para iterar al revés. Para ello, se utiliza la sintaxis `i--` en la sección de actualización del bucle en lugar de `i++`.*

**La sintaxis del método `for` para iterar en reversa es la siguiente:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

for (let i = 10; i >= 0; i--) {
  if (i === 0) {
    console.log('¡Despegue 🚀!');
  } else {
    console.log('Faltan ' + i + ' segundos');
  }
}
```

---

#### ***Llevando más allá el bucle `for`***

- *Aunque siempre los ejemplos con `for` son los mismos, ten en cuenta que puedes hacer cualquier cosa en la inicialización, condición y actualización. Podrías, por ejemplo, usar dos variables a la vez.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

for (let i = 0, j = 5; i < 5; i++, j--) {
  console.log(i, j);
}
```

*La coma `,` nos permite declarar dos variables en la inicialización y actualizarlas en la actualización. En este caso, la `,` es un operador que evalúa cada uno de sus operandos (de izquierda a derecha) y retorna el valor del último operando. No es muy común su uso, pero es bueno saber que existe.*

---

#### ***`continue` y `break`***

- *Al igual que en `while`, `for` también tiene las palabras reservadas `continue` y `break` para controlar el flujo de ejecución del bucle.*

- **`continue`:** *Se usa para saltar a la siguiente iteración del bucle.*
- **`break`:** *Se usa para salir del bucle.*

**Ejemplo:**

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

for (let i = 0; i < 10; i++) {
  const esPar = i % 2 === 0;
  if (esPar) {
    continue;
  }

  // Solo mostramos este console.log si es impar
  console.log(i);

  // Salimos del bucle al llegar al 7
  if (i === 7) {
    break;
  }
}
```

---

#### ***Bucles anidados con `for`***

- *Imagina que quieres crear la tabla de multiplicar del 1 al 10. Para ello, necesitas un bucle que itere del 1 al 10 y, dentro de ese bucle, otro bucle que itere del 1 al 10. Esto se puede hacer con dos bucles `for` anidados (uno dentro del otro).*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

for (let i = 1; i <= 10; i++) {
  for (let j = 1; j <= 10; j++) {
    const resultado = i * j;
    console.log(i + ' x ' + j + ' = ' + resultado);
  }
}
```

---

### ***Examen interactivo***

---

#### ***¿Cuál es la sintaxis correcta para crear un bucle `for` en JavaScript?***

1. ```javascript
    // Autor: Daniel Benjamin Perez Morales
    // GitHub: https://github.com/D4nitrix13
    // Correo electrónico: danielperezdev@proton.me
   
   for (let i = 0, i < array.length, i++) {
    // código a ejecutar en cada iteración
   }
   ```

2. **Correcto:**

   ```javascript
   // Autor: Daniel Benjamin Perez Morales
   // GitHub: https://github.com/D4nitrix13
   // Correo electrónico: danielperezdev@proton.me
   
   for (let i = 0; i < array.length; i++) {
    // código a ejecutar en cada iteración
   }
   ```

---

#### ***¿Cuántas veces veremos el mensaje "Hola" en consola?***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

for (let i = 0; i < 10 && i !== 3; i++) {
  console.log('Hola');
}
```

1. *10 veces*
2. *4 veces*
3. **Correcto:** *3 veces. Como tenemos la condición de `i !== 3`, cuando lleguemos ahí dejará de iterar.*

---

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/estructuras-de-control/bucles-con-for "https://www.aprendejavascript.dev/clase/estructuras-de-control/bucles-con-for")*
