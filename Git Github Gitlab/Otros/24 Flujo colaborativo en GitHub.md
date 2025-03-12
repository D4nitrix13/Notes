<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"Flujo colaborativo en GitHub"***

- *El flujo de trabajo colaborativo en GitHub implica que varios colaboradores trabajen juntos en un proyecto, ya sea un repositorio público o privado, utilizando GitHub como plataforma de colaboración. Aquí tienes un flujo de trabajo básico para colaborar en GitHub:*

1. **Fork del Repositorio Original:**

   - *Cada colaborador que desee contribuir al proyecto debe hacer un "fork" del repositorio original en su propia cuenta de GitHub. Esto crea una copia del repositorio original en la cuenta del colaborador, sobre la cual pueden trabajar sin afectar al repositorio original.*

2. **Clonar el Fork Localmente:**

   - *Después de hacer un fork, cada colaborador debe clonar su fork en su máquina local utilizando el comando `git clone <URL_del_fork>`. Esto crea una copia local del repositorio en la máquina del colaborador, donde pueden realizar cambios y trabajar en el código.*

3. **Agregar un Remote Upstream:**

   - *Para mantener su fork actualizado con el repositorio original, cada colaborador debe agregar un "remote upstream" que apunte al repositorio original. Esto se hace ejecutando el comando `git remote add upstream <URL_del_repositorio_original>`.*

4. **Crear una Rama de Característica:**

   - *Para trabajar en una nueva característica o solucionar un problema, cada colaborador debe crear una nueva rama en su repositorio local utilizando el comando `git checkout -b nombre_de_la_rama`. Es una buena práctica nombrar la rama de manera descriptiva, como `feature/nueva-caracteristica` o `bugfix/arreglo-de-bug`.*

5. **Realizar Cambios Locales:**

   - *Una vez que estén en la rama de la característica, los colaboradores pueden realizar los cambios necesarios en el código utilizando su editor de texto o IDE preferido.*

6. **Hacer Commit de los Cambios:**

   - *Después de realizar los cambios, los colaboradores deben hacer commit de sus cambios utilizando el comando `git add .` para agregar los ficheros modificados y `git commit -m "Mensaje del commit"` para realizar el commit con un mensaje descriptivo.*

7. **Enviar los Cambios al Fork:**

   - *Una vez que los cambios estén listos, los colaboradores deben enviar sus cambios al fork en GitHub utilizando el comando `git push origin nombre_de_la_rama`.*

8. **Enviar una Pull Request:**

   - *Después de enviar los cambios al fork, los colaboradores pueden enviar una "pull request" al repositorio original. Esto se hace desde la página del fork en GitHub haciendo clic en el botón "Pull Request" y siguiendo los pasos para crear la solicitud de extracción.*

9. **Revisión y Fusión:**

   - *Los propietarios del repositorio original pueden revisar la pull request, comentar los cambios y, si todo está bien, fusionar los cambios en el repositorio original. Esto integra los cambios del colaborador en el proyecto principal.*

10. **Sincronizar el Fork:**

- *Es importante mantener el fork actualizado con el repositorio original para poder colaborar eficientemente en el proyecto. Los colaboradores pueden hacerlo ejecutando `git fetch upstream` para obtener los últimos cambios del repositorio original y luego `git merge upstream/main` (o el nombre de la rama principal) para fusionar esos cambios en su fork local.*

- *Este flujo de trabajo colaborativo en GitHub permite a múltiples colaboradores trabajar juntos de manera eficiente en un proyecto, contribuir con cambios, revisar el trabajo de otros y mantener una versión estable y actualizada del proyecto.*
