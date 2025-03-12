<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git push"***

> *El comando `git push` se utiliza para enviar los cambios locales que has realizado en tu repositorio Git a un repositorio remoto, como GitHub, GitLab o Bitbucket. Aquí tienes cómo usar `git push`:*

```bash
git push <nombre_remoto> <nombre_rama_local>:<nombre_rama_remota>
```

- *`<nombre_remoto>` es el nombre del repositorio remoto al que deseas enviar tus cambios. Por lo general, este es `origin` si has clonado el repositorio, pero también puedes tener otros repositorios remotos configurados.*

- *`<nombre_rama_local>` es el nombre de la rama local que deseas enviar al repositorio remoto.*

- *`<nombre_rama_remota>` es el nombre de la rama en el repositorio remoto donde deseas enviar tus cambios. Por lo general, es el mismo nombre que la rama local, pero puedes enviar cambios a una rama con un nombre diferente si es necesario.*

**Ejemplo:**

```bash
git push origin main
```

- *Esto enviará los cambios de tu rama local `main` al repositorio remoto llamado `origin` y los fusionará con la rama `main` en el repositorio remoto.*

```bash
git push origin ramaLocal:ramaRemota
```

- **El carácter:** *se utiliza para especificar qué ramas locales deben ser empujadas a qué ramas remotas.*

- *Esto enviará los cambios de tu rama local `ramaLocal` al repositorio remoto llamado `origin` y los fusionará con la rama `ramaRemota` en el repositorio remoto.*

- *Después de ejecutar `git push`, los cambios serán enviados al repositorio remoto y estarán disponibles para otros colaboradores del proyecto. Es importante tener en cuenta que necesitas tener permisos de escritura en el repositorio remoto para poder realizar un push exitoso.*

> [!IMPORTANT]
> *El comando `git push` se utiliza para enviar los commits del repositorio local al repositorio remoto. Existen varias opciones interesantes que puedes usar con `git push` para personalizar el proceso de envío de cambios.*

---

## ***Opciones de `git push`***

1. **`<remoto> <rama>`**
   - **Función:** *Envía la rama local especificada al repositorio remoto.*
   - **Uso:** *Permite enviar cambios a una rama específica en un repositorio remoto.*
   - **Ejemplo:**

     ```bash
     git push origin main
     ```

2. **`-u` o `--set-upstream`**
   - **Función:** *Establece la rama remota como la rama de seguimiento para la rama local.*
   - **Uso:** *Hace que `git push` y `git pull` usen esta rama remota como predeterminada para la rama local.*
   - **Ejemplo:**

     ```bash
     git push -u origin feature-branch
     ```

3. **`--force` o `-f`**
   - **Función:** *Forza el envío de cambios al repositorio remoto, sobrescribiendo el historial de la rama remota.*
   - **Uso:** *Útil para sobrescribir cambios en el repositorio remoto, pero debe usarse con precaución.*
   - **Ejemplo:**

     ```bash
     git push --force origin main
     ```

4. **`--force-with-lease`**
   - **Función:** *Forza el envío de cambios solo si la rama remota no ha cambiado desde la última vez que se sincronizó.*
   - **Uso:** *Proporciona una forma más segura de forzar el push que `--force`, evitando sobrescribir cambios inesperados.*
   - **Ejemplo:**

     ```bash
     git push --force-with-lease origin feature-branch
     ```

5. **`--dry-run`**
   - **Función:** *Muestra qué cambios se enviarían sin realmente hacer el push.*
   - **Uso:** *Permite verificar qué cambios serían enviados al remoto sin realizar el envío.*
   - **Ejemplo:**

     ```bash
     git push --dry-run origin main
     ```

6. **`--tags`**
   - **Función:** *Envía todas las etiquetas (tags) locales al repositorio remoto.*
   - **Uso:** *Útil para asegurarte de que todas las etiquetas locales estén sincronizadas con el remoto.*
   - **Ejemplo:**

     ```bash
     git push --tags
     ```

7. **`--all`**
   - **Función:** *Envía todas las ramas locales al repositorio remoto.*
   - **Uso:** *Para sincronizar todas las ramas locales con el remoto en una sola operación.*
   - **Ejemplo:**

     ```bash
     git push --all origin
     ```

8. **`--delete`**
   - **Función:** *Elimina una rama del repositorio remoto.*
   - **Uso:** *Se utiliza para borrar ramas que ya no son necesarias en el remoto.*
   - **Ejemplo:**

     ```bash
     git push origin --delete feature-branch
     ```

9. **`--push-option <opciones>`**
   - **Función:** *Permite pasar opciones personalizadas al repositorio remoto durante el push.*
   - **Uso:** *Utilizado con configuraciones específicas del servidor remoto que soportan opciones de push.*
   - **Ejemplo:**

     ```bash
     git push --push-option=some-option origin main
     ```

10. **`--no-verify`**
    - **Función:** *Evita la ejecución de hooks de pre-push durante el envío.*
    - **Uso:** *Útil si necesitas omitir las verificaciones automáticas antes de hacer el push.*
    - **Ejemplo:**

      ```bash
      git push --no-verify origin main
      ```

*Estas opciones te permiten personalizar cómo se envían los cambios al repositorio remoto, brindando mayor control sobre el proceso de sincronización.*
