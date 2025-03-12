<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

<?php

  require "./database.php";

  session_start();
  if (!isset($_SESSION["user"])) {
    header("Location: ./login.php");
    return;
  }

  $id = $_GET["id"];

  $statement = $connection->prepare("SELECT * FROM contacts WHERE id = :id LIMIT 1");
  $statement->execute([":id" => $id]);

  // var_dump($_SERVER["REQUEST_METHOD"]); die();

  if ($statement->rowCount() == 0) {
    http_response_code(404);
    echo("HTTP 404 NOT FOUND");
    return;
  }

  // fetchAll(): Devuelve todas las filas en un solo array. Es útil cuando necesitas trabajar con todos los resultados a la vez.
  // fetch(): Devuelve una fila a la vez. Es útil cuando trabajas con grandes volúmenes de datos o cuando solo necesitas una fila en cada iteración (por ejemplo, cuando usas un bucle).
  $contact = $statement->fetch(PDO::FETCH_ASSOC);


  if ($contact["user_id"] != $_SESSION["user"]["id"]) {
    http_response_code(401); echo("[x] HTTP 401 UNAUTHORIZED" . PHP_EOL); return;
  }

  $error = null;

  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    
    $name = $_POST["name"];
    $phoneNumber = $_POST["phone_number"];

    if (empty($name) || empty($phoneNumber)) {
      $error = "Please All The Fields";
    } else if (strlen($phoneNumber) < 9) {
      $error = "Phone Number Must Be At Least 9 Characters.";
    } else {
      $statement = $connection->prepare("UPDATE contacts SET name = :name, phone_number = :phone_number WHERE id = :id");
      $statement->execute([
        ":id" => $id,
        ":name" => $name,
        ":phone_number" => $phoneNumber
      ]);
      // En Php Para Acceer A Atriubots Y Metodos De Un Clase Usamos ->
      $_SESSION["flash"] = [
        "message" => "Contact {$_POST['name']} Added",
        "type" => "primary" // Colour Blue
      ];
      header("Location: ./home.php");
      return;
    }
  }
?>

<?php require "./partials/header.php" ?>
<div class="container pt-5">
  <div class="row justify-content-center">
    <div class="col-md-8">
      <div class="card">
        <div class="card-header">Update Contact</div>
        <div class="card-body">
          <?php if ($error): ?>
            <p class="text-danger">
              <?= $error ?>
            </p>
          <?php endif ?>
          <form method="post" action="./update.php?id=<?= $contact['id'] ?>">
            <div class="mb-3 row">
              <label for="name" class="col-md-4 col-form-label text-md-end">Name</label>

              <div class="col-md-6">
                <input value="<?= $contact['name'] ?>" id="name" type="text" class="form-control" name="name" autocomplete="name" autofocus>
              </div>
            </div>

            <div class="mb-3 row">
              <label for="phone_number" class="col-md-4 col-form-label text-md-end">Phone Number</label>

              <div class="col-md-6">
                <input value="<?= $contact['phone_number'] ?>" id="phone_number" type="tel" class="form-control" name="phone_number" autocomplete="phone_number" autofocus>
              </div>
            </div>

            <div class="mb-3 row">
              <div class="col-md-6 offset-md-4">
                <button type="submit" class="btn btn-primary">Submit</button>
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