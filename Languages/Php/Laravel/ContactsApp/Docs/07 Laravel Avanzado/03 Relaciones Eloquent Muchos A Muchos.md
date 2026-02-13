<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Eloquent Many-to-Many Relationships in Laravel**

## **Imagen de perfil por defecto**

**La ruta al archivo por defecto de la imagen de perfil usada para los contactos es:**

```bash
storage/app/public/profiles/default.png
```

**Laravel puede acceder a esta imagen si se crea un *symlink* con:**

```bash
php artisan storage:link
```

---

## **Contexto de práctica**

*Vamos a implementar un caso práctico donde **un usuario pueda compartir uno o varios de sus contactos con otros usuarios**. Aunque este caso no es común en la mayoría de aplicaciones, es excelente para practicar relaciones *many-to-many* en Laravel.*

---

## **Estructura actual de la tabla `contacts`**

**La tabla no sigue ninguna convención especial de Laravel, pero eso no impide establecer relaciones.**

```sql
contacts_app=# \d contacts
```

```sql
           Table "public.contacts"
 Column         | Type                | Nullable | Default
----------------+---------------------+----------+----------------------------
 id             | bigint              | not null | nextval(...)
 name           | varchar(255)        | not null |
 phone_number   | varchar(255)        | not null |
 email          | varchar(255)        | not null |
 age            | smallint            | not null |
 user_id        | bigint              | not null |
 created_at     | timestamp           |          |
 updated_at     | timestamp           |          |
 profile_picture| varchar(255)        | not null | 'profiles/default.png'
Indexes:
  "contacts_pkey" PRIMARY KEY, btree (id)
```

---

## **¿Qué es una tabla pivote?**

**Una **tabla pivote** es una tabla intermedia que se utiliza para representar relaciones de muchos a muchos.**

*Referencia: [Laravel Docs - Many to Many](https://laravel.com/docs/12.x/eloquent-relationships#many-to-many "https://laravel.com/docs/12.x/eloquent-relationships#many-to-many")*

### **Ejemplo clásico en Laravel**

```bash
users
  id - integer
  name - string

roles
  id - integer
  name - string

role_user (tabla pivote)
  user_id - integer
  role_id - integer
```

*Laravel por convención **espera que las tablas pivote**:*

* *Tengan nombres en singular (de las dos tablas) separados por guión bajo.*
* *Estén ordenadas **alfabéticamente**: `role_user`, no `user_role`.*

---

## **Crear migración para la tabla pivote personalizada**

*Ya que queremos que los usuarios puedan compartir contactos con otros usuarios, creamos una tabla pivote: `contact_shares`.*

```bash
php artisan make:migration create_contacts_shares_table
```

**Modificamos el archivo generado para que la tabla se vea así:**

```php
Schema::create('contact_shares', function (Blueprint $table) {
    $table->id();
    $table->foreignId('user_id')->constrained()->onDelete('cascade');
    $table->foreignId('contact_id')->constrained()->onDelete('cascade');
    $table->timestamps();
});
```

**Y luego ejecutamos:**

```bash
php artisan migrate
```

---

## **Controlador de relaciones**

*No es necesario crear un modelo para `contact_shares` porque no tiene atributos propios relevantes. Solo necesitamos un controlador para manejar las acciones.*

```bash
php artisan make:controller ContactShareController
```

**Este controlador manejará las rutas relacionadas a compartir contactos.**

---

## **Rutas registradas**

**Para confirmar las rutas generadas:**

```bash
php artisan route:list | grep contacts-shares
```

**Resultado:**

```bash
GET|HEAD        contacts-shares ................................................................................................................ contacts-shares.index › ContactShareController@index
POST            contacts-shares ................................................................................................................ contacts-shares.store › ContactShareController@store
GET|HEAD        contacts-shares/create ....................................................................................................... contacts-shares.create › ContactShareController@create
DELETE          contacts-shares/{contacts_share} ........................................................................................... contacts-shares.destroy › ContactShareController@destroy
```

**Estas rutas están asociadas a acciones para:**

* *Listar contactos compartidos*
* *Crear nuevas asociaciones*
* *Eliminar asociaciones*
* *Mostrar formulario de compartir*

---

## **Consulta directa en PostgreSQL**

**Para acceder directamente a la base de datos dentro de un contenedor Docker:**

```bash
docker container exec -it --user 0:0 --privileged --workdir / db /usr/bin/psql -h localhost -U postgres -p 5432 -d contacts_app
```

**Explicación:**

* *`exec -it`: Ejecuta de forma interactiva dentro del contenedor.*
* *`--user 0:0`: Accede como root.*
* *`--privileged`: Da permisos extendidos.*
* *`--workdir /`: Directorio de trabajo.*
* *`psql`: Cliente PostgreSQL.*
* *`-h localhost`: Host.*
* *`-U postgres`: Usuario.*
* *`-p 5432`: Puerto.*
* *`-d contacts_app`: Base de datos.*

**Consulta de tabla:**

```sql
SELECT * FROM contact_shares;
```

**Ejemplo de salida:**

```bash
 id | user_id | contact_id 
----+---------+------------
  1 |       2 |         33
```

---

## **Relación en Eloquent**

*Asumiendo que tienes el modelo `Contact` definido, y la relación está así:*

```php
public function sharedWithUsers()
{
    return $this->belongsToMany(User::class, 'contact_shares', 'contact_id', 'user_id');
}
```

**Entonces, para obtener los usuarios con quienes fue compartido un contacto:**

```php
Contact::find(33)->sharedWithUsers;
```

### **¿Por qué no se usan paréntesis?**

*Porque `sharedWithUsers` es una **propiedad mágica** generada por Eloquent (tipo `getSharedWithUsersAttribute()`). Si quisieras hacer una consulta más compleja podrías usarla como método:*

```php
Contact::find(33)->sharedWithUsers()->where('id', 2)->get();
```

---

## **El campo `pivot`**

**Cuando accedes a una relación muchos a muchos en Laravel, cada resultado incluirá una propiedad `pivot`, que representa los datos de la tabla intermedia (`contact_shares` en este caso).**

```php
App\Models\User {
  id: 2,
  name: "Carol",
  ...
  pivot: Illuminate\Database\Eloquent\Relations\Pivot {
    contact_id: 33,
    user_id: 2
  }
}
```

### **¿Para qué sirve `wherePivot()`?**

**Permite filtrar resultados en la relación por los valores de la tabla intermedia.**

**Ejemplo:**

```php
$contact->sharedWithUsers()->wherePivot('user_id', 2)->get();
```
