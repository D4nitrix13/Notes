<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"Reintegración de ramas en Git"***

> *La reintegración de ramas en Git se refiere al proceso de fusionar los cambios de una rama secundaria en una rama principal, como la rama `main` o `master`. Este proceso suele realizarse después de haber completado el trabajo en una rama secundaria y haber confirmado los cambios en esa rama. Luego, los cambios se fusionan de vuelta a la rama principal para incorporarlos al flujo de trabajo principal del proyecto.*

**Aquí hay un procedimiento básico para reintegrar una rama secundaria en Git:**

1. **Asegúrate de estar en la rama principal:** *Primero, asegúrate de estar en la rama principal a la que deseas reintegrar los cambios. Por ejemplo, si la rama principal es `main`, puedes cambiar a ella utilizando:*

   ```bash
   git checkout main
   ```

2. **Obtén los últimos cambios de la rama principal:** *Antes de reintegrar los cambios de la rama secundaria, es una buena práctica asegurarse de tener los últimos cambios de la rama principal. Puedes hacerlo mediante:*

   ```bash
   git pull origin main
   ```

3. **Fusiona la rama secundaria en la rama principal:** *Ahora, puedes fusionar los cambios de la rama secundaria en la rama principal utilizando `git merge`. Por ejemplo, si la rama secundaria se llama `mi-rama`, puedes usar:*

   ```bash
   git merge mi-rama
   ```

   **Si estás utilizando Git versión 2.23 o superior, también puedes utilizar `git switch` para cambiar a la rama principal y fusionar al mismo tiempo:**

   ```bash
   git switch main
   ```

   ```bash
   git merge mi-rama
   ```

4. **Resuelve los conflictos si es necesario:** *Si hay conflictos entre los cambios de la rama principal y los de la rama secundaria, Git te notificará y marcará los ficheros en conflicto. Deberás resolver estos conflictos manualmente antes de continuar con la fusión.*

5. **Confirma la fusión:** *Después de resolver cualquier conflicto, confirma la fusión utilizando `git commit` si es necesario. Si no hay conflictos, Git creará automáticamente un commit de fusión.*

6. **Publica los cambios si es necesario:** *Si estás trabajando en un repositorio compartido, es posible que desees publicar los cambios fusionados en el repositorio remoto utilizando `git push`.*

7. **Opcional: Elimina la rama secundaria:** *Una vez que los cambios se hayan reintegrado en la rama principal y no necesites más la rama secundaria, puedes eliminarla utilizando `git branch -d mi-rama`.*

*Este proceso de reintegración de ramas es fundamental en Git y es una parte importante del flujo de trabajo de desarrollo colaborativo, ya que permite a los equipos trabajar en paralelo en diferentes características o correcciones de errores y luego integrar esos cambios de manera ordenada en el proyecto principal.*
