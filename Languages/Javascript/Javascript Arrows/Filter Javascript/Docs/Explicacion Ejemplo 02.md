<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 02***

---

## ***Ejemplo con Función Flecha sin Paréntesis***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20];

/**
 * Filtra los precios que son mayores o iguales a 20.
 * Utiliza el método `filter` de arrays para crear un nuevo array con los precios filtrados.
 *
 * @param {number} dollar - El precio a evaluar.
 * @returns {boolean} `true` si el precio es mayor o igual a 20, `false` si no lo es.
 */
const expensive = prices.filter(dollar => {
  // Devuelve `true` si el precio es mayor o igual a 20, `false` si no lo es.
  if (dollar >= 20) {
    return true;
  } else {
    return false;
  }
});

console.log("Sin paréntesis:", expensive); // [ 32, 20 ]
```

---

### ***Explicación***

1. **Función Flecha sin Paréntesis:** *La función flecha `dollar => { ... }` toma un solo parámetro (`dollar`) y evalúa si es mayor o igual a `20`.*

2. **Método `filter`:** *`filter` es un método de arrays que crea un nuevo array con elementos que pasan una prueba especificada por la función callback.*

3. **Condición `if`:** *Dentro de la función flecha, se evalúa si `dollar` es mayor o igual a `20`.*

4. **Retorno de `filter`:** *La función flecha devuelve `true` si la condición se cumple (precio mayor o igual a `20`) y `false` si no se cumple.*

5. **Array Resultante:** *El array resultante `expensive` contiene los precios filtrados que son mayores o iguales a `20`.*

---

### ***Ejemplo con Función Flecha y Paréntesis***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20];

/**
 * Filtra los precios que son mayores o iguales a 20.
 * Utiliza el método `filter` de arrays para crear un nuevo array con los precios filtrados.
 *
 * @param {number} dollar - El precio a evaluar.
 * @returns {boolean} `true` si el precio es mayor o igual a 20, `false` si no lo es.
 */
const expensive = prices.filter((dollar) => {
  // Devuelve `true` si el precio es mayor o igual a 20, `false` si no lo es.
  if (dollar >= 20) {
    return true;
  } else {
    return false;
  }
});

console.log("Con paréntesis:", expensive); // [ 32, 20 ]
```

---

#### ***Explicación:***

1. **Función Flecha con Paréntesis:** *La función flecha `(dollar) => { ... }` también toma un solo parámetro (`dollar`) y evalúa si es mayor o igual a `20`.*

2. **Método `filter`:** *Igual que en el ejemplo anterior, `filter` se utiliza para crear un nuevo array con elementos que pasan una prueba especificada por la función callback.*

3. **Condición `if`:** *Dentro de la función flecha, se evalúa si `dollar` es mayor o igual a `20`.*

4. **Retorno de `filter`:** *La función flecha devuelve `true` si la condición se cumple (precio mayor o igual a `20`) y `false` si no se cumple.*

5. **Array Resultante:** *El array resultante `expensive` contiene los precios filtrados que son mayores o iguales a `20`.*

- *Ambos enfoques son válidos y producen el mismo resultado. La diferencia está en el estilo y la preferencia personal del desarrollador en cuanto al uso de paréntesis alrededor del parámetro de la función flecha.*
