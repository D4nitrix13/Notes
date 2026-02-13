<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Componentes Blade**

*[Components](https://laravel.com/docs/12.x/blade#components "https://laravel.com/docs/12.x/blade#components")*
*[Passing Data To Components](https://laravel.com/docs/12.x/blade#passing-data-to-components "https://laravel.com/docs/12.x/blade#passing-data-to-components")*
*[Heroicons/](https://heroicons.com/ "https://heroicons.com/")*

## **1. ¿Qué son los componentes en Blade?**

> [!NOTE]
> *Los **componentes Blade** son fragmentos reutilizables de código que encapsulan HTML + lógica. Son ideales para botones, íconos, tarjetas, modales, etc.*

*Se usan como etiquetas personalizadas (`<x-nombre-componente />`).*

**Laravel separa los componentes en:**

* **Clase PHP** *(`app/View/Components/Nombre.php`)*
* **Vista Blade** *(`resources/views/components/nombre.blade.php`)*

---

### **2. Comando para crear un componente**

```bash
php artisan make:component Alert -v
```

```bash
php artisan make:component Alert -v

   INFO  Component [app/View/Components/Alert.php] created successfully.
```

**Explicación:**

* **`php artisan`:** *ejecuta comandos de consola propios de Laravel.*
* **`make:component`:** *genera un nuevo componente Blade.*
* **`Alert`:** *es el **nombre del componente**.*
* **`-v` o `--verbose`:** *muestra detalles adicionales al ejecutar el comando (útil para ver qué archivos se crearon o si hubo errores).*

**Este comando crea:**

* *`app/View/Components/Alert.php` → clase del componente.*
* *`resources/views/components/alert.blade.php` → vista asociada.*

---

### **Ejemplo práctico: componente `Alert`**

```php
<x-alert type="error" :message="$message" />
```

*Aquí se utiliza el componente `<x-alert>` con dos parámetros:*

* *`type="error"` → pasa el valor `"error"` como **texto plano**.*
* *`:message="$message"` → el símbolo `:` indica que el valor es **código PHP**, no texto plano.*

#### *Clase asociada (`app/View/Components/Alert.php`)*

```php
<?php

namespace App\View\Components;

use Illuminate\View\Component;

class Alert extends Component
{
    /**
     * Create a new component instance.
     *
     * @return void
     */
    public function __construct(public string $message, public string $type)
    {
        $this->message = $message;
        $this->type = $type;
    }

    /**
     * Get the view / contents that represent the component.
     *
     * @return \Illuminate\Contracts\View\View|\Closure|string
     */
    public function render()
    {
        return view('components.alert');
    }
}
```

#### *Vista asociada (`resources/views/components/alert.blade.php`)*

```php
<div class="alert alert-{{ $type }}">
    {{ $message }}
</div>
```

* **Resultado Final**

```php
@if ($alert = session()->get('alert'))
    <x-alert :type="$alert['type']" :message="$alert['message']" />
@endif
```

**¿Qué hace?**

```php
@if ($alert = session()->get('alert'))
```

*Evalúa si existe una variable de sesión llamada alert, y si existe, la guarda en la variable local `$alert`.*

* *`session()` → función global de Laravel que accede a los datos almacenados en la sesión del usuario.*
* *`get('alert')` → obtiene el valor asociado con la clave `'alert'`.*

*Importante: esta asignación (`$alert = session()->get(...)`) no solo verifica si existe, también asigna el valor a la variable $alert si la sesión lo contiene.*

```php
<x-alert :type="$alert['type']" :message="$alert['message']" />
```

**Esto muestra el componente Blade personalizado alert, pasando dos propiedades:**

* **`:type="$alert['type']"`** *→ el tipo de alerta (por ejemplo, success, error, etc.).*
* **`:message="$alert['message']"`** *→ el mensaje que se mostrará al usuario.*

* **Notación**

*El prefijo : significa que estás pasando una variable PHP y no una cadena de texto estática.*
*Sin :, Laravel interpretaría type="success" literalmente como texto.*

---

### **4. Componente `Icon`**

```bash
php artisan make:component Icon -v
```

**Esto genera:**

* *`app/View/Components/Icon.php`*
* *`resources/views/components/icon.blade.php`*

**Usos:**

```php
<x-icon icon="pencil" />
```

#### **Clase del componente**

```php
<?php

namespace App\View\Components;

use Illuminate\View\Component;

class Icon extends Component
{
    /**
     * Create a new component instance.
     *
     * @return void
     */
    public function __construct(public string $icon)
    {
        $this->icon = $icon;
    }

    /**
     * Get the view / contents that represent the component.
     *
     * @return \Illuminate\Contracts\View\View|\Closure|string
     */
    public function render()
    {
        return view('components.icon');
    }
}
```

---

### **5. Uso dentro de botones**

#### **Botón de editar**

```php
<a class="btn btn-secondary mb-0 me-2 p-1 px-2" href="{{ route('contacts.edit', $contact->id) }}">
    <x-icon icon="pencil" />
</a>
```

* *`btn btn-secondary ...` → clases de estilo (Bootstrap).*
* *`{{ route('contacts.edit', $contact->id) }}` → genera la URL para editar un contacto según su ID.*
* *`<x-icon icon="pencil" />` → inserta un ícono de lápiz usando el componente.*

#### **Botón de eliminar**

```php
<form action="{{ route('contacts.destroy', ['contact' => $contact->id]) }}" method="POST">
    @csrf
    @method('DELETE')
    <button type="submit" class="btn btn-danger mb-0 me-2 p-1 px-2">
        <x-icon icon="trash" />
    </button>
</form>
```

* *`@csrf` → agrega un token de seguridad contra ataques CSRF.*
* *`@method('DELETE')` → Laravel usa esta directiva para emular métodos HTTP como `DELETE`, ya que los formularios HTML solo aceptan `GET` y `POST`.*
* *`route('contacts.destroy', [...])` → genera la URL para borrar el contacto con su ID.*
* *`<x-icon icon="trash" />` → muestra el ícono de eliminar (basado en la clase del componente `Icon`).*

---

### **Conclusión y resumen**

| **Elemento**                   | **Función**                                                       |
| ------------------------------ | ----------------------------------------------------------------- |
| *`php artisan make:component`* | *Crea un componente con clase y vista*                            |
| *`:variable`*                  | *Pasa un valor de PHP a la vista del componente*                  |
| *`<x-alert>` / `<x-icon>`*     | *Usos prácticos de componentes Blade reutilizables*               |
| *`@csrf`*                      | *Protege el formulario contra ataques CSRF*                       |
| *`@method('DELETE')`*          | *Emula métodos HTTP no permitidos en formularios HTML*            |
| *`route()`*                    | *Genera rutas basadas en el nombre de ruta definido en `web.php`* |
