<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Servidores Web y Apache***

- *Un **servidor web** es un software diseñado para manejar solicitudes de clientes, generalmente navegadores, y enviarles respuestas en forma de páginas web, imágenes u otros contenidos. Apache es uno de los servidores web más populares, usado ampliamente en todo el mundo.*

## ***Ejemplo de una URL en un servidor web***

- *`http://142.250.200.142:80`:*
  - *Una dirección IP con un puerto especificado explícitamente (`80`). Aquí, el cliente accede al servidor usando el **protocolo HTTP** en el puerto 80.*

- *`google.com`:*
  - *Un dominio que apunta a una dirección IP, haciendo más fácil para los usuarios acceder a servidores web. Los dominios son traducidos a direcciones IP mediante el **sistema DNS** (Domain Name System).*

---

## ***Dominios***

> [!NOTE]
> *Un **dominio** es el nombre que se utiliza para identificar una dirección IP en Internet de forma amigable. Por ejemplo:*

- *`google.com` es el dominio, mientras que su IP podría ser `142.250.200.142`.*
- *Los dominios se gestionan mediante registros DNS, que asocian nombres legibles por humanos con direcciones IP.*

---

## ***Protocolo HTTP y HTTPS***

### **HTTP (Hypertext Transfer Protocol):**

- *Es el protocolo estándar para transferir datos a través de la web.*
- *Usa el puerto **80** por defecto.*
- *La información enviada no está cifrada, lo que significa que es menos segura.*

### **HTTPS (Hypertext Transfer Protocol Secure):**

- *Es la versión segura de HTTP, que usa cifrado para proteger los datos transmitidos.*
- *Utiliza el puerto **443** por defecto.*
- *Requiere un certificado SSL/TLS para establecer una conexión cifrada entre el cliente y el servidor.*

---

## ***Puertos en servidores***

- Los **puertos** *son puntos de conexión que permiten que los servicios en una máquina sean accesibles desde Internet o una red local.*
- El rango de puertos posibles va de **0 a 65535** *(2¹⁶ combinaciones, ya que un puerto es un número de 16 bits). Sin embargo, los **puertos reservados** (0-1023) están destinados a servicios bien conocidos, como:*
  - **80:** *HTTP.*
  - **443:***HTTPS.*
  - **21:** *FTP.*
  - **22:** *SSH.*

*![WebPeticionServidor](/Images/WebPeticionServidor.png "/Images/WebPeticionServidor.png")*
*![WebRespuestaServidor](/Images/WebRespuestaServidor.png "/Images/WebRespuestaServidor.png")*
*![PuertosOrdenadores](/Images/PuertosOrdenadores.png "/Images/PuertosOrdenadores.png")*
*![ServidorApache](/Images/ServidorApache.png "/Images/ServidorApache.png")*
