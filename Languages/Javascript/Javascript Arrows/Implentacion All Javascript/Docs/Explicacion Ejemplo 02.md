<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 02***

---

## ***Caso 1: Implementación de Funciones en Cadena Lineal***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const dollars = ['32$', '15$', '12$', '17$', '20$'];

let sum = 0;

// Implementación de funciones en cadena lineal
sum = dollars.map(dollar => Number(dollar.slice(0, dollar.length - 1))).filter(dollar => dollar >= 20).reduce((acum, price) => acum + price, 0);

console.log(sum); // Output: 52
```

---

### ***Explicación***

1. **Array de Precios:** *`dollars` es un array que contiene strings con precios en formato `"$NN"`, donde `NN` es un número.*

2. **Función `map`:**
   - **Objetivo:** *Extraer y convertir los precios de formato string a números.*
   - **Implementación:** *`dollars.map(dollar => Number(dollar.slice(0, dollar.length - 1)))`*
   - **Función Flecha:** *`map` itera sobre cada elemento `dollar` del array `dollars`. `Number(dollar.slice(0, dollar.length - 1))` convierte cada precio de string a número eliminando el símbolo `$`.*

3. **Función `filter`:**
   - **Objetivo:** *Filtrar los precios que son mayores o iguales a `20`.*
   - **Implementación:** *`.filter(dollar => dollar >= 20)`*
   - **Función Flecha:** *`filter` verifica si cada `dollar` es mayor o igual a `20`, devolviendo un nuevo array con los valores que cumplen la condición.*

4. **Función `reduce`:**
   - **Objetivo:** *Sumar todos los precios filtrados que cumplen la condición.*
   - **Implementación:** *`.reduce((acum, price) => acum + price, 0)`*
   - **Función Flecha:** *`reduce` acumula los valores sumando `price` al acumulador `acum`. El `0` al final de `reduce` es el valor inicial del acumulador.*

5. **Resultado Final:** *Se imprime `sum`, que es `52`, la suma total de los precios que son mayores o iguales a `20` en el array `dollars`.*

---

### ***Caso 2: Implementación de Funciones en Cadena de Múltiples Líneas***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const dollars = ['32$', '15$', '12$', '17$', '20$'];

let sum = 0;

// Implementación de funciones en cadena de múltiples líneas
sum = dollars
  .map(dollar => Number(dollar.slice(0, dollar.length - 1)))
  .filter(dollar => dollar >= 20)
  .reduce((acum, price) => acum + price, 0);

console.log(sum); // Output: 52
```

---

#### ***Explicación:***

1. **Array de Precios:** *`dollars` es un array que contiene strings con precios en formato `"$NN"`, donde `NN` es un número.*

2. **Funciones en Cadena de Múltiples Líneas:**
   - *Las funciones `map`, `filter`, y `reduce` están escritas en líneas separadas para mejorar la legibilidad y organización del código.*

3. **Implementación:**
   - **Función `map`:** *`map(dollar => Number(dollar.slice(0, dollar.length - 1)))` convierte cada precio de string a número eliminando el símbolo `$`.*
   - **Función `filter`:** *`filter(dollar => dollar >= 20)` filtra los precios que son mayores o iguales a `20`.*
   - **Función `reduce`:** *`reduce((acum, price) => acum + price, 0)` suma todos los precios filtrados comenzando desde `0`.*

4. **Resultado Final:** *Se imprime `sum`, que es `52`, la suma total de los precios que son mayores o iguales a `20` en el array `dollars`.*

- *Ambas implementaciones son equivalentes en función y producen el mismo resultado, pero la segunda opción con funciones en cadena de múltiples líneas proporciona una estructura más clara y fácil de mantener, especialmente cuando las operaciones son más complejas o requieren más líneas de código.*
