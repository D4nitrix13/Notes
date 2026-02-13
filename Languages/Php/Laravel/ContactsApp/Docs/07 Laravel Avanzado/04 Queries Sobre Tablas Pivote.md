<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Queries sobre Tablas Pivote en Laravel**

---

## **Contexto**

*En nuestro modelo, un `User` puede **compartir** contactos con otros usuarios. La relación es muchos a muchos entre `users` y `contacts`, mediante la tabla pivote `contact_shares`.*

---

## **Query: Obtener contactos que un usuario ha recibido como compartidos**

```php
User::find(2)->sharedContacts()->with("user")->get()
```

### **Explicación paso a paso**

* **`User::find(2)`**
  *Busca al usuario con ID 2.*

* **`sharedContacts()`**
  *Es una relación `belongsToMany` definida en el modelo `User`. Representa los contactos que este usuario ha recibido de otros usuarios.*

  ```php
  public function sharedContacts()
  {
      return $this->belongsToMany(Contact::class, 'contact_shares', 'user_id', 'contact_id');
  }
  ```

* **`with("user")`**
  *Eager loads la relación inversa: el dueño original del contacto. Esto asume que en el modelo `Contact` existe:*

  ```php
  public function user()
  {
      return $this->belongsTo(User::class);
  }
  ```

* **`get()`**
  *Ejecuta la consulta y devuelve una colección.*

---

## **Ejemplo del resultado (tinker)**

```php
= Illuminate\Database\Eloquent\Collection {
  all: [
    App\Models\Contact {
      id: 33,
      name: "batman",
      ...
      pivot: Illuminate\Database\Eloquent\Relations\Pivot {
        user_id: 2,
        contact_id: 33,
      },
      user: App\Models\User {
        id: 1,
        name: "Daniel",
        ...
      }
    }
  ]
}
```

### **Nota importante**

* *El objeto `pivot` indica que esta es una relación **many-to-many**, e incluye los valores de la tabla intermedia `contact_shares`.*
* *La propiedad `user` dentro del contacto es el **dueño original** del contacto, no quien lo recibió.*

---

## *Lógica para **eliminar un contacto compartido***

### **Objetivo**

*Permitir que el **usuario dueño del contacto** elimine una relación de compartido (revocar acceso a otro usuario).*

---

## **Código: `ContactShareController.php`**

```php
function destroy(int $id)
{
    // 1. Buscar la fila en la tabla pivote contact_shares
    $contactShare = DB::selectOne(
        query: "SELECT * FROM contact_shares WHERE id = ?", 
        bindings: [$id]
    );

    // 2. Buscar el contacto relacionado
    $contact = Contact::findOrFail($contactShare->contact_id);

    // 3. Verificar que el usuario autenticado sea el dueño del contacto
    abort_if(
        is_null($contact->user_id !== auth()->id()), 
        Response::HTTP_FORBIDDEN
    );

    // 4. Remover la relación en la tabla pivote
    $contact->sharedWithUsers()->detach($contactShare->user_id);

    // 5. Redirigir con mensaje de éxito
    return redirect()
        ->route("contacts-shares.index")
        ->with("alert", [
            "message" => "Contact $contact->email unshared",
            "type" => "success"
        ]);
}
```

### **Detalles clave**

* *`DB::selectOne(...)`: Ejecuta una consulta SQL sin usar Eloquent. Esto se hace aquí para obtener una fila específica por ID.*
* *`abort_if(...)`: Lanza un error HTTP 403 si el usuario autenticado no es dueño del contacto.*
* *`->detach(...)`: Método Eloquent para eliminar una relación en tabla pivote.*
* *`->with(...)`: Agrega un mensaje flash para mostrar al usuario.*

---

## **Autorización en `ContactPolicy.php`**

```php
public function view(User $user, Contact $contact)
{
    return $user->id === $contact->user_id ||
           $user->sharedContacts()->firstWhere("contact_id", $contact->id);
}
```

### **Explicación**

* *Si el usuario autenticado **es el dueño** del contacto (`$user->id === $contact->user_id`), puede verlo.*
* *Si **no lo es**, pero el contacto ha sido compartido con él (`sharedContacts()->firstWhere(...)`), también tiene acceso.*
