<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Iniciar un contenedor Docker con PostgreSQL**

```bash
docker container run -itdePOSTGRES_PASSWORD=root -lstage=development -p5432:5432 --expose 5432 --network bridge --name db postgres:latest
```

---

## **Descripción de cada opción**  

- **`docker container run`:** *Este comando se utiliza para crear e iniciar un contenedor de Docker con una imagen específica.*  

- **`-it`:** *Combinación de dos opciones:*  
  - **`-i`** *(interactivo): Mantiene la entrada estándar (stdin) abierta, lo que permite la interacción con el contenedor.*  
  - **`-t`** *(tty): Asigna una terminal virtual al contenedor para una experiencia más interactiva.*  

- **`-d`:** *Ejecuta el contenedor en segundo plano (modo "detached"). Esto permite que el proceso se ejecute sin bloquear la terminal.*  

- **`-e POSTGRES_PASSWORD=root`:** *Define la variable de entorno `POSTGRES_PASSWORD` dentro del contenedor, estableciendo la contraseña del usuario `postgres`. PostgreSQL utiliza este usuario por defecto para la administración de la base de datos.*  

- **`--env POSTGRES_PASSWORD=root`:** *Es otra forma de definir variables de entorno, equivalente a `-e POSTGRES_PASSWORD=root`.*  

- **`-l stage=development`** *(Etiqueta o label):* *Asigna una etiqueta (`stage=development`) al contenedor. Las etiquetas son metadatos utilizados para organizar y gestionar contenedores dentro de Docker.*  

- **`-p 5432:5432`:** *Mapea el puerto `5432` del contenedor al puerto `5432` de la máquina host. Esto permite que aplicaciones externas accedan a la base de datos PostgreSQL dentro del contenedor.*  

- **`--expose 5432`:** *Expone el puerto `5432` dentro del contenedor para permitir la comunicación entre contenedores en la misma red de Docker. Sin embargo, por sí solo, no hace que el puerto sea accesible desde fuera del contenedor; para eso es necesario `-p`.*  

- **`--network bridge`:** *Conecta el contenedor a la red `bridge`, que es la red predeterminada en Docker. Esto facilita la comunicación entre contenedores sin necesidad de exponer puertos al host.*  

- **`--name db`:** *Asigna el nombre `db` al contenedor, permitiendo referenciarlo más fácilmente en otros comandos de Docker.*  

- **`postgres:latest`:** *Especifica que se usará la última versión disponible de la imagen de PostgreSQL en Docker Hub. Esta imagen contiene todo lo necesario para ejecutar un servidor PostgreSQL.*  

---

## **Eliminar Una Base De Datos En PostgreSQL**

```bash
docker container exec -it db psql -h localhost -U postgres -p 5432 -c "DROP DATABASE IF EXISTS contacts_app"
```

- **Descripción de cada opción**

- **`docker container exec`:** *Este comando permite ejecutar un comando dentro de un contenedor en ejecución.*
  
- **`-it`:** *Como antes, abre una sesión interactiva para ejecutar el comando dentro del contenedor.*
  
- **`db`:** *Es el nombre del contenedor donde se va a ejecutar el comando, que en este caso es el contenedor de PostgreSQL que hemos creado previamente.*

- **`psql`:** *Es el cliente de línea de comandos de PostgreSQL para interactuar con la base de datos.*
  
- **`-h localhost`:** *Especifica el host del servidor de base de datos. En este caso, usamos `localhost`, ya que estamos ejecutando PostgreSQL dentro de un contenedor en nuestra máquina local.*

- **`-U postgres`:** *Indica el nombre de usuario con el que queremos conectarnos a la base de datos, en este caso `postgres`, que es el usuario por defecto de PostgreSQL.*

- **`-p 5432`:** *Especifica el puerto del servidor de PostgreSQL, en este caso el predeterminado `5432`.*

- **`-c`:** *Ejecuta el comando SQL que sigue a esta opción. En este caso, el comando SQL es `DROP DATABASE IF EXISTS contacts_app`, que elimina la base de datos `contacts_app` si existe.*

---

## **Crear una base de datos en PostgreSQL**

```bash
docker container exec -it db psql -h localhost -U postgres -p 5432 -c "CREATE DATABASE contacts_app"
```

*Este comando es muy similar al anterior, pero en vez de eliminar la base de datos, la **crea** si no existe. La diferencia principal está en el comando SQL, que en este caso es `CREATE DATABASE contacts_app`.*

---

## **Instalar dependencias para la conexión de PostgreSQL en PHP**

- **Instalar Driver (Could Not Find Driver)**

**Ejecutar En Container `laravel-guide`**

```bash
docker container exec -itu0:0 --privileged -w/App laravel-guide /bin/bash -plic "apt-get update && apt-get install -y libpq-dev && docker-php-ext-install pdo_pgsql"
```

```bash
apt-get update && apt-get install -y libpq-dev
docker-php-ext-install pdo_pgsql
```

- **Descripción de cada opción**

- **`apt-get update`:** *Actualiza la lista de paquetes disponibles para la instalación en el sistema. Esto es necesario para asegurarse de que estamos trabajando con las versiones más recientes de los paquetes.*
  
- **`apt-get install -y libpq-dev`:** *Instala `libpq-dev`, que es una biblioteca de desarrollo de PostgreSQL necesaria para compilar la extensión `pdo_pgsql` de PHP. Esta extensión permite a PHP conectarse a una base de datos PostgreSQL.*

- **`docker-php-ext-install pdo_pgsql`:** *Este comando instala la extensión `pdo_pgsql` para PHP dentro del contenedor. La extensión `pdo_pgsql` permite a PHP interactuar con bases de datos PostgreSQL a través de la interfaz PDO (PHP Data Objects).*

---

## **Ejecutar las migraciones de Laravel**

```bash
php artisan migrate
```

*Este comando ejecuta las migraciones en Laravel. Las migraciones son archivos de PHP que definen cómo se deben crear o modificar las tablas de la base de datos.*

### **Salida**

*Cuando ejecutas `php artisan migrate`, Laravel prepara la base de datos y crea la tabla `migrations`, que es utilizada para rastrear qué migraciones han sido ejecutadas. Si no hay migraciones previas, ejecuta las migraciones definidas en los archivos dentro del directorio `database/migrations`.*

*Explicacion:*

- **`2014_10_12_000000_create_users_table`:** *Crea la tabla `users` para almacenar los datos de los usuarios.*
- **`2019_08_19_000000_create_failed_jobs_table`:** *Crea la tabla `failed_jobs` para almacenar los trabajos fallidos.*

*Si las migraciones se han ejecutado correctamente, la salida será algo como:*

```bash

  INFO  Preparing database.

  Creating migration table .............................................................................................................. 16ms DONE

   INFO  Running migrations.

  2014_10_12_000000_create_users_table .................................................................................................. 13ms DONE
  2014_10_12_100000_create_password_resets_table ......................................................................................... 8ms DONE
  2019_08_19_000000_create_failed_jobs_table ............................................................................................. 7ms DONE
  2019_12_14_000001_create_personal_access_tokens_table .................................................................................. 6ms DONE
```

- **Si Volvemos A Ejecutar**

```bash
php artisan migrate
```

```bash
INFO  Nothing to migrate.
```

---

## **Revertir migraciones en Laravel**

```bash
php artisan migrate:rollback --step 1
```

*Este comando revierte las migraciones más recientes. La opción **`--step`** permite especificar cuántas migraciones se deben revertir. En este caso, `--step 1` indica que solo se revertirá la última migración ejecutada.*

- **Salida**

**La salida mostrará qué migración se ha revertido:**

```bash
INFO  Rolling back migrations.
2019_12_14_000001_create_personal_access_tokens_table .............. 13ms DONE
```

---

### **Resumen**

- **`php artisan migrate`:** *Ejecuta las migraciones pendientes, creando o modificando tablas en la base de datos.*
- **`php artisan migrate:rollback`:** *Revierte las migraciones, deshaciendo los cambios realizados en la base de datos.*
- **`docker container exec`:** *Ejecuta comandos dentro de un contenedor Docker.*
- **`psql`:** *Herramienta de línea de comandos de PostgreSQL para ejecutar consultas directamente desde la terminal.*

*Este flujo es útil para gestionar bases de datos en un entorno de desarrollo o producción, asegurando que las tablas y la estructura de datos estén siempre actualizadas según las definiciones de las migraciones.*
