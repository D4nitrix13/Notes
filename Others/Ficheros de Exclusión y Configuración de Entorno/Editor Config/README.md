<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***EditorConfig es una herramienta increíble para mantener consistencia en los estilos de codificación a través de diferentes editores y entornos. [Más información aquí.](https://editorconfig.org "https://editorconfig.org")***

---

---

## ***Fichero principal de EditorConfig***

```ini
root = true
```

*Indica que este es el fichero principal de EditorConfig, por lo que no debe buscar otros ficheros de configuración en subdirectorios.*

---

### ***Saltos de línea estilo Unix con una nueva línea al final de cada fichero***

```ini
[*]
end_of_line = lf
insert_final_newline = true
```

- **end_of_line = lf:** *Define el estilo de salto de línea como LF (Line Feed), común en sistemas Unix/Linux.*
- **insert_final_newline = true:** *Añade automáticamente una nueva línea al final de cada fichero si no la tiene.*

---

### ***Coincidencia de múltiples ficheros con notación de expansión de llaves***

```ini
[*.{js,py}]
charset = utf-8
```

- **charset = utf-8:** *Establece UTF-8 como el conjunto de caracteres por defecto para ficheros `.js` y `.py`.*

---

### ***Indentación de 4 espacios para ficheros Python***

```ini
[*.py]
indent_style = space
indent_size = 4
```

- **indent_style = space:** *Usa espacios en lugar de tabulaciones para la indentación.*
- **indent_size = 4:** *Define que cada nivel de indentación usa 4 espacios.*

---

### ***Indentación con tabulaciones para ficheros Makefile***

```ini
[Makefile]
indent_style = tab
indent_size = 4
```

- **indent_style = tab:** *Utiliza tabulaciones para la indentación en ficheros `Makefile`.*
- **indent_size = 4:** *Equivale a 4 espacios por tabulación.*

---

### ***Sobrescritura de indentación para todos los ficheros JS bajo el directorio `lib`***

```ini
[lib/**.js]
indent_style = space
indent_size = 2
```

- **indent_style = space:** *Utiliza espacios en vez de tabulaciones.*
- **indent_size = 2:** *Usa 2 espacios de indentación para ficheros JS dentro de `lib`.*

---

### ***Coincidencia exacta con ficheros `package.json` o `.travis.yml`***

```ini
[{package.json,.travis.yml}]
indent_style = space
indent_size = 2
```

- **indent_style = space:** *Usa espacios para la indentación.*
- **indent_size = 2:** *Cada nivel de indentación tendrá 2 espacios para estos ficheros específicos.*

```bash
# Autor: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Correo electrónico: danielperezdev@proton.me

# EditorConfig is awesome: https://editorconfig.org

# top-most EditorConfig file
root = true

# Unix-style newlines with a newline ending every file
[*]
end_of_line = lf
insert_final_newline = true

# Matches multiple files with brace expansion notation
# Set default charset
[*.{js,py}]
charset = utf-8

# 4 space indentation
[*.py]
indent_style = space
indent_size = 4

# Tab indentation (no size specified)
[Makefile]
indent_style = tab
indent_size = 4

# Indentation override for all JS under lib directory
[lib/**.js]
indent_style = space
indent_size = 2

# Matches the exact files either package.json or .travis.yml
[{package.json,.travis.yml}]
indent_style = space
indent_size = 2
```
