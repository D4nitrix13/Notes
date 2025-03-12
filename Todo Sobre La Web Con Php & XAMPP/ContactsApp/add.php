<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

<?php

session_start();
if (!isset($_SESSION["user"])) {
  header("Location: ./login.php");
  return;
}

$error = null;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  
  require "./database.php";

  $name = $_POST["name"];
  $phoneNumber = $_POST["phone_number"];

  if (empty($name) || empty($phoneNumber)) {
    $error = "Please All The Fields";
  } else if (strlen($phoneNumber) < 9) {
    $error = "Phone Number Must Be At Least 9 Characters.";
  } else {
    // Inyeccion SQL'); DROP DATABASE ContactsApp; --
    // [x] PDO Connection Error: SQLSTATE[HY000] [1049] Unknown database 'ContactsApp' 

    // Manera Incorrecta De Hacerlo
    // ! $statement = $connection->prepare("INSERT INTO contacts (name, phone_number) VALUES ('$name','$phoneNumber')");

    // Vinculación de parámetros con valores seguros 
    // Los valores se escapan automáticamente al usar consultas preparadas
    $statement = $connection->prepare("INSERT INTO contacts (user_id, name, phone_number) VALUES (:user_id, :name, :phone_number)");
    $statement->bindParam(":user_id", $_SESSION['user']['id']);
    $statement->bindParam(":name", $name);
    $statement->bindParam(":phone_number", $phoneNumber);
    $statement->execute();

    $_SESSION["flash"] = [
      "message" => "Contact {$_POST['name']} Added",
      "type" => "success" // Colour Green
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
        <div class="card-header">Add New Contact</div>
        <div class="card-body">
          <?php if ($error): ?>
            <p class="text-danger">
              <?= $error ?>
            </p>
          <?php endif ?>
          <form method="post"
            action="./add.php">
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
              <label for="phone_number"
                class="col-md-4 col-form-label text-md-end">Phone Number</label>

              <div class="col-md-6">
                <input id="phone_number"
                  type="tel"
                  class="form-control"
                  name="phone_number"
                  required
                  placeholder="123456789"
                  autocomplete="phone_number"
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