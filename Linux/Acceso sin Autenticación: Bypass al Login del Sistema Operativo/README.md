<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- GitLab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Acceso sin Autenticación: Bypass al Login del Sistema Operativo**

---

## **Acceso a funcionalidades avanzadas de VirtualBox en Linux**

*Para poder usar características avanzadas de **VirtualBox** (como dispositivos USB, carpetas compartidas, etc.), es **necesario** que tu usuario pertenezca al grupo `vboxusers`.*

*Este grupo da los permisos adecuados para interactuar con componentes que requieren acceso a bajo nivel, como el controlador de USB.*

---

### **Pasos para agregar tu usuario al grupo `vboxusers`:**

```bash
sudo usermod -aG vboxusers $USER
```

* *`sudo`: ejecuta el comando como superusuario.*
* *`usermod`: utilidad para modificar una cuenta de usuario.*
* *`-aG`: opción para **agregar** (`a`) al usuario a un **grupo secundario** (`G`) sin eliminar los grupos actuales.*
* *`vboxusers`: nombre del grupo al que queremos unirnos.*
* *`$USER`: variable que representa tu nombre de usuario actual.*

---

### **Actualizar la sesión del grupo sin reiniciar completamente:**

```bash
newgrp vboxusers
```

* **`newgrp`:** *cambia temporalmente al grupo especificado en la terminal actual.*
* *Este comando **actualiza los permisos del grupo sin tener que cerrar sesión**, pero solo afecta a esa terminal abierta.*

> [!NOTE]
> *Esto no afecta otras sesiones o terminales. Para aplicar completamente el cambio a todo el sistema (y GUI como VirtualBox), **debes cerrar sesión y volver a iniciar**.*

---

### **Verifica si tu usuario ya está en el grupo:**

```bash
groups
```

* *Muestra todos los grupos a los que pertenece el usuario actual.*

*Si **no ves `vboxusers` en la lista**, prueba **cerrar sesión y volver a iniciar**, ya que el cambio no se refleja hasta que el entorno gráfico recarga la sesión del usuario.*

---

### **Ejemplo completo**

```bash
# Agregar Al Grupo
sudo usermod -aG vboxusers $USER

# Actualizar Permisos En Esta Terminal (Opcional)
newgrp vboxusers

# Verificar Grupos
groups

# Si No Aparece El Grupo vboxusers, Cerrar Sesión Gráfica Y Volver A Entrar
```
