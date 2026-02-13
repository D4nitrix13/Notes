<!DOCTYPE html>
<html lang="en">

<!-- https://stackoverflow.com/questions/36877/how-do-you-set-up-use-httponly-cookies-in-php -->
<!-- https://stackoverflow.com/questions/1388210/php-using-a-drop-down-list-to-change-site-theme -->
<!-- https://www.php.net/manual/en/language.variables.superglobals.php -->

<!--
path="/":
La Cookie Será Enviada Por El Navegador En Todas Las Solicitudes Realizadas Al Servidor, Independientemente De La Ruta.

"Theme":
Es el nombre de la cookie. Esta es la clave que se utiliza para acceder al valor almacenado.

$_SERVER["Theme"]:
Es el valor que se desea guardar en la cookie. Se está obteniendo del array $_SERVER, que generalmente no es el lugar adecuado para almacenar valores personalizados. Para propósitos más convencionales, podrías usar una variable como $_POST["Theme"] o una variable de sesión.

time() + (60 * 60 * 24 * 30):
Es la fecha de expiración de la cookie.
  - time() devuelve el tiempo actual en segundos desde la época Unix (1 de enero de 1970).
  - 60 * 60 * 24 * 30 calcula 30 días en segundos (60 segundos × 60 minutos × 24 horas × 30 días).
  - Por lo tanto, la cookie expirará en 30 días desde el momento en que se creó.

Resultado:
  Una cookie llamada "Theme" será almacenada en el navegador del usuario con el valor de $_SERVER["Theme"] y expirará en 30 días.

¿Qué hace esta cookie?
  Permite que el servidor almacene el tema seleccionado (u otra preferencia) en el navegador del usuario.
  En solicitudes futuras, el navegador enviará automáticamente esta cookie al servidor, lo que permite personalizar la experiencia del usuario sin necesidad de que elija su tema nuevamente.

Uso del array de opciones (setcookie mejorado):
  PHP 7.3+ permite pasar un array como tercer argumento de setcookie. Esto mejora la legibilidad y la configuración de atributos avanzados como SameSite.

samesite:
  "Lax": La cookie se envía con solicitudes realizadas desde la misma página y con enlaces que llevan al mismo sitio (predeterminado).
  "None": Permite que la cookie se envíe en contextos de terceros, pero requiere secure=true. Úsalo si necesitas que la cookie sea accesible en iframes o sitios cruzados.

secure:
Es obligatorio si usas samesite="None". Asegúrate de usar HTTPS en tu servidor.

httponly:
Mejora la seguridad al evitar que la cookie sea accesible desde JavaScript.

path:
Indica que la cookie estará disponible para todas las rutas en el dominio.

Consideraciones:

Navegadores antiguos: Si estás trabajando con navegadores más antiguos que no soportan SameSite, las cookies sin este atributo pueden comportarse de forma inesperada. Para maximizar compatibilidad, considera establecer "samesite=Lax" como estándar.

HTTPS obligatorio: Si tu sitio no usa HTTPS, asegúrate de establecer "secure" como false. Sin embargo, para mayor seguridad, se recomienda implementar HTTPS.
-->

<!-- 
Borrar Una Cookie
Valor Vacío (""): Se Establece Un Valor Vacío Para Indicar Que La Cookie Se Eliminará.
Fecha De Expiración (time() - 3600): Se Establece Una Fecha De Expiración En El Pasado (1 Hora Antes De La Hora Actual). Esto Hará Que El Navegador Elimine La Cookie.
-->
<?php
  if (!isset($_COOKIE["Theme"])) {
    $_COOKIE["Theme"] = "flatly";
    setcookie(
      "Theme",
      $_COOKIE["Theme"],
      [
        "expires" => time() + (60 * 60 * 24 * 30),
        "path" => "/",
        // "secure" => true,         // Asegúrate de usar HTTPS si está activado
        "httponly" => true,       // Evita el acceso de JavaScript
        "samesite" => "Lax"       // O "None" si es necesario para contextos de terceros
      ]
    );
  }

  if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $_COOKIE["Theme"] = $_POST["Theme"];
    setcookie(
      "Theme",
      $_POST["Theme"],
      [
        "expires" => time() + (60 * 60 * 24 * 30),
        "path" => "/",
        // "secure" => true,
        "httponly" => true,
        "samesite" => "Lax"
      ]
    );
  }
?>

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible"
    content="IE=edge">
  <meta name="viewport"
    content="width=device-width, initial-scale=1.0">

  <!-- Link: https://bootswatch.com/ -->
  <!-- Github: https://github.com/thomaspark/bootswatch -->

  <!-- Bootstrap: Biblioteca CSS y JS para diseño y componentes frontend -->
  <!-- Bootswatch: Temas personalizados para Bootstrap -->
  <!-- Enlace a Bootswatch desde una CDN (cdnjs) -->
  <!-- https://cdnjs.com/libraries/bootswatch -->


  <!-- CDN (Content Delivery Network) Red De Distribución De Contenidos:

  Permite cargar recursos (como CSS o JavaScript) desde servidores distribuidos globalmente, mejorando la velocidad de carga y disponibilidad.

  Atributos adicionales en los enlaces:

  integrity: Proporciona una firma hash para garantizar la integridad del fichero descargado.
  crossorigin: Indica que el recurso proviene de otro dominio.
  referrerpolicy: Especifica cómo manejar la información de referencia (en este caso, no se envía información) 
  -->
  <?php if ($_COOKIE["Theme"] == "flatly"): ?>
    <!-- Theme Light -->
    <link data-Theme="flatly" class="theme" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.3/flatly/bootstrap.min.css" integrity="sha512-qoT4KwnRpAQ9uczPsw7GunsNmhRnYwSlE2KRCUPRQHSkDuLulCtDXuC2P/P6oqr3M5hoGagUG9pgHDPkD2zCDA==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <?php else: ?>
    <!-- Theme Dark -->
    <link data-Theme="darkly" class="theme" rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.3/darkly/bootstrap.min.css" integrity="sha512-HDszXqSUU0om4Yj5dZOUNmtwXGWDa5ppESlX98yzbBS+z+3HQ8a/7kcdI1dv+jKq+1V5b01eYurE7+yFjw6Rdg==" crossorigin="anonymous" referrerpolicy="no-referrer" />
  <?php endif ?>

  <!-- Bootstrap JavaScript Bundle (incluye Popper.js) -->
  <!-- Enlace a Bootstrap desde jsDelivr CDN -->
  <!-- https://www.bootstrapcdn.com/ -->

  <!-- El atributo defer en una etiqueta <script> es una instrucción al navegador que indica que el script debe ser descargado en segundo plano y ejecutado solo después de que el documento HTML haya sido completamente analizado (parsing). Es útil para mejorar el rendimiento de carga de las páginas. -->
  <script defer
    src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"
    integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz"
    crossorigin="anonymous"></script>

  <!-- Static Content -->
  <link rel="stylesheet"
    href="./static/css/index.css">

  <!-- <script defer src="./static/js/changesTheme.js"></script> -->
  
  
  
  <!-- La diferencia entre **URL** (Uniform Resource Locator) y **URI** (Uniform Resource Identifier) es una cuestión de especificidad.

  - **URL (Localizador Uniforme de Recursos):** Es un tipo específico de URI que no solo identifica un recurso, sino que también proporciona la forma de localizarlo en internet. Incluye el protocolo (por ejemplo, HTTP, FTP) y la dirección del recurso (por ejemplo, `www.ejemplo.com`).

  - **URI (Identificador Uniforme de Recursos):** Es un término más amplio que hace referencia a cualquier cadena de caracteres que identifica de manera única un recurso. Un URI puede ser una URL o un URN (Nombre Uniforme de Recurso). Un URI no especifica necesariamente cómo localizar el recurso, a diferencia de una URL.

  En resumen:
  - **URL** es un tipo específico de **URI** que incluye detalles para localizar un recurso.
  - **URI** es un término más amplio que incluye tanto URLs como otros tipos de identificadores, como los URNs.
  -->

  <?php $uri = parse_url($_SERVER["REQUEST_URI"], PHP_URL_PATH) ?>
  <?php if ($uri == "/contacts-app/" || $uri == "/contacts-app/index.php"): ?>
    <script defer src="./static/js/welcome.js"></script>
  <?php endif ?>

  <title>Contacts App</title>
</head>

<body>
  <?php require "./partials/navbar.php"?>
  <!-- Link: https://getbootstrap.com/docs/5.3/components/alerts/#examples -->
  <?php if (isset($_SESSION["flash"])): ?>
    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
      <symbol id="check-circle-fill" fill="currentColor" viewBox="0 0 16 16">
        <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zm-3.97-3.03a.75.75 0 0 0-1.08.022L7.477 9.417 5.384 7.323a.75.75 0 0 0-1.06 1.06L6.97 11.03a.75.75 0 0 0 1.079-.02l3.992-4.99a.75.75 0 0 0-.01-1.05z"/>
      </symbol>
    </svg>

    <div class="container mt-4">
      <div class="alert alert-<?=$_SESSION["flash"]["type"]?> d-flex align-items-center" role="alert">
        <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Success:"><use xlink:href="#check-circle-fill"/></svg>
        <div class="ml-2">
          <?= $_SESSION["flash"]["message"] ?>
        </div>
      </div>
    </div>
    <?php unset($_SESSION["flash"]) ?>
  <?php endif ?>
  <main>
<!-- Content Here -->