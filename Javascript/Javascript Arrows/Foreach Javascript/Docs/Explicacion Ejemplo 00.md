<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Explicacion del Ejemplo 00***

```javascript
// Autor: Daniel Benjamin Perez Morales
// GitHub: https://github.com/D4nitrix13
// Correo electrónico: danielperezdev@proton.me

const prices = [32, 15, 12, 17, 20]

// Iterar sobre el array de precios usando forEach
prices.forEach(price => {
  console.log(price) // Imprimir cada precio
})
```

---

## ***Explicación***

1. **Array de Precios:** *`prices` es un array que contiene números enteros representando precios.*

2. **Método `forEach`:** *`forEach` es un método disponible en arrays en JavaScript que ejecuta una función proporcionada una vez por cada elemento del array.*

3. **Función Flecha:** *Dentro de `forEach`, utilizamos una función flecha (`price => { ... }`) que toma un parámetro `price`, representando cada elemento del array `prices`.*

4. **Acción de la Función:** *En este ejemplo, la función simplemente imprime cada precio utilizando `console.log(price)`.*

5. **Resultado:** *Al ejecutar este código, cada precio en el array `prices` será impreso en la consola, uno por línea.*

- *El método `forEach` es útil cuando necesitas ejecutar una operación para cada elemento de un array, sin necesidad de crear un nuevo array como lo harías con `map`.*
