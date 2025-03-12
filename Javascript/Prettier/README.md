<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Opciones de Configuración de Prettier***

1. **arrowParens:** *Define si se deben usar paréntesis en las funciones de flecha. El valor `"always"` indica que siempre se deben usar paréntesis, incluso si no son necesarios.*

2. **bracketSpacing:** *Determina si se debe agregar espacio entre los corchetes en objetos. Si es `true`, se añadirá un espacio antes y después de los corchetes.*

3. **htmlWhitespaceSensitivity:** *Controla cómo Prettier maneja el espacio en blanco en ficheros HTML. El valor `"css"` significa que el espacio en blanco se manejará de acuerdo con las reglas de CSS.*

4. **insertPragma:** *Si está habilitado (`true`), Prettier insertará un pragma al inicio de los ficheros que han sido formateados. En tu caso, está deshabilitado (`false`).*

5. **bracketSameLine:** *Indica si la etiqueta de apertura de un componente JSX debe estar en la misma línea que el contenido. Con el valor `false`, se coloca en una nueva línea.*

6. **jsxSingleQuote:** *Define si se deben usar comillas simples o dobles en JSX. `false` significa que se usarán comillas dobles.*

7. **printWidth:** *Establece la longitud máxima de línea que Prettier intentará mantener. En tu caso, está configurada a 80 caracteres.*

8. **proseWrap:** *Controla el ajuste de texto en ficheros de prosa (como Markdown). Con el valor `"preserve"`, se mantiene el ajuste de texto tal como está.*

9. **quoteProps:** *Controla cuándo se deben usar comillas en las propiedades de los objetos. Con el valor `"as-needed"`, solo se usarán comillas cuando sea necesario.*

10. **requirePragma:** *Si está habilitado (`true`), Prettier solo formateará ficheros que contengan un pragma específico al principio. Está deshabilitado en tu configuración.*

11. **semi:** *Define si se deben usar punto y coma al final de las declaraciones. Con `true`, se incluirán puntos y coma.*

12. **singleQuote:** *Controla si se deben usar comillas simples en lugar de comillas dobles. Tu configuración está en `true`, por lo que se usarán comillas simples.*

13. **tabWidth:** *Define el número de espacios por tabulación. En tu caso, está configurada a 4.*

14. **trailingComma:** *Controla si se deben incluir comas finales en listas y objetos. Con el valor `"all"`, se añadirán comas finales donde sea posible.*

15. **useTabs:** *Indica si se deben usar tabulaciones (`true`) o espacios (`false`). En tu configuración, se están usando espacios.*

16. **endOfLine:** *Controla el tipo de final de línea que se debe usar. Con el valor `"lf"`, se utilizarán saltos de línea de tipo LF (Line Feed).*

17. **embeddedLanguageFormatting:** *Controla si Prettier debe formatear el código de lenguajes embebidos automáticamente. El valor `"auto"` significa que lo hará cuando detecte esos lenguajes.*

---

## ***Overrides***

*La sección `overrides` permite definir configuraciones específicas para diferentes tipos de ficheros:*

- **HTML:** *Usa `printWidth` de 120 y coloca corchetes de apertura en la misma línea.*
- **CSS:** *Configuraciones similares a HTML, con un `printWidth` de 120.*
- **JavaScript:** *Usa el parser de Babel y un `tabWidth` de 2.*
- **TypeScript:** *Utiliza el parser de TypeScript y un `tabWidth` de 2.*
- **Python:** *Usa el parser de Python, `printWidth` de 88 y un `tabWidth` de 4.*
- **PHP:** *Usa el parser de PHP, con la versión 7.4 y un `tabWidth` de 4.*
- **Lua:** *Usa el parser de Lua con un `tabWidth` de 2.*
- **Rust:** *Usa el parser de Rust, con un `printWidth` de 100 y un `tabWidth` de 4.*
- **C:** *Usa el parser de C y un `tabWidth` de 4.*
- **YAML:** *Usa un `tabWidth` de 2, `printWidth` de 40 y comillas simples.*

---

### ***Conclusión***

*Esta configuración de Prettier proporciona una guía clara sobre cómo formatear tu código de manera consistente en múltiples lenguajes y formatos. Puedes ajustar estas opciones según las necesidades específicas de tu proyecto o las convenciones de estilo que desees seguir.*
