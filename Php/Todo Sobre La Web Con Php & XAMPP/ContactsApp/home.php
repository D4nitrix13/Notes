<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

<?php 
  require "./database.php";
  // Reanudamos La Sesión Existente O Iniciamos Una Nueva Si No Hay Ninguna Activa
  session_start();

  if (!isset($_SESSION["user"])) {
    header("Location: ./login.php");
    return;
  }
  // Sintaxis Para Reemplazar El Valor En Un Array Asociativo Usando {}
  $contacts = $connection->query("SELECT * FROM contacts WHERE user_id = {$_SESSION['user']['id']}");
?>

<?php require "./partials/header.php" ?>
<div class="container pt-4 p-3">
  <div class="row">
  <?php if ($contacts->rowCount() == 0): ?>
      <div class="col-md-4 mx-auto">
        <div class="card card-body text-center">
          <p>No contacts saved yet</p>
          <a href="./add.php">Add One!</a>
        </div>
      </div>
    <?php endif ?>
    <?php foreach ($contacts as $contact): ?>
      <div class="col-md-4 mb-3">
        <div class="card text-center">
          <div class="card-body">
            <h3 class="card-title text-capitalize"><?=$contact["name"]?></h3>
            <p class="m-2"><?=$contact["phone_number"]?></p>
            <a href="./update.php?id=<?=$contact["id"]?>"
              class="btn btn-secondary mb-2">Edit Contact</a>
            <a href="./delete.php?id=<?= $contact["id"]?>"
              class="btn btn-danger mb-2">Delete Contact</a>
          </div>
        </div>
      </div>
    <?php endforeach ?>
  </div>
</div>
<?php require "./partials/footer.php" ?>