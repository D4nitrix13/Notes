<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Instalación de Laravel UI con Webpack**  

- *Laravel ha migrado de **Webpack** a **Vite** en sus versiones más recientes. Sin embargo, para usar Webpack en lugar de Vite, es necesario instalar una versión específica del paquete `laravel/ui`.*

## **Instalar Laravel UI con Webpack (`https://github.com/laravel/ui`)**  

```bash
composer require laravel/ui=^3.4
```

- **Explicación:**  

- **`composer require` →** *Instala un paquete en el proyecto utilizando **Composer** (el gestor de dependencias de PHP).*
- **`laravel/ui` →** *Es el paquete oficial de Laravel para generar el **scaffolding** (estructura base) de autenticación y estilos.*
- **`=^3.4` →** *Especifica que se debe instalar la versión `3.4` o una versión compatible dentro del mismo rango (`3.x`), evitando instalar versiones más recientes que usan **Vite** en lugar de **Webpack**.*

- **Nota:**  

- *Laravel UI **3.4** usa **Bootstrap**.*
- *Las versiones posteriores utilizan **Tailwind CSS**.*

### **Generar la interfaz de usuario con Bootstrap**  

```bash
php artisan ui bootstrap --auth
```

- **Explicación:**  

- **`php artisan` →** *Comando de Laravel para ejecutar tareas en la aplicación.*
- **`ui bootstrap` →** *Indica que se debe generar la estructura base con **Bootstrap**.*
- **`--auth` →** *Agrega las vistas y lógica de autenticación (login, registro, recuperación de contraseña).*

- **Salida esperada:**  

```bash
Bootstrap scaffolding installed successfully.
Please run "npm install && npm run dev" to compile your fresh scaffolding.
Authentication scaffolding generated successfully.
```

- *Esto significa que Laravel ha creado la estructura base para las vistas con **Bootstrap**, incluyendo autenticación.*

### **Instalar dependencias de Node.js**  

**Para que Laravel compile los assets (CSS, JS), ejecutamos:**

```bash
npm install
npm run dev
```

- **Explicación:**  

- **`npm install` →** *Descarga e instala todas las dependencias definidas en el archivo `package.json`.*
- **`npm run dev` →** *Ejecuta el proceso de compilación de archivos CSS y JS para desarrollo.*

*Esto compila los archivos CSS y JS usando **Laravel Mix**, que se configura en el archivo `webpack.mix.js`.*

### **Contenido del `package.json`**  

```json
{
    "private": true,
    "scripts": {
        "dev": "npm run development",
        "development": "mix",
        "watch": "mix watch",
        "watch-poll": "mix watch -- --watch-options-poll=1000",
        "hot": "mix watch --hot",
        "prod": "npm run production",
        "production": "mix --production"
    },
    "devDependencies": {
        "@popperjs/core": "^2.10.2",
        "axios": "^0.25",
        "bootstrap": "^5.1.3",
        "laravel-mix": "^6.0.6",
        "lodash": "^4.17.19",
        "postcss": "^8.1.14",
        "resolve-url-loader": "^5.0.0",
        "sass": "^1.32.11",
        "sass-loader": "^11.0.1"
    }
}
```

- **Explicación de `scripts`:**  

- **`dev` →** *Ejecuta `npm run development`, que a su vez ejecuta `mix`.*
- **`watch` →** *Detecta cambios en los archivos y los recompila automáticamente.*
- **`hot` →** *Habilita la recarga en caliente (Hot Module Replacement).*
- **`prod` →** *Compila los assets para producción.*

- **Explicación de `devDependencies`:**  

- **`bootstrap` →** *Librería CSS para estilos responsivos.*
- **`laravel-mix` →** *Wrapper de Webpack que facilita la configuración de compilación.*
- **`sass` y `sass-loader` →** *Permiten compilar archivos SCSS/SASS.*
- **`axios` →** *Cliente HTTP para realizar peticiones AJAX.*

---

## **Iniciar el servidor Laravel**  

```bash
php artisan serve --host=0.0.0.0 --port=3030 --tries=10 --ansi -vvv
```

- **Explicación:**  

- **`php artisan serve` →** *Inicia un servidor de desarrollo de Laravel.*
- **`--host=0.0.0.0` →** *Permite acceder al servidor desde cualquier IP de la red local.*
- **`--port=3030` →** *Define el puerto en el que correrá la aplicación (`3030`).*
- **`--tries=10` →** *Intenta iniciar el servidor hasta 10 veces en caso de error.*
- **`--ansi` →** *Habilita colores en la salida de la terminal.*
- **`-vvv` →** *Modo **verboso** (muestra más detalles en la salida).*

- **Acceder A La Aplicación:**  
*Una vez que el servidor está corriendo, podemos acceder desde un navegador a:*

```bash
http://172.17.0.2:3030/register
```

*Esto nos mostrará el formulario de registro de usuario.*

---

## **Prueba de registro de usuario**  

*En el formulario ingresamos:*

- **Nombre:** *Daniel Perez*
- **Correo:** *`batman@gmail.com`*
- **Contraseña:** *`12345678`*
- **Confirmación de contraseña:** *`12345678`*

- **Laravel valida que la contraseña tenga al menos 8 caracteres.**

### **PostgreSQL Identificadores**

*En PostgreSQL, los **identificadores** (como nombres de tablas o columnas) **no son sensibles a mayúsculas y minúsculas**, **a menos que estén entre comillas dobles**.*

**Entonces, sí, estas dos sentencias:**

```sql
SELECT * FROM USERS;
SELECT * FROM users;
```

**son exactamente iguales** *para PostgreSQL.*

### **Pero ojo con esto**

*Si tú haces esto:*

```sql
CREATE TABLE "Users" (id SERIAL);
```

*Estás creando una tabla llamada literalmente `"Users"` (con **U mayúscula**), y a partir de ahí **tendrás que usar siempre comillas y respetar las mayúsculas**:*

```sql
SELECT * FROM "Users"; -- Correcto
SELECT * FROM users;   -- Error: no existe la tabla
```

### *Reglas rápidas*

- *Sin comillas dobles → PostgreSQL convierte el identificador a **minúsculas**.*
- *Con comillas dobles → se conserva el **formato exacto**, incluyendo mayúsculas y minúsculas.*

## **Verificar el usuario en la base de datos**  

```sql
SELECT * FROM USERS;
```

- **Ejecutando en PostgreSQL:**  

```sql
contacts_app=# SELECT * FROM USERS;
 id |     name     |      email       | email_verified_at |                           password                           | remember_token |     created_at      |     updated_at
----+--------------+------------------+-------------------+--------------------------------------------------------------+----------------+---------------------+---------------------
  1 | Daniel Perez | batman@gmail.com |                   | $2y$10$zE0WZGV7uNmR3yRHYeT35eeqR2ox5B6EiFlaE.PWFnkxLimkhwiJ6 |                | 2025-03-02 03:06:26 | 2025-03-02 03:06:26
(1 row)
```

- **Explicación de cada columna:**  

- **`id` →** *Identificador único del usuario.*
- **`name` →** *Nombre del usuario.*
- **`email` →** *Correo electrónico.*
- **`email_verified_at` →** *Fecha de verificación del correo (vacío, porque no se ha verificado).*
- **`password` →** *Contraseña encriptada con **bcrypt**.*
- **`remember_token` →** *Token para recordar sesión.*
- **`created_at` / `updated_at` →** *Fechas de creación y actualización del usuario.*

---

## **Resumen**  

- **Instalamos Laravel UI con Webpack**  
- **Generamos el scaffolding de Bootstrap con autenticación**  
- **Instalamos dependencias con `npm install` y compilamos los assets con `npm run dev`**  
- **Ejecutamos Laravel con `php artisan serve`**  
- **Registramos un usuario en la interfaz web**  
- **Verificamos los datos almacenados en PostgreSQL**  
