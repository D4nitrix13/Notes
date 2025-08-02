<?php 

$HOST = "localhost";
$DATABASE = "ContactsApp";
$USER = "root";
$PASSWORD = "";

try {
    $connection = new PDO("mysql:host=$HOST;dbname=$DATABASE", $USER, $PASSWORD);
    // foreach ($connection->query("SHOW DATABASES") as $row) {
    //     print_r($row);
    // }
    // die();
} catch (PDOException $e) {
    die("[x] PDO Connection Error: " . $e->getMessage() . PHP_EOL);
}
?>