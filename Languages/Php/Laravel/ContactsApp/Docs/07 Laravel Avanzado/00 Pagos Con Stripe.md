<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Pagos Con Stripe**

---

## **Objetivo del Proyecto**

> [!NOTE]
> *Crear una aplicación Laravel con un sistema de **suscripción con Stripe**, que ofrezca un **período de prueba gratuito de 10 días** antes de comenzar a cobrar.*

---

## **Paso 1: Crear Cuenta en Stripe (Modo de Pruebas)**

- *Ir a [Stripe Dashboard](https://dashboard.stripe.com/test/dashboard "https://dashboard.stripe.com/test/dashboard") y crear una cuenta de pruebas. Esta cuenta te permite probar integraciones de pago sin usar dinero real.*

- **Referencia visual:**

- *![`Crear Cuentas`](/Languages/Php/Laravel/ContactsApp/Docs/Images/CrearCuentas.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/CrearCuentas.png")*
- *![`Creacion De Cuenta Para App`](/Languages/Php/Laravel/ContactsApp/Docs/Images/CreacionDeCuentaParaApp.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/CreacionDeCuentaParaApp.png")*

---

## **Paso 2: Crear Producto en Stripe**

1. *Ve a: [https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/products?active=true](https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/products?active=true "https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/products?active=true")*
2. *Haz clic en **"Add product"** (Agregar producto).*
3. *Completa los campos:*

---

### 🧾 Configuración del Producto en Stripe

Para crear el producto asociado a la suscripción de la aplicación, completa los siguientes campos:

- **Nombre:**
  `Contacts App Subscription`

- **Descripción:**
  `Suscripción mensual que habilita el acceso completo a la aplicación Contacts. Incluye autenticación mediante API, gestión de credenciales y administración del estado de la suscripción del usuario.`

- **Imagen (opcional):**
  Puedes cargar una imagen representativa del producto (logo o icono de la aplicación).
  Formatos permitidos: **JPEG, PNG o WEBP** (máx. 2 MB).

---

## 💳 Configuración de la Tarifa

- **Tipo de tarifa:** Recurrente
- **Importe:** `US$ 10.00`
- **Periodo de facturación:** Mensual

Esta configuración generará un cargo automático mensual de **US$ 10.00**, facturado al inicio de cada período.

- **Referencia visual:** *![`Agregar Producto`](/Languages/Php/Laravel/ContactsApp/Docs/Images/AgregarProducto.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/AgregarProducto.png")*

- *Al crear el producto, Stripe te redirigirá a una página con los **precios** (Prices). No copies ni compartas la URL como:*

```bash
https://dashboard.stripe.com/test/prices/price_1RcG5jQNkVo21RxIbiHF2gfG
```

**Esa URL contiene información interna.**

---

## **Paso 3: Obtener las claves de la API (API Keys)**

**Ve a la sección de Desarrolladores → Claves API:**
*[https://dashboard.stripe.com/test/apikeys](https://dashboard.stripe.com/test/apikeys "https://dashboard.stripe.com/test/apikeys")*

**Obtendrás dos claves:**

| **Tipo**     | **Clave de ejemplo** | **Uso**                              |
| ------------ | -------------------- | ------------------------------------ |
| *Public Key* | *`pk_test_...`*      | *Se usa en el frontend o scripts JS* |
| *Secret Key* | *`sk_test_...`*      | *Se usa en el backend (Laravel)*     |

*Agrega estas claves en el archivo `.env` de Laravel:*

```ini
STRIPE_KEY=pk_test_51RcGuYQ2TRPhIB8unhXTEGPd9z3bsDBkyjYZSuLF2jOxzcZLZzYSGCzPdRf9zbF2DJDSoiidKxtiIni8Pz6nG7Je003PZAX06g
STRIPE_SECRET=sk_test_51RcGuYQ2TRPhIB8uF0C3qJV2KqsY2ONqBXO5xwMlMgkSewRTbokXfL5n0wf6f5yqzLl0r3v5vtqaTgLpohN5JFLv00gQqKepr5
```

**Documentación oficial:**

- *[Laravel Billing](https://laravel.com/docs/12.x/billing "https://laravel.com/docs/12.x/billing")*
- *[Claves API en Laravel Cashier](https://laravel.com/docs/12.x/billing#api-keys "https://laravel.com/docs/12.x/billing#api-keys")*

---

## **Paso 4: Instalar Laravel Cashier**

**Cashier es el paquete oficial de Laravel para manejar suscripciones con Stripe fácilmente.**

### **1. Ejecuta el siguiente comando en tu contenedor o terminal**

```bash
composer require laravel/cashier
```

**Este comando hace lo siguiente:**

- *Instala la dependencia `laravel/cashier` desde Packagist.*
- *Actualiza `composer.lock` y `vendor/`.*

---

## **Paso 5: Publicar Migraciones**

**Laravel Cashier necesita migraciones propias para manejar clientes y suscripciones.**

### **Ejecuta**

```bash
php artisan vendor:publish --tag="cashier-migrations"
```

**Este comando:**

- *Copia las migraciones predeterminadas del paquete hacia `database/migrations`.*

**Luego:**

```bash
php artisan migrate
```

**Esto crea 3 tablas nuevas:**

```bash
   INFO  Running migrations.  

  2019_05_03_000001_create_customer_columns ............................ DONE
  2019_05_03_000002_create_subscriptions_table ......................... DONE
  2019_05_03_000003_create_subscription_items_table .................... DONE
```

---

## **Paso 6: Hacer el modelo User "Facturable"**

**Debes permitir que el modelo `User` pueda tener suscripciones.**

**En `app/Models/User.php`:**

```php
use Laravel\Cashier\Billable;

class User extends Authenticatable
{
    use Billable;
}
```

**`Billable` es un trait que agrega métodos como:**

- *`$user->newSubscription()`*
- *`$user->subscribed()`*
- *`$user->subscription('default')->cancel()`*

---

## **Paso 7: Configurar la moneda**

*Por defecto, Laravel Cashier usa **USD**, pero puedes cambiarla en `.env`:*

```ini
CASHIER_CURRENCY=eur
```

*Valores posibles:*

- *`usd` – dólares estadounidenses*
- *`eur` – euros*
- *`gbp` – libras esterlinas*
- **etc.**

---

## **Resumen de Variables Clave en .env**

| **Variable**         | **Uso**                                              |
| -------------------- | ---------------------------------------------------- |
| *`STRIPE_KEY`*       | *Clave pública de Stripe (frontend, tokens)*         |
| *`STRIPE_SECRET`*    | *Clave secreta de Stripe (backend, Laravel Cashier)* |
| *`CASHIER_CURRENCY`* | *Moneda por defecto para todas las suscripciones*    |

---

## **Portal de Facturación con Stripe en Laravel**

---

## **Objetivo**

> [!NOTE]
> *Permitir que los usuarios gestionen su suscripción a través del **Stripe Billing Portal**, una interfaz automática proporcionada por Stripe para actualizar el método de pago, cancelar la suscripción, ver facturas, entre otros.*

---

## **Paso 1: Definir Ruta al Billing Portal**

> [!TIP]
> *Usamos el método `redirectToBillingPortal()` que proporciona Cashier a través del trait `Billable`.*

### **Agrega esta ruta en `routes/web.php`:**

```php
use Illuminate\Http\Request;

Route::get('/billing-portal', function (Request $request) {
    return $request->user()->redirectToBillingPortal();
});
```

- **Explicación:**

- *`$request->user()`* *accede al usuario autenticado.*
- *`redirectToBillingPortal()`* *crea y redirige automáticamente al portal de facturación de Stripe para ese usuario.*
- *Requiere que el usuario tenga una suscripción activa.*

- **Imagen de referencia:**

- *![`Producto Precio ID`](/Languages/Php/Laravel/ContactsApp/Docs/Images/ProductoPrecioID.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/ProductoPrecioID.png")*

---

## **Paso 2: Obtener ID del Precio de Stripe**

> [!TIP]
> *Cada producto en Stripe tiene uno o más precios. Copia el ID del precio desde tu dashboard de Stripe.*

- **URL del ejemplo:**
*[https://dashboard.stripe.com/test/prices/price\_1RcG5jQNkVo21RxIbiHF2gfG](https://dashboard.stripe.com/test/prices/price_1RcG5jQNkVo21RxIbiHF2gfG "https://dashboard.stripe.com/test/prices/price_1RcG5jQNkVo21RxIbiHF2gfG")*

- **Este ID es el que usaremos para crear suscripciones.**

---

## **Paso 3: Guardar ID del Precio en `.env`**

```ini
STRIPE_PRICE_ID=price_1RcGzCQ2TRPhIB8uTQRUbKmZ
```

- *Este valor se usará desde Laravel para referenciar el precio activo del producto en Stripe.*

---

## **Paso 4: Crear Archivo de Configuración `config/stripe.php`**

> [!TIP]
> *Este archivo permite acceder al `price_id` desde cualquier parte de la app usando `config()`.*

### **Ejecuta en terminal:**

```bash
touch config/stripe.php
```

### **Contenido del archivo `config/stripe.php`:**

```php
<?php

return [
    "price_id" => env("STRIPE_PRICE_ID"),
];

?>
```

- **Explicación:**

- *`env("STRIPE_PRICE_ID")`* *carga el valor desde el archivo `.env`.*
- *El archivo retorna un array asociativo accesible con `config("stripe.price_id")`.*

---

## **Paso 5: Crear Ruta para Iniciar Checkout de Suscripción**

*Laravel Cashier proporciona el método `checkout()` para redirigir al formulario seguro de Stripe.*

### **Opción 1 (Hardcodeado):**

```php
Route::get('/subscription-checkout', function (Request $request) {
    return $request->user()
        ->newSubscription('default', 'price_monthly')
        ->checkout();
});
```

- *Este método no es flexible si cambias el ID en Stripe.*

---

### **Opción 2 (Usando archivo de configuración): Recomendado**

```php
Route::get('/subscription-checkout', function (Request $request) {
    return $request->user()
        ->newSubscription('default', config("stripe.price_id"))
        ->checkout();
});
```

- **Ventajas:**

- *Centraliza el ID del precio en un solo archivo.*
- *Facilita mantenimiento y cambios.*

---

## **Paso 6: Realizar Prueba de Checkout**

- **Abre en el navegador:**

```bash
http://172.17.0.2:8000/subscription-checkout
```

- **Imagen de referencia:**
*![`Subscription Checkout`](/Languages/Php/Laravel/ContactsApp/Docs/Images/SubscriptionCheckout.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/SubscriptionCheckout.png")*

> *Serás redirigido al **Stripe Checkout** con el producto seleccionado.*

---

## **Paso 7: Confirmación de Éxito**

- **Luego de pagar o simular el pago, Stripe redirige a:**

```bash
http://172.17.0.2:8000/home?checkout=success
```

- *Esto indica que el proceso de suscripción fue exitoso.*

---

## **Paso 8: Error común y cómo solucionarlo**

**Si ves este mensaje de error:**

```bash
No configuration provided and your test mode default configuration has not been created. Provide a configuration or create your default by saving your customer portal settings in test mode at https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/settings/billing/portal.
```

- **Significa que no has activado el portal de clientes (Customer Portal) en modo de prueba.**

---

## **Paso 9: Activar Portal de Clientes en Stripe (Modo Test)**

1. *Ve a:*
   *[https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/settings/billing/portal](https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/settings/billing/portal "https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/settings/billing/portal")*

2. *Haz clic en:*
   - **"Activar el enlace de prueba"**

- **Ubicación exacta:**

- *Parte superior de la sección “Lanzar portal de clientes con un enlace”*
- *Botón: `"Activar el enlace de prueba"`*

- **Imagen de referencia:**
*![`Billing Portal`](/Languages/Php/Laravel/ContactsApp/Docs/Images/BillingPortal.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/BillingPortal.png")*

---

## **Configuración de Webhooks con Stripe CLI en Laravel**

---

- **Objetivo**

> [!NOTE]
> *Permitir que Laravel reciba automáticamente los eventos de Stripe (como creación de suscripción, pagos, cancelaciones) y pueda almacenarlos en nuestra base de datos. Esto se logra usando los llamados **Webhooks**.*

---

## **¿Por qué usar Webhooks?**

- *Cuando un usuario paga, Stripe genera un **evento** en sus servidores.*
- *Ese evento debe ser **notificado a Laravel**, que es nuestro backend.*
- *Laravel lo procesa a través de una ruta `POST` especial y puede almacenar los datos en la base de datos.*

- **Referencia visual:**

- *![`Web Hooks`](/Languages/Php/Laravel/ContactsApp/Docs/Images/WebHooks.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/WebHooks.png")*

---

## **Paso 1: Ir a Webhooks en el Dashboard de Stripe**

- **Visita:**
*[https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/workbench/webhooks](https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/workbench/webhooks "https://dashboard.stripe.com/acct_1RcGuNLBPnpoQHwS/test/workbench/webhooks")*

- *Ahí puedes ver todos los Webhooks configurados.*
- *Pero en desarrollo local usaremos Stripe CLI para probarlo.*

- **Referencia visual:**

- *![`Configuration Oyente Local`](/Languages/Php/Laravel/ContactsApp/Docs/Images/ConfigurationOyenteLocal.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/ConfigurationOyenteLocal.png")*

---

## **Paso 2: Instalar Stripe CLI**

> [!TIP]
> *Stripe CLI es una herramienta de línea de comandos para interactuar con Stripe, probar Webhooks y manejar eventos.*

**Instrucciones oficiales:**

- *[Stripe CLI - Instalación](https://docs.stripe.com/stripe-cli#install "https://docs.stripe.com/stripe-cli#install")*
- *[Método para Linux / Arch Linux](https://docs.stripe.com/stripe-cli?install-method=linux "https://docs.stripe.com/stripe-cli?install-method=linux")*

---

### **Pasos para Arch Linux:**

1. *Descarga el archivo `.tar.gz` desde GitHub:*

    ```bash
    curl 'https://github.com/stripe/stripe-cli/releases/download/v1.27.0/stripe_1.27.0_linux_x86_64.tar.gz' \
    -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64)' \
    -H 'Accept: text/html' \
    -sSLO
    ```

2. *Extrae el archivo:*

    ```bash
    tar -xvf stripe_1.27.0_linux_x86_64.tar.gz
    ```

3. *Mueve el ejecutable `stripe` al PATH global (por ejemplo, `/usr/local/bin`):*

```bash
sudo mv stripe /usr/local/bin/
```

---

## **Paso 3: Login en Stripe CLI**

> [!WARNING]
> *Debes autenticarte con tu clave secreta (`sk_test...`) para conectar tu CLI con tu cuenta de Stripe (modo prueba).*

### **Comando:**

```bash
stripe login --api-key sk_test_51RcGuYQ2TRPhIB8uF0C3qJV2KqsY2ONqBXO5xwMlMgkSewRTbokXfL5n0wf6f5yqzLl0r3v5vtqaTgLpohN5JFLv00gQqKepr5
```

- *Como estamos en modo prueba, puedes mostrar esta clave en tus apuntes.*

**Salida esperada:**

```bash
Your pairing code is: avid-finely-lavish-fave
This pairing code verifies your authentication with Stripe.
Press Enter to open the browser or visit https://dashboard.stripe.com/stripecli/confirm_auth?t=o0dTZLAQHWBYFoA9He8tabR3TdUxaDY5 (^C to quit)
> Done! The Stripe CLI is configured for Contacts App Account sandbox with account id acct_1RcGuYQ2TRPhIB8u

Please note: this key will expire after 90 days, at which point you'll need to re-authenticate.
```

- **Referencia visual:**
*![`Confirm Auth`](/Languages/Php/Laravel/ContactsApp/Docs/Images/ConfirmAuth.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/ConfirmAuth.png")*

| **Parte**                                                                                            | **Explicación completa**                                                                                                                                                                                                 |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| *`Your pairing code is: avid-finely-lavish-fave`*                                                    | *Es un **código único de emparejamiento** que identifica la sesión entre tu Stripe CLI y tu cuenta en Stripe.*                                                                                                           |
| *`This pairing code verifies your authentication with Stripe.`*                                      | *Indica que ese código será usado para verificar que tú autorizas esta conexión entre tu CLI y la cuenta Stripe.*                                                                                                        |
| *`Press Enter to open the browser or visit https://dashboard.stripe.com/stripecli/confirm_auth?...`* | *Te da dos opciones para confirmar manualmente: 1. Presionar `Enter` para abrir tu navegador por defecto con ese enlace. 2. Copiar y pegar el enlace manualmente si usas entorno sin navegador (como servidores o WSL).* |
| *`^C to quit`*                                                                                       | *Si no deseas continuar, puedes cancelar la operación con `Ctrl + C`.*                                                                                                                                                   |
| *`> Done! The Stripe CLI is configured for Contacts App Account sandbox with account id acct_...`*   | *Indica que la autenticación fue exitosa. Tu Stripe CLI ahora está **asociado a tu cuenta Stripe (modo prueba)** con el ID que se muestra.*                                                                              |
| *`Please note: this key will expire after 90 days...`*                                               | *Stripe CLI recuerda tu sesión por **90 días**. Luego deberás volver a ejecutar `stripe login`.*                                                                                                                         |

> [!IMPORTANT]
> *Stripe solicita autenticación mediante el navegador para garantizar que tú estás autorizando el uso de la CLI desde ese equipo. Aunque pongas tu sk_test_..., también se requiere verificación manual para evitar accesos no autorizados.*

- *Una vez autenticado, no necesitas volver a ingresar el --api-key para otros comandos como stripe listen, ya que la CLI guarda esa sesión en el sistema local (por ejemplo: ~/.config/stripe).*

---

## **Paso 4: Redirigir Webhooks a Laravel (Stripe → Localhost)**

> [!TIP]
> *Stripe CLI creará un túnel que redirige los eventos al servidor local de Laravel.*

### **Comando estándar:**

```bash
stripe listen --forward-to localhost:4242/webhook
```

- *Este comando escucha los eventos desde Stripe y los reenvía a tu servidor.*

---

## **Paso 5: Verificar la Ruta del Webhook en Laravel**

> [!TIP]
> *Laravel Cashier ya incluye una ruta predeterminada para manejar webhooks.*

### **Comando para buscarla:**

```bash
php artisan route:list | grep -iE webhook
```

- **Salida esperada:**

```bash
POST  stripe/webhook  ..........  cashier.webhook › Laravel\Cashier\WebhookController@handleWebhook
```

---

## **Paso 6: Reenviar Webhooks a tu contenedor Laravel**

> [!WARNING]
> *Asegúrate de que el puerto y host coincidan con el que estás usando (Docker, etc).*

### **Ejemplo real si tu contenedor Laravel usa IP `172.17.0.2` y puerto `8000`:**

```bash
./stripe listen --forward-to 172.17.0.2:8000/stripe/webhook
```

- **Salida esperada:**

```bash
> Ready! You are using Stripe API Version [2025-05-28.basil]. Your webhook signing secret is whsec_7cc038d80ea83a0f93b24bc9ba163b1b15eb14a098ec2559d0fd600f7451cf8a (^C to quit)
```

- *Este `whsec_...` es el **Webhook Secret** que puedes copiar a `.env` si deseas validar la autenticidad de la petición.*

---

## **Resultado**

> [!NOTE]
> *Ahora Laravel recibe eventos reales de Stripe cada vez que se crea, actualiza o cancela una suscripción o pago. Puedes acceder al contenido del evento dentro del método `handleWebhook()` en Laravel Cashier o sobrescribirlo si deseas un comportamiento personalizado.*

---

## **Resultado Final**

> [!NOTE]
> *Una vez configurado todo correctamente, los usuarios podrán suscribirse, luego acceder al Billing Portal para:*

- *Cancelar su suscripción*
- *Cambiar tarjeta de pago*
- *Ver facturas*
- *Actualizar su información*

---

## **Cancelación y Reanudación de una Suscripción con Stripe y Laravel**

---

## **Paso 1: Cancelar una Suscripción**

- *Stripe muestra una interfaz para que el usuario cancele su suscripción directamente desde el Billing Portal.*

- *Imagen antes de cancelar:*
  *![`Cancel Subscription`](/Languages/Php/Laravel/ContactsApp/Docs/Images/CancelSubscription.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/CancelSubscription.png")*

- *Imagen después de cancelar:*
  *![`Subscription Has Been Canceled`](/Languages/Php/Laravel/ContactsApp/Docs/Images/SubscriptionHasBeenCanceled.png "/Languages/Php/Laravel/ContactsApp/Docs/Images/SubscriptionHasBeenCanceled.png")*

---

### **Log del Servidor al Cancelar:**

```bash
2025-06-22 23:35:20   --> billing_portal.session.created [evt_1RcxPvQ2TRPhIB8urjBZPNhz]
2025-06-22 23:35:20  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxPvQ2TRPhIB8urjBZPNhz]
```

- **Explicación:**

| **Evento**                         | **Descripción**                                                                |
| ---------------------------------- | ------------------------------------------------------------------------------ |
| *`billing_portal.session.created`* | *Se generó una sesión del portal de facturación (Billing Portal).*             |
| *`POST ... /stripe/webhook`*       | *Stripe notificó a tu servidor local Laravel mediante el Webhook configurado.* |

---

## **Paso 2: Volver a Suscribirse**

> [!TIP]
> *Al volver a realizar la suscripción usando `/subscription-checkout`, Stripe desencadena una serie de eventos automáticos.*

- **URL de re-suscripción:**

```bash
http://172.17.0.2:8000/subscription-checkout
```

---

### **Eventos Recibidos por Webhook al Volver a Suscribirse:**

```bash
2025-06-22 23:40:22   --> charge.succeeded [evt_3RcxUmQ2TRPhIB8u0mhsWz8d]
2025-06-22 23:40:22   --> checkout.session.completed [evt_1RcxUoQ2TRPhIB8uW39tapEL]
2025-06-22 23:40:22  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_3RcxUmQ2TRPhIB8u0mhsWz8d]
2025-06-22 23:40:22   --> payment_method.attached [evt_1RcxUoQ2TRPhIB8u216UTzIW]
2025-06-22 23:40:22  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxUoQ2TRPhIB8uW39tapEL]
2025-06-22 23:40:22  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxUoQ2TRPhIB8u216UTzIW]
2025-06-22 23:40:22   --> customer.subscription.created [evt_1RcxUoQ2TRPhIB8u1JE0H70h]
2025-06-22 23:40:22  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxUoQ2TRPhIB8u1JE0H70h]
2025-06-22 23:40:23   --> customer.subscription.updated [evt_1RcxUoQ2TRPhIB8uu2ZVJR1A]
2025-06-22 23:40:23   --> payment_intent.succeeded [evt_3RcxUmQ2TRPhIB8u0iL9ZbOO]
2025-06-22 23:40:23  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxUoQ2TRPhIB8uu2ZVJR1A]
2025-06-22 23:40:23  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_3RcxUmQ2TRPhIB8u0iL9ZbOO]
2025-06-22 23:40:23   --> payment_intent.created [evt_3RcxUmQ2TRPhIB8u0yic6fqf]
2025-06-22 23:40:23  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_3RcxUmQ2TRPhIB8u0yic6fqf]
2025-06-22 23:40:23   --> invoice.created [evt_1RcxUpQ2TRPhIB8uMUKdYPpH]
2025-06-22 23:40:23  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxUpQ2TRPhIB8uMUKdYPpH]
2025-06-22 23:40:23   --> invoice.finalized [evt_1RcxUpQ2TRPhIB8uG1SYhwkr]
2025-06-22 23:40:23  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxUpQ2TRPhIB8uG1SYhwkr]
2025-06-22 23:40:23   --> invoice.updated [evt_1RcxUpQ2TRPhIB8ujXIOOxv7]
2025-06-22 23:40:23  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxUpQ2TRPhIB8ujXIOOxv7]
2025-06-22 23:40:23   --> invoice.paid [evt_1RcxUpQ2TRPhIB8uA89s27qQ]
2025-06-22 23:40:23  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxUpQ2TRPhIB8uA89s27qQ]
2025-06-22 23:40:24   --> invoice.payment_succeeded [evt_1RcxUpQ2TRPhIB8uLuzkzdGo]
2025-06-22 23:40:24  <--  [200] POST http://172.17.0.2:8000/stripe/webhook [evt_1RcxUpQ2TRPhIB8uLuzkzdGo]
```

### **Explicación de los Principales Eventos:**

| **Evento**                        | **Significado**                                        |
| --------------------------------- | ------------------------------------------------------ |
| *`checkout.session.completed`*    | *El usuario completó el checkout en Stripe.*           |
| *`payment_method.attached`*       | *Se asoció una tarjeta o método de pago al cliente.*   |
| *`customer.subscription.created`* | *Se creó la nueva suscripción.*                        |
| *`invoice.created`*               | *Se generó una factura automática por la suscripción.* |
| *`invoice.paid`*                  | *La factura fue pagada exitosamente.*                  |
| *`payment_intent.succeeded`*      | *El intento de pago fue exitoso.*                      |

**Cada uno de estos eventos fue reenviado correctamente a:**

```bash
POST http://172.17.0.2:8000/stripe/webhook
```

*Y todos recibieron código de respuesta `[200]`, indicando **éxito**.*

---

## **Paso 3: Validar que los Datos Fueron Almacenados en la Base de Datos**

> [!NOTE]
> *Laravel Cashier guarda automáticamente la información relevante de la suscripción en las tablas `subscriptions` y `subscription_items`.*

### **Consulta SQL a la tabla `subscription_items`:**

```sql
SELECT * FROM subscription_items;
```

| **Campo**          | **Descripción**                                                 |
| ------------------ | --------------------------------------------------------------- |
| *`stripe_product`* | *ID del producto en Stripe (`prod_...`).*                       |
| *`stripe_price`*   | *ID del precio activo asociado a la suscripción.*               |
| *`quantity`*       | *Número de licencias o unidades del producto (generalmente 1).* |

- **Resultado**

```sql
contacts_app=# SELECT * FROM subscription_items;
 id | subscription_id |     stripe_id     |   stripe_product    |          stripe_price          | quantity |     created_at      |     updated_at      
----+-----------------+-------------------+---------------------+--------------------------------+----------+---------------------+---------------------
  1 |               1 | si_SY3bDgxP9Ywwzj | prod_SXLg5wT1yLfs26 | price_1RcGzCQ2TRPhIB8uTQRUbKmZ |        1 | 2025-06-22 23:40:22 | 2025-06-22 23:40:22
(1 row)
```

---

### **Consulta SQL a la tabla `subscriptions`:**

```sql
SELECT * FROM subscriptions;
```

| **Campo**         | **Descripción**                                         |
| ----------------- | ------------------------------------------------------- |
| *`stripe_id`*     | *ID de la suscripción en Stripe (`sub_...`).*           |
| *`stripe_status`* | *Estado actual: `active`, `canceled`, `past_due`, etc.* |
| *`stripe_price`*  | *ID del precio asociado a esta suscripción.*            |
| *`created_at`*    | *Fecha en que fue creada en la base de datos local.*    |

- **Resultado**

```sql
contacts_app=# SELECT * FROM subscriptions;
 id | user_id |  name   |          stripe_id           | stripe_status |          stripe_price          | quantity | trial_ends_at | ends_at |     created_at      |     updated_at      
----+---------+---------+------------------------------+---------------+--------------------------------+----------+---------------+---------+---------------------+---------------------
  1 |       1 | default | sub_1RcxUlQ2TRPhIB8uRa3MeGjM | active        | price_1RcGzCQ2TRPhIB8uTQRUbKmZ |        1 |               |         | 2025-06-22 23:40:22 | 2025-06-22 23:40:23
(1 row)
```

---

### **Verificar secuencias de ID (PostgreSQL):**

```sql
SELECT * FROM subscriptions_id_seq;
SELECT * FROM subscription_items_id_seq;
```

*Esto asegura que las secuencias internas (`serial` o `bigserial`) están siendo correctamente utilizadas.*

```sql
contacts_app=# SELECT * FROM subscriptions_id_seq;
 last_value | log_cnt | is_called 
------------+---------+-----------
          1 |      32 | t
(1 row)
```

```sql
contacts_app=# SELECT * FROM subscription_items_id_seq;
 last_value | log_cnt | is_called 
------------+---------+-----------
          1 |      32 | t
(1 row)
```

- **Conclusión**

> [!NOTE]
> *Al cancelar y luego volver a suscribirse:*

- *Los eventos de Stripe se activan correctamente.*
- *Laravel Cashier recibe esos eventos vía Webhooks.*
- *Los datos se almacenan automáticamente en las tablas locales (`subscriptions`, `subscription_items`).*
- *Todo queda sincronizado entre Stripe y tu base de datos.*

---

## **Agregar campo `trial_ends_at` al modelo `User` en Laravel**

- **Objetivo**

> [!NOTE]
> *Permitir que al momento de registrar un nuevo usuario, se le asigne automáticamente un **período de prueba gratuito** (free trial) de **10 días**, guardando esa fecha en la base de datos usando el campo `trial_ends_at`.*

---

## **Paso 1: Modificar el método `create()` en el controlador de registro**

- *Archivo:* `app/Http/Controllers/Auth/RegisterController.php`

```php
/**
 * Create a new user instance after a valid registration.
 *
 * @param  array  $data
 * @return \App\Models\User
 */
protected function create(array $data)
{
    return User::create([
        'name' => $data['name'],
        'email' => $data['email'],
        'password' => Hash::make($data['password']),
        "trial_ends_at" => now()->addDays(value: 10)
    ]);
}
```

---

### **Explicación detallada:**

| **Línea**                                  | **Significado**                                                                                |
| ------------------------------------------ | ---------------------------------------------------------------------------------------------- |
| *`protected function create(array $data)`* | *Función llamada automáticamente por Laravel cuando se realiza un registro exitoso.*           |
| *`User::create([...])`*                    | *Crea y guarda un nuevo usuario en la base de datos.*                                          |
| *`'name' => $data['name']`*                | *Asigna el valor del campo `name` que el usuario envió desde el formulario.*                   |
| *`'email' => $data['email']`*              | *Asigna el email.*                                                                             |
| *`'password' => Hash::make(...)`*          | *La contraseña se **encripta** usando `bcrypt` mediante el helper `Hash::make()`.*             |
| *`"trial_ends_at" => now()->addDays(10)`*  | *Agrega **10 días** a la fecha actual (`now()`), y los guarda como la fecha de fin del trial.* |

- **Nota:** *`now()` devuelve un objeto `Carbon\Carbon`, y `addDays(10)` suma 10 días exactos.*

- *Puedes usar `Carbon::now()->addDays(10)` si no tienes el helper global `now()` habilitado.*

---

## **Paso 2: Declarar `trial_ends_at` como campo asignable (`fillable`) en el modelo `User`**

- *Archivo:* `app/Models/User.php`

```php
/**
 * The attributes that are mass assignable.
 *
 * @var array<int, string>
 */
protected $fillable = [
    'name',
    'email',
    'password',
    'trial_ends_at'
];
```

---

### **¿Qué significa `fillable`?**

> [!TIP]
> *En Laravel, la propiedad `fillable` se usa para definir qué campos pueden ser asignados masivamente (mass assignment) mediante `Model::create()` o `Model::update([...])`.*

### **¿Por qué es necesario?**

- *Si no agregas `trial_ends_at` a `fillable`, Laravel **ignora** ese valor al crear el usuario.*
- *Esto protege contra ataques por asignación masiva no autorizada.*

- **Resultado Final**

> [!NOTE]
> *Cada vez que un nuevo usuario se registre, Laravel:*

- *Guardará su nombre, email y contraseña encriptada.*
- *Asignará una fecha de expiración de período de prueba (`trial_ends_at`) exactamente **10 días después del registro**.*
- *Al tener este campo disponible, puedes luego hacer verificaciones como:*

---

## **Visualizar Período de Prueba (`trial_ends_at`) para Usuarios Registrados**

- **Objetivo**

> [!NOTE]
> *Crear un sistema donde, al registrar un nuevo usuario (como Carol), se almacene la fecha de finalización del período de prueba (`trial_ends_at`) y se muestre automáticamente en la interfaz si el usuario aún se encuentra en período de prueba.*

---

## **Paso 1: Crear un Usuario de Prueba en la App (ej: Carol)**

- *Al registrarse, Laravel ejecuta el método `create()` que ya estableciste con `trial_ends_at = now()->addDays(10)`.*

### **Consulta en la base de datos PostgreSQL**

```sql
SELECT * FROM users WHERE name = 'Carol';
```

- **Resultado**

```sql
 id | name  |      email      | email_verified_at | password                                           | created_at          | updated_at          | trial_ends_at        
----+-------+-----------------+-------------------+---------------------------------------------------+---------------------+---------------------+-----------------------
  2 | Carol | carol@gmail.com |                   | $2y$10$3QB...xQIai                                | 2025-06-23 00:00:30 | 2025-06-23 00:00:30 | 2025-07-03 00:00:30
```

### **Explicación de campos**

| **Campo**             | **Descripción**                                                              |
| --------------------- | ---------------------------------------------------------------------------- |
| *`id`*                | *Identificador único del usuario.*                                           |
| *`email_verified_at`* | *Vacío si el usuario no ha verificado su correo.*                            |
| *`password`*          | *Contraseña encriptada con bcrypt (`Hash::make()`).*                         |
| *`trial_ends_at`*     | *Fecha en que finaliza el período de prueba (10 días después del registro).* |

---

## **Paso 2: Mostrar mensaje si el usuario está en período de prueba**

- *En cualquier vista Blade (por ejemplo `home.blade.php`, `dashboard.blade.php`, etc.):*

```php
@if (auth()->user()->onTrial())
    <x-alert type="info" message="Trial ends in 5 days" />
@endif
```

- **Explicación**

| **Código**          | **Función**                                                                                |
| ------------------- | ------------------------------------------------------------------------------------------ |
| *`auth()->user()`*  | *Obtiene el usuario autenticado.*                                                          |
| *`onTrial()`*       | *Método de Laravel Cashier que devuelve `true` si `trial_ends_at` es posterior a `now()`.* |
| *`<x-alert ... />`* | *Componente Blade personalizado que muestra un mensaje visual en la interfaz.*             |

---

## **Paso 3: Activar casting automático de fechas en el modelo `User`**

- *Archivo:* `app/Models/User.php`

```php
protected $casts = [
    'email_verified_at' => 'datetime',
    'trial_ends_at' => 'datetime',
];
```

- **Explicación**

| **Campo**             | **Tipo de cast** | **Descripción**                                                          |
| --------------------- | ---------------- | ------------------------------------------------------------------------ |
| *`email_verified_at`* | *datetime*       | *Laravel lo convertirá automáticamente en objeto `Carbon`.*              |
| *`trial_ends_at`*     | *datetime*       | *Permite usar métodos como `diffInDays()`, `isPast()`, `format()`, etc.* |

- *Gracias a esto puedes hacer cosas como:*

```php
auth()->user()->trial_ends_at->diffInDays(now());
```

---

## **Paso 4: Mostrar los días restantes de forma dinámica**

- *En Blade:*

```php
@if (auth()->user()->onTrial())
    @php
        $remainingTrialDays = now()->diffInDays(auth()->user()->trial_ends_at);
    @endphp
    <x-alert type="info" message="Trial ends in {{ $remainingTrialDays }} days" />
@endif
```

### **Explicación línea a línea**

| **Código**                          | **Explicación**                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------ |
| *`@if (auth()->user()->onTrial())`* | *Evalúa si el usuario aún está en período de prueba.*                          |
| *`now()->diffInDays(...)`*          | *Calcula la diferencia en días entre la fecha actual y la de `trial_ends_at`.* |
| *`<x-alert ... />`*                 | *Componente para mostrar un mensaje visual con el número de días restantes.*   |

- **Resultado Final**

> [!NOTE]
> *Al iniciar sesión como Carol (u otro usuario), Laravel automáticamente:*

- *Verifica si su período de prueba está activo.*
- *Muestra el mensaje “Trial ends in **X days**”.*
- *Calcula los días restantes dinámicamente sin necesidad de guardarlos por separado.*

---

## **Manejo del Período de Prueba con Control de Sesión y Subscripciones**

- **Objetivo**

> [!NOTE]
> *Mostrar dinámicamente el mensaje "Trial ends in X days" sólo si el usuario está autenticado, está en período de prueba y **aún no tiene una suscripción activa**.*

---

## **Paso 1: Verificar el campo `trial_ends_at`**

### **Consulta SQL**

```sql
SELECT trial_ends_at FROM users WHERE name='Carol';
```

- **Resultado esperado:**

```sql
 trial_ends_at     
---------------------
 2025-07-03 00:00:30
(1 row)
```

---

## **Paso 2: Comprobación del mensaje en `/home`**

**Al hacer la petición:**

```bash
http://172.17.0.2:8000/home
```

- **Muestra:**

```bash
Trial ends in 9 days
```

---

## **Paso 3: Modificación temporal del valor `trial_ends_at`**

### **Consulta SQL para prueba**

```sql
UPDATE users SET trial_ends_at = '2025-06-26 00:00:30' WHERE name = 'Carol';
```

- **Al recargar la misma URL, muestra:**

```bash
Trial ends in 2 days
```

✔️ *Esto confirma que el mensaje depende directamente del valor `trial_ends_at`.*

---

## **Paso 4: Crear una suscripción**

- **Se accede al checkout con Stripe:**

```bash
http://172.17.0.2:8000/subscription-checkout
```

- *Una vez completado, el usuario deja de estar sólo en “modo trial” y pasa a estar suscrito (`subscribed() === true`).*

---

## **Paso 5: Código Blade mejorado en `resources/views/layouts/app.blade.php`**

### **Lógica inicial**

```php
@if (!auth()->user()->subscribed() && auth()->user()->onTrial())
    @php
        $remainingTrialDays = now()->diffInDays(auth()->user()->trial_ends_at);
    @endphp
    <x-alert type="info" message="Trial ends in {{ $remainingTrialDays }} days" />
@endif
```

- **Problema:** *Si el usuario **no está logueado**, `auth()->user()` devuelve `null`. Y `null->subscribed()` lanza error:*

```bash
Call to a member function subscribed() on null
```

---

## **Paso 6: Solución usando el operador `?->` en PHP 8+**

### **¿Qué es `?->`?**

> [!TIP]
> *Es el operador **"nullsafe"** de PHP 8.0+. Evita errores cuando se intenta acceder a un método o propiedad sobre `null`.*

```php
auth()->user()?->subscribed()
```

- *Si `auth()->user()` es `null`, el resultado será `null` sin lanzar error.*

---

## **Versión segura del bloque Blade**

```php
@if (!auth()->user()?->subscribed() && auth()->user()?->onTrial())
    @php
        $remainingTrialDays = now()->diffInDays(auth()->user()->trial_ends_at);
    @endphp
    <x-alert type="info" message="Trial ends in {{ $remainingTrialDays }} days" />
@endif
```

- **Explicación línea a línea**

| **Línea**                         | **Explicación técnica**                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------------ |
| *`auth()->user()?->subscribed()`* | *Devuelve `true` si el usuario está suscrito. Si no hay usuario logueado, retorna `null`.* |
| *`auth()->user()?->onTrial()`*    | *Devuelve `true` si el usuario está en período de prueba.*                                 |
| *`now()->diffInDays(...)`*        | *Calcula la diferencia entre hoy y `trial_ends_at`.*                                       |

**Este código evita errores cuando no hay sesión activa (usuario no autenticado).**

---

## **Bonus: Alternativa más segura aún (por legibilidad)**

**Puedes encapsular la verificación completa:**

```php
@php
    $user = auth()->user();
@endphp

@if ($user && !$user->subscribed() && $user->onTrial())
    <x-alert type="info" message="Trial ends in {{ now()->diffInDays($user->trial_ends_at) }} days" />
@endif
```

- *Esto reduce llamadas repetidas a `auth()->user()` y mejora rendimiento/claridad.*

---

## **Ventajas de cuenta Business para freelancers**

1. **Recibir pagos de clientes fácilmente**
    - *Puedes recibir pagos desde tarjetas de crédito, débito, y otras cuentas PayPal.*
    - *Tus clientes no necesitan tener cuenta PayPal para pagarte.*

2. **Facturación profesional**
    - *Puedes generar facturas con tu nombre o marca y enviarlas automáticamente.*

3. **Mejor reputación**
    - *PayPal Business da más confianza a clientes extranjeros (sobre todo si trabajas en plataformas como Upwork, Freelancer, Fiverr, etc.)*

4. **Opciones de integración**
    - *Si tienes una web o app, puedes integrar botones de pago, suscripciones o enlaces con más facilidad.*

5. **Separación de finanzas**
    - *Te permite mantener tus ingresos freelance separados de tus gastos personales (lo cual es bueno si algún día formalizas tu negocio).*
