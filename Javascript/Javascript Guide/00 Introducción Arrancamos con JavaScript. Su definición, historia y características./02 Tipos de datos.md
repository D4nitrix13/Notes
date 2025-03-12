<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Tipos de datos en JavaScript***

- *En JavaScript, al igual que en cualquier otro lenguaje de programación, necesitamos entender los tipos de datos para representar información del mundo real en nuestro código. Estos se dividen en dos grandes grupos: primitivos y no primitivos. Ahora nos enfocaremos en los tipos primitivos.*

**Dentro de los tipos primitivos encontramos 7 tipos de datos:**

- *`number`*
- *`string`*
- *`boolean`*
- *`null`*
- *`undefined`*
- *`symbol`*
- *`bigint`*

**En esta lección nos centraremos en los primeros tres, que son los más utilizados al inicio del curso.**

## ***Números***

**Los números (tipo `number`) son los datos más básicos en JavaScript y pueden representar tanto enteros como decimales:**

```javascript
7
3.14
19.95
2.998e8
-1
```

### ***Operadores aritméticos***

**Con los números, puedes usar los siguientes operadores aritméticos para realizar operaciones matemáticas:**

- **`+`:** *suma*
- **`-`:** *resta*
- **`*`:** *multiplicación*
- **`/`:** *división*
- **`%`:** *módulo (resto de la división)*
- **`**`:** *exponente*

Ejemplos:

```javascript
2 + 2 // 4
4 - 2 // 2
3 * 2 // 6
2 / 2 // 1
2 % 2 // 0
3 ** 3 // 27
```

#### ***Comentarios en JavaScript***

- *¿Qué significa el `//` que ves en los ejemplos? Es un comentario. En JavaScript, los comentarios se escriben con `//` y son útiles para explicar el código sin que sea ejecutado por el navegador.*

#### ***Orden de precedencia y paréntesis***

**Al igual que en matemáticas, las operaciones siguen un orden de precedencia. Por ejemplo:**

```javascript
2 + 2 * 3 // 8
(2 + 2) * 3 // 12
```

### ***Cadenas de texto***

**Las cadenas de texto (tipo `string`) son otro tipo de dato común en JavaScript. Se representan entre comillas simples, dobles o acentos graves:**

```javascript
'Estás aprendiendo JavaScript'
"JavaScript te va a gustar"
`Esto es una cadena de texto`
```

**Las comillas simples y dobles funcionan igual, pero los acentos graves permiten escribir cadenas multilínea:**

```javascript
`Esto es una cadena de texto
que ocupa varias líneas. Puedes escribir
tantas líneas como quieras`
```

### ***Concatenación de cadenas***

**Para unir dos cadenas de texto, utilizamos el operador `+`:**

```javascript
'Estás aprendiendo ' + 'JavaScript' // 'Estás aprendiendo JavaScript'
```

### ***Booleanos***

**Los booleanos representan solo dos valores: `true` (verdadero) o `false` (falso). Ejemplos:**

- *¿La luz está encendida (`true`) o apagada (`false`)?*
- *¿Está lloviendo (`true`) o no está lloviendo (`false`)?*
- *¿Está el usuario logueado (`true`) o no está logueado (`false`)?*

```javascript
true
false
```

### ***Examen interactivo***

**¿Cuántos tipos de datos existen en JavaScript?**

1. *Sólo existen 2 tipos de datos*
2. *9 tipos de datos que se dividen en dos grandes grupos*

    - *¡Efectivamente! A día de hoy existen 9 tipos de datos distintos en JavaScript (aunque en el futuro puede que se añadan más), que están divididos en 2 grandes grupos: los tipos primitivos y los no primitivos.*

**¿Cuántos valores se pueden representar en el tipo de dato Boolean?**

1. *`true` y `false`*

    - *Exacto, los tipos booleanos sólo pueden ser verdadero o falso.*

**El operador + se utiliza para...**

1. *Sólo sirve para sumar dos números*
2. *Concatenar dos textos*
3. *Depende del tipo de dato que se esté utilizando*

    - *¡Exacto! El operador + será utilizado para sumar dos números o para concatenar dos cadenas de texto, dependiendo del tipo de dato que se esté utilizando en la operación.*

> [!TIP]
> *[Recurso](https://www.aprendejavascript.dev/clase/introduccion/tipos-de-datos "https://www.aprendejavascript.dev/clase/introduccion/tipos-de-datos")*
