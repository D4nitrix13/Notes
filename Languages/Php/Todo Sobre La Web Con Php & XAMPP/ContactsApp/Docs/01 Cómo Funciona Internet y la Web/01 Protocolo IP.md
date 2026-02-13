<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Protocolo IP (Internet Protocol)***

> [!IMPORTANT]
> *El **Protocolo IP** (Internet Protocol) es uno de los fundamentos de las redes modernas. Su propósito principal es permitir la comunicación entre dispositivos a través de redes interconectadas, como Internet. Cada dispositivo que participa en esta comunicación tiene una dirección IP única que lo identifica.*

---

## ***Conexión entre Cliente y Servidor***

> [!IMPORTANT]
> *La conexión entre un cliente (como tu computadora) y un servidor (como Google) no es directa. No existe un único cable que los conecte directamente; en cambio, el paquete de datos pasa por varios puntos intermedios, llamados **routers**. Aquí está el flujo típico de una conexión:*

1. **Tu casa:**  
   - *Te conectas a Internet a través de un router, ya sea por conexión cableada o inalámbrica.*
   - *Este router tiene un cable que sale hacia el exterior y conecta con otro router de tu proveedor de servicios de Internet (ISP).*

2. **Red del proveedor de servicios (ISP):**  
   - *El ISP tiene una red compleja de routers que se extiende por el país y, en algunos casos, incluso a otros países.*
   - *Cada router en esta red tiene una tabla de enrutamiento que decide el siguiente paso para que tu paquete llegue a su destino.*

3. **Destino final (Servidor):**  
   - *Una vez que el paquete llega al servidor (por ejemplo, Google), el sistema operativo del servidor analiza el paquete, identifica el puerto de destino (como el puerto 80 para HTTP) y entrega la petición al programa que atiende las solicitudes en ese puerto.*

*Ejemplo visual:*  

- *![Red Proveedor](/Images/RedProvedor.png "/Images/RedProvedor.png")*
- *![Paquete Destino](/Images/PaqueteDestino.png "/Images/PaqueteDestino.png")*

---

### ***¿Qué sucede al llegar al servidor?***

1. *El servidor recibe el paquete y lo analiza.*
2. *Identifica que debe ser procesado por el puerto especificado en la solicitud (por ejemplo, **80** para HTTP).*
3. *El programa encargado del puerto procesa la petición y genera una respuesta.*
4. *Esa respuesta se envía de vuelta al cliente a través de la misma red (inversamente).*

*Ejemplo visual:*  

- *![Petición Protocolo IP](/Images/PeticionProtocoloIP.png "/Images/PeticionProtocoloIP.png")*
- *![Respuesta Protocolo IP](/Images/RespuestaProtocoloIP.png "/Images/RespuestaProtocoloIP.png")*

---

### ***Detalles sobre el Protocolo IP***

1. **Dirección IP:**  
   - *Una dirección única que identifica a un dispositivo en la red.*
   - *Ejemplo: `192.168.1.1` (IPv4) o `2001:0db8:85a3:0000:0000:8a2e:0370:7334` (IPv6).*

2. **Enrutamiento:**  
   - *Cada router en la red tiene una **tabla de enrutamiento**.*
   - *Esta tabla le indica al router hacia dónde enviar los paquetes según la dirección IP de destino.*

3. **Formato del paquete IP:**  
   - **Contiene información como:**
     - *Dirección IP de origen.*
     - *Dirección IP de destino.*
     - *Datos adicionales para asegurar la entrega correcta.*

---

### ***Resumen***

> *El Protocolo IP permite que los datos viajen de forma eficiente desde el cliente hasta el servidor, pasando por una serie de routers intermedios que determinan la mejor ruta. Gracias a este sistema, es posible conectar millones de dispositivos en todo el mundo de manera simultánea.*

### **Enrutamiento: Qué es y cómo funciona**

- *El **enrutamiento** es el proceso mediante el cual los datos, en forma de paquetes, viajan desde un dispositivo de origen (como tu computadora) hasta un dispositivo de destino (como un servidor web) a través de una red. Esto se logra utilizando una serie de dispositivos llamados **routers**, que toman decisiones sobre la mejor ruta para enviar los datos hacia su destino.*

---

### **Cómo funciona el enrutamiento**

1. **Paquetes de datos:**  
   - *Cuando envías información (por ejemplo, una solicitud para cargar una página web), esta se divide en pequeños bloques llamados **paquetes**. Cada paquete contiene:*
   - *La dirección IP de origen (tu dispositivo).*
   - *La dirección IP de destino (el servidor).*
   - *Información para que los datos puedan ser reconstruidos correctamente.*

2. **Los routers y las tablas de enrutamiento:**  
   - *Un **router** es un dispositivo que conecta diferentes redes y decide hacia dónde enviar los paquetes.*
   - *Para tomar estas decisiones, cada router tiene una **tabla de enrutamiento**, que es una lista de rutas posibles hacia diferentes destinos.*

3. **Proceso de enrutamiento:**  
   - *Cuando un paquete llega a un router, el router analiza la dirección IP de destino y consulta su tabla de enrutamiento.*
   - *Basándose en esta tabla, elige el siguiente salto (el próximo router o dispositivo) al que enviará el paquete.*
   - *Este proceso se repite hasta que el paquete alcanza su destino final.*

---

### **Ejemplo de enrutamiento**

- *Imagina que estás en tu casa y quieres acceder a `google.com`. El proceso sería algo así:*

1. **Inicio del viaje:**  
   - *Tu computadora envía el paquete al router de tu casa. Este router no sabe directamente dónde está el servidor de Google, pero sabe que debe enviarlo al siguiente router del proveedor de Internet.*

2. **Red del ISP:**  
   - *El router de tu proveedor analiza la dirección de destino y lo envía al siguiente router dentro de su red, que puede estar más cerca del servidor de Google.*

3. **Interconexión de redes:**  
   - *Si el servidor de Google está en otro país, el paquete puede pasar por varias redes interconectadas a través de routers internacionales hasta llegar a la red de Google.*

4. **Destino final:**  
   - *Una vez en la red de Google, los routers locales entregan el paquete al servidor específico que tiene la información solicitada.*

---

### **Tipos de enrutamiento**

1. **Enrutamiento estático:**  
   - *Las rutas son configuradas manualmente por un administrador.*
   - *Adecuado para redes pequeñas con pocas conexiones.*

2. **Enrutamiento dinámico:**  
   - *Los routers se comunican entre sí utilizando **protocolos de enrutamiento** (como RIP, OSPF o BGP) para descubrir y actualizar rutas automáticamente.*
   - *Es más eficiente para redes grandes o dinámicas.*

---

### **Factores clave en el enrutamiento**

1. **Latencia:**  
   - *Tiempo que tarda un paquete en llegar a su destino. Los routers buscan minimizar este tiempo.*

2. **Coste de la ruta:**  
   - *Algunos protocolos consideran factores como la cantidad de saltos o la calidad del enlace al elegir la mejor ruta.*

3. **Redundancia:**  
   - *Los routers mantienen rutas alternativas para asegurar la entrega de paquetes si una ruta falla.*

---

### **Importancia del enrutamiento**

- *El enrutamiento es esencial para que Internet funcione. Permite que los datos lleguen correctamente incluso cuando las redes son complejas y dinámicas. Sin enrutamiento, los dispositivos no podrían comunicarse fuera de su red local.*
