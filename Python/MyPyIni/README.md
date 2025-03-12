<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración de MyPy:***

```ini
[mypy]
# Habilitar verificaciones estrictas
strict = True
```

- **strict:** *Esta opción habilita un conjunto de verificaciones estrictas que ayudan a garantizar que el código cumpla con las mejores prácticas de tipado. Cuando se activa, MyPy aplicará reglas más rigurosas en el chequeo de tipos en todo el código, lo que puede ayudar a identificar errores potenciales y mejorar la calidad del código.*

```ini
# Habilitar chequeo de tipos en los métodos que se encuentran en módulos de código externo
disallow_untyped_calls = True
disallow_untyped_defs = True
```

- **disallow_untyped_calls:** *Si se activa, MyPy generará un error si se intenta llamar a una función que no tiene anotaciones de tipo. Esto es útil para evitar que se utilicen funciones que no están tipadas, lo que podría causar errores en tiempo de ejecución.*
  
- **disallow_untyped_defs:** *Similar a `disallow_untyped_calls`, esta opción genera un error si se define una función sin anotaciones de tipo. Esto asegura que todas las funciones tengan tipos explícitos, lo que ayuda a la claridad y la mantenibilidad del código.*

```ini
# Deshabilitar inferencias de tipo en funciones o métodos que no tienen tipos explícitos
warn_return_any = True
```

- **warn_return_any:** *Cuando se activa, MyPy generará una advertencia si una función no tiene un tipo de retorno explícito y devuelve un valor de tipo `Any`. Esto es útil para identificar funciones que pueden no estar cumpliendo con las expectativas de tipo, ya que el tipo `Any` no proporciona información sobre qué tipo se espera.*

```ini
# Fallar si se encuentran errores en el código
strict_optional = True
```

- **strict_optional:** *Si se habilita, MyPy considerará que los tipos `Optional[T]` (donde `T` es cualquier tipo) son diferentes de `T`. Esto significa que MyPy será más estricto al manejar valores que podrían ser `None`, lo que puede ayudar a evitar errores en tiempo de ejecución relacionados con el manejo incorrecto de valores `None`.*

```ini
# Informa cuando se utilizan variables no definidas
disallow_untyped_decorators = True
```

- **disallow_untyped_decorators:** *Esta opción generará un error si se utiliza un decorador que no tiene tipos especificados. Esto es especialmente útil porque los decoradores a menudo modifican el comportamiento de las funciones, y tener tipos claros es esencial para comprender su efecto.*

```ini
# Habilitar chequeo en cualquier fichero que use tipos de `Any`
disallow_any_expr = True
disallow_any_unimported = True
```

- **disallow_any_expr:** *Al habilitar esta opción, MyPy generará un error si se encuentra cualquier expresión que tenga un tipo de `Any`. Esto ayuda a evitar que se utilicen tipos ambiguos que pueden conducir a errores en tiempo de ejecución.*
  
- **disallow_any_unimported:** *Esta opción generará un error si se intenta usar un tipo `Any` de un módulo que no se ha importado. Esto asegura que los tipos que se utilizan en el código provengan de módulos que han sido importados y que se tengan definiciones claras de tipos.*

```ini
# Habilitar advertencias para el uso de tipos `Any`
warn_unused_ignores = True
```

- **warn_unused_ignores:** *Esta opción generará advertencias si se utilizan comentarios de tipo `# type: ignore` que no son necesarios. Esto ayuda a limpiar el código y asegura que solo se utilicen ignorancias cuando realmente son necesarias, lo que mejora la calidad general del tipado.*

```ini
# Fallar en el chequeo si hay nombres en conflicto
check_untyped_defs = True
```

- **check_untyped_defs:** *Cuando se activa, MyPy comprobará las definiciones de funciones no tipadas en el contexto del código. Esto significa que incluso si una función no tiene anotaciones de tipo, MyPy intentará inferir su tipo basándose en el uso dentro del código y generará errores si hay conflictos.*

```ini
# Permitir solo imports que sean absolutamente necesarios
follow_imports = silent
```

- **follow_imports:** *Esta opción especifica cómo MyPy debe manejar las importaciones. `silent` significa que MyPy no generará advertencias o errores sobre las importaciones que no se pueden encontrar o que no están tipadas. Esto puede ser útil para proyectos grandes donde algunas dependencias pueden no tener anotaciones de tipo, pero es importante utilizar esta opción con precaución, ya que puede ocultar problemas en el código.*

## ***Resumen***

*Esta configuración de MyPy es bastante estricta y está diseñada para ayudar a los desarrolladores a escribir código Python más seguro y fácil de mantener. Al forzar la especificación de tipos, evitar el uso de `Any` sin justificación y garantizar que las funciones y decoradores estén correctamente tipados, se reduce la probabilidad de errores en tiempo de ejecución y se mejora la claridad del código. Esto es especialmente valioso en proyectos grandes o en aquellos en los que múltiples desarrolladores están trabajando juntos.*
