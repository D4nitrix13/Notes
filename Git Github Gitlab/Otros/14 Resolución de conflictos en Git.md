<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"Resolución de conflictos en Git"***

> *La resolución de conflictos en Git ocurre cuando hay diferencias entre dos ramas que Git no puede fusionar automáticamente. Esto sucede cuando se modifican las mismas partes de un fichero en ramas separadas o cuando se eliminan o renombran ficheros en una rama pero no en la otra. Git no puede determinar automáticamente cuál es la versión correcta, por lo que requiere intervención manual para resolver el conflicto.*

**Aquí hay algunos pasos generales para resolver conflictos en Git:**

1. **Identificar los conflictos:** *Cuando Git detecta un conflicto durante una fusión (por ejemplo, después de ejecutar `git merge`), marcará los ficheros conflictivos y mostrará un mensaje que indica que hay conflictos sin resolver.*

2. **Abrir los ficheros conflictivos:** *Abre los ficheros conflictivos en un editor de texto o en tu IDE. Dentro de estos ficheros, verás secciones delimitadas por marcas especiales de Git que indican el inicio y el final de las secciones en conflicto. Estas secciones contendrán las versiones de los cambios conflictivos de ambas ramas.*

3. **Resolver los conflictos:** *Edita manualmente el fichero para eliminar las marcas de conflicto (`<<<<<<<`, `=======`, `>>>>>>>`) y decidir qué cambios mantener, eliminar o modificar. Puedes decidir mantener una versión, ambas versiones o una combinación de ambas, según tus necesidades y el propósito de la fusión.*

4. **Guardar los cambios:** *Después de resolver los conflictos, guarda los cambios en el fichero conflictivo.*

5. **Agregar los ficheros resueltos:** *Una vez que hayas resuelto todos los conflictos en los ficheros conflictivos, añade los ficheros al área de preparación (staging area) utilizando `git add`.*

6. **Finalizar la fusión:** *Continúa el proceso de fusión utilizando `git merge --continue`. Esto finalizará la fusión y creará un nuevo commit de fusión que incluya los cambios resueltos.*

7. **Revisar y confirmar la fusión:** *Verifica que la fusión se haya completado satisfactoriamente revisando los ficheros y la historia del repositorio. Si todo está bien, confirma el commit de fusión utilizando `git commit` si es necesario.*

> [!IMPORTANT]
*Es importante tomarse el tiempo necesario para resolver los conflictos de manera adecuada, ya que esto asegurará que la fusión resultante sea coherente y que el historial del proyecto se mantenga limpio y organizado.*
