<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Configuración de Git para Soportar Caracteres UTF-8***

---

## ***Introducción***

*Git es un sistema de control de versiones ampliamente utilizado que maneja ficheros y nombres de ficheros en diversos sistemas operativos y configuraciones regionales. Para asegurar que Git maneje correctamente los caracteres UTF-8 (como tildes, eñes, caracteres acentuados, etc.), es importante configurarlo adecuadamente.*

*Este documento explica por qué ocurren los problemas con los caracteres UTF-8 en Git, cómo resolverlos y proporciona detalles sobre los comandos específicos que se utilizan para configurar Git correctamente.*

---

## ***Problema***

*Cuando los nombres de ficheros contienen caracteres no ASCII, Git puede mostrar estos caracteres de manera incorrecta en la consola, utilizando una notación octal entre comillas en lugar de los caracteres Unicode reales. Esto puede hacer que los nombres de ficheros sean difíciles de leer y entender, especialmente en contextos multilingües o internacionales.*

*Por ejemplo, un fichero llamado `canción.txt` podría aparecer como `"canci\303\263n.txt"` en la salida de Git.*

---

## ***Solución***

---

### ***Paso 1: Configuración del Encoding***

*Primero, asegúrate de que Git esté configurado para usar UTF-8 como codificación de caracteres para los mensajes de commit y la salida del log.*

```bash
git config --global i18n.commitencoding utf-8
git config --global i18n.logoutputencoding utf-8
```

*Estos comandos aseguran que Git utilice UTF-8 para codificar correctamente los mensajes de commit y la salida del log.*

---

### ***Paso 2: Configuración de core.quotepath***

- *Configura Git para que muestre los nombres de fichero no ASCII directamente como caracteres Unicode en lugar de su representación octal.*

```bash
git config --global core.quotepath off
```

*Este comando desactiva la notación octal entre comillas (`"\nnn\nnn..."`) para los nombres de fichero no ASCII en la salida de Git, mejorando la legibilidad.*

### ***Paso 3: Verificación de la Configuración***

*Para verificar que la configuración se haya aplicado correctamente, puedes listar todas las configuraciones globales de Git:*

```bash
git config --global --list
```

```bash
user.name=d4nitrix13
user.email=danielperezdev@proton.me
core.editor=code --wait
core.precomposeunicode=true
core.quotepath=off
init.defaultbranch=master
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
filter.lfs.clean=git-lfs clean -- %f
i18n.commitencoding=utf-8
i18n.logoutputencoding=utf-
```

*Asegúrate de que `i18n.commitencoding` y `i18n.logoutputencoding` estén configurados como `utf-8`, y `core.quotepath` esté configurado como `false` o `off`.*

---

### ***Paso 4: Entendiendo core.precomposeunicode (si es necesario)***

*En sistemas como macOS, donde los nombres de fichero pueden estar en forma descompuesta (NFD) en lugar de la forma precompuesta (NFC), también puedes configurar:*

```bash
git config --global core.precomposeunicode true
```

*Esto ayuda a manejar nombres de fichero Unicode de manera coherente entre diferentes sistemas de ficheros.*

---

### ***Paso 5: Cambios Visibles en la Consola***

*Después de configurar Git correctamente, los nombres de fichero con caracteres UTF-8 deberían mostrarse correctamente en la consola, sin la notación octal entre comillas.*

---

## ***Conclusiones y Recomendaciones***

- *Configurar Git para soportar caracteres UTF-8 asegura una experiencia de usuario consistente y legible, especialmente en entornos multilingües. Es crucial mantener las configuraciones adecuadas a nivel global (`--global`) para que se apliquen a todos los repositorios de Git en tu sistema.*

*Para más detalles sobre cada comando y configuración, consulta la documentación oficial de Git o utiliza `git help config` para obtener ayuda detallada sobre configuraciones específicas.*
