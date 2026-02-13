<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# **1. Login y Registro**

- *Cuando implementas un sistema de login y registro en PHP, es común utilizar sesiones para mantener el estado del usuario autenticado. Estas sesiones permiten almacenar datos relacionados con el usuario (como su ID, nombre, correo electrónico, etc.) y acceder a ellos durante la interacción del usuario con el sistema.*
- *En este caso, se están creando ficheros de sesión en el directorio `/opt/lampp/temp/`, que es el lugar donde PHP almacena por defecto los datos de las sesiones en este servidor (XAMPP).*

---

## **2. Comando y salida**

```bash
lsd /opt/lampp/temp/ -lA
.rw------- daemon daemon 82 B Wed Dec 18 22:14:13 2024  sess_6fc371of1ikof4g4ill1lr4ehf
.rw------- daemon daemon 82 B Wed Dec 18 22:14:01 2024  sess_db9j4dpe3f3pc4mrp346rbmio4
```

- **Ficheros de sesión:** *Los nombres de los ficheros (`sess_6fc371of1ikof4g4ill1lr4ehf` y `sess_db9j4dpe3f3pc4mrp346rbmio4`) son identificadores únicos generados por PHP para cada sesión activa.*
- **Tamaño:** *Cada fichero tiene un tamaño de **82 bytes**, lo que indica que contienen datos serializados que ocupan este espacio.*
- **Permisos y propietario:** *Los ficheros son propiedad del usuario `daemon` (el proceso del servidor web) y tienen permisos restrictivos (`rw-------`), asegurando que solo el propietario puede leer/escribir.*

---

### **3. Formato PHP Serializado**

- **El contenido del fichero de sesión se puede leer con permisos de superusuario, como muestra el comando:**

```bash
sudo cat /opt/lampp/temp/sess_6fc371of1ikof4g4ill1lr4ehf
user|a:3:{s:2:"id";i:5;s:4:"name";s:5:"Daniel";s:5:"email";s:15:"Daniel@gmail.com";}
```

#### **Explicación del contenido:**

- **El formato de los datos está serializado en PHP, lo que significa que la información está codificada en una cadena para que pueda ser almacenada y recuperada fácilmente. Vamos a desglosar:**

1. **`user|`:**
   - *`user` es la clave de sesión que contiene los datos serializados.*

2. **`a:3:{...}`:**
   - *`a:3` indica que es un **array asociativo con 3 elementos**.*

3. **`s:2:"id";i:5;`:**
   - *`s:2:"id"`: Una clave con nombre `"id"` que tiene 2 caracteres.*
   - *`i:5`: Un valor entero (`5`) asociado a esa clave.*

4. **`s:4:"name";s:5:"Daniel";`:**
   - *`s:4:"name"`: Una clave con nombre `"name"` que tiene 4 caracteres.*
   - *`s:5:"Daniel"`: Un valor de tipo cadena con 5 caracteres.*

5. **`s:5:"email";s:15:"Daniel@gmail.com";`:**
   - *`s:5:"email"`: Una clave con nombre `"email"` que tiene 5 caracteres.*
   - *`s:15:"Daniel@gmail.com"`: Un valor de tipo cadena con 15 caracteres.*

---

### **4. Uso y Seguridad**

- **Uso:** *Este formato es útil porque permite almacenar estructuras de datos complejas (como arrays) en una forma compacta y fácil de deserializar. PHP automáticamente convierte este contenido en un array disponible en `$_SESSION` cuando la sesión se carga.*

- **Seguridad:**
  - **Riesgos de exposición:** *Si los ficheros de sesión son accesibles para usuarios no autorizados (por ejemplo, mediante mala configuración del servidor), podrían exponer información sensible del usuario.*
  - **Buenas prácticas:**
    - *Configurar permisos seguros para los ficheros de sesión.*
    - *Utilizar HTTPS para evitar que el identificador de sesión sea interceptado.*
    - *Establecer un límite de tiempo para las sesiones y usar cookies seguras.*

---

### **5. Resumen**

- *Los ficheros en `/opt/lampp/temp/` almacenan datos de sesiones activas.*
- *El contenido está serializado en PHP para facilitar el almacenamiento y recuperación.*
- *En el ejemplo, los datos corresponden a un usuario con ID `5`, nombre `Daniel`, y correo electrónico `Daniel@gmail.com`.*
- *Es esencial proteger estos datos para garantizar la privacidad y seguridad de los usuarios.*
