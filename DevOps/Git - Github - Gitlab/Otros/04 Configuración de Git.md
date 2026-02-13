<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración de Git***

> *La configuración de usuario de Git se almacena en un fichero llamado `.gitconfig` que se encuentra en tu directorio de inicio. La ruta exacta del fichero dependerá de tu sistema operativo:*

- *En Linux y Mac, la ruta será `~/.gitconfig`.*

- *En Windows, la ruta será `C:\Users\<TuNombreDeUsuario>\.gitconfig`.*

> *Puedes ver la configuración de tu usuario en este fichero con un editor de texto, o puedes usar el comando `git config --list` para listar todas las configuraciones de Git actuales en la terminal.*

```bash
git config --list
```

> [!NOTE]
> *Si solo quieres ver la configuración de tu usuario, puedes usar los siguientes comandos:*

```bash
git config --get user.name
```

```bash
git config --get user.email
```

> *Estos comandos mostrarán tu nombre de usuario y correo electrónico de Git, respectivamente.*

---

## ***`git`***

> *El comando `git` por sí solo muestra una lista de los comandos más comúnmente usados en Git. Es una forma rápida de recordar o aprender los comandos básicos de Git.*

```bash
git
```

---

## ***`git -h` y `git --help`***

> *Los comandos `git -h` y `git --help` muestran la ayuda de Git. Proporcionan una lista de los comandos de Git disponibles y una breve descripción de lo que hace cada uno. Ambos comandos hacen lo mismo, por lo que puedes usar el que prefieras.*

```bash
git -h
```

```bash
git --help
```

> *Si necesitas ayuda con un comando específico de Git, puedes usar `git help <comando>` o `git <comando> --help`. Por ejemplo, `git help status` o `git status --help` te mostrarán ayuda para el comando `git status`.*

```bash
git help status
```

```bash
git status --help
```

> [!TIP]
> **Nota:** *La documentación de Git es muy completa y útil. Si alguna vez te encuentras atascado o no estás seguro de cómo funciona un comando, no dudes en consultar la ayuda de Git o la documentación en línea.*

---

## ***Configuración inicial***

> *Antes de empezar a usar Git, necesitarás configurar tu nombre de usuario y correo electrónico.*

***configurar tu nombre de usuario***

```bash
git config --global user.name "Tu Nombre"
```

***configurar tu nombre de correo electrónico***

```bash
git config --global user.email "tuemail@example.com"
```

**Este comando configura master como la rama predeterminada cuando se inicializa un nuevo repositorio Git en tu sistema.**

```bash
git config --global init.defaultBranch master
```

***Este comando configura Visual Studio Code como el editor predeterminado para Git en tu sistema.***

```bash
git config --global core.editor "code --wait"
```

```bash
git config --global core.abbrev 15
```

- **`git config --global core.abbrev 15`:** *Este comando establece el valor de la variable `core.abbrev` en 15 de forma global. Esta configuración controla el número de caracteres abreviados mostrados por Git. En este caso, se establece en 15 caracteres.*

- *El valor predeterminado para `git config --global core.abbrev` es 7. Esto significa que, de forma predeterminada, Git mostrará los identificadores de commit (hashes) abreviados a 7 caracteres de longitud. Sin embargo, si estableces `git config --global core.abbrev` sin proporcionar un valor, Git restablecerá esta configuración al valor predeterminado de 7 caracteres.*

---

## ***Enviar cambios a un repositorio remoto***

> [!NOTE]
> *Una vez que hayas realizado cambios en tu repositorio local y los hayas confirmado (commit), puedes enviar estos cambios a tu repositorio remoto utilizando el comando `git push`.*

## ***Comando `git push`***

*El comando `git push` se utiliza para enviar los cambios que has realizado en tu repositorio local a un repositorio remoto.*

```bash
git push <remote> <branch>
```

> *Donde `<remote>` es el repositorio remoto al que deseas enviar tus cambios, y `<branch>` es la rama de ese repositorio que deseas actualizar.*

## ***Opción `-u` o `--set-upstream`***

*La opción `-u` o `--set-upstream` se utiliza para establecer el repositorio y la rama especificados como el "upstream" predeterminado para la rama local actual. Esto significa que, en el futuro, puedes simplemente usar `git push` o `git pull` sin especificar un repositorio o rama, y Git sabrá a qué te refieres.*

```bash
git push -u origin master
```

*Y aquí está el mismo comando, pero utilizando la versión larga `--set-upstream` de la opción:*

```bash
git push --set-upstream origin master
```

- *En ambos casos, `origin` es el repositorio remoto y `master` es la rama que deseas actualizar. Estos comandos enviarán tus cambios a la rama `master` del repositorio `origin`, y también establecerán esa rama como el "upstream" predeterminado para tu rama local actual.*

> [!TIP]
**Nota:** *`origin` es el nombre predeterminado que Git da al repositorio remoto desde el que clonaste, y `master` es la rama predeterminada.*

```bash
git mv main.py lib.py
```

- *`git mv main.py lib.py`: Este comando renombra el fichero `main.py` a `lib.py` dentro del repositorio Git. Git detectará automáticamente el cambio y lo registrará como una modificación de fichero.*

---

## ***Enlaces útiles***

- [*Documentación oficial de Git*](https://git-scm.com/doc "https://git-scm.com/doc")
