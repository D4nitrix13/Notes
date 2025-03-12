<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# **Protocolo TCP (Transmission Control Protocol)**

- *El **TCP (Transmission Control Protocol)** es uno de los principales protocolos utilizados en la comunicación de redes, especialmente en Internet. Su propósito es garantizar que los datos se transmitan de forma **fiable**, **ordenada** y sin errores entre dos programas, que pueden estar en máquinas diferentes.*

---

## **Problemas que resuelve TCP**

- *En una red por naturaleza insegura, como Internet, pueden ocurrir problemas que dificultan la transmisión de datos. TCP aborda los siguientes desafíos:*

1. **Pérdida de paquetes:**  
   - *Los paquetes de datos pueden perderse si un router falla o si hay interrupciones en la red.*
   - *TCP detecta esta pérdida y retransmite los paquetes necesarios.*

2. **Orden de los paquetes:**  
   - *Los paquetes pueden llegar desordenados porque toman diferentes rutas a través de la red.*
   - *TCP asigna números de secuencia a los paquetes para reordenarlos correctamente en el destino.*

3. **Integridad de los datos:**  
   - *Los datos pueden dañarse durante la transmisión debido a problemas en los cables o interferencias.*
   - *TCP utiliza un **checksum** para verificar si los datos están corruptos. Si lo están, solicita su retransmisión.*

4. **Control de flujo:**  
   - *Si el receptor tiene poca memoria disponible, TCP ajusta la cantidad de datos enviados para evitar sobrecargas.*
   - *Esto se logra mediante un mecanismo que establece un límite en el número de paquetes que se pueden enviar sin recibir confirmación.*

---

### **Cómo funciona TCP**

1. **Establecimiento de conexión (Three-Way Handshake):**  
   *TCP utiliza un proceso de negociación de tres pasos para establecer una conexión fiable entre cliente y servidor:*
   - **SYN:** *El cliente envía una solicitud para iniciar la conexión.*
   - **SYN-ACK:** *El servidor confirma la solicitud y solicita la confirmación del cliente.*
   - **ACK:** *El cliente responde y la conexión queda establecida.*

2. **Transmisión de datos:**  
   - *Los datos se dividen en paquetes, que incluyen información clave como:*
     - **Puerto de origen y puerto de destino.**  
     - **Número de secuencia.**  
     - **Checksum** *para verificar errores.*
   - *Los paquetes viajan encapsulados en paquetes IP, que contienen las direcciones IP de origen y destino.*

3. **Recepción y confirmación:**  
   - *El receptor verifica los datos utilizando el **checksum** y reordena los paquetes según sus números de secuencia.*
   - *Cuando un paquete se recibe correctamente, el receptor envía una **confirmación (ACK)**. Si no se recibe una confirmación, TCP retransmite el paquete.*

4. **Cierre de conexión:**  
   - *Una vez que se han transferido todos los datos, TCP finaliza la conexión mediante un proceso llamado **four-way handshake**, asegurándose de que ambas partes hayan terminado de enviar datos.*

---

### **Ventajas del TCP**

1. **Fiabilidad:**  
   *TCP asegura que los datos lleguen correctamente al destino, incluso si hay múltiples saltos o problemas en la red.*

2. **Control de errores:**  
   *Detecta y corrige errores en la transmisión.*

3. **Ordenación de datos:**  
   *Reordena los paquetes desordenados para garantizar que los datos se reconstruyan correctamente.*

4. **Adaptabilidad:**  
   *TCP ajusta dinámicamente la cantidad de datos enviados según las capacidades del receptor y las condiciones de la red.*

---

### **Ejemplo práctico de TCP**

- *Imagina que tienes un programa cliente y un programa servidor que desean comunicarse:*

1. **Configuración inicial:**  
   - *El cliente abre el puerto 5001, y el servidor escucha en el puerto 5000.*
   - *La conexión se establece utilizando el proceso de handshake.*

2. **Transmisión de datos:**  
   - *El cliente envía la cadena `"Mi Nombre Es Daniel"` al servidor.*
   - *TCP divide esta cadena en varios paquetes, los numera y los envía encapsulados en paquetes IP.*
   - *Cada paquete incluye:*
     - *Dirección IP de origen y destino (nivel de red).*
     - *Puerto de origen (5001) y puerto de destino (5000) (nivel de transporte).*

3. **Recepción:**  
   - *En el servidor, TCP verifica la integridad de los paquetes y los reordena si llegaron desordenados.*
   - *Luego, los datos se entregan al programa que escucha en el puerto 5000.*

4. **Cierre:**  
   - *Una vez finalizada la comunicación, ambas partes cierran la conexión de manera controlada.*

---

### **Relación con el modelo OSI**

- *TCP opera en la **Capa de Transporte** del modelo OSI, proporcionando servicios a las capas superiores (como la **Capa de Aplicación**, donde se ejecutan programas como navegadores web) y utilizando servicios de las capas inferiores (como la **Capa de Red**, que utiliza el protocolo IP).*

---

### **Diferencia entre TCP y UDP**

| *Característica* | *TCP*                                     | *UDP*                                              |
| ---------------- | ----------------------------------------- | -------------------------------------------------- |
| **Fiabilidad**   | *Sí (retransmisión y ordenación).*        | *No (no garantiza entrega ni orden).*              |
| **Velocidad**    | *Más lento debido al control de errores.* | *Más rápido por menor sobrecarga.*                 |
| **Uso**          | *Aplicaciones críticas (HTTP, correo).*   | *Aplicaciones en tiempo real (streaming, juegos).* |

---

### **Conclusión**

- *TCP es fundamental para garantizar una comunicación segura y fiable en redes como Internet. Aunque es más complejo y lento que otros protocolos como UDP, es esencial para aplicaciones donde la precisión y la fiabilidad son cruciales.*

*![ProblemaConLaRed](/Images/ProblemaConLaRed.png "/Images/ProblemaConLaRed.png")*
*![ProblemaConLaRedAlEnviarVariosPaquetes](/Images/ProblemaConLaRedAlEnviarVariosPaquetes.png "/Images/ProblemaConLaRedAlEnviarVariosPaquetes.png")*
*![Socket](/Images/Socket.png "/Images/Socket.png")*

---

### **Protocolo UDP (User Datagram Protocol)**

> [!NOTE]
> *El **UDP (User Datagram Protocol)** es un protocolo de comunicación de red que opera en la **Capa de Transporte** del modelo OSI, al igual que TCP, pero con un enfoque distinto. UDP prioriza la velocidad y la eficiencia sobre la fiabilidad. Es ideal para aplicaciones que necesitan transmitir datos rápidamente y pueden tolerar cierta pérdida de paquetes.*

---

### **Características principales de UDP**

1. **Sin conexión (Connectionless):**  
   - *No establece una conexión previa entre el cliente y el servidor.*
   - *Los datos se envían directamente en forma de **datagramas** sin negociaciones iniciales.*

2. **Velocidad:**  
   - *UDP es más rápido que TCP porque no hay confirmaciones, retransmisiones ni controles de flujo.*

3. **Fiabilidad limitada:**  
   - *No garantiza que los datos lleguen al destino.*
   - *No asegura el orden de los paquetes ni realiza comprobaciones de errores avanzadas.*

4. **Ligereza:**  
   - *Los datagramas de UDP tienen menos sobrecarga (menos cabecera y sin mecanismos complejos de control), lo que lo hace eficiente para ciertas aplicaciones.*

---

### **Estructura del datagrama UDP**

**Un datagrama UDP incluye:**

1. **Puerto de origen:** *Identifica el programa que envió el datagrama.*
2. **Puerto de destino:** *Indica el programa en la máquina receptora.*
3. **Longitud:** *Especifica el tamaño total del datagrama.*
4. **Checksum:** *Permite detectar errores básicos en los datos, aunque no corrige errores.*

- *Comparado con TCP, esta cabecera es mucho más simple, lo que contribuye a su rapidez.*

---

### **Cómo funciona UDP**

1. **Envío de datos:**  
   - *El programa emisor crea un datagrama y lo envía directamente a la dirección IP y el puerto de destino.*
   - *No espera ninguna confirmación del receptor.*

2. **Recepción de datos:**  
   - *El receptor simplemente lee los datagramas que llegan al puerto especificado, sin garantías de que estén completos, ordenados o libres de errores.*

3. **Sin retransmisión:**  
   - *Si un datagrama se pierde o llega dañado, el protocolo no intenta retransmitirlo.*
   - *Esto queda a cargo de la aplicación, si es necesario.*

---

### **Ventajas de UDP**

1. **Alta velocidad:**  
   - *Es ideal para aplicaciones donde la rapidez es más importante que la fiabilidad.*

2. **Menor sobrecarga:**  
   - *La estructura simple del datagrama reduce el tiempo de procesamiento y el uso de ancho de banda.*

3. **Soporte para difusión y multidifusión:**  
   - *Permite enviar datos a múltiples destinatarios al mismo tiempo (por ejemplo, transmisión en vivo o juegos en red).*

---

### **Desventajas de UDP**

1. **Sin fiabilidad:**  
   - *No garantiza la entrega, el orden ni la integridad de los datos.*
2. **Gestión manual de errores:**  
   - *Las aplicaciones que necesitan fiabilidad deben implementar sus propios mecanismos de corrección de errores.*

---

### **Ejemplos de uso de UDP**

1. **Transmisión de medios (streaming):**  
   - *Para videos y audios en tiempo real (por ejemplo, YouTube Live, Zoom).*
   - *Una pequeña pérdida de paquetes no afecta significativamente la calidad del servicio.*

2. **Juegos en línea:**  
   - *Los juegos requieren datos rápidos para actualizaciones en tiempo real, como movimientos y acciones.*
   - *La retransmisión de datos retrasaría el juego.*

3. **Protocolos específicos:**  
   - *`DNS`* **(Sistema de Nombres de Dominio).**
   - *`VoIP`* **(Voz sobre IP).**
   - *`TFTP`* **(Protocolo de transferencia de ficheros trivial).**

---

### **Diferencias entre TCP y UDP**

| *Característica*         | *TCP*                                                         | *UDP*                              |
| ------------------------ | ------------------------------------------------------------- | ---------------------------------- |
| **Conexión**             | *Orientado a conexión.*                                       | *Sin conexión.*                    |
| **Fiabilidad**           | *Garantiza entrega, orden y corrección de errores.*           | *No garantiza entrega ni orden.*   |
| **Velocidad**            | *Más lento debido a su fiabilidad.*                           | *Más rápido por su simplicidad.*   |
| **Aplicaciones típicas** | *Navegadores, correo electrónico, transferencia de ficheros.* | *Streaming, juegos en línea, DNS.* |

- *UDP es el protocolo ideal cuando la velocidad y la eficiencia son prioritarias, y cuando se puede tolerar la pérdida de datos o asumir que la aplicación gestiona los errores. Aunque menos fiable que TCP, su simplicidad y rapidez lo hacen indispensable para aplicaciones modernas en tiempo real.*
