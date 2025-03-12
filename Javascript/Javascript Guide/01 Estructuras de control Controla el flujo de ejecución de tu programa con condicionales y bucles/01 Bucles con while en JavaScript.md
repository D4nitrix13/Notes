<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Bucles con while en JavaScript***

- *Un bucle es una estructura de control que permite repetir un bloque de instrucciones. Vamos a ver cómo funciona y cómo se utiliza el bucle while en JavaScript.*

---

## ***Sintaxis***

- *La sintaxis del bucle while es similar a la de un condicional if, con la diferencia de que el código se ejecuta repetidamente mientras la condición sea verdadera.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

while (condición) {
  // código a ejecutar mientras se cumpla la condición
}
```

- *El bucle comienza evaluando la condición. Si la condición es `true`, se ejecuta el código dentro de las llaves. Después de ejecutar el código, la condición se evalúa de nuevo. Este proceso se repite hasta que la condición se evalúa como `false`.*

- *Si la condición es `false` desde el principio, el código dentro de las llaves nunca se ejecutará.*

> *A cada vuelta del bucle se le llama iteración. Una iteración es la repetición de un proceso o acción un número determinado de veces, de manera ordenada y sistemática.*

---

### ***Ejemplo de uso de while***

- *Vamos a crear la cuenta atrás de un cohete. Iniciamos una variable `cuentaAtras` que contenga el número de segundos que faltan para el lanzamiento, empezando con 10 segundos.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let cuentaAtras = 10;

while (cuentaAtras > 0) {
  console.log(cuentaAtras);
  cuentaAtras -= 1;
}

console.log('¡Despegue! 🚀');
```

- *Si ejecutas este código en consola, deberías ver los números del 10 al 1, y después el mensaje de despegue.*

---

#### ***Cuidado con los bucles infinitos***

- *Los bucles while son muy potentes, pero también pueden ser peligrosos. Si la condición nunca se evalúa como `false`, el bucle se ejecutará infinitamente.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

while (true) {
  console.log('¡Hola hasta el infinito!');
}
```

- *Esto evaluará la condición `true` como verdadera y ejecutará el código dentro de las llaves una y otra vez.*

---

#### ***Saliendo de un bucle con break***

- *Podemos controlar cuándo queremos salir de un bucle utilizando la palabra reservada `break`. Cuando el intérprete de JavaScript encuentra la palabra `break`, sale del bucle y continúa ejecutando el código que haya después.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let cuentaAtras = 10;

while (cuentaAtras > 0) {
  console.log(cuentaAtras);
  cuentaAtras -= 1;

  if (cuentaAtras === 5) {
    break;
  }
}
```

- *En este código, el bucle sale cuando `cuentaAtras` es igual a 5. Por lo tanto, el valor de `cuentaAtras` es 5 al finalizar el bucle.*

---

#### ***Saltando una iteración con continue***

- *La palabra reservada `continue` permite saltar una iteración del bucle.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let cuentaAtras = 10;

while (cuentaAtras > 0) {
  cuentaAtras -= 1;

  if (cuentaAtras % 2 === 0) {
    continue;
  }

  console.log(cuentaAtras);
}
```

*En este código, si `cuentaAtras` es un número par, se salta la iteración y no se ejecuta el `console.log`. Por ello, los números pares no aparecen en la consola.*

---

#### ***Anidación de bucles***

- *Podemos anidar bucles dentro de otros bucles. Por ejemplo, en una cuenta atrás para un cohete, revisamos tres parámetros: oxígeno, combustible y temperatura.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const NUMERO_REVISIONES = 3;
let cuentaAtras = 10;

while (cuentaAtras > 0) {
  console.log(cuentaAtras);

  let revisionesRealizadas = 0;

  while (revisionesRealizadas < NUMERO_REVISIONES) {
    revisionesRealizadas += 1;
    console.log(revisionesRealizadas + ' revisiones realizadas...');
  }

  cuentaAtras -= 1;
}
```

- *Las variables creadas con `let` y `const` dentro de un bucle solo existen dentro de ese bucle y desaparecen cuando el bucle termina. Si intentas acceder a una variable creada dentro de un bucle fuera de él, obtendrás un error.*

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let cuentaAtras = 10;

while (cuentaAtras > 0) {
  let revisionesRealizadas = 3;
  console.log(revisionesRealizadas);
  cuentaAtras -= 1;
}

console.log(revisionesRealizadas); // -> ERROR: ReferenceError
```

- *Esto también ocurre con otras estructuras de control, ya que el alcance de las variables creadas con `let` y `const` es el bloque entre `{}` en el que se crean.*

---

### ***Examen interactivo***

---

#### ***¿Cuál es la sintaxis correcta para utilizar un bucle while en JavaScript?***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

while (condition) {
  // código a ejecutar mientras se cumpla la condición
}
```

---

#### ***¿Cuál es la palabra reservada que se utiliza para salir de un bucle en JavaScript?***

- *`continue`*
- *`exit`*
- *`break`* **(correcta)**

---

#### ***¿Cuántas veces saldrá en consola la palabra 'Café'?***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

let drinkCoffee = 0;

while (drinkCoffee < 10) {
  drinkCoffee += 1;
  
  if (drinkCoffee === 8) { break; }
  if (drinkCoffee === 5) { continue; }

  console.log('Café');
}
```

**Respuesta 6:**

- *El bucle imprime 'Café' 6 veces. Se salta la iteración cuando `drinkCoffee` es 5 y sale del bucle cuando `drinkCoffee` es 8.*

---

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/estructuras-de-control/bucles-con-while "https://www.aprendejavascript.dev/clase/estructuras-de-control/bucles-con-while")*
