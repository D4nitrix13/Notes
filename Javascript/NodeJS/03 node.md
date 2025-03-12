<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Node.js REPL: ¿Qué es y Cómo Funciona?***

- *Cuando ejecutas el comando `node` en la terminal sin ningún argumento adicional, estás entrando en un entorno interactivo conocido como REPL. REPL es un acrónimo que significa **Read-Eval-Print Loop**. Es una herramienta poderosa para probar código JavaScript en tiempo real, y es muy útil para desarrolladores que quieren experimentar o depurar rápidamente sin necesidad de crear ficheros separados.*

## ***Componentes del REPL***

1. **Read (Leer):** *Lee la entrada del usuario.*
2. **Eval (Evaluar):** *Evalúa (ejecuta) el código ingresado.*
3. **Print (Imprimir):** *Imprime el resultado de la evaluación.*
4. **Loop (Bucle):** *Vuelve al paso de lectura y repite el proceso.*

### ***Uso Básico del REPL***

**Al entrar en el REPL, verás un mensaje de bienvenida y algunas instrucciones básicas:**

```plaintext
Welcome to Node.js v22.3.0.
Type ".help" for more information.
```

**Puedes ingresar comandos de JavaScript directamente en la consola:**

```javascript
> const nombre = "Daniel"
undefined
```

- **Entrada:** *`const nombre = "Daniel"`*
- **Salida:** *`undefined` (El REPL muestra `undefined` porque la asignación de una constante no tiene un valor de retorno explícito.)*

```javascript
> console.log(nombre)
Daniel
undefined
```

- **Entrada:** *`console.log(nombre)`*
- **Salida:** *`Daniel` (resultado de `console.log`) seguido de `undefined` (porque `console.log` devuelve `undefined`).*

### ***Comandos Especiales del REPL***

**Puedes utilizar varios comandos especiales en el REPL para facilitar tu trabajo:**

- **.help:** *Muestra la ayuda del REPL.*

```plaintext
> .help
.break    Sometimes you get stuck, this gets you out
.clear    Alias for .break
.editor   Enter editor mode
.exit     Exit the REPL
.help     Print this help message
.load     Load JS from a file into the REPL session
.save     Save all evaluated commands in this REPL session to a file
```

- **.break / .clear:** *Salir del bucle actual o limpiar la entrada.*
- **.editor:** *Entra en modo editor para escribir múltiples líneas de código.*
- **.exit:** *Salir del REPL.*
- **.load [filename]:** *Cargar un fichero JavaScript en la sesión del REPL.*
- **.save [filename]:** *Guardar todos los comandos evaluados en la sesión del REPL a un fichero.*

### ***Ejemplos de Uso***

**Definiendo una variable:**

```javascript
> const nombre = "Daniel"
undefined
```

**Mostrando el valor de la variable:**

```javascript
> console.log(nombre)
Daniel
undefined
```

**Definiendo una función y llamándola:**

```javascript
> function saludar(name) { console.log("hola " + name) }
undefined
> saludar("Daniel Perez")
hola Daniel Perez
undefined
```

### ***Atajos de Teclado***

- **Ctrl+C:** *Abortar la expresión actual.*
- **Ctrl+D:** *Salir del REPL.*

### ***Ventajas del REPL***

- **Interactividad:** *Permite probar rápidamente fragmentos de código.*
- **Aprendizaje:** *Excelente herramienta para aprender y experimentar con JavaScript y Node.js.*
- **Depuración:** *Facilita la depuración de código y la resolución de problemas en tiempo real.*

- *El REPL de Node.js es una herramienta extremadamente útil para desarrolladores, permitiendo una manera rápida y eficiente de interactuar con el entorno de ejecución de JavaScript.*
