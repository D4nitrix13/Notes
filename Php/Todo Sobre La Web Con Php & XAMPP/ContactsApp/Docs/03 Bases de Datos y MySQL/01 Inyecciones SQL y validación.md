<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Inyecciones SQL y validación***

```php
<?php
// Ejemplo de prevención de inyecciones SQL y validación de datos

// Manera incorrecta de hacerlo:
// Evita concatenar directamente valores externos en consultas SQL.
// Esto se llama "inyección SQL" y expone la base de datos a riesgos graves.
// $statement = $connection->prepare("INSERT INTO contacts (name, phone_number) VALUES ('$name','$phoneNumber')");

// Forma correcta de realizar la inserción de datos:
// 1. Usa consultas preparadas con marcadores de posición.
// 2. Vincula los valores de forma segura para evitar inyecciones SQL.

// Consulta preparada con parámetros nombrados
$statement = $connection->prepare("INSERT INTO contacts (name, phone_number) VALUES (:name, :phone_number)");

// Vinculación de parámetros con valores seguros
// Los valores se escapan automáticamente al usar consultas preparadas
$statement->bindParam(":name", $name);
$statement->bindParam(":phone_number", $phoneNumber);

// Ejecución de la consulta
$statement->execute();

?>
```

## ***Ejemplo de solicitud HTTP para probar la inserción***

### ***Utiliza curl para enviar datos al script de inserción***

```bash
curl -X POST --location \
     --header "application/x-www-form-urlencoded" \
     --data "name=&phone_number=" \
     http://172.17.0.x/contacts-app/edit.php
```

#### ***Ejemplo de consulta y su resultado en MariaDB:***

#### ***Consulta válida:***

```sql
MariaDB [ContactsApp]> SELECT * FROM contacts WHERE name = "" && phone_number = "";
+----+------+--------------+
| id | name | phone_number |
+----+------+--------------+
|  6 |      |              |
+----+------+--------------+
1 row in set (0.001 sec)
```

- **Ejemplo de inyección SQL:**
- **Intenta insertar datos maliciosos.**
- **Esto sucede cuando no se usan parámetros seguros.**

```bash
'); DROP DATABASE ContactsApp; --
```

- **Resultado de una consulta maliciosa en MariaDB:**

```sql
MariaDB [ContactsApp]> SELECT * FROM contacts WHERE phone_number = "'); DROP DATABASE ContactsApp; --";
+----+-------------------------------+-----------------------------------+
| id | name                          | phone_number                      |
+----+-------------------------------+-----------------------------------+
|  7 | Daniel Benjamin Perez Morales | '); DROP DATABASE ContactsApp; -- |
+----+-------------------------------+-----------------------------------+
1 row in set (0.001 sec)
```
