<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Introduccion ala terminal***

---

- [***Introduccion ala terminal***](#introduccion-ala-terminal)
- [***Primeros Comandos***](#primeros-comandos)

---

# ***Primeros Comandos***

> **Conceptos importantes sobre linux**

1. *Directorio: En programacion un directorio es una directorio*

2. *Fichero: En programacion un fichero es una fichero con o sin extensio*

   1. **Ejemplo:**

        ```bash
         script.py
         ```

   2. *script es el nombre del fichero y lo que esta luego del punto es la extension del fichero*

3. ***.:** Representa el directorio actual.*

4. ***~:** Representa el directorio home del usuario actual.*

   1. *Por ejemplo, si tu nombre de usuario es daniel, ~ generalmente se traduciría a /home/daniel.*

5. ***..:** Representa el directorio padre del directorio actual. Entonces, si estás en /home/daniel/Escritorio/directorio y ejecutas cd .., te moverías al directorio /home/daniel/Escritorio.*

   1. ***Ejemplo:** ../descargas: Esto te movería al directorio descargas que se encuentra en el mismo nivel que tu directorio actual. Entonces, si estás en /home/daniel/Escritorio/directorio y ejecutas*

       ```bash
       cd ../descargas 
       ```

   2. *Te moverías al directorio /home/daniel/Escritorio/descargas.*

> ***Comandos***

1. *`<kbd>` **Ctrl** `</kbd>` + `<kbd>` **Alt** `</kbd>` + `<kbd>` **t** `</kbd>`*

    - *Abre una nueva ventana de terminal*

2. *`<kbd>` **Alt** `</kbd>` + `<kbd>` **tab** `</kbd>`*

   - *moverte entre ventana*

3. *`whoami`*

   ```bash
   whoami
   ```

    - *imprimir el nombre de usuario del usuario actual*

    - **Traduccion:** *whoami ,quién soy yo?*

4. *`pwd`*

   ```bash
   pwd
   ```

    - *muestra la ruta completa del directorio en el que te encuentras actualmente*
    - **Traduccion:** *"Print Working Directory", que se traduce al español como "Imprimir el Directorio de Trabajo*

5. *`clear`*

   ```bash
   clear
   ```

    - *limpiar la pantalla de la termina*

    - **Traduccion:** *clear, limpiar*

   1. *Otra manera de hacerlo*

      - `<kbd>` **Ctrl** `</kbd>` **+** `<kbd>` **l** `</kbd>`

6. *cd `<directorio>`*

     ```bash
      cd <directorio>
      ```

   - *Este comando se utiliza para cambiar el directorio de trabajo actual a otro directorio y toma como parametro el nombre del directorio*

     - *Entonces, cd . simplemente te mantendría en el mismo directorio.*

   - **Traduccion:** *Change Directory, Cambiar - Directorio*

7. *`ls`*

   ```bash
   ls ./
   ```

   ```bash
   ls ./Escritorio/
   ```

   ```bash
   ls ../
   ```

   ```bash
   ls ../directorio/
   ```

   - *Este comando se utiliza para listar los ficheros y directorios en el directorio actual. **Tambien se le puede pasar rutas relativas como absoluta***
   - **Traduccion:** *"List", lista*

8. *`mkdir`*

   ```bash
   mkdir directorio/
   ```

   ```bash
   mkdir ./Escritorio/directorio/
   ```

   ```bash
   mkdir ../directorio/
   ```

   ```bash
   mkdir directorio/ otro/
   ```

   ```bash
   mkdir ./Escritorio/directorio ./Escritorio/otro/
   ```

   ```bash
   mkdir ../directorio/ ../otro/
   ```

   ```bash
   mkdir ./"nuevo directorio"/
   ```

   ```bash
   mkdir ./nuevo\ directorio/
   ```

   - *Este comando se utiliza para crear un nuevo directorio. Toma como parámetro el nombre del directorio que se desea crear. **Tambien se le puede pasar rutas relativas como absoluta***

   - **Traduccion:** *Make Directory, Crear Directorio*

9. *`rmdir`*

   ```bash
   rmdir directorio/
   ```

   ```bash
   rmdir ./Escritorio/directorio/
   ```

   ```bash
   rmdir ../directorio/
   ```

   ```bash
   rmdir directorio/ otro/
   ```

   ```bash
   rmdir ./Escritorio/directorio/ ./Escritorio/otro/
   ```

   ```bash
   rmdir ../directorio/ ../otro/
   ```

   ```bash
   rmdir ./"nuevo directorio"/
   ```

   ```bash
   rmdir ./nuevo\ directorio/
   ```

   - *Este comando se utiliza para eliminar un directorio vacío. Toma como parámetro el nombre del directorio que se desea eliminar. **Tambien se le puede pasar rutas relativas como absoluta***

     - ***Nota:** rmdir sólo eliminará un directorio si está vacío*

     - **Se pueden pasar mas de un parametro**

   - **Traduccion:** *Remove Directory,Eliminar Directorio*

10. *`touch`*

    ```bash
    touch fichero.txt
    ```

    ```bash
    touch ./Escritorio/directorio/fichero.txt
    ```

    ```bash
    touch ../directorio/fichero.txt
    ```

    ```bash
    touch fichero.txt fichero2.txt
    ```

    ```bash
    touch ./Escritorio/directorio/fichero.txt ./Escritorio/directorio/fichero2.txt
    ```

    ```bash
    touch ../directorio/fichero.txt ../directorio/copia.txt
    ```

    ```bash
    touch ./"mi primer programa.py"
    ```

    ```bash
    touch ./"mi primer programa".py
    ```

    ```bash
    touch ./mi\ primer\ programa.py
    ```

    - *El comando touch en Linux se utiliza para cambiar las marcas de tiempo de acceso y modificación de un fichero. También se puede utilizar para crear un nuevo fichero si el fichero especificado no existe. **Tambien se le puede pasar rutas relativas como absoluta***

    - **Se pueden pasar mas de un parametro**

11. *`rm`*

      ```bash
      rm fichero.txt
      ```

      ```bash
      rm ./Escritorio/directorio/fichero.txt
      ```

      ```bash
      rm ../directorio/fichero.txt
      ```

      ```bash
      rm fichero.txt copia.txt
      ```

      ```bash
      rm ./Escritorio/directorio/fichero.txt ./Escritorio/directorio/copia.txt
      ```

      ```bash
      rm ../directorio/fichero.txt ../directorio/copia.txt
      ```

      ```bash
      rm ./"mi primer programa.py"
      ```

      ```bash
      rm ./"mi primer programa".py
      ```

      ```bash
      rm ./mi\ primer\ programa.py
      ```

      - *El comando rm en Linux se utiliza para eliminar ficheros y directorios. **Tambien se le puede pasar rutas relativas como absoluta***

        - **Se pueden pasar mas de un parametro**

        - *Este comando eliminará el fichero llamado fichero.txt del directorio actual. Ten en cuenta que este comando no moverá el fichero a la papelera de reciclaje, sino que lo eliminará permanentemente. Por lo tanto, debes tener cuidado al usarlo.*

      - **Traduccion:** *Las siglas rm provienen del inglés y significan "remove", que en español se traduce como "eliminar".*

12. *`cp`*

      ```bash
      cp fichero.txt ./copia.txt
      ```

      ```bash
      cp ./Escritorio/directorio/fichero.txt ./Escritorio/directorio/copia.txt
      ```

      ```bash
      cp ../directorio/fichero.txt ../directorio/copia.txt
      ```

      - *Se utilizan para copiar ficheros.*

        - *Si la el fichero ya existe, será sobrescrito.*

      - **Traduccion:** *cp proviene de las siglas en inglés "copy", que significa "copiar".*

13. *`mv`*

    ```bash
    mv fichero.txt ./copia.txt
    ```

    ```bash
    mv ./Escritorio/directorio/fichero.txt ./Escritorio/directorio/copia.txt
    ```

    ```bash
    mv ../directorio/fichero.txt ../directorio/copia.txt
    ```  

    - *Este comando mover el fichero a otra ubicacion si ya existe, será sobrescrito.*

      - *Además, mv también se puede utilizar para renombrar ficheros.*

    - **Traduccion:** *mv proviene de las siglas en inglés "move", que significa "mover".*

14. *`echo`*

      ```bash
       echo "Este mensaje se imprimira en la terminal"
       ```

      ```bash
      echo $HOME
      ```

     - *El comando echo en Linux se utiliza para mostrar una línea de texto u otras variables de entorno en la terminal.*

     - **Traduccion:** *echo es una palabra en inglés que significa "eco", en el sentido de repetir lo que se le da.*

15. *`cat`*

      ```bash
      cat ./fichero.txt
      ```

      ```bash
      cat ./fichero.txt ./fichero2.txt
      ```

      ```bash
      cat ./fichero.txt > ./fichero2.txt
      ```

      ```bash
      cat ./Escritorio/directorio/fichero.txt
      ```

      ```bash
      cat ./Escritorio/directorio/fichero.txt ./Escritorio/directorio/fichero2.txt
      ```

      ```bash
      cat ./Escritorio/directorio/fichero.txt > ./Escritorio/directorio/fichero2.txt
      ```

      ```bash
      cat ../directorio/fichero.txt
      ```

      ```bash
      cat ../directorio/fichero.txt ../directorio/fichero2.txt
      ```

      ```bash
      cat ../directorio/fichero.txt > ../directorio/fichero2.txt
      ```

      ```bash
      cat ./fichero.txt ./fichero2.txt > fichero3.txt
      ```

     - *El comando cat en Linux se utiliza para concatenar y mostrar ficheros.*

       - *Este comando concatenará el contenido de **fichero.txt** y **fichero2.txt**, y el resultado se guardará en **fichero3.txt**. **Si fichero3.txt ya existe, será sobrescrito si no sera se creara el fichero.***

       - *El símbolo > en Linux se utiliza para redirigir la salida de un comando a un fichero.*

       - **Se pueden pasar mas de un parametro**

     - **Traduccion:** *cat es una abreviatura de la palabra en inglés "concatenate", que significa "concatenar".*

16. *`man <command>`*

      ```bash
      man ls
      ```

      - *El comandos man en Linux se utiliza para obtener ayuda sobre un comando toma como parametro el comando.*

      - **Traduccion:** *man es un acrónimo de "manual", y man `<comando>` muestra la página del manual para el `<comando>`. Las páginas del manual contienen una descripción detallada del comando, sus opciones y su uso.*

17. *`nano <fichero>`*

      ```bash
      nano fichero.txt
      ```

      - *nano es un editor de texto en la línea de comandos de Linux. nano fichero.txt abrirá el fichero fichero.txt en el editor nano.*

18. *`grep palabra <fichero>`*

      ```bash
      grep lista fichero.txt
      ```

    - *El comando grep en Linux se utiliza para buscar texto en ficheros.*

      - *El comando grep lista fichero.txt buscará la palabra "lista" en el fichero fichero.txt y mostrará las líneas que contienen esa palabra.*

    - **Traduccion:** *grep es un acrónimo de "Global Regular Expression Print", Impresión global de expresiones regulares.*

19. *`comando con opciones`*

     - > *Las opciones en Linux, también conocidas como flags o switches, son argumentos que se utilizan para modificar el comportamiento de un comando. Generalmente se añaden después del nombre del comando y antes de cualquier otro argumento.*

       - > *Las opciones suelen comenzar con un guion - o dos guiones --. Las opciones que comienzan con un solo guion suelen ser abreviaturas de una sola letra, mientras que las opciones que comienzan con dos guiones suelen ser palabras completas.*

     ```bash
     <command> --help
     ```

      ```bash
      ls --help
      ```

       - *Este comando mostrará la ayuda para el comando `ls`*

   ```bash
   rm -r ./directorio
   ```

   ```bash
   rm -r -i ./directorio
   ```

   ```bash
   rm -ri ./directorio
   ```

   ```bash
   rm -ir ./directorio
   ```

   ```bash
   rm --recursive ./directorio 
   ```

   ```bash
   rm --recursive --interactive ./directorio
   ```

   ```bash
   rm --interactive --recursive ./directorio
   ```

   ```bash
   rm --recursive -i ./directorio
   ```

   ```bash
   rm -i --recursive ./directorio
   ```

   ```bash
   rm -r --interactive ./directorio
   ```

   ```bash
   rm --interactive -r ./directorio
   ```
