<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# **Conexión con un Cliente MySQL**

- *![NavegadorPeticionServidorMySQL](/Images/NavegadorPeticionServidorMySQL.png "/Images/NavegadorPeticionServidorMySQL.png")*
- **Para conectarse a un cliente MySQL, se pueden usar los siguientes comandos:**

```bash
mysql --user=root --password
mysql -u root -p
mysql -uroot -p
```

## **Creación y Manipulación de Bases de Datos en MariaDB**

- *A continuación, se presentan los pasos para crear una base de datos, ver las bases de datos disponibles y realizar operaciones básicas dentro de una base de datos en MariaDB.*

```sql
DROP DATABASE IF EXISTS ContactsApp;

CREATE DATABASE IF NOT EXISTS ContactsApp;

SHOW DATABASES;

USE ContactsApp;

CREATE TABLE contacts (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(255) NOT NULL, phone_number VARCHAR(255) NOT NULL);

INSERT INTO contacts (name, phone_number) VALUES ("Daniel Perez", "12345678"), ("Danna Morales", "87654321"), ("Benjamin Perez", "22443377");
```

```sql
MariaDB [(none)]> DROP DATABASE IF EXISTS ContactsApp;
Query OK, 0 rows affected, 1 warning (0.000 sec)

MariaDB [(none)]> CREATE DATABASE IF NOT EXISTS ContactsApp;
Query OK, 1 row affected (0.001 sec)

MariaDB [(none)]> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| ContactsApp        |
| information_schema |
| mysql              |
| performance_schema |
| phpmyadmin         |
| test               |
+--------------------+
6 rows in set (0.001 sec)

MariaDB [(none)]> USE ContactsApp;
Database changed

MariaDB [ContactsApp]> CREATE TABLE contacts (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(255) NOT NULL, phone_number VARCHAR(255) NOT NULL);
Query OK, 0 rows affected (0.017 sec)

MariaDB [ContactsApp]> INSERT INTO contacts (name, phone_number) VALUES ("Daniel Perez", "12345678"), ("Danna Morales", "87654321"), ("Benjamin Perez", "22443377");
Query OK, 3 rows affected (0.007 sec)
Records: 3  Duplicates: 0  Warnings: 0
```

### **Creación de un Fichero SQL para la Configuración**

- **Para automatizar la creación de la base de datos y la tabla de contactos, se puede crear un fichero SQL con los comandos necesarios.**

1. **Crear un directorio y fichero SQL:**

    ```bash
    mkdir ./sql
    touch setup.sql
    ```

2. Insertar los siguientes comandos SQL en el fichero `setup.sql`:

    ```sql
    -- Author: Daniel Benjamin Perez Morales
    -- GitHub: https://github.com/D4nitrix13
    -- Email: danielperezdev@proton.me

    DROP DATABASE IF EXISTS ContactsApp;

    CREATE DATABASE IF NOT EXISTS ContactsApp;

    USE ContactsApp;

    CREATE TABLE IF NOT EXISTS contacts (id INT PRIMARY KEY AUTO_INCREMENT NOT NULL, name VARCHAR(255) NOT NULL, phone_number VARCHAR(255) NOT NULL);

    INSERT INTO contacts (name, phone_number) VALUES ("Daniel Perez", "12345678"), ("Danna Morales", "87654321"), ("Benjamin Perez", "22443377");
    ```

#### **Ejecutar el Fichero SQL en MySQL**

- **Una vez creado el fichero SQL, se puede ejecutar el script dentro de MySQL utilizando el comando `SOURCE` para cargar y ejecutar el fichero.**

```bash
SOURCE /App/contacts-app/sql/setup.sql;
```
