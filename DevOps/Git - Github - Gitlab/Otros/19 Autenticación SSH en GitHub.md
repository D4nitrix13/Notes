<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"Autenticación SSH en GitHub"***

> *El proceso de autenticación SSH en GitHub implica la generación de una nueva clave SSH y su posterior adición al agente SSH para facilitar la autenticación en GitHub. Aquí tienes los pasos detallados para realizar este proceso:*

- *[Generating a new SSH key and adding it to the ssh-agent](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent "https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent")*
- *[Use SSH keys to communicate with GitLab](https://docs.gitlab.com/ee/user/ssh.html "https://docs.gitlab.com/ee/user/ssh.html")*

---

## ***Generación de una nueva clave SSH:***

1. ***Abre Terminal:** En tu sistema operativo, abre la terminal o la línea de comandos.*

2. ***Genera la clave SSH:** Ejecuta el siguiente comando en la terminal, reemplazando `correo@example.com` con tu dirección de correo electrónico de GitHub:*

   ```bash
   ssh-keygen -t ed25519 -C "correo@example.com"
   ```

   **Si tu sistema no admite el algoritmo Ed25519, puedes usar el siguiente comando en su lugar:**

   ```bash
   ssh-keygen -t rsa -b 4096 -C "correo@example.com"
   ```

3. ***Sigue las instrucciones:** Se te pedirá que elijas la ubicación para guardar la clave y una frase de contraseña opcional. Puedes presionar `Enter` para aceptar la ubicación predeterminada y dejar la frase de contraseña en blanco si lo deseas.*

---

### ***Agregar la clave SSH al ssh-agent:***

1. **Inicia el agente SSH:** *En la terminal, ejecuta el siguiente comando para iniciar el agente SSH en segundo plano:*

   ```bash
   eval "$(ssh-agent -s)"
   ```

2. **Agrega la clave privada al ssh-agent:** *Ejecuta el siguiente comando para agregar la clave privada SSH al agente SSH. Asegúrate de reemplazar `~/.ssh/id_ed25519` con la ubicación de tu clave privada si utilizaste un nombre diferente o una ubicación personalizada al generar la clave SSH:*

   ```bash
   ssh-add ~/.ssh/id_ed25519
   ```

- **Ubicacion de la claves**

```bash
cat ~/.ssh/id_ed25519.pub
```

```bash
cat ~/.ssh/id_ed25519.pub | xclip -selection clipboard
```

---

### ***Generar una nueva clave SSH para una llave de seguridad de hardware:***

> *Si estás utilizando una llave de seguridad de hardware, los pasos son similares, pero debes seguir las instrucciones específicas de tu dispositivo para confirmar la generación de la clave SSH.*

1. **Inserta tu clave de seguridad de hardware:** *Conecta tu llave de seguridad de hardware a tu computadora.*

2. **Genera la clave SSH:** *Ejecuta el comando `ssh-keygen` en la terminal, reemplazando `correo@example.com` con tu dirección de correo electrónico de GitHub. Asegúrate de seguir las instrucciones específicas de tu dispositivo cuando se te solicite:*

   ```bash
   ssh-keygen -t ed25519-sk -C "correo@example.com"
   ```

3. **Sigue las instrucciones:** *Sigue las instrucciones en la terminal y en tu dispositivo de seguridad de hardware para completar el proceso de generación de la clave SSH.*

*Una vez completados estos pasos, tendrás una nueva clave SSH generada y agregada al agente SSH, lo que te permitirá autenticarte en GitHub utilizando SSH. También puedes agregar la clave pública SSH a tu cuenta de GitHub para habilitar la autenticación SSH.*
