<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# ***Limpiar Toda La Caché, Vistas Compiladas, Configuración, Rutas Y Archivos Basura Generados Por Laravel**, Puedes Usar Estos Comandos Artisan. Esto Es Útil Cuando Notas Comportamientos Extraños, Cambios Que No Se Reflejan O Simplemente Quieres Dejar Limpio El Entorno*

---

## **Comando Completo Para Limpiar Todo En Laravel**

**Ejecuta lo siguiente en la raíz de tu proyecto:**

```bash
php artisan optimize:clear
```

```bash
php artisan optimize:clear

   INFO  Clearing cached bootstrap files.  

  events .................................................................................................................................. 1ms DONE
  views ................................................................................................................................... 2ms DONE
  cache ................................................................................................................................... 2ms DONE
  route ................................................................................................................................... 0ms DONE
  config .................................................................................................................................. 0ms DONE
  compiled ................................................................................................................................ 0ms DONE
```

---

### **¿Qué limpia `optimize:clear`?**

*Este comando **borra en una sola línea**:*

| *Caché eliminada*         | *Descripción*                                              |
| ------------------------- | ---------------------------------------------------------- |
| *Config cache*            | *Cache de archivos de configuración (`config:cache`)*      |
| *Route cache*             | *Cache de rutas (`route:cache`)*                           |
| *View cache*              | *Vistas compiladas de Blade (`view:clear`)*                |
| *Event cache*             | *Eventos cacheados (`event:clear`)*                        |
| *Compiled services*       | *Archivos generados por el optimizador (`clear-compiled`)* |
| *Package discovery cache* | *Cache de los paquetes cargados (`package:discover`)*      |

---

## **Comandos Individuales (Por Si Quieres Borrar Partes Específicas)**

```bash
php artisan config:clear     # Limpia cache de configuración
php artisan route:clear      # Limpia cache de rutas
php artisan view:clear       # Limpia vistas Blade compiladas
php artisan cache:clear      # Limpia la cache general de la app (ej. Cache::put)
php artisan event:clear      # Limpia eventos cacheados
php artisan clear-compiled   # Borra archivos de bootstrap/cache
php artisan package:discover # Vuelve a descubrir proveedores de servicios
```

---

## **También Puedes Borrar Manualmente Archivos De Cache**

```bash
rm -rf bootstrap/cache/*
```
