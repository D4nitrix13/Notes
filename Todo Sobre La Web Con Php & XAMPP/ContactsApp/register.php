<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

<?php

  require "./database.php";

  $error = null;

  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    if (empty($_POST["name"]) || empty($_POST["email"]) || empty($_POST["password"])) {
      $error = "Please Fill All The Fields";
    } else if (!str_contains($_POST["email"], "@")) {
      $error = "Email Format Is Invalid";
    } else {
      $statement = $connection->prepare("SELECT * FROM users WHERE email = :email");
      $statement->bindParam(":email", $_POST["email"]);
      $statement->execute();

      if ($statement->rowCount() > 0) {
        $error = "This Email Is Taken";
      } else {
        $connection->prepare("INSERT INTO users (name, email, password) VALUES (:name, :email, :password)")->execute([
          ":name" => $_POST["name"],
          ":email" => $_POST["email"],
          ":password" => password_hash($_POST["password"], PASSWORD_BCRYPT)
        ]);

        $statement = $connection->prepare("SELECT * FROM users WHERE email = :email LIMIT 1");
        $statement->bindParam(":email", $_POST["email"]);
        $statement->execute();
        
        $user = $statement->fetch(PDO::FETCH_ASSOC);
        session_start();
        unset($user["password"]);
        $_SESSION["user"] = $user;

        header("Location: ./home.php");
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
            action="./register.php">
            <div class="mb-3 row">
              <label for="name"
                class="col-md-4 col-form-label text-md-end">Name</label>

              <div class="col-md-6">
                <input id="name"
                  type="text"
                  class="form-control"
                  name="name"
                  required
                  placeholder="Daniel Benjamin Perez Morales"
                  autocomplete="name"
                  autofocus>
              </div>
            </div>

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

method="post"

  Especifica el método HTTP que se usará para enviar los datos del formulario al servidor.
  En este caso, el método es POST, que:
    Transmite los datos en el cuerpo de la solicitud HTTP, no en la URL (a diferencia de GET).
    Es más adecuado para enviar datos sensibles o grandes volúmenes de información, ya que no expone los datos en la barra de direcciones del navegador.
    Es utilizado típicamente en operaciones como agregar, actualizar o eliminar datos.

action="./add.php"

  Define la URL o ruta a la que se enviarán los datos del formulario.
  En este caso, el fichero add.php, ubicado en el mismo directorio que la página actual (./ indica el directorio actual).
  Cuando el formulario se envíe, el servidor ejecutará el código en add.php, que probablemente procesará los datos enviados.
-->