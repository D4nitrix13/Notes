<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***"Fichero .gitignore"***

> [!NOTE]
> *El fichero `.gitignore` se utiliza en Git para especificar ficheros y directorios que deseas ignorar en el control de versiones. Esto significa que Git no rastreará ni incluirá los ficheros y directorios enumerados en este fichero en tus commits. Esto es útil para evitar incluir ficheros generados automáticamente, ficheros de compilación, ficheros temporales y otros ficheros que no deseas que estén bajo control de versiones.*

**Aquí hay un ejemplo simple de un fichero `.gitignore`:**

```bash
# Ignorar ficheros de compilación generados
*.o
*.out
*.py

# Ignorar todos los ficheros dentro de la directorio fotos
fotos/

# Excepto el fichero background.png dentro de la directorio fotos
!fotos/background.png

# No ignorar "main.py" incluso si otros ficheros están siendo ignorados
!main.py

# Ignorar ficheros de objetos compilados en C
*.c~

# Ignorar ficheros de respaldo de Emacs
*~

# Ignorar ficheros de configuración local
config.ini

# Ignorar directorios generados automáticamente
/build/
/node_modules/

# Ignorar ficheros temporales de Python
**/__pycache__/
```

```css
proyecto/
│   main.py
│
├── fotos/
│   │   foto1.jpg
│   │   foto2.jpg
│   │   background.png
│   │
│   └── subfolder/
│       │   foto3.jpg
│       │   foto4.jpg
```

*En este ejemplo:*

- *`*.o` e `*.out` y `*.py` ignorarán todos los ficheros con extensión `.o` e `.out` y `*.py`, respectivamente.*

- *`fotos/` indica que se deben ignorar todos los ficheros y subdirectorios dentro de la directorio fotos.*

- *`!fotos/background.png` anula la regla anterior y especifica que el fichero background.png dentro de la directorio fotos no debe ser ignorado. La exclamación ! se utiliza para negar la regla de ignorar.*

- *`!main.py` especifica que el fichero main.py no debe ser ignorado, incluso si otros ficheros están siendo ignorados por otras reglas en el .gitignore.*

- *`*.c~` ignorará todos los ficheros que terminen en `.c~`.*

- *`*~` ignorará todos los ficheros que terminen en `~`.*

- *`config.ini` ignorará un fichero específico llamado `config.ini`.*

- *`/build/` y `/node_modules/` ignorarán los directorios llamados `build` y `node_modules`, respectivamente, junto con todo su contenido.*

- *`**/__pycache__/` ignorará todos los directorios llamados `__pycache__` en cualquier nivel de subdirectorio.*
  - *`**` es un comodín que representa cualquier número de directorios entre el directorio actual y el directorio `__pycache__`. Esto significa que se ignorarán todos los directorios `__pycache__` en cualquier lugar dentro de la estructura de directorios del proyecto.*
  - *`__pycache__` es un directorio utilizado por Python para almacenar bytecode compilado.*

- *Puedes crear y personalizar tu fichero `.gitignore` según las necesidades específicas de tu proyecto. Es importante tener en cuenta que los patrones en este fichero se aplican de manera recursiva a los subdirectorios a menos que se especifique lo contrario.*

```bash
git config --global core.excludesfile sda/sda1/directory/.gitignore
```

- *`git config --global core.excludesfile sda/sda1/directory/.gitignore`: Este comando configura un fichero `.gitignore` global para tu usuario. Especifica la ubicación del fichero `.gitignore` global en el directorio `sda/sda1/directory`. Los patrones de ignorados definidos en este fichero se aplicarán a todos los repositorios en tu sistema.*
