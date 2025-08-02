<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Paginación en Laravel: Uso, Ventajas y Comparación con Limitación Manual**

*[Laravel Eloquent Limit And Offset](https://stackoverflow.com/questions/35643192/laravel-eloquent-limit-and-offset "https://stackoverflow.com/questions/35643192/laravel-eloquent-limit-and-offset")*
*[Pagination](https://laravel.com/docs/11.x/pagination "https://laravel.com/docs/11.x/pagination")*
*[Queries Main-Content](https://laravel.com/docs/11.x/queries#main-content "https://laravel.com/docs/11.x/queries#main-content")*

## **Objetivo**

*Implementar paginación usando el sistema nativo de Laravel para dividir grandes volúmenes de datos (como contactos) en páginas, aplicar estilos Bootstrap 5, y entender cuándo es mejor usar `take(n)` en lugar de `paginate(n)`.*

---

## **1. Activar la paginación en Blade**

### **Vista:** `resources/views/contacts/index.blade.php`

```php
{{ $contacts->links() }}
```

### **Explicación:**

* *Muestra los enlaces de paginación (`<< anterior | siguiente >>`) automáticamente.*
* *Solo funciona si `$contacts` es un objeto de tipo `LengthAwarePaginator` o `Paginator`.*

---

## **2. Habilitar soporte para Bootstrap 5**

### **Archivo:** `app/Providers/AppServiceProvider.php`

```php
use Illuminate\Pagination\Paginator;

public function boot()
{
    Paginator::useBootstrapFive();
}
```

* **Explicación:**

* *Laravel usará los estilos de Bootstrap 5 para generar los enlaces de paginación automáticamente (`.pagination`, `.page-item`, etc.).*

---

## **3. Controlador con paginación**

### **Archivo:** `app/Http/Controllers/ContactController.php`

```php
public function index()
{
    $contacts = auth()->user()
        ->contacts()
        ->orderBy('name', 'desc')
        ->paginate(6);

    return view('contacts.index', [
        'contacts' => $contacts
    ]);
}
```

* **Explicación:**

* *`paginate(6)`: Devuelve 6 resultados por página y convierte el resultado en un objeto `Paginator`.*
* *`orderBy('name', 'desc')`: Ordena alfabéticamente en orden descendente.*
* *El resultado es accesible vía:*

  ```bash
  http://localhost:8000/contacts?page=1
  ```

---

## **Parámetros de Consulta en Paginación de Laravel**

* **Objetivo**

*Entender cómo Laravel utiliza parámetros de consulta (`query parameters`) para controlar la navegación entre páginas en una lista paginada.*

---

## **URL de ejemplo**

```bash
http://localhost:8000/contacts?page=1
```

---

## **Explicación del parámetro `page=1`**

### **`?page=1`**

* *Este es un **query parameter** (parámetro de consulta) que forma parte de la URL.*
* *Laravel lo utiliza internamente para saber **qué página de resultados se desea mostrar**.*
* *Se pasa automáticamente cuando usas `{{ $contacts->links() }}` en tu Blade.*

---

### **¿Qué representa?**

| **Componente** | **Significado**                                                                       |
| -------------- | ------------------------------------------------------------------------------------- |
| *`/contacts`*  | *Ruta base definida en Laravel (por ejemplo: `Route::get('/contacts', ...)`)*         |
| *`?page=1`*    | *Parámetro que indica a Laravel que debe mostrar la **primera página** de resultados* |

---

## **¿Qué ocurre si cambiamos el valor?**

* *`?page=2`: muestra la segunda página.*
* *`?page=5`: muestra la quinta página (si existe).*
* *Si se pasa un valor que no existe (como `?page=9999` y no hay tantos registros), Laravel simplemente mostrará una página vacía.*

---

## **¿Quién genera ese `?page=...`?**

**Laravel lo incluye automáticamente cuando usas:**

```php
{{ $contacts->links() }}
```

**Esta función genera un conjunto de enlaces de navegación tipo:**

```html
<a class="page-link" href="http://localhost:8000/contacts?page=1" rel="prev">&laquo; Previous</a>
<a class="page-link" href="http://localhost:8000/contacts?page=2" rel="prev">&laquo; Previous</a>
...
```

---

## **¿Puedo acceder a este valor desde el backend?**

**Sí. Puedes usar:**

```php
$request->query('page'); // Devuelve '1' si la URL es ?page=1
```

---

## **Importante sobre SEO y paginación**

**Laravel mantiene las URLs limpias y amigables como:**

```bash
/contacts?page=1
/contacts?page=2
```

---

## **4. Comparación: paginación vs limitación manual (`take(n)`)**

### **Ejemplo con paginación (consume más recursos):**

```php
$contacts = auth()->user()
    ->contacts()
    ->latest()
    ->paginate(1000);
```

* *Laravel ejecuta una query con `LIMIT` y también hace un `COUNT(*)` adicional para saber el total de registros y calcular cuántas páginas existen.*
* *Esto puede consumir más recursos si tienes **miles de registros**.*

---

### **Ejemplo con limitación manual (más eficiente):**

```php
$contacts = auth()->user()
    ->contacts()
    ->latest()
    ->take(9)
    ->get();
```

### **Ventajas:**

* *Solo ejecuta una consulta con `LIMIT 9`.*
* *No se calcula el total de registros ni se genera paginación.*
* *Ideal para páginas donde solo se quiere mostrar "los 9 más recientes", como en una portada o dashboard.*

> [!TIP]
> *Usa `take(n)` cuando no necesitas paginar ni mostrar el total de páginas; usa `paginate(n)` cuando sí.*

---

## **Resumen visual**

| **Método**      | **Recursos usados** | **Ideal para...**         | **Comentarios**                               |
| --------------- | ------------------- | ------------------------- | --------------------------------------------- |
| *`paginate(n)`* | *Más alto*          | *Listados con navegación* | *Calcula total y páginas, genera enlaces*     |
| *`take(n)`*     | *Bajo*              | *Dashboards, previews*    | *Solo limita la cantidad mostrada, sin links* |
