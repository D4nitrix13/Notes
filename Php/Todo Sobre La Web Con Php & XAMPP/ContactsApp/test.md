<!-- Author: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Email: danielperezdev@proton.me -->

# **Explicación de `<?php`, `?>` y `<?=` en PHP con comentarios**

- **El código PHP utiliza delimitadores específicos para identificar bloques de código PHP dentro de ficheros que también pueden contener HTML, CSS o JavaScript. A continuación, se explican estos elementos con ejemplos:**

---

```php
<?php
// Este es el delimitador de apertura estándar de PHP.
// Todo el código que sigue se interpreta como PHP hasta que se encuentra el delimitador de cierre "?>".
echo "Hola Mundo"; // Imprime "Hola Mundo".
?>
```

---

```php
<?php
// Puedes escribir cualquier código PHP aquí.

?>

<!-- Fuera de los delimitadores, todo se trata como HTML estático. -->
<p>Esto es HTML</p>
```

---

## **`<?php`**

- **Significado:** *Este es el **delimitador de apertura** de un bloque de código PHP.*
- **Propósito:** *Señala el inicio de una sección de código PHP dentro de un fichero que puede contener otros lenguajes (HTML, CSS, JS, etc.).*
- **Uso estándar:** *Es obligatorio usar `<?php` en la mayoría de los entornos porque es el más ampliamente soportado.*

---

### **`?>`**

- **Significado:** *Este es el **delimitador de cierre** de un bloque de código PHP.*
- **Propósito:** *Marca el final del código PHP. Después de esto, el resto del contenido se interpreta como HTML o texto plano.*
- **Importante:** *En ficheros **solo PHP** (como ficheros de configuración o scripts), es común omitir el delimitador de cierre `?>` para evitar problemas con caracteres adicionales al final del fichero.*

**Ejemplo:**

```php
<?php
echo "Hola Mundo"; // Código PHP.
?>
<p>Esto es un párrafo HTML.</p> <!-- Código HTML -->
```

---

#### **`<?=`**

- **Significado:** *Este es un **atajo** para `<?php echo`.*
- **Propósito:** *Se utiliza para imprimir valores o resultados directamente. Es útil para simplificar el código, especialmente al incrustar variables o expresiones dentro de HTML.*
- **Ejemplo equivalente:**  
  *`<?= $variable ?>` es igual a `<?php echo $variable; ?>`.*

**Ejemplo:**

```php
<?php
$nombre = "Daniel";
?>

<!-- Con <?= -->
<p>Hola, <?= $nombre ?>!</p> <!-- Esto imprime: "Hola, Daniel!" -->

<!-- Equivalente usando <?php echo -->
<p>Hola, <?php echo $nombre; ?>!</p> <!-- También imprime: "Hola, Daniel!" -->
```

---

### **Resumen**

1. **`<?php`:** *Marca el inicio del código PHP.*
2. **`?>`:** *Marca el fin del código PHP.*
3. **`<?=`:** *Es un atajo para imprimir contenido con `echo`. Es equivalente a `<?php echo`.*

- *Estos delimitadores hacen que PHP sea flexible y fácil de integrar con otros lenguajes.*
