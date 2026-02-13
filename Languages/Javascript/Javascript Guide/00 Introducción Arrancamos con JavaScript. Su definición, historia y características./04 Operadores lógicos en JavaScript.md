<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Operadores lógicos en JavaScript***

- **Los operadores lógicos en JavaScript se utilizan para evaluar expresiones lógicas y devuelven valores booleanos. Aquí te explico cada uno de ellos:**

## ***Operador lógico AND (&&)***

- *El operador `&&` devuelve `true` solo si ambos operandos son `true`.*

**Ejemplos:**

```javascript
true && true // → true
true && false // → false
false && false // → false
```

**Ejemplo en la vida real:** *Determinar si todas las luces están encendidas.*

## ***Operador lógico OR (||)***

- *El operador `||` devuelve `true` si al menos uno de los operandos es `true`.*

**Ejemplos:**

```javascript
true || true // → true
true || false // → true
false || false // → false
```

**Ejemplo en la vida real:** *Saber si hay al menos una luz encendida.*

## ***Operador lógico NOT (!)***

- *El operador `!` invierte el valor de un operando booleano.*

**Ejemplos:**

```javascript
!true // → false
!false // → true
```

**Ejemplo en la vida real:** *Apagar o encender una luz con un interruptor.*

## ***Combinando operadores lógicos y otros***

- *Puedes combinar operadores lógicos con operadores de comparación y aritméticos para crear expresiones más complejas.*

### ***Ejemplos***

```javascript
2 < 3 && 3 < 4 // → true
(2 + 2) < 3 && (10 < (8 * 2)) // → false
```

- *En el segundo ejemplo, primero se realizan las operaciones aritméticas y luego las comparaciones.*

### ***Ejercicios interactivos***

1. **Comprobar si 7 es mayor que 8 y menor que 10:**

   ```javascript
   7 > 8 && 7 < 10 // Respuesta correcta: false
   ```

2. **Decidir si puedo comprar un producto que cuesta 1500€ con un descuento del 25%, teniendo 1150€ en mi cartera:**

   ```javascript
   1500 * 0.75 <= 1150 // Respuesta correcta: true
   ```

### ***Más de dos operandos***

- *Los operadores lógicos también pueden usarse con más de dos operandos y combinados entre sí.*

**Ejemplos:**

```javascript
true && true && true // → true
true && true || false // → true
!true && !true // → false
false && true || !true // → false
```

**Examen interactivo:**

1. **¿Qué operador lógico se utiliza para comprobar si dos o más condiciones son verdaderas?**
   - *Respuesta: `AND (&&)`*

2. **¿Qué operador lógico se utiliza para invertir el valor de una expresión booleana?**
   - *Respuesta: `NOT (!)`*

3. **¿Qué valor devuelve la expresión `false || true`?**
   - *Respuesta: `true`*

- *Con práctica y ejemplos adicionales, te familiarizarás cada vez más con estos conceptos. ¡Sigue practicando!*

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/introduccion/operadores-logicos "https://www.aprendejavascript.dev/clase/introduccion/operadores-logicos")*
