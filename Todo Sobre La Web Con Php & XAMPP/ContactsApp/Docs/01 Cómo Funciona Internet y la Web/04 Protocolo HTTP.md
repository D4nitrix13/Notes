
# **Qué sucede cuando hacemos una petición HTTP**

- *Por defecto, el **puerto 80** es el estándar utilizado por el protocolo **HTTP**. Esto significa que, a menos que se especifique un puerto diferente, los navegadores intentarán conectarse al servidor web a través del puerto 80. Sin embargo, cualquier puerto puede ser configurado para servir contenido HTTP si el servidor lo permite, pero usar el puerto 80 se considera una convención ampliamente aceptada.*

- *Al realizar una petición desde un navegador, podemos inspeccionar las cabeceras de la solicitud en las herramientas de desarrollo del navegador (generalmente en la pestaña de "Red"). Una cabecera típica para una solicitud HTTP podría verse así:*

```bash
GET /contacts-app/index.html HTTP/1.1
Host: 172.17.0.2
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://172.17.0.2/contacts-app/add.html
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```

---

## **Detalles técnicos: cómo viaja la solicitud**

1. **Paquete IP**  
   - *La solicitud HTTP viaja encapsulada dentro de un paquete **IP**. Este paquete contiene:*
   - **IP de origen:** *La dirección IP del cliente que envía la solicitud (ejemplo: `192.168.1.17`).*
   - **IP de destino:** *La dirección IP del servidor que recibe la solicitud (ejemplo: `172.17.0.2`).*

2. **Paquete TCP**  
   *Dentro del paquete IP hay un **paquete TCP** que incluye:*
   - **Puerto de origen:** *Un puerto aleatorio asignado por el sistema operativo del cliente (por ejemplo: `47500`).*
     - *Los navegadores asignan un puerto dinámico para cada nueva conexión.*
   - **Puerto de destino:** *El puerto del servidor al que se dirige la solicitud. Para HTTP, este es generalmente el puerto `80`.*

3. **Datos de la solicitud HTTP**  
   - *Finalmente, dentro del paquete TCP, se encuentra la solicitud HTTP propiamente dicha. Por ejemplo:*

   ```bash
   GET /contacts-app/index.html HTTP/1.1
   Host: 172.17.0.2
   ```

---

### **¿El navegador tiene una máquina virtual para ejecutar JavaScript?**

- *¡Sí! Los navegadores modernos incluyen un motor de JavaScript que funciona como una máquina virtual optimizada. Este motor se encarga de interpretar, compilar y ejecutar el código JavaScript en tiempo real.*

- **Algunos ejemplos de motores de JavaScript son:**

- **V8:** *Usado en Chrome y Edge.*
- **SpiderMonkey:** *Usado en Firefox.*
- **JavaScriptCore (Nitro):** *Usado en Safari.*

- *El propósito de esta máquina virtual es proporcionar un entorno seguro y eficiente para que los scripts puedan interactuar con el DOM (Modelo de Objetos del Documento), gestionar eventos, realizar solicitudes HTTP asincrónicas y manipular contenido en la página web.*

- *Por lo tanto, cuando el navegador recibe una respuesta que incluye JavaScript, su motor lo ejecuta en este entorno virtual, permitiendo la interacción dinámica de la página.*

```bash
curl http://172.17.0.2:80/contacts-app/index.html
```

```html
<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible"
    content="IE=edge">
  <meta name="viewport"
    content="width=device-width, initial-scale=1.0">

  <!-- Bootstrap: Biblioteca CSS y JS para diseño y componentes frontend -->
  <!-- Bootswatch: Temas personalizados para Bootstrap -->
  <!-- Enlace a Bootswatch desde una CDN (cdnjs) -->
  <!-- https://cdnjs.com/libraries/bootswatch -->


  <!-- CDN (Content Delivery Network):

  Permite cargar recursos (como CSS o JavaScript) desde servidores distribuidos globalmente, mejorando la velocidad de carga y disponibilidad.

  Atributos adicionales en los enlaces:

  integrity: Proporciona una firma hash para garantizar la integridad del fichero descargado.
  crossorigin: Indica que el recurso proviene de otro dominio.
  referrerpolicy: Especifica cómo manejar la información de referencia (en este caso, no se envía información)
  -->

  <link rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/bootswatch/5.3.3/darkly/bootstrap.min.css"
    integrity="sha512-HDszXqSUU0om4Yj5dZOUNmtwXGWDa5ppESlX98yzbBS+z+3HQ8a/7kcdI1dv+jKq+1V5b01eYurE7+yFjw6Rdg=="
    crossorigin="anonymous"
    referrerpolicy="no-referrer" />

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

  <title>Contacts App</title>
</head>

<body>
  <nav class="navbar bg-dark navbar-expand-lg bg-body-tertiary"
    data-bs-theme="dark">
    <div class="container-fluid">
      <a class="navbar-brand"
        href="#">
        <img src="./static/img/logo.png"
          alt="Logo Aplication">
        ContactApp
      </a>
      <button class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse"
        id="navbarSupportedContent">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active"
              aria-current="page"
              href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link"
              href="./add.html">Add Contact</a>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <main>
    <div class="container pt-4 p-3">
      <div class="row">
        <div class="col-md-4 mb-3">
          <div class="card text-center">
            <div class="card-body">
              <h3 class="card-title text-capitalize">Contact Name 1</h3>
              <p class="m-2">987654321</p>
              <a href="#"
                class="btn btn-secondary mb-2">Edit Contact</a>
              <a href="#"
                class="btn btn-danger mb-2">Delete Contact</a>
            </div>
          </div>
        </div>

        <div class="col-md-4 mb-3">
          <div class="card text-center">
            <div class="card-body">
              <h3 class="card-title text-capitalize">Contact Name 2</h3>
              <p class="m-2">987654321</p>
              <a href="#"
                class="btn btn-secondary mb-2">Edit Contact</a>
              <a href="#"
                class="btn btn-danger mb-2">Delete Contact</a>
            </div>
          </div>
        </div>

        <div class="col-md-4 mb-3">
          <div class="card text-center">
            <div class="card-body">
              <h3 class="card-title text-capitalize">Contact Name 3</h3>
              <p class="m-2">987654321</p>
              <a href="#"
                class="btn btn-secondary mb-2">Edit Contact</a>
              <a href="#"
                class="btn btn-danger mb-2">Delete Contact</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</body>
```

- *![PeticionNavegador](/Images/PeticionNavegador.png "/Images/PeticionNavegador.png")*
