<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

<!-- <pre>
  <?php # die(var_dump($_COOKIE)); ?>
</pre> -->

<?php
  require "./database.php";
  $error = null;

  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["email"]) || empty($_POST["password"])) {
      $error = "Please Fill All The Fields";
    } else if (!str_contains($_POST["email"], "@")) {
      $error = "Email Format Is Invalid";
    } else {
      $statement = $connection->prepare("SELECT * FROM users WHERE email = :email LIMIT 1");
      $statement->bindParam(":email", $_POST["email"]);
      $statement->execute();

      if ($statement->rowCount() == 0) {
        $error = "Invalid Credentials";
      } else {
        $user = $statement->fetch(PDO::FETCH_ASSOC);
        if (!password_verify($_POST["password"], $user["password"])) {
          $error = "Invalid Credentials";
        } else {
          // Inicia Una Sesión Sin Establecer Una Fecha De Expiración Explícita
          session_start();

          unset($user["password"]);

          $_SESSION["user"] = $user;
          header("Location: ./home.php"); 
        }
      }
    }
  }
?>

<?php require "./partials/header.php" ?>
<div class="container pt-5">
  <div class="row justify-content-center">
    <div class="col-md-8">
      <div class="card">
        <div class="card-header">Register</div>
        <div class="card-body">
          <?php if ($error): ?>
            <p class="text-danger">
              <?= $error ?>
            </p>
          <?php endif ?>
          <form method="post"
            action="./login.php">
            <div class="mb-3 row">
              <label for="email"
                class="col-md-4 col-form-label text-md-end">Email</label>

              <div class="col-md-6">
                <input id="email"
                  type="email"
                  class="form-control"
                  name="email"
                  required
                  placeholder="example@example.com"
                  autocomplete="email"
                  autofocus>
              </div>
            </div>

            <div class="mb-3 row">
              <label for="password"
                class="col-md-4 col-form-label text-md-end">Password</label>

              <div class="col-md-6">
                <input id="password"
                  type="password"
                  class="form-control"
                  name="password"
                  required
                  placeholder="*****"
                  autocomplete="password"
                  autofocus>
              </div>
            </div>

            <div class="mb-3 row">
              <div class="col-md-6 offset-md-4">
                <button type="submit"
                  class="btn btn-primary">Submit</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</div>
<?php require "./partials/footer.php" ?>


<!-- 

# **Sesiones y Login: Conceptos y Características**

---

## **1. Sesiones**

**Concepto:**  

Una sesión es un mecanismo que permite a las aplicaciones web mantener información sobre un usuario durante su interacción con el sitio, incluso cuando las solicitudes HTTP (que son sin estado) no lo permiten de forma nativa. Las sesiones permiten rastrear al usuario desde el momento en que accede al sistema hasta que se desconecta o la sesión expira.

**Características:**  

- **Persistencia temporal:** Los datos de la sesión están disponibles solo mientras el usuario está activo (generalmente hasta que cierra el navegador o el servidor elimina la sesión por inactividad).
- **Identificación única:** Cada sesión está asociada a un identificador único (por ejemplo, un `session ID`) que se genera cuando el usuario inicia una nueva sesión.
- **Almacenamiento:** Los datos de la sesión pueden almacenarse en el servidor (seguro) o en cookies en el cliente (menos seguro).
- **Datos personalizados:** Permite guardar información específica del usuario, como su nombre, preferencias, carrito de compras, etc.

**Ventajas:**

- Facilita la experiencia del usuario al mantener información entre solicitudes.
- Mejora la seguridad al no exponer datos sensibles directamente en el cliente.

**Ejemplo común:**

En PHP, las sesiones se inician con `session_start()` y permiten almacenar datos como:  

```php
$_SESSION['username'] = 'usuario123';
```

---

### **2. Login**

**Concepto:**  

El login (o inicio de sesión) es el proceso mediante el cual un usuario verifica su identidad en un sistema, generalmente proporcionando credenciales como un nombre de usuario y contraseña. El objetivo es garantizar que solo los usuarios autorizados puedan acceder a recursos específicos.

**Características:**  

- **Autenticación:** Es el proceso principal del login, donde el sistema valida las credenciales ingresadas contra las almacenadas (por ejemplo, en una base de datos).
- **Seguridad:** El sistema utiliza técnicas como cifrado (hashing) de contraseñas para proteger las credenciales del usuario.
- **Control de acceso:** Después de un login exitoso, el sistema asigna privilegios o roles al usuario (por ejemplo, administrador, usuario estándar).
- **Persistencia opcional:** Algunas aplicaciones permiten mantener la sesión activa mediante cookies (como "Recordarme").

**Ventajas:**

- Proporciona acceso seguro a recursos restringidos.
- Permite personalizar la experiencia del usuario basado en sus credenciales y perfil.

**Flujo típico de un login:**

1. El usuario ingresa su nombre de usuario y contraseña en un formulario.
2. El sistema valida las credenciales contra los datos almacenados.
3. Si son correctos, se crea una sesión para ese usuario.
4. Si no, se muestra un mensaje de error.

---

### **Relación entre Sesiones y Login**

- **Login** inicia una sesión al autenticar al usuario.  
- La **sesión** mantiene el estado del usuario autenticado durante su interacción con la aplicación.  
- Sin sesiones, el usuario tendría que autenticarse en cada solicitud, lo cual sería poco práctico.  
-->
