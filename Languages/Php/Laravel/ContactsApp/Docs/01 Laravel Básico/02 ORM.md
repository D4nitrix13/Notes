<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **ORM (Object-Relational Mapping)** *Es Una Técnica De Programación Que Permite Interactuar Con Bases De Datos Relacionales Utilizando Un Enfoque Orientado A Objetos. En Lugar De Escribir Consultas Sql Manualmente, Un Orm Mapea Las Tablas De La Base De Datos A Clases Y Objetos En El Código, Lo Que Permite Realizar Operaciones De Base De Datos De Manera Más Natural Y Fluida Utilizando El Lenguaje De Programación Orientado A Objetos.*

## **¿Cómo funciona un ORM?**

1. **Mapeo de tablas a clases:**
   - *Cada tabla en la base de datos se mapea a una clase en el código.*
   - *Cada fila en la tabla se mapea a una instancia de la clase.*
   - *Las columnas de la tabla se mapean a los atributos de la clase.*

2. **Consultas a través de objetos:**
   - *En lugar de escribir sentencias SQL, el ORM permite realizar operaciones de la base de datos como inserciones, actualizaciones, borrados y selecciones utilizando métodos de la clase.*
   - *Por ejemplo, en lugar de escribir una consulta SQL como `SELECT * FROM users WHERE age > 30`, puedes hacer algo como `User::where('age', '>', 30)->get()` (esto varía según el ORM y el lenguaje de programación).*

3. **Abstracción de la base de datos:**
   - *Los ORMs abstraen el trabajo con la base de datos, por lo que no necesitas preocuparte por las diferencias entre los diferentes sistemas de gestión de bases de datos (DBMS). En vez de escribir SQL específico para MySQL, PostgreSQL, etc., puedes utilizar el mismo código para interactuar con cualquier base de datos compatible con el ORM.*

### **Beneficios de usar un ORM**

1. **Facilita el desarrollo:**
   - *Hace que trabajar con bases de datos sea mucho más sencillo y rápido. No es necesario escribir SQL manualmente, lo que reduce el código repetitivo y los errores.*
  
2. **Manejo de relaciones entre tablas:**
   - *Los ORMs permiten manejar relaciones entre tablas (como `1 a muchos`, `muchos a muchos`, etc.) de manera muy sencilla. Esto es especialmente útil cuando trabajas con bases de datos complejas.*
  
3. **Mayor legibilidad y mantenimiento del código:**
   - *El código con ORM es más limpio, fácil de leer y más fácil de mantener. Esto se debe a que todo el trabajo con la base de datos se realiza utilizando el modelo de objetos, lo que alinea mejor la lógica del negocio con la estructura de la base de datos.*

4. **Seguridad:**
   - *Los ORM ayudan a prevenir ataques de inyección SQL, ya que preparan automáticamente las consultas y manejan los valores de manera segura.*

### **Desventajas de un ORM**

1. **Rendimiento:**
   - *En algunos casos, los ORM pueden generar consultas SQL menos eficientes que las escritas manualmente, lo que puede afectar al rendimiento en operaciones complejas.*
  
2. **Curva de aprendizaje:**
   - *Si no estás familiarizado con el ORM, puede haber una curva de aprendizaje, ya que necesitas entender cómo funciona el mapeo entre objetos y tablas.*

3. **Menos control sobre la base de datos:**
   - *El ORM abstrae muchas de las decisiones que normalmente tomarías al escribir SQL directamente. Esto significa que a veces no tienes tanto control sobre el rendimiento o la estructura exacta de las consultas.*

### **Resumen**

*Un **ORM** simplifica la interacción con bases de datos relacionales mediante la utilización de clases y objetos en lugar de SQL directo. Permite a los desarrolladores escribir menos código, mejora la legibilidad y facilita la gestión de bases de datos complejas. Aunque puede haber algunas desventajas como el rendimiento y la pérdida de control en ciertas situaciones, los beneficios de productividad y seguridad lo convierten en una herramienta muy popular en el desarrollo de aplicaciones web modernas.*
