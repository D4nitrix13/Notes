# ***Prohibimos El Acceso A Contactos Que No Te Pertenecen***

- *Para incluir una **cookie** en tu solicitud `cURL` junto con los datos del formulario, puedes usar la opción `-b` (o `--cookie`) de `cURL`, que permite enviar cookies en la solicitud.*

- *En tu caso, para enviar la cookie `PHPSESSID` en la solicitud, puedes agregar `-b "PHPSESSID=6fc371of1ikof4g4ill1lr4ehf"` a tu comando `cURL`.*

- **Aquí está el comando completo:**

```bash
curl -X POST -L -H "Content-Type: application/x-www-form-urlencoded" -d "name=Duki&phone_number=123456789" -b "PHPSESSID=6fc371of1ikof4g4ill1lr4ehf" http://172.17.0.2:80/contacts-app/update.php?id=1
```

## Explicación de las opciones

- **`-X POST`:** *Especifica que la solicitud es de tipo `POST`.*
- **`-L`:** *Sigue cualquier redirección (si hay alguna).*
- **`-H "Content-Type: application/x-www-form-urlencoded"`:** *Define el tipo de contenido como `application/x-www-form-urlencoded`, que es el formato adecuado para enviar datos de un formulario HTML.*
- **`-d "name=Duki&phone_number=123456789"`:** *Los datos del formulario que se envían en la solicitud `POST`.*
- **`-b "PHPSESSID=6fc371of1ikof4g4ill1lr4ehf"`:** *Incluye la cookie `PHPSESSID` con el valor proporcionado, que se utiliza para mantener la sesión del usuario.*
- **`http://172.17.0.2:80/contacts-app/update.php?id=1`:** *La URL de la solicitud `POST`, que incluye el parámetro `id` en la URL.*

### **Nota**

- *Asegúrate de que el servidor está configurado para leer las cookies correctamente y mantener la sesión activa a través de la cookie `PHPSESSID`. También, verifica que el valor de la cookie es válido y que corresponde a una sesión activa en el servidor.*

- **URL de la solicitud POST, donde se pasa el parámetro id=1 para eliminar el contacto con ID 1.**

```bash
curl -X GET -L -H "Content-Type: application/x-www-form-urlencoded" -b "PHPSESSID=6fc371of1ikof4g4ill1lr4ehf" http://172.17.0.2:80/contacts-app/delete.php?id=1
```

- *En PHP nativo, cuando no se utilizan frameworks o bibliotecas externas, a menudo es necesario hacer uso del método POST incluso para operaciones que normalmente serían gestionadas con métodos PUT o PATCH, debido a las limitaciones del servidor web o la forma en que PHP maneja los métodos HTTP.*
- **¿Por qué usar POST en lugar de PUT o PATCH?**

- *Por defecto, la mayoría de los servidores web (como Apache o Nginx) solo manejan bien los métodos GET, POST, y DELETE de manera nativa. Si intentas usar PUT o PATCH, puede que no sean manejados adecuadamente a menos que tengas configuraciones específicas o use algún framework que lo soporte.*

- *PHP no tiene un manejo nativo de PUT o PATCH a través de su sistema de formularios estándar, lo que significa que al enviar un formulario HTML (que generalmente solo soporta GET o POST), el servidor no sabría cómo manejar esos métodos sin alguna personalización.*
