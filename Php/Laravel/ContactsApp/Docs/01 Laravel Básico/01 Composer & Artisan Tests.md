<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Composer y Artisan en Laravel**

## **¿Qué es Composer?**

*Composer es un **gestor de dependencias para PHP**. Laravel lo usa para instalar y actualizar paquetes necesarios para el framework y el desarrollo.*

### **Comandos básicos de Composer**

- **Instalar Dependencias** *Del Proyecto (Ejecutar En La Raíz Del Proyecto):*

   ```bash
   composer install
   ```

- **Actualizar Todas Las Dependencias:**

   ```bash
   composer update
   ```

- **Añadir Un Paquete Nuevo:**

   ```bash
   composer require name/package
   ```

- **Eliminar Un Paquete:**

   ```bash
   composer remove name/package
   ```

---

## **¿Qué es Artisan?**

*Artisan es la **línea de comandos de Laravel**, que permite ejecutar tareas como **migraciones**, tests, generación de controladores, etc.*

### **Comandos básicos de Artisan**

- **Ver Todos Los Comandos Disponibles:**

   ```bash
   php artisan list
   ```

- **Crear Una Clave De Aplicación (Necesaria Después De Instalar Laravel):**

   ```bash
   php artisan key:generate
   ```

- **Ver Rutas Registradas En Laravel:**

   ```bash
   php artisan route:list
   ```

   **Salida**

   ```bash
   GET|HEAD  / ..........................................................................................................
   POST      _ignition/execute-solution ... ignition.executeSolution › Spatie\LaravelIgnition › ExecuteSolutionController
   GET|HEAD  _ignition/health-check ............... ignition.healthCheck › Spatie\LaravelIgnition › HealthCheckController
   POST      _ignition/update-config ............ ignition.updateConfig › Spatie\LaravelIgnition › UpdateConfigController
   GET|HEAD  api/user ...................................................................................................
   GET|HEAD  ejercicio1 .................................................................................................
   POST      ejercicio1 .................................................................................................
   PUT       ejercicio1 .................................................................................................
   PATCH     ejercicio1 .................................................................................................
   DELETE    ejercicio1 .................................................................................................
   GET|HEAD  sanctum/csrf-cookie ............................................ Laravel\Sanctum › CsrfCookieController@show

   ```

- **Limpiar Caché De Configuración:**

   ```bash
   php artisan config:clear
   ```

   ```bash
   INFO  Configuration cache cleared successfully.
   ```

- **Ejecutar Migraciones De Base De Datos:**

   ```bash
   php artisan migrate
   ```

---

### **Tests Automatizados en Laravel**

*Laravel usa PHPUnit para escribir y ejecutar **tests automatizados**.*

## **Tipos de Tests en Laravel**

- **Tests Unitarios:**
  - *Verifican **funciones o métodos individuales**.*
  - *Se guardan en `tests/Unit/`.*

- **Tests De Características (Feature Tests):**
  - *Prueban **partes completas del sistema** como controladores y rutas.*
  - *Se guardan en `tests/Feature/`.*

---

## **Configuración Inicial**

1. *Copiar el archivo de configuración de entorno:*

   ```bash
   cp .env.example .env
   ```

2. *Generar una clave de aplicación:*

   ```bash
   php artisan key:generate
   ```

---

### **Ejecutar Tests En Laravel**

#### **Ejecutar Todos Los Tests**

   ```bash
   php artisan test
   ```

   **Salida esperada:**

   ```bash
       PASS  Tests\Feature\Ejercicio1Test
   ✓ ejercicio1 get ok
   ✓ ejercicio1 post ok
   ✓ ejercicio1 put ok
   ✓ ejercicio1 patch ok
   ✓ ejercicio1 delete ok
   
   Tests:  5 passed
   Time:   0.18s
   ```

#### **Ejecutar Un Test Específico Por Nombre De Clase**

   ```bash
   php artisan test --filter Ejercicio1Test
   ```

- **Salida Esperada:**  

    ```bash
        PASS  Tests\Feature\Ejercicio1Test
    ✓ ejercicio1 get ok
    ✓ ejercicio1 post ok
    ✓ ejercicio1 put ok
    ✓ ejercicio1 patch ok
    ✓ ejercicio1 delete ok

    Tests:  5 passed
    Time:   0.18s
    ```

#### **Ejecutar Un Test Específico Por Nombre De Método**

   ```bash
   php artisan test --filter test_ejercicio1_get_ok
   ```

- **Salida Esperada:**  

    ```bash
      PASS  Tests\Feature\Ejercicio1Test
    ✓ ejercicio1 get ok

    Tests:  1 passed
    Time:   0.15s
    ```

---

### **Subir Cambios A Github**

#### **Subir una rama específica**

   ```bash
   git push -u origin Exercises
   ```

#### *Subir **Todas Las Ramas***

   ```bash
   git push --all origin
   ```
