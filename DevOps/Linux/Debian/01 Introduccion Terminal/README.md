<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Introduccion ala terminal***

---

- [***Introduccion ala terminal***](#introduccion-ala-terminal)
  - [***Primeros Comandos***](#primeros-comandos)

---

## ***Primeros Comandos***

> **Conceptos importantes sobre linux**

1. *Directorio: En programcion un directory es una directory*

2. *Fichero: En programcion un file es una file con o sin extensio*

   1. **Ejemplo:**

        ```bash
         script.py
         ```

   2. *script es el nombre del file y lo que esta luego del punto es la extension del file*

3. ***.:** Representa el directory actual.*

4. ***~:** Representa el directory home del usuario actual.*

   1. *Por ejemplo, si tu nombre de usuario es D4nitrix13, ~ generalmente se traduciría a /home/D4nitrix13.*

5. ***..:** Representa el directory padre del directory actual. Entonces, si estás en /home/D4nitrix13/Desktop/directory y ejecutas cd .., te moverías al directory /home/D4nitrix13/Desktop.*

   1. ***Ejemplo:** ../Dowloands: Esto te movería al directory Dowloands que se encuentra en el mismo nivel que tu directory actual. Entonces, si estás en /home/D4nitrix13/Desktop/directory y ejecutas*

       ```bash
       cd ../Dowloands 
       ```

   2. *Te moverías al directory /home/D4nitrix13/Desktop/Dowloands.*

> ***Comandos***

1. **`Ctrl`** **`+`** **`Alt`** **`+`** **`t`**

    - *Abre una nueva ventana de terminal*

2. **`Alt`** **`+`** **tab**

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

    - *muestra la ruta completa del directory en el que te encuentras actualmente*
    - **Traduccion:** *"Print Working Directory", que se traduce al español como "Imprimir el Directorio de Trabajo*

5. *`clear`*

   ```bash
   clear
   ```

    - *limpiar la pantalla de la termina*

    - **Traduccion:** *clear, limpiar*

   1. *Otra manera de hacerlo*

      - **`Ctrl`** **`+`** **`l`**

6. *cd `<directory>`*

     ```bash
      cd <directory>
      ```

   - *Este comando se utiliza para cambiar el directory de trabajo actual a other directory y toma como parametro el nombre del directory*

     - *Entonces, cd . simplemente te mantendría en el mismo directory.*

   - **Traduccion:** *Change Directory, Cambiar - Directorio*

7. *`ls`*

   ```bash
   ls ./
   ```

   ```bash
   ls ./Desktop/
   ```

   ```bash
   ls ../
   ```

   ```bash
   ls ../directory/
   ```

   - *Este comando se utiliza para listar los ficheros y directorios en el directory actual. **Tambien se le puede pasar rutas relativas como absoluta***
   - **Traduccion:** *"List", lista*

8. *`mkdir`*

   ```bash
   mkdir directory/
   ```

   ```bash
   mkdir ./Desktop/directory/
   ```

   ```bash
   mkdir ../directory/
   ```

   ```bash
   mkdir directory/ other/
   ```

   ```bash
   mkdir ./Desktop/directory ./Desktop/other/
   ```

   ```bash
   mkdir ../directory/ ../other/
   ```

   ```bash
   mkdir ./"new directory"/
   ```

   ```bash
   mkdir ./new\ directory/
   ```

   - *Este comando se utiliza para crear un new directory. Toma como parámetro el nombre del directory que se desea crear. **Tambien se le puede pasar rutas relativas como absoluta***

   - **Traduccion:** *Make Directory, Crear Directorio*

9. *`rmdir`*

   ```bash
   rmdir directory/
   ```

   ```bash
   rmdir ./Desktop/directory/
   ```

   ```bash
   rmdir ../directory/
   ```

   ```bash
   rmdir directory/ other/
   ```

   ```bash
   rmdir ./Desktop/directory/ ./Desktop/other/
   ```

   ```bash
   rmdir ../directory/ ../other/
   ```

   ```bash
   rmdir ./"new directory"/
   ```

   ```bash
   rmdir ./new\ directory/
   ```

   - *Este comando se utiliza para eliminar un directory vacío. Toma como parámetro el nombre del directory que se desea eliminar. **Tambien se le puede pasar rutas relativas como absoluta***

     - ***Nota:** rmdir sólo eliminará un directory si está vacío*

     - **Se pueden pasar mas de un parametro**

   - **Traduccion:** *Remove Directory,Eliminar Directorio*

10. *`touch`*

    ```bash
    touch file.txt
    ```

    ```bash
    touch ./Desktop/directory/file.txt
    ```

    ```bash
    touch ../directory/file.txt
    ```

    ```bash
    touch file.txt fichero2.txt
    ```

    ```bash
    touch ./Desktop/directory/file.txt ./Desktop/directory/fichero2.txt
    ```

    ```bash
    touch ../directory/file.txt ../directory/copy.txt
    ```

    ```bash
    touch ./"my first program.py"
    ```

    ```bash
    touch ./"my first program".py
    ```

    ```bash
    touch ./my\ first\ program.py
    ```

    - *El comando touch en Linux se utiliza para cambiar las marcas de tiempo de acceso y modificación de un file. También se puede utilizar para crear un new file si el file especificado no existe. **Tambien se le puede pasar rutas relativas como absoluta***

    - **Se pueden pasar mas de un parametro**

11. *`rm`*

      ```bash
      rm file.txt
      ```

      ```bash
      rm ./Desktop/directory/file.txt
      ```

      ```bash
      rm ../directory/file.txt
      ```

      ```bash
      rm file.txt copy.txt
      ```

      ```bash
      rm ./Desktop/directory/file.txt ./Desktop/directory/copy.txt
      ```

      ```bash
      rm ../directory/file.txt ../directory/copy.txt
      ```

      ```bash
      rm ./"my first program.py"
      ```

      ```bash
      rm ./"my first program".py
      ```

      ```bash
      rm ./my\ first\ program.py
      ```

      - *El comando rm en Linux se utiliza para eliminar ficheros y directorios. **Tambien se le puede pasar rutas relativas como absoluta***

        - **Se pueden pasar mas de un parametro**

        - *Este comando eliminará el file llamado file.txt del directory actual. Ten en cuenta que este comando no moverá el file a la papelera de reciclaje, sino que lo eliminará permanentemente. Por lo tanto, debes tener cuidado al usarlo.*

      - **Traduccion:** *Las siglas rm provienen del inglés y significan "remove", que en español se traduce como "eliminar".*

12. *`cp`*

      ```bash
      cp file.txt ./copy.txt
      ```

      ```bash
      cp ./Desktop/directory/file.txt ./Desktop/directory/copy.txt
      ```

      ```bash
      cp ../directory/file.txt ../directory/copy.txt
      ```

      - *Se utilizan para copiar ficheros.*

        - *Si la el file ya existe, será sobrescrito.*

      - **Traduccion:** *cp proviene de las siglas en inglés "copy", que significa "copiar".*

13. *`mv`*

    ```bash
    mv file.txt ./copy.txt
    ```

    ```bash
    mv ./Desktop/directory/file.txt ./Desktop/directory/copy.txt
    ```

    ```bash
    mv ../directory/file.txt ../directory/copy.txt
    ```  

    - *Este comando mover el file a otra ubicacion si ya existe, será sobrescrito.*

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
      cat ./file.txt
      ```

      ```bash
      cat ./file.txt ./fichero2.txt
      ```

      ```bash
      cat ./file.txt > ./fichero2.txt
      ```

      ```bash
      cat ./Desktop/directory/file.txt
      ```

      ```bash
      cat ./Desktop/directory/file.txt ./Desktop/directory/fichero2.txt
      ```

      ```bash
      cat ./Desktop/directory/file.txt > ./Desktop/directory/fichero2.txt
      ```

      ```bash
      cat ../directory/file.txt
      ```

      ```bash
      cat ../directory/file.txt ../directory/fichero2.txt
      ```

      ```bash
      cat ../directory/file.txt > ../directory/fichero2.txt
      ```

      ```bash
      cat ./file.txt ./fichero2.txt > fichero3.txt
      ```

     - *El comando cat en Linux se utiliza para concatenar y mostrar ficheros.*

       - *Este comando concatenará el contenido de **file.txt** y **fichero2.txt**, y el resultado se guardará en **fichero3.txt**. **Si fichero3.txt ya existe, será sobrescrito si no sera se creara el file.***

       - *El símbolo > en Linux se utiliza para redirigir la salida de un comando a un file.*

       - **Se pueden pasar mas de un parametro**

     - **Traduccion:** *cat es una abreviatura de la palabra en inglés "concatenate", que significa "concatenar".*

16. *`man <command>`*

      ```bash
      man ls
      ```

      - *El comandos man en Linux se utiliza para obtener ayuda sobre un comando toma como parametro el comando.*

      - **Traduccion:** *man es un acrónimo de "manual", y man `<comando>` muestra la página del manual para el `<comando>`. Las páginas del manual contienen una descripción detallada del comando, sus opciones y su uso.*

17. *`nano <file>`*

      ```bash
      nano file.txt
      ```

      - *nano es un editor de texto en la línea de comandos de Linux. nano file.txt abrirá el file file.txt en el editor nano.*

18. *`grep palabra <file>`*

      ```bash
      grep lista file.txt
      ```

    - *El comando grep en Linux se utiliza para buscar texto en ficheros.*

      - *El comando grep lista file.txt buscará la palabra "lista" en el file file.txt y mostrará las líneas que contienen esa palabra.*

    - **Traduccion:** *grep es un acrónimo de "Global Regular Expression Print", Impresión global de expresiones regulares.*

19. *`Comando con opciones`*

     - > *Las opciones en Linux, también conocidas como flags o switches, son argumentos que se utilizan para modificar el comportamiento de un comando. Generalmente se añaden después del nombre del comando y antes de cualquier other argumento.*

       - > *Las opciones suelen comenzar con un guion - o dos guiones --. Las opciones que comienzan con un solo guion suelen ser abreviaturas de una sola letra, mientras que las opciones que comienzan con dos guiones suelen ser palabras completas.*

     ```bash
     <command> --help
     ```

      ```bash
      ls --help
      ```

       - *Este comando mostrará la ayuda para el comando `ls`*

   ```bash
   rm -r ./directory
   ```

   ```bash
   rm -r -i ./directory
   ```

   ```bash
   rm -ri ./directory
   ```

   ```bash
   rm -ir ./directory
   ```

   ```bash
   rm --recursive ./directory 
   ```

   ```bash
   rm --recursive --interactive ./directory
   ```

   ```bash
   rm --interactive --recursive ./directory
   ```

   ```bash
   rm --recursive -i ./directory
   ```

   ```bash
   rm -i --recursive ./directory
   ```

   ```bash
   rm -r --interactive ./directory
   ```

   ```bash
   rm --interactive -r ./directory
   ```
