<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git reset --hard" y "git reflog"***

- *`git reset --hard` y `git reflog` son comandos y herramientas importantes en Git que se utilizan en situaciones de gestión de cambios y recuperación. Aquí hay una explicación de cada uno:*

---

## ***`git reset --hard`***

- *El comando `git reset --hard` se utiliza para deshacer cambios en el área de preparación (staging area) y en el directorio de trabajo, llevando la rama actual al commit especificado.*

- *Si se especifica un commit, la rama actual se moverá al commit especificado y se descartarán los cambios en el área de preparación y el directorio de trabajo desde ese punto hasta el último commit.*
- *Si no se especifica ningún commit, el comando simplemente deshace todos los cambios en el área de preparación y el directorio de trabajo desde el último commit.*

- *Es importante tener en cuenta que `git reset --hard` puede ser una operación destructiva, ya que descarta los cambios no guardados. Se debe utilizar con precaución, especialmente si hay cambios importantes que no han sido confirmados.*

---

### ***`git reflog`***

- *`git reflog` es una herramienta que muestra un registro de referencia de HEAD, que es una lista cronológica de los cambios en la referencia HEAD, como movimientos de ramas y cambios de commit. Esta herramienta es útil para recuperar referencias o cambios que se han perdido o deshecho accidentalmente.*

- *Cuando ejecutas `git reflog`, verás una lista de acciones realizadas en tu repositorio, cada una con un identificador de commit y un mensaje descriptivo. Puedes usar estos identificadores de commit para recuperar accidentalmente deshacer cambios o restaurar ramas a estados anteriores.*

- *Por ejemplo, si has deshecho accidentalmente un commit con `git reset --hard`, puedes buscar el identificador de commit correspondiente en el registro de referencia de HEAD generado por `git reflog` y luego restaurar la rama a ese commit utilizando `git reset` con el identificador de commit correcto.*

*En resumen, `git reset --hard` se utiliza para deshacer cambios en el área de preparación y el directorio de trabajo, mientras que `git reflog` se utiliza para ver un registro de referencia de HEAD y recuperar cambios o referencias perdidas.*
