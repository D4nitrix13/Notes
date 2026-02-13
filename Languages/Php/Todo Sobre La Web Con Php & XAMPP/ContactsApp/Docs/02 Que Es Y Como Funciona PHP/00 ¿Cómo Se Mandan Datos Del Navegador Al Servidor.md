<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# **¿Cómo Se Mandan Datos Del Navegador Al Servidor?**

- *Cuando un navegador envía datos al servidor, utiliza un proceso que sigue el protocolo HTTP (o HTTPS). Esto ocurre principalmente al interactuar con formularios web o realizar solicitudes a través de JavaScript. A continuación, se detalla el flujo:*

---

## **1. Navegador envía la solicitud**

- *Cuando se envían datos desde un formulario o por otros medios (como `fetch` o `XMLHttpRequest` en JavaScript), el navegador construye una **solicitud HTTP** que contiene los datos proporcionados por el usuario.*

- **Tipo de solicitud:** *Generalmente **POST** o **GET**.*
- **Destino:** *Se envían al servidor indicado en el atributo `action` del formulario o en la URL especificada por la solicitud.*
- **Datos:** *Se codifican y empaquetan en un formato específico.*

---

### **2. Datos en formato "Raw"**

- *El navegador convierte los datos ingresados en un formulario en un formato llamado **"raw"** (texto plano con una estructura específica). Por ejemplo:*

**Formulario HTML enviado:**

```html
<form method="post" action="https://example.com/submit">
    <input type="text" name="name" value="Daniel Benjamin Perez Morales">
    <input type="text" name="phone_number" value="123456789">
    <button type="submit">Enviar</button>
</form>
```

**Datos enviados (en formato raw):**

```bash
name=Daniel+Benjamin+Perez+Morales&phone_number=123456789
```

#### **Explicación del formato:**

- **`name` y `phone_number`:** *Son las claves o nombres de los campos del formulario.*
- **`Daniel+Benjamin+Perez+Morales` y `123456789`:** *Son los valores proporcionados por el usuario.*
- **`&`:** *Separa cada par clave-valor.*
- **`+`:** *Representa los espacios en los valores, ya que los espacios no son válidos en este formato.*
- **Codificación:** *Los caracteres especiales (como `&`, `=` o espacios) se codifican para evitar conflictos.*

---

### **3. Ejemplo de solicitud**

- **Cuando el navegador en*vía los datos, la solicitud HTTP podría verse así:**

#### **Solicitud POST:**

```bash
POST /contacts-app/edit.php HTTP/1.1
Host: 172.17.0.2
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:133.0) Gecko/20100101 Firefox/133.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://172.17.0.2/contacts-app/edit.php
Content-Type: application/x-www-form-urlencoded
Content-Length: 57
Origin: http://172.17.0.2
Connection: keep-alive
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
Priority: u=0, i
Pragma: no-cache
Cache-Control: no-cache
```

- **Encabezados HTTP:**
  - **`POST /submit HTTP/1.1`:** *Indica que se está enviando una solicitud al recurso `/submit` utilizando el método POST.*
  - **`Host: example.com`:** *Especifica el dominio del servidor.*
  - **`Content-Type: application/x-www-form-urlencoded`:** *Declara que los datos están codificados en formato URL.*
  - **`Content-Length: 65`:** *Indica el tamaño de los datos enviados en el cuerpo de la solicitud.*
- **Cuerpo de la solicitud:** *Contiene los datos enviados (formato raw).*

---

### **4. Procesamiento en el servidor**

- **El servidor recibe la solicitud y extrae los datos:**

- **PHP (ejemplo):**

  ```php
  <?php
      $name = $_POST['name']; // "Daniel Benjamin Perez Morales"
      $phone_number = $_POST['phone_number']; // "123456789"
      echo "Nombre: $name, Teléfono: $phone_number";
  ?>
  ```

- **Salida esperada:**

  ```bash
  Nombre: Daniel Benjamin Perez Morales, Teléfono: 123456789
  ```

---

### **5. Otras formas de enviar datos**

- **Además de los formularios clásicos, los datos también pueden enviarse mediante:**

- **AJAX (JavaScript):**

  ```javascript
  fetch("https://example.com/submit", {
      method: "POST",
      headers: {
          "Content-Type": "application/x-www-form-urlencoded"
      },
      body: "name=Daniel+Benjamin+Perez+Morales&phone_number=123456789"
  });
  ```

- **URL con GET (como parámetros):**

  ```bash
  https://example.com/submit?name=Daniel+Benjamin+Perez+Morales&phone_number=123456789
  ```

---

### **Resumen**

- *El navegador envía datos al servidor utilizando solicitudes HTTP, donde los datos se codifican en un formato específico como `application/x-www-form-urlencoded`. Este proceso incluye convertir el contenido del formulario en una cadena raw de pares clave-valor, que el servidor interpreta para realizar acciones específicas como almacenar información o procesar solicitudes del usuario.### **¿Cómo Se Mandan Datos Del Navegador Al Servidor?***
- *Cuando un navegador envía datos al servidor, utiliza un proceso que sigue el protocolo HTTP (o HTTPS). Esto ocurre principalmente al interactuar con formularios web o realizar solicitudes a través de JavaScript. A continuación, se detalla el flujo:*
