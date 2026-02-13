<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Ejercicio 2: Implementación de rutas en Laravel con pruebas**

## **Apartado a: Ruta `/ejercicio2/a` (Devuelve lo que recibe)**

**Requisitos:**

- *Se debe crear una ruta en Laravel que acepte peticiones `POST`.*
- *La ruta recibe un JSON con los campos `name`, `description` y `price`.*
- *La respuesta debe ser exactamente igual al JSON recibido.*

**Ejemplo de petición y respuesta esperada:**

```bash
curl -sSL -X POST \
     -H 'Content-Type: application/json' \
     -H 'Accept: application/json' \
     -d '{"name":"Keyboard","description":"Mechanical RGB keyboard","price":200}' \
     http://172.17.0.2:80/ejercicio2/a | jq --ascii-output --color-output --indent 2
```

**Salida esperada:**

```json
{
  "name": "Keyboard",
  "description": "Mechanical RGB keyboard",
  "price": 200
}
```

**Ejecución de prueba en Laravel:**

```bash
php artisan test --filter test_ejercicio_2_apartado_a_devuelve_lo_que_recibe
```

**Salida esperada:**

```bash
PASS  Tests\Feature\Ejercicio2Test
✓ ejercicio 2 apartado a devuelve lo que recibe

Tests: 1 passed
Time: 0.15s
```

- **`php artisan test`** *→ Ejecuta las pruebas en Laravel usando PHPUnit.*
- **`--filter test_ejercicio_2_apartado_a_devuelve_lo_que_recibe`** *→ Filtra las pruebas y ejecuta solo la que verifica el apartado a.*

---

### **Apartado b: Ruta `/ejercicio2/b` (Valida si el precio es menor que cero)**

**Requisitos:**

- *La ruta `/ejercicio2/b` debe aceptar peticiones `POST`.*
- *Si el campo `price` es negativo, la respuesta debe tener código HTTP `422`.*
- *El contenido de la respuesta en este caso debe ser:*

  ```json
  {
    "message": "Price can't be less than 0"
  }
  ```

**Ejemplo de petición:**

```bash
curl -sSL -X POST \
     -H 'Content-Type: application/json' \
     -H 'Accept: application/json' \
     -d '{"name":"Keyboard","description":"Mechanical RGB keyboard","price":-200}' \
     http://172.17.0.2:80/ejercicio2/b
```

**Ejecución de prueba en Laravel:**

```bash
php artisan test --filter test_ejercicio_2_apartado_b_comprueba_si_el_precio_es_menor_que_cero
```

**Salida obtenida:**

```bash
WARN  Tests\Feature\Ejercicio2Test
- *ejercicio 2 apartado b comprueba si el precio es menor que cero → This test depends on "Tests\Feature\Ejercicio2Test::test_ejercicio_2_apartado_a_devuelve_lo_que_recibe" to pass.*

Tests: 1 skipped
Time: 0.01s
```

**Explicación de la advertencia:**

- *Laravel detecta que la prueba de este apartado depende de que primero pase la prueba del apartado `a`.*
- *Si la prueba del apartado `a` falla, la de este apartado será omitida (`skipped`).*

---

#### **Apartado c: Ruta `/ejercicio2/c` (Aplica descuento si es válido)**

**Requisitos:**

- *La ruta `/ejercicio2/c` debe aceptar peticiones `POST`.*
- *Opcionalmente, puede recibir un parámetro en la URL llamado `discount`.*
- *Si el `discount` es uno de estos códigos válidos:*
  - *`SAVE5`: Aplica 5% de descuento.*
  - *`SAVE10`: Aplica 10% de descuento.*
  - *`SAVE15`: Aplica 15% de descuento.*
- *Si el `discount` es inválido o no está presente, se devuelve `discount: 0`.*

**Ejemplo de petición con descuento válido:**

```bash
curl -sSL -X POST \
     -H 'Content-Type: application/json' \
     -H 'Accept: application/json' \
     -d '{"name":"Keyboard","description":"Mechanical RGB keyboard","price":200}' \
     http://172.17.0.2:80/ejercicio2/c?discount=SAVE10 | jq --ascii-output --color-output --indent 2
```

- **`curl`** *→ Cliente para hacer peticiones HTTP.*
- **`-sSL`**
  - **`-s (silent)`** *→ Oculta la barra de progreso.*
  - **`-S (show error)`** *→ Muestra errores en caso de fallo.*
  - **`-L (location)`** *→ Sigue redirecciones si las hay.*

- **`-X POST`** *→ Especifica que la petición es de tipo POST.*
- **`-H 'Content-Type: application/json'`** *→ Define que el contenido de la petición es JSON.*
- **`-H 'Accept: application/json'`** *→ Indica que se espera una respuesta en formato JSON.*
- **`-d '{"name":"Keyboard","description":"Mechanical RGB keyboard","price":200}'`** *→ Envía el JSON en el body de la petición.*
- **`http://172.17.0.2:80/ejercicio2/a`** *→ URL del endpoint.*
- **`| jq --ascii-output --color-output --indent 2`**
  - **`jq`** *→ Herramienta para formatear JSON en la terminal.*
    - **`--ascii-output`** *→ Muestra los caracteres especiales en ASCII en lugar de Unicode.*
    - **`--color-output`** *→ Resalta el JSON con colores.*
    - **`--indent 2`** *→ Indenta con 2 espacios.*

**Salida esperada:**

```json
{
  "name": "Keyboard",
  "description": "Mechanical RGB keyboard",
  "price": 180,
  "discount": "SAVE10"
}
```

**Ejemplo de petición con descuento inválido:**

```bash
curl -sSL -X POST \
     -H 'Content-Type: application/json' \
     -H 'Accept: application/json' \
     -d '{"name":"Keyboard","description":"Mechanical RGB keyboard","price":200}' \
     http://172.17.0.2:80/ejercicio2/c?discount=SAVE20 | jq --ascii-output --color-output --indent 2
```

**Salida obtenida:**

```json
{
  "name": "Keyboard",
  "description": "Mechanical RGB keyboard",
  "price": 200,
  "discount": "SAVE10"
}
```

**Error en la respuesta:**

- *El campo `discount` debería haber sido `0`, pero en la respuesta se muestra `SAVE10`, lo que indica un problema en la implementación.*

**Ejecución de prueba en Laravel:**

```bash
php artisan test --filter test_ejercicio_2_apartado_c_aplica_descuento
```

**Salida obtenida:**

```bash
WARN  Tests\Feature\Ejercicio2Test
- *ejercicio 2 apartado c aplica descuento → This test depends on "Tests\Feature\Ejercicio2Test::test_ejercicio_2_apartado_b_comprueba_si_el_precio_es_menor_que_cero" to pass.*

Tests: 1 skipped
Time: 0.01s
```

**Explicación de la advertencia:**

- *La prueba depende de que el test del apartado `b` pase correctamente. Como fue omitida, esta también es omitida.*

**Ejecución final de pruebas:**

```bash
php artisan test
```

**Salida esperada si todas las pruebas pasan:**

```bash
PASS  Tests\Feature\Ejercicio2Test
✓ ejercicio 2 apartado a devuelve lo que recibe
✓ ejercicio 2 apartado b comprueba si el precio es menor que cero
✓ ejercicio 2 apartado c aplica descuento

Tests: 3 passed
Time: 0.17s
```

---

### **Resumen de problemas detectados:**

1. **Prueba del apartado `b` omitida:**
   - *Laravel requiere que primero pase la prueba del apartado `a`.*
2. **Error en el descuento de `SAVE20`:**
   - *El código de descuento inválido debería devolver `discount: 0`, pero en la salida aparece `SAVE10`.*
   - *Es necesario revisar la lógica del controlador.*

*Estos errores deben corregirse para que todas las pruebas pasen correctamente.*

---

### *En **`cURL`**, el JSON debe escribirse en una sola línea sin espacios innecesarios, porque algunos intérpretes pueden interpretar mal el formato si se incluyen saltos de línea o espacios incorrectos.*

*Si escribimos el JSON con espacios de esta forma:*

```bash
curl -sSL -X POST \
     -H 'Content-Type: application/json' \
     -H 'Accept: application/json' \
     -d '{
            "name": "Keyboard",
            "description": "Mechanical RGB keyboard",
            "price": 200
        }' \
     http://172.17.0.2:80/ejercicio2/a | jq --ascii-output --color-output --indent 2
```

> [!WARNING]
> **Puede no funcionar correctamente.**  

### **Formato correcto para `cURL`**

*Siempre debemos escribir el JSON en una sola línea:*

```bash
-d '{"name":"Keyboard","description":"Mechanical RGB keyboard","price":200}'
```

*Esto evita errores de interpretación y asegura que `cURL` procese correctamente la petición.*

---

### **Ejemplo de uso en `cURL` con JSON correctamente formateado**

```bash
curl -sSL -X POST \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  -d '{"name":"Keyboard","description":"Mechanical RGB keyboard","price":200}' \
  http://172.17.0.2:80/ejercicio2/a
```

- **Nota:** *Si queremos evitar posibles problemas con comillas en diferentes shells, podemos usar `echo` y `jq` para asegurarnos de que el JSON esté bien formateado:*

```bash
echo '{"name":"Keyboard","description":"Mechanical RGB keyboard","price":200}' | jq -c
```
