<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"Desplazamiento en una rama"***

> *El desplazamiento en una rama en Git se refiere a cambiar la referencia de la rama actual a un commit específico en esa rama. Esto significa que, después del desplazamiento, la rama apuntará al commit al que te has movido.*

*Puedes desplazarte en una rama de varias maneras, algunas de las cuales incluyen:*

1. **Checkout:** *Utilizando el comando `git checkout` seguido del nombre del commit al que deseas desplazarte. Por ejemplo:*

   ```bash
   git checkout <nombre_commit>
   ```

   *Esto cambiará la referencia de la rama actual al commit especificado.*

2. **Reset:** *Utilizando el comando `git reset` para mover la referencia de la rama a un commit específico. Por ejemplo:*

   ```bash
   git reset <nombre_commit>
   ```

   *Dependiendo de la opción que utilices con `git reset` (como `--soft`, `--mixed` o `--hard`), los cambios en el área de preparación y el directorio de trabajo pueden mantenerse, eliminarse o modificarse respectivamente.*

3. **Merge:** *Realizando un merge de otra rama en la rama actual. Por ejemplo:*

   ```bash
   git merge <otra_rama>
   ```

   *Esto incorporará los cambios de la otra rama en la rama actual y moverá la referencia de la rama actual al commit resultante del merge.*

*Cada uno de estos métodos tiene sus propios usos y consideraciones, así que es importante entender cómo funcionan y cuándo utilizarlos en función de tu flujo de trabajo específico.*
