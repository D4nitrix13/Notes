<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Ejercicio 3 - Descripción y Validación en Laravel**

## **Objetivo**

*Crear una ruta `/ejercicio3` en Laravel que acepte peticiones de tipo `POST` y valide un JSON con la siguiente estructura:*

```json
{
  "name": "Keyboard",
  "description": "Mechanical RGB Keyboard",
  "price": 200,
  "has_battery": true,
  "battery_duration": 8,
  "colors": ["blue", "white", "black"],
  "dimensions": { "width": 40, "height": 5, "length": 20 },
  "accessories": [
    { "name": "Wrist rest", "price": 20 },
    { "name": "Keycaps", "price": 15 }
  ]
}
```

## **Condiciones de validación**

**Para que el JSON sea válido, debe cumplir con las siguientes reglas:**

- **Todos los campos son obligatorios,** *excepto `battery_duration` si `has_battery` es `false`.*
- **Restricciones de texto:**
  - **`name`:** *Máximo **64 caracteres**.*
  - **`description`:** *Máximo **512 caracteres**.*
- **Restricciones numéricas:**
  - **`price`:** *Debe ser un **número mayor que cero**.*
  - **`battery_duration`:** *Debe ser un **número mayor que cero** (si está presente).*
  - *`dimensions`:*
    - **`width`, `height`, `length`:** *Deben ser **números mayores que cero**.*
- **Restricciones de listas:**
  - **`colors`:** *Debe ser un **array de strings**.*
  - **`accessories`:** *Cada elemento debe tener:*
    - **`name`:** ***String obligatorio**.*
    - **`price`:** ***Número mayor que cero**.*
- **Valores booleanos:**
  - *`has_battery` debe ser un **booleano** (`true` o `false`).*

---

## **Implementación en Laravel**

*Archivo: `ApplicationLaravel/routes/web.php`*

```php
// Ejercicio 3 - Definición de ruta y validación en Laravel
Route::post(
    uri: "/ejercicio3",
    action: function (Request $request) {
        $request->validate(
            rules: [
                'name' => 'required|string|max:64',
                'description' => 'required|string|max:512',
                'price' => 'required|numeric|min:0.01',
                'has_battery' => 'required|boolean',

                // Si has_battery es true, battery_duration debe existir y ser un número > 0
                'battery_duration' => 'required_if:has_battery,true|numeric|min:1',

                'colors' => 'required|array',
                'colors.*' => 'string',

                'dimensions' => 'required|array',
                'dimensions.width' => 'required|numeric|min:0.01',
                'dimensions.height' => 'required|numeric|min:0.01',
                'dimensions.length' => 'required|numeric|min:0.01',

                'accessories' => 'required|array',
                'accessories.*' => 'required|array',
                'accessories.*.name' => 'required|string',
                'accessories.*.price' => 'required|numeric|min:0.01',
            ]
        );
        return response()->json(data: [
            "message" => "Finish"
        ]);
    }
);
```

### **Explicación del código:**

- *Se define una ruta `POST` en `/ejercicio3`.*
- *Se valida la estructura del JSON con `validate()`.*
- *Si la validación es exitosa, se devuelve una respuesta JSON con `{"message": "Finish"}`.*
- *Se usan reglas de validación propias de Laravel para verificar cada campo.*

### **Otra manera de escribir la validación:**

*Otra forma equivalente de escribir la validación con `gt:0` en vez de `min:0.01`:*

```php
// Ejercicio 3 - Definición de ruta y validación en Laravel
Route::post(
    uri: "/ejercicio3",
    action: function (Request $request) {
        // Alternativa de validación
        $request->validate([
            'name' => 'required|string|max:64',
            'description' => 'required|string|max:512',
            'price' => 'required|numeric|gt:0',
            'has_battery' => 'required|boolean',
            'battery_duration' => 'required_if:has_battery,true|numeric|gt:0',
            'colors' => 'required|array',
            'colors.*' => 'required|string',
            'dimensions' => 'required|array',
            'dimensions.width' => 'required|numeric|gt:0',
            'dimensions.length' => 'required|numeric|gt:0',
            'dimensions.height' => 'required|numeric|gt:0',
            'accessories' => 'required|array',
            'accessories.*' => 'required|array',
            'accessories.*.name' => 'required|string',
            'accessories.*.price' => 'required|numeric|gt:0',
        ]);
    }
);
```

---

## **Explicación Detallada de Validaciones en Laravel**

*Laravel proporciona un sistema de validación robusto para manejar la entrada de datos en las solicitudes HTTP. A continuación, se explican en detalle cada una de las reglas de validación usadas en el código:*

---

## **Análisis del Código**

```php
$request->validate(
    rules: [
        'name' => 'required|string|max:64',
```

### **Explicación de cada regla**

- **`required`:** *Indica que el campo es obligatorio. Si está ausente o es `null`, la validación fallará.*
- **`string`:** *El valor debe ser una cadena de texto. Si se pasa un número o un array, la validación fallará.*
- **`max:64`:** *La longitud máxima permitida es **64 caracteres**.*

```php
        'description' => 'required|string|max:512',
```

- **`max:512`:** *La longitud máxima permitida es **512 caracteres**.*

```php
        'price' => 'required|numeric|min:0.01',
```

- **`numeric`:** *El valor debe ser un número (entero o decimal).*
- **`min:0.01`:** *El valor mínimo permitido es **0.01** (es decir, debe ser mayor que 0).*

```php
        'has_battery' => 'required|boolean',
```

- **`boolean`:** *Debe ser un **valor booleano** (`true` o `false`). Laravel acepta `1`, `0`, `"true"`, `"false"`, `true`, `false`.*

```php
        'battery_duration' => 'required_if:has_battery,true|numeric|min:1',
```

- **`required_if:has_battery,true`:** *El campo es obligatorio **solo si** `has_battery` es `true`.*
- **`numeric`:** *Debe ser un número.*
- **`min:1`:** *Debe ser al menos `1`.*

```php
        'colors' => 'required|array',
        'colors.*' => 'string',
```

- **`array`:** *`colors` debe ser una lista.*
- **`colors.*`:** *Significa que **cada elemento dentro de la lista `colors` debe ser un string**.*

```php
        'dimensions' => 'required|array',
        'dimensions.width' => 'required|numeric|min:0.01',
        'dimensions.height' => 'required|numeric|min:0.01',
        'dimensions.length' => 'required|numeric|min:0.01',
```

- **`dimensions` debe ser un array**.
- **Cada subcampo (`width`, `height`, `length`) debe ser numérico y mayor a `0.01`**.

```php
        'accessories' => 'required|array',
        'accessories.*' => 'required|array',
        'accessories.*.name' => 'required|string',
        'accessories.*.price' => 'required|numeric|min:0.01',
    ]
);
```

- **`accessories` debe ser una lista de objetos.**
- **`accessories.*`:** *Indica que **cada elemento dentro de `accessories` debe ser un array**.*
- **`accessories.*.name`:** *Debe ser un string obligatorio.*
- **`accessories.*.price`:** *Debe ser un número mayor a `0.01`.*

---

### **Significado de los Operadores**

1. **`|` (Pipe):** *Separa varias reglas dentro de una validación. Ejemplo:*

   ```php
   'name' => 'required|string|max:64'
   ```

   - *Aquí se combinan `required`, `string` y `max:64`.*

2. **`.*` (Wildcard en arrays):** *Se usa para validar cada elemento dentro de un array. Ejemplo:*

   ```php
   'colors.*' => 'string'
   ```

   - *Cada elemento de `colors` debe ser un string.*

3. **`:` (Parámetro en reglas):** *Se usa para definir valores dentro de una regla. Ejemplo:*

   ```php
   'max:64'
   ```

   - *Significa que el valor máximo permitido es 64 caracteres.*

4. **`=>` (Asignación en arrays asociativos de PHP):** *Se usa en PHP para asignar claves a valores dentro de un array asociativo. Ejemplo:*

   ```php
   'name' => 'required|string|max:64'
   ```

   - *La clave `name` tiene asignada la validación `'required|string|max:64'`.*

---

### **Ejemplo alternativo de validación:**

```php
$request->validate([
    'name' => 'required|string|max:64',
    'description' => 'required|string|max:512',
    'price' => 'required|numeric|gt:0',
    'has_battery' => 'required|boolean',
    'battery_duration' => 'required_if:has_battery,true|numeric|gt:0',
    'colors' => 'required|array',
    'colors.*' => 'required|string',
    'dimensions' => 'required|array',
    'dimensions.width' => 'required|numeric|gt:0',
    'dimensions.length' => 'required|numeric|gt:0',
    'dimensions.height' => 'required|numeric|gt:0',
    'accessories' => 'required|array',
    'accessories.*' => 'required|array',
    'accessories.*.name' => 'required|string',
    'accessories.*.price' => 'required|numeric|gt:0',
]);
```

- **`gt:0`:** *Similar a `min:0.01`, pero estrictamente mayor que 0.*

---

## **Existen varias reglas similares a `gt` (greater than, "mayor que") en Laravel.**

1. **`gt:value`** *(Greater Than)*
   - *El campo debe ser **mayor** que el `value` especificado.*
   - *Ejemplo: `'price' => 'numeric|gt:0'` (el precio debe ser mayor que 0).*

2. **`gte:value`** *(Greater Than or Equal)*
   - *El campo debe ser **mayor o igual** que el `value` especificado.*
   - *Ejemplo: `'age' => 'integer|gte:18'` (edad debe ser **18 o más**).*

3. **`lt:value`** *(Less Than)*
   - *El campo debe ser **menor** que el `value` especificado.*
   - *Ejemplo: `'discount' => 'numeric|lt:100'` (descuento debe ser menor a 100).*

4. **`lte:value`** *(Less Than or Equal)*
   - *El campo debe ser **menor o igual** que el `value` especificado.*
   - *Ejemplo: `'max_participants' => 'integer|lte:50'` (máximo de participantes es **50 o menos**).*

5. **`between:min,max`**  
   - *El valor debe estar **dentro del rango** definido por `min` y `max`.*
   - *Ejemplo: `'score' => 'numeric|between:1,10'` (el puntaje debe estar entre **1 y 10**).*

6. **`digits:value`**  
   - *El campo debe ser un número con exactamente `value` dígitos.*
   - *Ejemplo: `'code' => 'digits:5'` (el código debe tener exactamente 5 dígitos).*

7. **`digits_between:min,max`**  
   - *El número debe tener entre `min` y `max` dígitos.*
   - *Ejemplo: `'phone' => 'digits_between:8,12'` (el número de teléfono debe tener **entre 8 y 12 dígitos**).*

*Estas reglas son útiles para validar valores numéricos en Laravel.*

## **Código List Validation**

```php
$request->validate(
    rules: [
        'name' => [
            'required',  // Campo obligatorio
            'string',    // Debe ser una cadena de texto
            'max:64'     // Longitud máxima de 64 caracteres
        ],
```

```php
        'description' => [
            'required',  // Campo obligatorio
            'string',    // Debe ser una cadena de texto
            'max:512'    // Longitud máxima de 512 caracteres
        ],
```

```php
        'price' => [
            'required',  // Campo obligatorio
            'numeric',   // Debe ser un número
            'min:0.01'   // Debe ser al menos 0.01
        ],
```

```php
        'has_battery' => [
            'required',  // Campo obligatorio
            'boolean'    // Debe ser verdadero o falso
        ],
```

```php
        'battery_duration' => [
            'required_if:has_battery,true',  // Obligatorio si has_battery es true
            'numeric',   // Debe ser un número
            'min:1'      // Debe ser al menos 1
        ],
```

```php
        'colors' => [
            'required',  // Campo obligatorio
            'array'      // Debe ser un array
        ],
        'colors.*' => [
            'string'     // Cada elemento del array debe ser una cadena de texto
        ],
```

```php
        'dimensions' => [
            'required',  // Campo obligatorio
            'array'      // Debe ser un array
        ],
        'dimensions.width' => [
            'required',  // Campo obligatorio
            'numeric',   // Debe ser un número
            'min:0.01'   // Debe ser al menos 0.01
        ],
        'dimensions.height' => [
            'required',
            'numeric',
            'min:0.01'
        ],
        'dimensions.length' => [
            'required',
            'numeric',
            'min:0.01'
        ],
```

```php
        'accessories' => [
            'required',  // Campo obligatorio
            'array'      // Debe ser un array
        ],
        'accessories.*' => [
            'required',  // Cada accesorio debe ser un array
            'array'
        ],
        'accessories.*.name' => [
            'required',  // Campo obligatorio
            'string'     // Debe ser una cadena de texto
        ],
        'accessories.*.price' => [
            'required',  // Campo obligatorio
            'numeric',   // Debe ser un número
            'min:0.01'   // Debe ser al menos 0.01
        ],
    ]
);
```

- **Significado de los Operadores**

1. **`|` (Pipe):** *Se usaba para separar reglas dentro de una validación. Ahora, en lugar de `|`, se usa una lista de reglas en un array.*

2. **`.*` (Wildcard en arrays):** *Se usa para validar cada elemento dentro de un array. Ejemplo:*

   ```php
   'colors.*' => ['string']
   ```

   - *Cada elemento de `colors` debe ser un string.*

3. **`:` (Parámetro en reglas):** *Se usa para definir valores dentro de una regla. Ejemplo:*

   ```php
   'max:64'
   ```

   - *Significa que el valor máximo permitido es 64 caracteres.*

4. **`=>` (Asignación en arrays asociativos de PHP):** *Se usa en PHP para asignar claves a valores dentro de un array asociativo. Ejemplo:*

   ```php
   'name' => ['required', 'string', 'max:64']
   ```

   - *La clave `name` tiene asignada la validación en formato de array.*

- **Ejemplo alternativo de validación:**

```php
$request->validate([
    'name' => ['required', 'string', 'max:64'],
    'description' => ['required', 'string', 'max:512'],
    'price' => ['required', 'numeric', 'gt:0'],
    'has_battery' => ['required', 'boolean'],
    'battery_duration' => ['required_if:has_battery,true', 'numeric', 'gt:0'],
    'colors' => ['required', 'array'],
    'colors.*' => ['required', 'string'],
    'dimensions' => ['required', 'array'],
    'dimensions.width' => ['required', 'numeric', 'gt:0'],
    'dimensions.length' => ['required', 'numeric', 'gt:0'],
    'dimensions.height' => ['required', 'numeric', 'gt:0'],
    'accessories' => ['required', 'array'],
    'accessories.*' => ['required', 'array'],
    'accessories.*.name' => ['required', 'string'],
    'accessories.*.price' => ['required', 'numeric', 'gt:0'],
]);
```

---

## **Recursos y Herramientas**

### **Documentación de Laravel**

- *[Reglas de validación en Laravel](https://laravel.com/docs/12.x/validation#available-validation-rules "https://laravel.com/docs/12.x/validation#available-validation-rules")*
- *[Conversor JSON a PHP Array](https://appdevtools.com/json-php-array-converter "https://appdevtools.com/json-php-array-converter")*

### **Extensiones de VSCode útiles**

- *`rangav.vscode-thunder-client` (para pruebas de APIs REST)*
- *`humao.rest-client` (alternativa para pruebas de APIs REST)*

*![Petition Correct](/Docs/Images/Send%20Petition%20Correct.png "/Docs/Images/Send%20Petition%20Correct.png")*
*![Petition Incorrect](/Docs/Images/Send%20Petition%20Incorrect.png "/Docs/Images/Send%20Petition%20Incorrect.png")*

### **Herramienta para probar la API**

- **`cartero`:** *instalar con `sudo snap install cartero`*

### **Foros y Recursos de Discusión**

- *[Validar un campo entero que debe ser mayor que otro](https://stackoverflow.com/questions/32036882/laravel-validate-an-integer-field-that-needs-to-be-greater-than-another "https://stackoverflow.com/questions/32036882/laravel-validate-an-integer-field-that-needs-to-be-greater-than-another")*
- *[Reglas de validación condicional en Laravel](https://stackoverflow.com/questions/42319050/laravel-validation-rules-optional-but-validated-if-present "https://stackoverflow.com/questions/42319050/laravel-validation-rules-optional-but-validated-if-present")*
- *[Ejemplos de validación condicional en Laravel](https://laraveldaily.com/post/laravel-conditional-validation-other-fields-examples "https://laraveldaily.com/post/laravel-conditional-validation-other-fields-examples")*

---

## **Ejecución de Tests en Laravel**

*Para ejecutar los tests de validación en Laravel:*

```bash
php artisan test
```

**Ejemplo de salida de la ejecución de pruebas:**

```bash
   PASS  Tests\Feature\Ejercicio3Test
  ✓ ejercicio3 datos correctos pasan la validación
  ✓ ejercicio3 campo battery_duration no se tiene en cuenta si has_battery es falso
  ✓ ejercicio3 datos con campos que faltan no pasan la validación
  ✓ ejercicio3 nombre y descripción con demasiados caracteres no pasan la validación
  ✓ ejercicio3 precios de un centavo son correctos
  ✓ ejercicio3 datos con campos null o números negativos no pasan la validación

  Tests:  6 passed
  Time:   0.22s
```

**Ejecutar solo un test en particular:**

```bash
php artisan test --filter Ejercicio3Test
```

**Ejecutar un test específico:**

```bash
php artisan test --filter test_ejercicio3_datos_correctos_pasan_la_validacion
```
