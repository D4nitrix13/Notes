<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"git tag"***

> *El comando `git tag` en Git se utiliza para administrar etiquetas, que son puntos específicos en la historia del repositorio que se marcan con un nombre. Estas etiquetas pueden ser útiles para marcar versiones específicas de tu código, como versiones estables o lanzamientos importantes.*

*Aquí están algunos usos comunes de `git tag`:*

1. **Crear una etiqueta:**

   *Para crear una etiqueta, puedes usar el comando `git tag` seguido del nombre que deseas para la etiqueta y **opcionalmente el identificador del commit al que deseas asociar la etiqueta. Por ejemplo:***

   ```bash
   git tag v1.0.0
   ```

2. **Crear una etiqueta anotada:**

   *Puedes crear una etiqueta anotada que incluya un mensaje utilizando `-a` y opcionalmente `-m` para **especificar el mensaje. Por ejemplo:***

   ```bash
   git tag -a v1.0.0 -m "Versión 1.0.0 lanzada"
   ```

3. **Listar etiquetas:**

   **Puedes listar todas las etiquetas en el repositorio utilizando:**

   ```bash
   git tag
   ```

4. **Mostrar información sobre una etiqueta:**

   **Para mostrar información detallada sobre una etiqueta específica, puedes usar:**

   ```bash
   git show <label-name>
   ```

5. **Eliminar una etiqueta:**

   **Puedes eliminar una etiqueta específica utilizando:**

   ```bash
   git tag -d <label-name>
   ```

6. **Empujar etiquetas al repositorio remoto:**

   **Para empujar etiquetas al repositorio remoto, puedes usar:**

   ```bash
   git push origin <label-name>
   ```

   **Para empujar todas las etiquetas al repositorio remoto:**

   ```bash
   git push origin --tags
   ```

## **Ejemplos de comandos `git tag` junto con sus formas no abreviadas y abreviadas:**

1. **Crear una etiqueta:**

   **Abreviado:**

   ```bash
   git tag v1.0.0
   ```

   **No abreviado:**

   ```bash
   git tag <label-name> [<commit>]
   ```

   **Por ejemplo, para etiquetar el commit actual como v1.0.0:**

   ```bash
   git tag v1.0.0
   ```

2. **Crear una etiqueta anotada:**

   **Abreviado:**

   ```bash
   git tag -a v1.0.0 -m "Versión 1.0.0 lanzada"
   ```

   **No abreviado:**

   ```bash
   git tag --annotate <label-name> --message "Versión 1.0.0 lanzada" [<commit>]
   ```

   **Por ejemplo, para etiquetar el commit actual con un mensaje:**

   ```bash
   git tag --annotate v1.0.0 --message "Versión 1.0.0 lanzada"
   ```

3. **Listar etiquetas:**

   **Abreviado:**

   ```bash
   git tag
   ```

   **No abreviado:**

   ```bash
   git tag --list
   ```

4. **Mostrar información sobre una etiqueta:**

   **Abreviado:**

   ```bash
   git show v1.0.0
   ```

   **No abreviado:**

   ```bash
   git show <label-name>
   ```

   **Por ejemplo, para mostrar información detallada sobre la etiqueta v1.0.0:**

   ```bash
   git show v1.0.0
   ```

5. **Eliminar una etiqueta:**

   **Abreviado:**

   ```bash
   git tag -d v1.0.0
   ```

   **No abreviado:**

   ```bash
   git tag --delete <label-name>
   ```

   **Por ejemplo, para eliminar la etiqueta v1.0.0:**

   ```bash
   git tag --delete v1.0.0
   ```

6. **Empujar etiquetas al repositorio remoto:**

   **Abreviado:**

   ```bash
   git push origin v1.0.0
   ```

   ```bash
   git push -u origin v1.0.0
   ```

   ```bash
   git push --set-upstream origin v1.0.0
   ```

   **No abreviado:**

   ```bash
   git push origin <label-name>
   ```

   ```bash
   git push origin -u <label-name>
   ```

   ```bash
   git push origin --set-upstream <label-name>
   ```

   **Por ejemplo, para empujar la etiqueta v1.0.0 al repositorio remoto:**

   ```bash
   git push origin v1.0.0
   ```

   ```bash
   git push -u origin v1.0.0
   ```

   ```bash
   git push --set-upstream origin v1.0.0
   ```  

   **Para empujar todas las etiquetas al repositorio remoto, la opción no abreviada es la misma que la abreviada:**

   ```bash
   git push origin --tags
   ```

   ```bash
   git push --set-upstream origin --tags
   ```

   ```bash
   git push -u origin --tags
   ```

> *Estos ejemplos muestran tanto las formas abreviadas como las no abreviadas de los comandos `git tag`. La forma no abreviada es útil para entender más claramente qué hace cada comando y para escribir scripts o automatizaciones donde la claridad es importante.*
