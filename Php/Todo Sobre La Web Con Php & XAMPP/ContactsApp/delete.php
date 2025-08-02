<?php 

  require "./database.php";

  session_start();
  if (!isset($_SESSION["user"])) {
    header("Location: ./login.php");
    return;
  }

  $id = $_GET["id"];

  $statement = $connection->prepare("SELECT * FROM contacts WHERE id IN (:id) LIMIT 1");
  $statement->execute([":id" => $id]);

  if ($statement->rowCount() == 0) {
      http_response_code(404);
      echo("[x] HTTP 404 NOT FOUND");
      return;
  }

  // $statement = $connection->prepare("DELETE FROM contacts WHERE id = :id");
  // $statement->bindParam(":id", $id);
  // $statement->execute();

  // Forma Abreviada
  // $statement->execute([":id" => $id]);

  $contact = $statement->fetch(PDO::FETCH_ASSOC);

  if ($contact["user_id"] != $_SESSION["user"]["id"]) {
    http_response_code(401); echo("[x] HTTP 401 UNAUTHORIZED" . PHP_EOL); return;
  }

  $connection->prepare("DELETE FROM contacts WHERE id = :id")->execute([":id" => $id]);
  $_SESSION["flash"] = [
    "message" => "Contact {$contact['name']} Deleted",
    "type" => "danger" // Colour Red
  ];
  header("Location: ./home.php");
  return;
  
  # Validacion
  // curl -X GET http://172.17.0.2/contacts-app/delete.php?id=10

  // El query string: ?id=10 envía un parámetro llamado id con el valor 10 al script.
  // Un query string (cadena de consulta) es una parte de una URL que se utiliza para enviar datos adicionales al servidor como parámetros. Generalmente, contiene claves y valores en formato clave=valor, separados por el signo & si hay múltiples parámetros. El query string siempre va precedido por el signo ? en la URL.
  // Esta URL podría ser usada para realizar una búsqueda en el servidor. El servidor recibiría los parámetros producto=libro y categoria=ficcion, procesaría esta información, y devolvería resultados relacionados.
?>