<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Cómo Publicar una App en Internet***

**Hosting Recomendado:**

- **Para la publicación de aplicaciones web, se recomienda utilizar [DigitalOcean](https://cloud.digitalocean.com/ "https://cloud.digitalocean.com/"), una plataforma de hosting escalable y fácil de usar.**

## ***Pasos para subir tu aplicación a un servidor***

1. **Acceder al servidor remoto:**
   - **Conéctate a tu máquina virtual utilizando `ssh` con la dirección IP pública proporcionada por tu proveedor de hosting.**

   ```bash
   ssh root@178.62.116.94
   ```

2. **Comprimir los ficheros de la aplicación:**
   - **En tu máquina local, utiliza `zip` para comprimir los ficheros de la aplicación (en este caso, el directorio `contacts-app`) antes de transferirlos al servidor.**

   ```bash
   apt install -y zip  # Instalar zip si aún no está instalado
   zip -r /opt/lampp/htdocs/contacts-app.zip /opt/lampp/htdocs/contacts-app
   ```

3. **Transferir los ficheros al servidor:**
   **Utiliza `scp` (secure copy) para transferir el fichero comprimido a la máquina virtual en el servidor remoto.**

   ```bash
   scp /opt/lampp/htdocs/contacts-app.zip root@178.62.116.94:/opt/lampp/htdocs/
   ```

4. **Descomprimir los ficheros en la máquina virtual:**
   - **Una vez que los ficheros estén en el servidor, accede a la máquina virtual y descomprime el fichero `.zip`.**

   ```bash
   apt update && apt install -y unzip  # Instalar unzip si no está disponible
   unzip /opt/lampp/htdocs/contacts-app.zip -d /opt/lampp/htdocs/
   ```

5. **Configurar el servidor web (si es necesario):**
   - **Asegúrate de que el servidor web (como Apache o Nginx) esté configurado correctamente para servir tu aplicación en la dirección deseada.**

---

### ***Notas adicionales***

- **DigitalOcean** *ofrece opciones de servidores (droplets) con diferentes configuraciones para proyectos pequeños o grandes.*
- **SSH** *es fundamental para gestionar el servidor de forma remota.*
- **`scp`** *permite transferir ficheros de forma segura entre máquinas locales y remotas.*
- *Asegúrate de que los permisos de los ficheros y directorios en el servidor estén correctamente configurados para evitar problemas de acceso.*

```bash
/opt/lampp/lampp start
/opt/lampp/bin/mysql -h localhost -u root -p -P 3306 start
```

- **Ejecutar el Fichero de Configuración para Crear la Base de Datos y Tablas**

- **Para configurar nuestra base de datos y crear las tablas necesarias para la aplicación, ejecutamos el fichero de configuración SQL utilizando el siguiente comando:**

```bash
source /opt/lampp/htdocs/contacts-app/sql/setup.sql
```

- **Este comando ejecuta el script SQL ubicado en /opt/lampp/htdocs/contacts-app/sql/setup.sql, que contiene las instrucciones para:**

- *Crear la base de datos.*
- *Definir las tablas necesarias para la aplicación (como users, contacts, etc.).*
- *Establecer las relaciones entre las tablas, como las claves foráneas.*

```bash
Enter password:
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 230
Server version: 10.4.32-MariaDB Source distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> source /opt/lampp/htdocs/contacts-app/sql/setup.sql
Query OK, 2 rows affected (0.029 sec)

Query OK, 1 row affected (0.001 sec)

Database changed
Query OK, 0 rows affected (0.014 sec)

Query OK, 0 rows affected (0.014 sec)
```
