<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Conceptos de la Web con PHP sin Dependencias usando XAMPP***

- *Este proyecto tiene como objetivo demostrar los conceptos fundamentales de la web utilizando PHP, sin depender de bibliotecas externas. Utilizaremos XAMPP como servidor local, lo que nos permitirá gestionar servidores, bases de datos y protocolos HTTP de manera eficiente.*

## ***Requisitos***

- **XAMPP:** *Un paquete que incluye Apache (servidor web), MySQL (base de datos), y PHP.*
- **Conocimientos básicos de HTML, PHP, y SQL.**

## ***Estructura Básica del Proyecto***

- **`index.php`:** *Fichero principal que maneja las solicitudes HTTP y genera respuestas dinámicas.*
- **Base de Datos:** *Usaremos MySQL, que está integrado en XAMPP, para almacenar y recuperar información.*
- **Configuración del servidor:** *Apache se utilizará para servir el contenido web a través de HTTP.*

## ***Conceptos Fundamentales***

### ***1. Protocolos Web***

- *El protocolo principal utilizado en la web es **HTTP** (Hypertext Transfer Protocol). Cuando un usuario realiza una solicitud en el navegador, el servidor web Apache recibe la solicitud y responde con contenido, generalmente en formato HTML, CSS o JavaScript.*

### ***2. Servidor Web***

- *El servidor web **Apache** en XAMPP maneja las solicitudes HTTP y ejecuta ficheros PHP para generar contenido dinámico. Apache sirve los ficheros desde el directorio `htdocs` y puede gestionar varias solicitudes simultáneamente.*

### ***3. Base de Datos***

En este ejemplo, usaremos **MySQL** para manejar bases de datos. XAMPP incluye phpMyAdmin, una interfaz web que facilita la gestión de bases de datos MySQL.

### ***4. PHP Sin Dependencias***

- *Para trabajar con PHP sin dependencias externas, basta con usar las funciones nativas del lenguaje para interactuar con la base de datos, manejar formularios y generar contenido dinámico.*

### ***5. Flujo de Datos***

- *Cuando un usuario envía una solicitud (por ejemplo, un formulario), el servidor Apache procesa la solicitud y ejecuta el script PHP correspondiente. Si el script necesita datos, puede obtenerlos de la base de datos MySQL. El servidor luego genera una respuesta (en formato HTML, JSON, etc.) que se envía al navegador del usuario.*

### ***6. PHP y HTTP***

- *El lenguaje PHP se ejecuta en el servidor y genera respuestas dinámicas basadas en las solicitudes HTTP del cliente. En este caso, el servidor Apache procesa las solicitudes y ejecuta el código PHP, lo que permite mostrar contenido personalizado según la interacción del usuario.*

## ***Conclusión***

- *Este proyecto proporciona una introducción básica a los conceptos fundamentales de la web: protocolos HTTP, servidores, y bases de datos. Usando XAMPP y PHP, puedes crear aplicaciones web dinámicas sin depender de bibliotecas adicionales, lo que te permite comprender cómo funcionan los componentes de la web a nivel fundamental.*
