<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Los operadores de comparación***

- *Los operadores de comparación en JavaScript nos permiten comparar dos valores y siempre devuelven un valor booleano (true o false).*

- *Por ejemplo, podemos comparar si un número es mayor que otro con el operador `>`, o si un número es menor que otro con el operador `<`.*

```javascript
5 > 3 // true
5 < 3 // false
```

- *También tenemos los operadores `>=` y `<=`, que nos permiten comparar si un número es mayor o igual que otro, o si un número es menor o igual que otro.*

```javascript
5 >= 3 // true
5 >= 5 // true
5 <= 3 // false
5 <= 5 // true
```

- *Para verificar si dos valores son iguales, usamos el operador `===`, y para verificar si son diferentes, usamos `!==`.*

```javascript
5 === 5 // true
5 !== 5 // false
```

## ***Ejercicios de código interactivos***

- *Escribe un código que compruebe si 10 es mayor o igual que 9*

```javascript
10 >= 9 // true
```

**Comprueba que 0 es igual a 0:**

```javascript
0 === 0 // true
```

### ***Comparando cadenas de texto***

- *No solo podemos usar los operadores de comparación para números, también podemos usarlos para cadenas de texto y otros tipos de datos.*

```javascript
'JavaScript' === 'JavaScript' // true
'JavaScript' === 'Java' // false
"JavaScript" !== 'PHP' // true
`Estoy Aprendiendo JavaScript` === 'Estoy Aprendiendo JavaScript' // true
```

### ***Comportamiento con cadenas de texto y booleanos***

- *Podemos usar los operadores `>`, `>=`, `<` y `<=` para comparar cadenas de texto. JavaScript compara las cadenas basándose en sus valores Unicode.*

```javascript
'Alfa' > 'Beta' // false
'Omega' > 'Beta' // true
'alfa' > 'Alfa' // true
```

**También podemos comparar booleanos:**

```javascript
true === true // true
true === false // false
false !== false // false
```

**Para datos booleanos, es interesante notar que `true` es considerado mayor que `false`.**

### ***Comparando valores de diferentes tipos***

- *En JavaScript, aunque posible, comparar valores de diferentes tipos no siempre es recomendable. Más adelante veremos los operadores de igualdad débil `==` y desigualdad débil `!=`, pero por ahora, es mejor usar siempre el operador de igualdad estricta `===` y el operador de desigualdad estricta `!==`.*

### ***Examen interactivo***

**¿Cuál es el resultado de `24 > 12`?**

1. *`true`*
2. *`false`*

    - *¡Correcto! La afirmación `24 > 12` es verdadera.*

**¿Los operadores de comparación sólo se pueden usar con números?:**

1. *Sí, sólo ahí tiene sentido.*
2. *No, se pueden usar con otros tipos de datos, como cadenas de texto o booleanos*

    - *¡Exacto! Los operadores de comparación en JavaScript se pueden usar con diferentes tipos de datos, no solo con números.*

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/introduccion/operadores-de-comparacion "https://www.aprendejavascript.dev/clase/introduccion/operadores-de-comparacion")*
