<?php 

// Reanudamos la sesión existente para acceder a sus datos
session_start(); 

// Destruimos todos los datos de la sesión y eliminamos el fichero asociado
session_destroy(); 

// Redirigimos al usuario a la página de inicio, invalidando cualquier intento de autenticación
header("Location: ./index.php"); 


?>