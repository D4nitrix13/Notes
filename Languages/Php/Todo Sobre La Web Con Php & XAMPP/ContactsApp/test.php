<?php

// Este es el delimitador de apertura estándar de PHP.
// Todo el código que sigue se interpreta como PHP hasta que se encuentra el delimitador de cierre "?>".

# Este es un ejemplo básico en PHP que utiliza arrays y estructuras de control.

// Array llamado $contacts que contiene una lista de nombres.
$contacts = ["Daniel", "Benjamin", "Danna", "Isabella", "Matias"];

// Este bloque de código está comentado, pero ilustra cómo recorrer el array.
// foreach ($contacts as $i) {
//     # Dentro del bucle, $i toma el valor de cada elemento del array $contacts.
//     # Se interpreta dentro de comillas dobles. En comillas simples, no ocurre la interpretación.
//     # El operador . se usa para concatenar cadenas.
//     # PHP_EOL representa un salto de línea para la salida en consola o ficheros.
//     print("<div>$i</div>" . PHP_EOL); // Genera una etiqueta <div> con el nombre actual.
// }

# El siguiente bloque HTML muestra dinámicamente los contactos excepto "Daniel".
?>
<?php foreach ($contacts as $i) { ?> 
    <?php if ($i != "Daniel") { ?> 
        <!-- Si el contacto actual no es "Daniel", genera un div con el nombre -->
        <div><?= $i ?></div>
    <?php } ?>
<?php } ?>

<?php 
# Otra forma de hacer lo mismo, pero con sintaxis de PHP completa.
foreach ($contacts as $i) {
    if ($i != "Daniel") {
        # echo imprime el div con el contacto y añade un salto de línea usando PHP_EOL.
        echo("<div>$i</div>". PHP_EOL);
    }
}
?>

<!-- Fuera de los delimitadores, todo se trata como HTML estático. -->
 
<!-- # **¿Qué es CGI?**

- **Interfaz de Puerta de Enlace Común** **Common Gateway Interface (CGI) ** es un protocolo que define cómo un servidor web interactúa con aplicaciones externas, llamadas **scripts CGI**.
- Estos scripts pueden estar escritos en lenguajes como Python, Perl, Ruby, PHP o incluso C.
- Los scripts CGI se ejecutan en el servidor y generan contenido dinámico que se envía de vuelta al navegador del usuario.

---

## **¿Cómo funciona CGI?**

1. **Solicitud del cliente:**  
   Cuando un usuario accede a una URL que invoca un script CGI, el servidor recibe la solicitud HTTP y detecta que debe ejecutar un programa en lugar de simplemente enviar un fichero.

2. **Ejecución del script:**  
   El servidor web ejecuta el script CGI especificado y le pasa la información de la solicitud como variables de entorno. Por ejemplo:  
   - Datos del formulario enviados por el usuario.  
   - Parámetros de consulta en la URL.  

3. **Respuesta generada por el script:**  
   El script CGI genera una respuesta (generalmente en formato HTML) y la envía de vuelta al servidor.

4. **Respuesta al cliente:**  
   El servidor envía la salida generada al navegador del cliente.

---

### **Ventajas de CGI:**
1. Es compatible con cualquier lenguaje que pueda ejecutarse en el servidor.  
2. Permite la generación de contenido dinámico.  
3. Fue uno de los primeros métodos utilizados para crear aplicaciones web.

---

### **Desventajas de CGI:**
1. **Poco eficiente:** Cada solicitud al script inicia un nuevo proceso en el servidor, lo que puede ser costoso en términos de recursos.  
2. **Obsoleto:** Métodos más modernos, como FastCGI, mod_php, o aplicaciones basadas en frameworks como Django o Node.js, son mucho más eficientes.  
3. **Problemas de seguridad:** Los scripts CGI pueden ser vulnerables si no se manejan adecuadamente los datos de entrada.

En resumen, aunque CGI fue fundamental en los inicios del desarrollo web, actualmente es poco utilizado debido a sus limitaciones. Sin embargo, sigue siendo importante entenderlo desde un punto de vista histórico y académico. -->

<pre>
<?php 
  var_dump($_SERVER);
  die();
?>

<!-- 
</pre>
<pre>

Es una etiqueta HTML que mantiene el formato de texto preformateado, incluyendo saltos de línea y espacios en blanco.
Ayuda a que la salida de var_dump se vea más clara y legible en el navegador, ya que muestra el contenido tal cual, sin aplicarle estilos o formateos adicionales.

var_dump($_SERVER);

La función var_dump muestra el tipo de datos, la estructura y los valores de la variable proporcionada.
En este caso, $_SERVER es una superglobal de PHP que contiene información sobre el entorno del servidor y la solicitud HTTP, como:
    La URL solicitada.
    El método HTTP utilizado (GET, POST, etc.).
    La dirección IP del cliente.
    Detalles del software del servidor.
Esta función es útil para depurar y entender qué información está disponible en el entorno del servidor.

die();

La función die() detiene inmediatamente la ejecución del script.
Se usa aquí para evitar que se ejecute cualquier código adicional después de mostrar el contenido de $_SERVER. 
-->


<!-- array(34) {
  ["UNIQUE_ID"]=>
  string(27) "Z19NAmao8GyaT7u_zSXrRgAAAAE"
  ["HTTP_HOST"]=>
  string(10) "172.17.0.2"
  ["HTTP_USER_AGENT"]=>
  string(78) "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0"
  ["HTTP_ACCEPT"]=>
  string(63) "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
  ["HTTP_ACCEPT_LANGUAGE"]=>
  string(35) "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
  ["HTTP_ACCEPT_ENCODING"]=>
  string(13) "gzip, deflate"
  ["HTTP_CONNECTION"]=>
  string(10) "keep-alive"
  ["HTTP_UPGRADE_INSECURE_REQUESTS"]=>
  string(1) "1"
  ["HTTP_SEC_GPC"]=>
  string(1) "1"
  ["HTTP_PRIORITY"]=>
  string(6) "u=0, i"
  ["PATH"]=>
  string(70) "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"
  ["LD_LIBRARY_PATH"]=>
  string(29) "/opt/lampp/lib:/opt/lampp/lib"
  ["SERVER_SIGNATURE"]=>
  string(0) ""
  ["SERVER_SOFTWARE"]=>
  string(75) "Apache/2.4.58 (Unix) OpenSSL/1.1.1w PHP/8.2.12 mod_perl/2.0.12 Perl/v5.34.1"
  ["SERVER_NAME"]=>
  string(10) "172.17.0.2"
  ["SERVER_ADDR"]=>
  string(10) "172.17.0.2"
  ["SERVER_PORT"]=>
  string(2) "80"
  ["REMOTE_ADDR"]=>
  string(10) "172.17.0.1"
  ["DOCUMENT_ROOT"]=>
  string(17) "/opt/lampp/htdocs"
  ["REQUEST_SCHEME"]=>
  string(4) "http"
  ["CONTEXT_PREFIX"]=>
  string(0) ""
  ["CONTEXT_DOCUMENT_ROOT"]=>
  string(17) "/opt/lampp/htdocs"
  ["SERVER_ADMIN"]=>
  string(15) "you@example.com"
  ["SCRIPT_FILENAME"]=>
  string(38) "/opt/lampp/htdocs/contacts-app/add.php"
  ["REMOTE_PORT"]=>
  string(5) "48602"
  ["GATEWAY_INTERFACE"]=>
  string(7) "CGI/1.1"
  ["SERVER_PROTOCOL"]=>
  string(8) "HTTP/1.1"
  ["REQUEST_METHOD"]=>
  string(3) "GET"
  ["QUERY_STRING"]=>
  string(0) ""
  ["REQUEST_URI"]=>
  string(21) "/contacts-app/add.php"
  ["SCRIPT_NAME"]=>
  string(21) "/contacts-app/add.php"
  ["PHP_SELF"]=>
  string(21) "/contacts-app/add.php"
  ["REQUEST_TIME_FLOAT"]=>
  float(1734298882.5643520355224609375)
  ["REQUEST_TIME"]=>
  int(1734298882)
} -->


<?php
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    var_dump($_POST);
    die();
  }
?>

<!-- 
array(2) { ["name"]=> string(29) "Daniel Benjamin Perez Morales" ["phone_number"]=> string(9) "123456789" } 
-->

<?php
  if ($_SERVER["REQUEST_METHOD"] == "POST") {
    var_dump($_POST);
    die();
  }
?>