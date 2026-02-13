<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# ***Persistencia De Datos***

- *Para crear páginas web, uno de los problemas más comunes es la **persistencia de datos**. En el pasado, se solían usar ficheros para almacenar la información, pero esta práctica ha caído en desuso por varias razones. A continuación te explico algunas de las limitaciones de los ficheros y por qué se recomienda usar bases de datos en su lugar:*

## ***Problemas de usar ficheros para persistencia de datos***

1. **Escalabilidad Limitada:**
   - *Los ficheros se vuelven ineficaces cuando la cantidad de datos crece. Al intentar leer o escribir en grandes volúmenes de información, la gestión de ficheros se vuelve lenta y propensa a errores.*
   - *Las bases de datos están diseñadas para manejar grandes cantidades de datos de manera eficiente.*

2. **Concurrencia:**
   - *En un sistema que usa ficheros, varios usuarios o procesos no pueden acceder a los datos de manera simultánea sin riesgo de corrupción. Si dos personas intentan modificar el mismo fichero al mismo tiempo, el fichero puede quedar corrupto o incompleto.*
   - *Las bases de datos gestionan la concurrencia de manera eficiente, permitiendo múltiples accesos simultáneos sin problemas.*

3. **Integridad de los Datos:**
   - *Cuando se usan ficheros, puede ser complicado asegurar que los datos sean consistentes. Si el sistema se apaga inesperadamente mientras se está escribiendo en un fichero, este podría quedar dañado o incompleto.*
   - *Las bases de datos suelen incluir mecanismos de transacciones, que permiten asegurar que los datos se escriban correctamente, garantizando su integridad incluso ante fallos inesperados.*

4. **Búsqueda y Recuperación de Datos:**
   - *Al utilizar ficheros, la búsqueda de datos específicos dentro de un fichero puede ser lenta, ya que se tiene que leer todo el fichero en secuencia.*
   - *Las bases de datos proporcionan índices y otras estructuras que permiten realizar búsquedas rápidas y eficientes.*

5. **Manejo de Relación de Datos:**
   - *Los ficheros no están diseñados para manejar relaciones entre diferentes tipos de datos de manera eficiente. Por ejemplo, si se desea vincular la información de un usuario con los datos de sus contactos, sería complicado hacerlo en un fichero plano.*
   - *Las bases de datos utilizan tablas y relaciones para organizar y conectar los datos de manera estructurada, lo que facilita consultas complejas.*

6. **Seguridad:**
   - *Los ficheros no tienen mecanismos avanzados para gestionar permisos de acceso o cifrado, lo que hace más difícil mantener los datos seguros.*
   - *Las bases de datos proporcionan características como control de acceso, cifrado y auditoría para garantizar la seguridad de los datos.*

### ***Ventajas de usar Bases de Datos***

1. **Escalabilidad y Rendimiento:** *Las bases de datos están optimizadas para manejar grandes volúmenes de datos y acceder a ellos rápidamente.*
2. **Concurrencia y Gestión de Usuarios:** *Permiten a múltiples usuarios acceder y modificar los datos sin causar problemas de integridad.*
3. **Seguridad Avanzada:** *Ofrecen medidas de seguridad como autenticación, cifrado y control de acceso.*
4. **Manejo de Relaciones:** *Son excelentes para manejar datos estructurados que tienen relaciones entre sí.*
5. **Respaldo y Recuperación:** *La mayoría de las bases de datos permiten realizar copias de seguridad y recuperación ante fallos.*

### ***Conclusión***

- *Si bien es posible almacenar datos en ficheros, las bases de datos proporcionan una solución mucho más robusta y eficiente para gestionar la persistencia de datos en aplicaciones web. El uso de bases de datos permite evitar los problemas mencionados anteriormente, como la falta de escalabilidad, la gestión de concurrencia y la seguridad de los datos, haciendo que la aplicación sea más confiable y fácil de mantener.*

*Las bases de datos generalmente utilizan protocolos y mecanismos propios para la comunicación entre el cliente (aplicación que consulta o actualiza la base de datos) y el servidor de base de datos. Algunos de los protocolos más comunes que utilizan las bases de datos son:*

### 1. *SQL (Structured Query Language) - Protocolos de consulta*  

*Aunque SQL no es un protocolo en sí mismo, es el lenguaje estándar utilizado por la mayoría de las bases de datos para interactuar con los datos. El protocolo de red utilizado para transmitir las consultas SQL y recibir las respuestas varía según el sistema de gestión de bases de datos (DBMS).*

### *Protocolos comunes para la comunicación con bases de datos:*

### 2. *MySQL / MariaDB - Protocolo MySQL*  

- *Protocolo utilizado:* *Protocolo MySQL*  
- *Descripción:* *MySQL utiliza su propio protocolo de red para permitir que las aplicaciones cliente se comuniquen con el servidor MySQL. Este protocolo es responsable de enviar consultas SQL y recibir resultados.*  
   *El protocolo de MySQL funciona sobre TCP/IP y generalmente usa el puerto **3306** para la comunicación.*  
   *Ejemplo de uso: cuando una aplicación web como PHP quiere interactuar con una base de datos MySQL, envía consultas SQL a través de este protocolo y recibe los resultados como respuesta.*

### 3. *PostgreSQL - Protocolo PostgreSQL*  

- *Protocolo utilizado:* *Protocolo PostgreSQL*  
- *Descripción:* *PostgreSQL también tiene su propio protocolo para manejar las solicitudes y respuestas entre el cliente y el servidor. Este protocolo es más complejo que el de MySQL y permite una gran variedad de operaciones y optimizaciones.*  
   *Similar a MySQL, PostgreSQL utiliza **TCP/IP** para la comunicación y generalmente escucha en el puerto **5432**.*  
   *Ejemplo de uso: un servidor web que utiliza PostgreSQL envía consultas SQL a través de este protocolo y recibe los datos correspondientes.*

### 4. *SQL Server - TDS (Tabular Data Stream)*  

- *Protocolo utilizado:* *TDS (Tabular Data Stream)*  
- *Descripción:* *SQL Server utiliza el protocolo TDS, que es un protocolo de comunicación binario para la transmisión de datos entre el cliente y el servidor de SQL Server.*  
   *TDS es usado por aplicaciones cliente como SQL Server Management Studio, así como por aplicaciones que utilizan ODBC (Open Database Connectivity) o ADO.NET para interactuar con SQL Server.*  
   *TDS funciona sobre **TCP/IP** y generalmente se comunica en el puerto **1433**.*  
   *Ejemplo de uso: las consultas SQL de una aplicación .NET o cualquier otro cliente SQL Server utilizan el protocolo TDS para comunicarse con el servidor.*

### 5. *SQLite - No requiere protocolo de red*  

- *Protocolo utilizado:* *Local, No aplica*  
- *Descripción:* *SQLite es una base de datos ligera que no requiere un servidor de base de datos externo, ya que se almacena directamente en un fichero de disco. Debido a esto, no utiliza un protocolo de red como los demás sistemas de bases de datos mencionados.*  
   *En lugar de un protocolo de red, SQLite simplemente accede al fichero de la base de datos localmente.*

### 6. *MongoDB - Protocolo MongoDB*  

- *Protocolo utilizado:* *Protocolo MongoDB*  
- *Descripción:* *MongoDB utiliza su propio protocolo binario para manejar la comunicación entre el cliente y el servidor. Este protocolo es eficiente y optimizado para las necesidades de las bases de datos NoSQL.*  
   *El protocolo de MongoDB se comunica a través de **TCP/IP** y generalmente usa el puerto **27017**.*  
   *Ejemplo de uso: cuando una aplicación que usa MongoDB quiere leer o escribir documentos, se comunica con el servidor MongoDB utilizando este protocolo.*

### 7. *Redis - Protocolo RESP (Redis Serialization Protocol)*  

- *Protocolo utilizado:* *RESP (Redis Serialization Protocol)*  
- *Descripción:* *Redis utiliza RESP, que es un protocolo de texto simple y eficiente diseñado para ser fácil de entender y utilizar. RESP permite a los clientes y servidores Redis intercambiar comandos y respuestas.*  
   *El protocolo RESP funciona sobre **TCP/IP** y generalmente se comunica en el puerto **6379**.*  
   *Ejemplo de uso: cuando una aplicación realiza una solicitud para almacenar o recuperar una clave-valor en Redis, utiliza el protocolo RESP.*

### 8. *Cassandra - Protocolo CQL (Cassandra Query Language)*  

- *Protocolo utilizado:* *CQL (Cassandra Query Language)*  
- *Descripción:* *Cassandra usa CQL, que es un lenguaje similar a SQL pero adaptado a su arquitectura distribuida. A pesar de estar basado en SQL, Cassandra no utiliza un protocolo SQL estándar, sino que emplea un protocolo binario propio para interactuar con el servidor.*  
   *Cassandra generalmente usa **TCP/IP** y se comunica en el puerto **9042**.*  
   *Ejemplo de uso: las aplicaciones que interactúan con Cassandra envían comandos CQL a través de este protocolo para acceder y manipular datos distribuidos.*

---

### *Resumen:*

- *Las bases de datos tradicionales como **MySQL**, **PostgreSQL** y **SQL Server** utilizan **protocolos personalizados** o estándares como **TCP/IP** para la comunicación entre clientes y servidores.*  
- *Las bases de datos **NoSQL** como **MongoDB** y **Cassandra** también tienen sus propios protocolos binarios o de consulta como **CQL**.*  
- *En general, estos protocolos son optimizados para manejar la transmisión de consultas SQL o comandos, la recuperación de datos y la gestión de la concurrencia y seguridad.*

*Cada tipo de base de datos tiene su propio protocolo, que se adapta a sus necesidades específicas de rendimiento, escalabilidad y funcionalidad.*
