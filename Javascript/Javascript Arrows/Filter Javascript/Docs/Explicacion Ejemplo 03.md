<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 03***

---

## ***Caso 1: Función Flecha con Paréntesis***

```javascript
const prices = [32, 15, 12, 17, 20];

const expensive = prices.filter((dollar) => dollar >= 20);

console.log(expensive); // [ 32, 20 ]
```

---

## ***Explicación***

1. **Array de Precios:** *`prices` es un array que contiene números enteros representando precios.*

2. **Método `filter`:** *`filter` es un método de los arrays en JavaScript que crea un nuevo array con todos los elementos que pasan una prueba (función callback).*

3. **Función Flecha con Paréntesis:** *`(dollar) => dollar >= 20` es una función flecha que toma un solo parámetro `dollar`. Los paréntesis alrededor de `dollar` son opcionales en este caso porque es un solo parámetro.*

4. **Condición `>=`:** *Dentro de la función flecha, se evalúa si `dollar` es mayor o igual a `20`.*

5. **Retorno de `filter`:** *La función flecha devuelve `true` si la condición se cumple (es decir, si `dollar` es mayor o igual a `20`), lo cual indica que el elemento debe ser incluido en el nuevo array resultante.*

6. **Array Resultante `expensive`:** *El resultado de `filter` es almacenado en el array `expensive`, que contiene los precios filtrados que son mayores o iguales a `20`.*

7. **Impresión del Resultado:** *Se imprime el array `expensive`, que contiene los precios filtrados `[ 32, 20 ]`.*

---

### ***Caso 2: Función Flecha sin Paréntesis***

```javascript
const prices = [32, 15, 12, 17, 20];

const expensive = prices.filter(dollar => dollar >= 20);

console.log(expensive); // [ 32, 20 ]
```

---

#### ***Explicación:***

1. **Array de Precios:** *`prices` es un array que contiene números enteros representando precios.*

2. **Método `filter`:** *Al igual que en el caso anterior, `filter` es un método de los arrays que crea un nuevo array con elementos que pasan una prueba (función callback).*

3. **Función Flecha sin Paréntesis:** *`dollar => dollar >= 20` es una función flecha que toma un solo parámetro `dollar`. En este caso, no se utilizan paréntesis alrededor de `dollar`.*

4. **Condición `>=`:** *Dentro de la función flecha, se evalúa si `dollar` es mayor o igual a `20`.*

5. **Retorno de `filter`:** *La función flecha devuelve `true` si la condición se cumple (es decir, si `dollar` es mayor o igual a `20`), lo cual indica que el elemento debe ser incluido en el nuevo array resultante.*

6. **Array Resultante `expensive`:** *El resultado de `filter` es almacenado en el array `expensive`, que contiene los precios filtrados que son mayores o iguales a `20`.*

7. **Impresión del Resultado:** *Se imprime el array `expensive`, que contiene los precios filtrados `[ 32, 20 ]`.*

---

### ***Comparación***

- *Ambos enfoques son equivalentes en términos de funcionalidad y producen el mismo resultado `[ 32, 20 ]`. La diferencia radica principalmente en el estilo de codificación y la preferencia personal. La versión sin paréntesis alrededor del parámetro es más concisa y es comúnmente utilizada en situaciones donde hay un solo parámetro en la función flecha.*
