<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 01***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const dollars = ['32$', '15$', '12$', '17$', '20$'];

let sum = 0;

// Implementación manual de map, filter y reduce con for...of
for (const item of dollars) {
  // Implementación de map (extracción y conversión del número)
  const price = Number(item.slice(0, item.length - 1));

  // Implementación de filter (condición de filtro)
  if (price >= 20) {
    // Implementación de reduce (acumulación de valores)
    sum += price;
  }
}

console.log(sum); // Output: 52
```

---

## ***Explicación***

1. **Array de Precios:** *`dollars` es un array que contiene strings con precios en formato `"$NN"`, donde `NN` es un número.*

2. **Bucle `for...of`:** *Utilizamos un bucle `for...of` para iterar sobre cada elemento del array `dollars`.*

3. **Implementación de `map`:**
   - **Objetivo:** *Extraer y convertir los precios de formato string a números.*
   - **Implementación:** *`const price = Number(item.slice(0, item.length - 1));`*
   - **Función:** *`Number` convierte el string del precio a un número eliminando el símbolo `$` al final.*

4. **Implementación de `filter`:**
   - **Objetivo:** *Filtrar los precios que son mayores o iguales a `20`.*
   - **Implementación:** *`if (price >= 20) { ... }`*
   - **Función:** *El `if` verifica si el precio es mayor o igual a `20`.*

5. **Implementación de `reduce`:**
   - **Objetivo:** *Sumar todos los precios filtrados que cumplen la condición.*
   - **Implementación:** *`sum += price;`*
   - **Función:** *Acumula el precio al total `sum` si cumple con la condición del filtro.*

6. **Resultado Final:** *Se imprime `sum`, que es `52`, la suma total de los precios que son mayores o iguales a `20` en el array `dollars`.*

- *Esta implementación manual con `for...of` demuestra cómo replicar el comportamiento de las funciones `map`, `filter` y `reduce` utilizando un enfoque funcional moderno en JavaScript, iterando sobre cada elemento del array y aplicando las transformaciones y operaciones necesarias.*
