<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 02***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const dollars = ['32$', '15$', '12$', '17$', '20$'];

let prices = [];

// Usar map con una arrow function para convertir las cadenas de dólares a números
prices = dollars.map(dollar => Number(dollar.slice(0, dollar.length - 1)));

console.log(prices); // [ 32, 15, 12, 17, 20 ]
```

---

## ***Explicación***

1. **Array de Dólares:** *`dollars` es un array que contiene cadenas con un signo `$` al final.*

2. **Uso de `map`:** *Se utiliza el método `map` de los arrays para aplicar una función a cada elemento del array `dollars`.*

3. **Funciones Flecha:** *La función pasada a `map` es una función flecha que toma cada elemento `dollar`, elimina el último carácter (`$`) usando `slice`, y convierte el resultado a un número con `Number`.*

4. **Asignación a `prices`:** *El resultado de `map` es un nuevo array con los valores convertidos, que se asigna a `prices`.*

5. **Impresión del Resultado:** *Se imprime el array `prices`, que contiene los números enteros correspondientes a las cantidades de dólares sin el signo `$`.*

---

### ***Características Modernas Utilizadas***

- **Arrow Functions:** *Las funciones flecha proporcionan una sintaxis más corta y clara para definir funciones anónimas.*
- **Método `map`:** *`map` es una manera funcional de transformar elementos de un array, haciendo el código más declarativo y fácil de leer.*

---

### ***Nota sobre Paréntesis en Arrow Functions***

**Si la arrow function tiene un solo parámetro, los paréntesis son opcionales. Ambas formas son correctas:**

```javascript
// Sin paréntesis
dollars.map(dollar => Number(dollar.slice(0, dollar.length - 1)));

// Con paréntesis
dollars.map((dollar) => Number(dollar.slice(0, dollar.length - 1)));
```

- **Ambas versiones hacen lo mismo, y la elección entre usar o no los paréntesis es una cuestión de preferencia personal o estilo de código.**
