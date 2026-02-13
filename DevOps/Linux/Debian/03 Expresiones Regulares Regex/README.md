<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->
# ***Expresiones regulares***

1. ***Usando `*` para coincidir con cero o más caracteres:***

   *- Eliminar todos los ficheros en el directorio actual:*

   ```bash
   rm ./*
   ```

   - *Eliminar todos los ficheros `.py` en el directorio actual:*

   ```bash
   rm *.py
   ```

   - *Eliminar todos los ficheros que comienzan con `f` en el directorio actual:*

   ```bash
   rm f*
   ```

2. **Usando `?` para coincidir con un solo carácter:**

   - *Eliminar todos los ficheros `.py` con un solo carácter en el nombre:*

   ```bash
   rm ?.py
   ```

   - *Eliminar todos los ficheros `.py` que comienzan con 'a' seguidos de un solo carácter:*

   ```bash
   rm a?.py
   ```

3. **Usando `[]` para coincidir con uno de los caracteres incluidos:**

   - *Eliminar los ficheros `fA.py`, `fB.py` y `fC.py`:*

   ```bash
   rm f[ABC].py
   ```

   - *Eliminar ficheros `.py` que comienzan con 'f' y no terminan en A, B o C:*

   ```bash
   rm f[^ABC].py
   ```

   - *Eliminar ficheros `.py` que comienzan con 'f' y terminan en un dígito. Asignar rango:*

   ```bash
   rm f[0-9].py
   ```

4. **Usando `{}` para coincidir con una de las cadenas incluidas:**

   - *Eliminar los ficheros `fAB.py` y `fDC.py`:*

   ```bash
   rm f{AB,DC}.py
   ```
