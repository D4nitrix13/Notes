<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Contraseñas***

> *Para crear una contraseña segura debemos seguir los siguientes pasos*

* ***La contraseña:** debe contener al menos 12 caracteres*

* ***La contraseña:** debe contener numeros y caracteres especiales*

* ***Recomendacion:** la contraseña no debe estar relacionada con datos personales*
  
  * **Ejemplos**

    * *~~Fechas importante~~*

    * ~~*Nombre de familiares*~~

* ***La contraseña:** Debes tener una contraseña distinta para cada plataforma, web*

> [!NOTE]
> *Hash es un algoritmo matemático utilizado para mejorar la seguridad de las contraseñas. Este algoritmo toma una cadena como parámetro y devuelve una cadena de longitud fija. Es importante destacar que, independientemente de la longitud de la cadena de entrada, el resultado del hash siempre tendrá la misma longitud. Cuando una cadena está en formato hash, la representación suele ser en secuencia de bits. Sin embargo, por cuestiones de legibilidad, a menudo convertimos esta cadena de bits a su equivalente en formato hexadecimal. Este formato hexadecimal es más amigable para los humanos y facilita la visualización y comparación de los valores hash. Sin embargo, es importante destacar que el proceso de hash es unidireccional, lo que significa que no es posible recuperar la contraseña original a partir del hash.*

## ***Existen distintos tipos de cifrado entre los mas conocidos***

1. **MD5 (Message Digest Algorithm 5-Algoritmo de resumen de mensajes 5)**

    > *MD5 produce un hash de 128 bits (32 caracteres hexadecimales). Aunque fue ampliamente utilizado en el pasado, MD5 se considera ahora débil en términos de seguridad debido a vulnerabilidades que permiten colisiones (dos entradas diferentes que producen el mismo hash).*

2. **SHA-1 (Secure Hash Algorithm 1-Algoritmo hash seguro 1)**
    > *SHA-1 produce un hash de 160 bits (40 caracteres hexadecimales). Al igual que MD5, SHA-1 se considera obsoleto y vulnerable a ataques de colisión. No se recomienda su uso en aplicaciones de seguridad.*

3. **SHA-256 (Secure Hash Algorithm 256-bit-Algoritmo hash seguro de 256 bits)**

    > *SHA-256 es parte de la familia de algoritmos SHA-2 y produce un hash de 256 bits (64 caracteres hexadecimales). Es ampliamente utilizado y considerado seguro para muchos propósitos, incluido el almacenamiento seguro de contraseñas.*

4. **SHA-3 (Secure Hash Algorithm 3-Algoritmo hash seguro 3)**

    > *SHA-3 es la última versión de la familia de algoritmos SHA y fue diseñada como un reemplazo de SHA-2. Ofrece una estructura diferente y se basa en el principio de la esponja. SHA-3 tiene variantes con diferentes tamaños de salida, como SHA3-256, SHA3-512, etc.*

5. **bcrypt**

    > *bcrypt no es solo una función de hash, sino un algoritmo de derivación de claves diseñado específicamente para almacenar contraseñas de manera segura. Realiza múltiples iteraciones de hash y es resistente a ataques de fuerza bruta.*

6. **Argon2**

    > *Argon2 es otro algoritmo diseñado específicamente para el almacenamiento seguro de contraseñas. Es el algoritmo ganador del concurso Password Hashing Competition (PHC) y está diseñado para ser resistente a una amplia variedad de ataques, incluidos los ataques de fuerza bruta y los ataques de tiempo de memoria.*

*![HASH](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.ionos.mx%2Fdigitalguide%2Ffileadmin%2FDigitalGuide%2FSchaubilder%2Fesquema-de-la-funcion-hash.png&f=1&nofb=1&ipt=46f2ea3475dc080d4bbed64f0ff98411cad30729187f1b4cfeae157f6bed7196&ipo=images "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.ionos.mx%2Fdigitalguide%2Ffileadmin%2FDigitalGuide%2FSchaubilder%2Fesquema-de-la-funcion-hash.png&f=1&nofb=1&ipt=46f2ea3475dc080d4bbed64f0ff98411cad30729187f1b4cfeae157f6bed7196&ipo=images")*

---

### *Existen aplicaciones de escritorio y extension del navegador que nos pueden a ayudar a gestionar nuestras contraseñas*

1. [**Keepassx**](#keepassx)

2. [**LastPass**](#lastpass)

# ***Keepassx***

*KeePassX es un gestor de contraseñas de código abierto diseñado para ayudarte a gestionar de manera segura tus contraseñas. Te permite almacenar y organizar contraseñas de forma cifrada, y solo necesitas recordar una contraseña maestra para acceder a todas las demás. Es una aplicación útil para mejorar la seguridad al utilizar contraseñas fuertes y únicas para cada cuenta.*

> *Para instalar keepassx en ubuntu sigue los siguientes pasos*

1. ***Abre la terminal:***

   1. *Puedes abrir la terminal usando el atajo de teclado `<kbd>` Ctrl`</kbd>`  + `<kbd>` Alt`</kbd>`  + `<kbd>` T`</kbd>` . Actualiza la lista de paquetes:*

   ```bash
   sudo apt-get update
   ```

2. ***Instala KeePassXC:***

    1. ```bash
        sudo apt-get install -y keepassxc
        ```

        *Confirma la instalación: Se te pedirá que ingreses tu contraseña de administrador para confirmar la instalación.*

3. ***Inicia KeePassXC:***

    1. *Después de la instalación, puedes iniciar KeePassX desde el menú de aplicaciones o ejecutando el siguiente comando en la terminal:*

    ```bash
    keepassxc
    ```

---

# ***LastPass***

*LastPass es un servicio de gestión de contraseñas lanzado en 2008 que ayuda a los usuarios a organizar y almacenar de manera segura sus contraseñas en línea. Ofrece funciones clave como el almacenamiento seguro de contraseñas con una única contraseña maestra, generador de contraseñas fuertes, autocompletado de formularios, y la capacidad de almacenar información adicional de forma segura. LastPass facilita la sincronización entre dispositivos, permitiendo a los usuarios acceder a sus datos desde diferentes plataformas. El servicio prioriza la seguridad mediante medidas como el cifrado de extremo a extremo.*

> [!IMPORTANT]
> *Es una extension del navegador*

*[LastPass](https://my.lastpass.com/create_account.php?fromloginpage=1 "https://my.lastpass.com/create_account.php?fromloginpage=1")*
