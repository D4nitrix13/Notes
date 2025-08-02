<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Almacenamiento de Ficheros en Laravel (Imágenes)**

## **Objetivo**

*Permitir que los usuarios suban una imagen de perfil (o cualquier archivo) desde un formulario y almacenarla en el **disco del servidor**. La ruta del archivo se guarda en la base de datos, y **no el archivo como tal en binario**.*

---

## **1. Formulario para subir la imagen**

**Ubicación del archivo: `resources/views/contacts/create.blade.php`**

### **Código**

```php
<div class="row mb-3">
    <label for="profile_picture" class="col-md-4 col-form-label text-md-end">Profile Picture</label>
    <div class="col-md-6">
        <input id="profile_picture" type="file"
        class="form-control @error('profile_picture') is-invalid @enderror" required name="profile_picture">
        
        @error('profile_picture')
        <span class="invalid-feedback" role="alert">
            <strong>{{ $message }}</strong>
        </span>
        @enderror
    </div>
</div>
```

- **Explicación**
  - *`type="file"`: Define que el input permite seleccionar un archivo desde el dispositivo del usuario.*
  - *`name="profile_picture"`: Nombre con el cual se accede al archivo desde el backend (`$request->file('profile_picture')`).*
  - *`@error('profile_picture') ... @enderror`: Blade directive que muestra errores de validación si existen.*
  - *`class="@error(...) is-invalid"`: Aplica la clase de Bootstrap para marcar el campo como inválido visualmente.*

> [!IMPORTANT]
> **Importante:** *Asegúrate de que el formulario use `enctype="multipart/form-data"` para que los archivos se envíen correctamente:*

```php
<form method="POST" action="{{ route('contacts.store') }}" enctype="multipart/form-data">
```

---

## **2. Mostrar la imagen desde el almacenamiento**

```php
<div class="d-flex justify-content-center mb-2">
    <img src="{{ Storage::url($contact->profile_picture) }}" class="profile-picture">
</div>
```

- **Explicación**
  - *`Storage::url(...)`: Convierte una ruta interna del disco (por ejemplo: `public/images/miimagen.jpg`) a una URL accesible públicamente.*
  - *`$contact->profile_picture`: Valor almacenado en la base de datos (ruta relativa del archivo).*

> [!NOTE]
> *Asegúrate de haber corrido `php artisan storage:link` para crear el **enlace simbólico** entre `storage/app/public` y `public/storage`.*

---

## **3. Migración para agregar campo de imagen en la base de datos**

### **Comando para crear migración**

```bash
php artisan make:migration add_profile_picture_to_contacts_table
```

### **Explicación del comando**

- *`make:migration`: Crea una nueva migración.*
- *`add_profile_picture_to_contacts_table`: Nombre descriptivo.*
  - *La convención `add_<campo>_to_<tabla>_table` ayuda a Laravel a detectar que quieres modificar una tabla existente.*
  - *Laravel generará el archivo automáticamente en `database/migrations/`.*

### **Dentro del archivo generado `database/migrations/2025_06_18_005935_add_profile_picture_to_contacts_table.php`**

```php
<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     *
     * @return void
     */
    public function up()
    {
        Schema::table('contacts', function (Blueprint $table) {
            $table->string(column: "profile_picture")->default(value: "profiles/default.png");
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::table('contacts', function (Blueprint $table) {
            $table->dropColumn(columns: "profile_picture");
        });
    }
};
```

> *El campo se define como `string` ya que almacenará la **ruta del archivo**, no el binario.*

### **Luego ejecutamos la migración**

```bash
php artisan migrate
```

**Salida esperada:**

```bash
INFO  Running migrations.

  2025_06_18_005935_add_profile_picture_to_contacts_table ............................ 4ms DONE
```

---

## **4. Guardar la imagen desde el controlador**

**En tu método `store()` del controlador `ContactController`. File `app/Http/Controllers/ContactController.php`:**

```php
if ($request->hasFile(key: "profile_picture")) {
    $path = $request->file(key: "profile_picture")->store(path: "profiles", options: "public");
    $data["profile_picture"] = $path;
}
```

### **Explicación**

- *`hasFile(...)`: Verifica si se subió un archivo.*
- *`file(...)`: Accede al archivo como instancia de `UploadedFile`.*
- *`store('profile_pictures', 'public')`:*

  - *`profile_pictures`: Carpeta dentro del disco `public` donde se almacenará el archivo.*
  - *`'public'`: Nombre del disco (configurado en `config/filesystems.php`).*
- *El valor retornado (`$path`) es algo como: `profile_pictures/abcd123.jpg`, y es lo que se guarda en la base de datos.*

---

## **Validación de Archivos en Laravel**

- **Código `app/Http/Requests/StoreContactRequest.php`**

```php
$request->validate([
    'profile_picture' => 'required|image|mimes:jpeg,png,jpg|max:2048',
]);
```

---

## **Explicación General**

*Esta línea valida la entrada enviada desde un formulario antes de procesarla en el backend. Laravel lanza automáticamente una redirección con errores si alguna validación falla, y los errores se pueden mostrar en la vista con `@error`.*

---

## **Desglose del Código**

- *`$request`: Instancia de `Illuminate\Http\Request` que representa la solicitud HTTP entrante.*
- *`validate([...])`: Método que aplica reglas de validación al array especificado. Si alguna regla falla, Laravel redirige automáticamente de vuelta al formulario y muestra los errores.*

---

## **Reglas Aplicadas a `'profile_picture'`**

```php
'required|image|mimes:jpeg,png,jpg|max:2048'
```

*Esto es una cadena de reglas separadas por `|`. Cada regla valida una condición:*

### **`required`**

- *La imagen debe estar presente en la solicitud.*
- *Si el campo está vacío o no se envió, la validación falla.*

### **`image`**

- *El archivo debe ser una imagen.*
- *Laravel verifica que el MIME type sea uno de: `image/jpeg`, `image/png`, `image/gif`, `image/webp`, etc.*

### **`mimes:jpeg,png,jpg`**

- *Restringe los tipos de archivo permitidos específicamente a:*

  - `image/jpeg` (`.jpeg`)
  - `image/png` (`.png`)
  - `image/jpg` (`.jpg`)
- *Evita que se suban otros formatos como `.gif`, `.bmp`, etc.*

### **`max:2048`**

- *Tamaño máximo permitido del archivo: 2048 kilobytes (KB), es decir, **2 MB**.*
- *Si el archivo supera este límite, la validación falla.*

---

### **Configuración de Carpeta y Validación de Imagen por Defecto en Laravel**

- **Objetivo**

*Crear una carpeta específica para almacenar imágenes de perfil (`profiles/`) dentro del almacenamiento público de Laravel, añadir una imagen por defecto, excluir selectivamente archivos en `.gitignore`, y establecer las reglas de validación para la imagen en el formulario.*

---

## **1. Crear la Carpeta para Imágenes de Perfil**

```bash
mkdir storage/app/public/profiles
```

- **Explicación**

- *`mkdir`: Comando de terminal para crear directorios (folders).*
- *`storage/app/public/profiles`: Ruta interna en Laravel donde se almacenarán las imágenes de perfil. Este directorio:*

  - *Es parte del **disco `public`** definido en `config/filesystems.php`.*
  - *Debe tener permisos de escritura para que Laravel pueda guardar archivos.*

> [!NOTE]
> *Luego debes ejecutar `php artisan storage:link` si no lo has hecho antes, para que los archivos sean accesibles públicamente desde `public/storage/profiles`.*

---

## **2. Agregar Imagen por Defecto**

**Coloca manualmente un archivo llamado `default.png` dentro de la carpeta:**

```bash
storage/app/public/profiles/default.png
```

*Esta imagen servirá como **foto por defecto** cuando un usuario no suba ninguna.*

---

## **3. Configurar `.gitignore` para incluir solo archivos deseados**

**Ruta del archivo: `storage/app/public/.gitignore`**

### **Contenido recomendado:**

```bash
*
!.gitignore
!profiles/
!profiles/default.png
```

### **Explicación línea por línea:**

| **Línea**                 | **Descripción**                                                                   |
| ------------------------- | --------------------------------------------------------------------------------- |
| *`*`*                     | *Ignora todos los archivos en este directorio y subdirectorios.*                  |
| *`!.gitignore`*           | *¡Exceptúa el mismo archivo `.gitignore`! Para que Git no lo borre ni lo ignore.* |
| *`!profiles/`*            | *¡Incluye la carpeta `profiles/` aunque esté dentro de `*`!*                      |
| *`!profiles/default.png`* | *¡Incluye solo la imagen por defecto dentro de `profiles/`!*                      |

> [!IMPORTANT]
> *Esta configuración garantiza que la imagen por defecto se mantenga en el repositorio sin subir imágenes de usuarios reales.*

---

## **4. Añadir regla de validación para imagen en `StoreContactRequest`**

**Ruta: `app/Http/Requests/StoreContactRequest.php`**

### **Código modificado:**

```php
public function rules()
{
    return [
        "name" => "required",
        "phone_number" => "required|digits:9",
        "email" => "required|email",
        "age" => "required|numeric|min:1|max:255",
        'profile_picture' => 'required|image|mimes:jpeg,png,jpg|max:2048',
    ];
}
```

### **Detalles de `profile_picture`**

- **`image`:** *Valida que el archivo sea una imagen (jpg, png, etc.).*
- **`nullable`:** *Permite que el campo esté vacío (es decir, no obligatorio).*

> [!NOTE]
> *Este Request debe estar vinculado al controlador para que se aplique. Ejemplo:*

```php
public function store(StoreContactRequest $request)
{
    $data = $request->validated();
    if ($request->hasFile(key: "profile_picture")) {
        $path = $request->file(key: "profile_picture")->store(path: "profiles", options: "public");
        $data["profile_picture"] = $path;
    }

    // dd(Storage::url(path: $path));
    $contact = auth()->user()->contacts()->create($data);
    return redirect(to: "home")->with(key: "alert", value: [
        "message" => "Contact $contact->name saved successfully",
        "type" => "success"
    ]);
}
```

---

## **Uso de `enctype="multipart/form-data"` en Formularios con Archivos**

- **Objetivo**

*Comprender la importancia de declarar correctamente el tipo de codificación (`enctype`) del formulario al trabajar con archivos en Laravel, y visualizar su impacto en los datos enviados al servidor.*

---

## **1. Qué sucede si no usamos `enctype="multipart/form-data"`**

### **Formulario incorrecto (sin enctype)**

```php
<form method="POST" action="{{ route('contacts.store') }}">
```

- *Si se envía el formulario sin `enctype`, los datos del archivo **no se enviarán correctamente** al servidor.*
- *Laravel no podrá procesar el archivo, aunque haya sido seleccionado.*

---

## **2. Ejemplo: Enviar un formulario con campos vacíos y una imagen cargada**

### **Datos enviados (formulario SIN `enctype`)**

- *`name`: vacío*
- *`phone_number`: vacío*
- *`email`: vacío*
- *`age`: vacío*
- *`profile_picture`: imagen seleccionada `image.png`*

### **Vista desde herramientas de desarrollador (Request Payload en pestaña Network)**

```bash
_token=ePXQ0RxEsPzTikIZccWUne4tT9WFMum3RvQ9hWse&name=&phone_number=&email=&age=&profile_picture=image.png
```

> [!WARNING]
> ***Observación crítica:** El archivo **no se envía en binario**, solo aparece su **nombre**, como si fuera texto plano. Laravel no podrá acceder al archivo real a través de `$request->file(...)`.*

---

## **3. Solución: Agregar `enctype="multipart/form-data"`**

### **Formulario correcto**

```php
<form method="POST" action="{{ route('contacts.store') }}" enctype="multipart/form-data">
```

### **Explicación de cada atributo**

| **Atributo**                     | **Función**                                                                                                             |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| *method="POST"`*                 | *Usa el método HTTP POST.*                                                                                              |
| *action="{{ route(...) }}"`*     | *Define la ruta donde se enviará el formulario.*                                                                        |
| *enctype="multipart/form-data"`* | ***Indica que el formulario incluirá archivos binarios**. Necesario para que el backend reciba archivos correctamente.* |

### **Vista del Request ahora (formato multipart)**

- **En la pestaña *Network → Headers → Request Payload*, ahora verás:**

  - *Cada campo separado por delimitadores `------`*
  - *La imagen `image.png` se muestra con su contenido binario (tipo MIME, tamaño, etc.)*

> [!NOTE]
> *Laravel ya podrá acceder al archivo correctamente con `$request->file('profile_picture')`.*

- **Vista Previa No Legible Para Humanos**

```bash
------geckoformboundary8b16d4e7cd276021ba6835fc52c18c21
Content-Disposition: form-data; name="_token"

ePXQ0RxEsPzTikIZccWUne4tT9WFMum3RvQ9hWse
------geckoformboundary8b16d4e7cd276021ba6835fc52c18c21
Content-Disposition: form-data; name="name"


------geckoformboundary8b16d4e7cd276021ba6835fc52c18c21
Content-Disposition: form-data; name="phone_number"


------geckoformboundary8b16d4e7cd276021ba6835fc52c18c21
Content-Disposition: form-data; name="email"


------geckoformboundary8b16d4e7cd276021ba6835fc52c18c21
Content-Disposition: form-data; name="age"


------geckoformboundary8b16d4e7cd276021ba6835fc52c18c21
Content-Disposition: form-data; name="profile_picture"; filename="joker.png"
Content-Type: image/png

PNG

   
IHDR  o  ù   ¾Ków   sBITÛáOà    IDATxÚìÝy|SUÚ8ðçÞ{³§IÚ´iîÝ([ÙA)0 *¢"3*Ê:"¿ÑqftÞwÔaæõ}]æ£8£Î0â¸¨0"
,R
Bº¥KÒ¦if_nrß](Ð%¶©ð|?~üÐäÞsÏ=9Io>÷9DæB!B!B
tB!B!Bý `4!B!B!ÐÐ0B!B!BhhMF!B!B!44&#B!B!FB!B!4D¤;pµÂEKÛáEúÔB!B! RµJEÇqøÊt8]<²tZu
ú¡Nëc£Ò¥A6$Dz0®Bî6É¶:§~¿BCl<â+Ã{oâd¸ª
k2PyÛ­7§§§B!©TråG·Û$IÖÕÕðÑ§¡P Ì #=&!B!"gL\QUëõú¼^ßH5+ð~nNæ÷Å§8.8Ðf¤´1»î&_'ë³²«_ÎðtÆêäÒWª¾_Q8ò+a¾7»?*k¼>'ÃÕJ àøL^nÖàA(þ÷o'b¤{uÅ7ÿé½^/FB!B¡ñ Ù3§ùþäèbîìièÿè$1ù±ìS/TFz®!S{ò+ú}j&W{oâd¸Æ2(üý3ÿE£XÖ8
ýöéÍTtL\¤Ç!B!BIMÑ67·z}£xètºâãTVýÒ§´ÕÆ£<\FOÌd£ÁuéSc0Ð¸âtºÔ¼7q2\k·Ü¼B«IÕ£!Jp>B!Bh¼S*ä£0òx}J¥¼ß§¢Ò%¾N%)_'+OöûÔL4®x¼¾èÞ8®5Lì YcÐì £»
_ÊdxIOI29¡N3øu¬¿ÉÏ]FsEüLGD(:áeÏxýÃmáîÄ( $làGzûàß,ã A !$zþ
Õ°x¸¯Öìuùa|@é±Â)©ÒX-§cd
Y\¦o¥Á}¬ÆfÂ¿ #B!Ð5,àF»"ª×ëpý}O' èbbòóu²A6\ºßL4®x½¾@ ÿNkÍ@a4j%÷Ñ&+(²H"ÈåÓ0"¢)2b~¹Ï¿ËáqZ¦´>A\/æÓ=£Eg½þaì  $Gæ0ÂÙZ ©à$A@çÿ
A <_×ÙN·º;VZ%ÿ®¹ê2 èi  '¯xpöÎñ÷¯&ÏH¿P!B!~ ¤RñXEÒßQB R#= ×"Zý<Æf2 qe 'Ã5¨ß=
I$cókB2*ÑäLw{*"Ç§µ<jÕeáÂÍê.dè>Í*(2OWúÜkcºBÉ$I¾ûìþ7"Hbb¼¨@#9Údÿû1S ìùÂ\ùC7hhÑû]ÇêiHLËå§H^ú´ñàÙÎzB!B!B(|#M( WËD}©e­®=Ày¡X¥âQé%%I ¢ÈËÅ[Ìp¯$Àlÿ¢çùÃ&_e<ôÆç»{tö@(ÔÍ&!M&F1 QBÄëÉYÍIÉ¼ÿÛo'ü£IÑ÷_OÝë@NÕÚëMÆv/MI*AfhZ¬+¸Ì§É'nKõ²ÁâjÛ¿j!B!B¡kßaµ*`¸;p4YCS·ö %Ü»§­O96  "X%J¤yv.ø®ÕfïD#îÿqûæøA$1¦Ã)ÁLvgNvr¬äÿÔÛ¼~Ò¨Ubúæ<åüTiWP¸ A|÷ôØmÅ¦Á,¹a@ IÐ&ç+_êÛí¢JSykJJ ~sGê¯T´Û°^B!B¡ bÒ§ÎV©WHhð:ÚÕÅªëðFºghÌæ®Z«¼à±ñÄ®ß0¦pMÄhâ® ·ÓØÚá
DºK(²<­¥»>ÞsÒè $ÏY¾biAöî#M^!öFh+|þmî~£¼î`èV×õbA±Ûç»(Ä|qwbr?°Ïå"dD$$1_*xÏâF/{WSº·ÜÛ]þ¿·Ù|yÊ®í²ûjlÍÖA§HâEuõáSæ7÷µô»e½Ñóó7ª¾3}Z¦ ø4yÿÍ?Ô]ökB!Bè*ÄÊY²ú¶9Ú>RUÊ´)Ó5ø`ç75¶Q
!±ÊÌÛbà¬¾þ ;  |öN­ÜÕQ÷¹Åsu-FMJ)(tW½iòd$NYÂÕ¼Öâtúå³[:] CÀeµ³R!pvv¸7FÄYç'4íÿ¶îê(ã/jê­ën+÷}¬³l×?>9Ññ(Ç,{öÅeõÏ<úÆÈÇfüâÍMì_ï~µ$Òç6úµ{ÞÿìdGÏÎÆ#ì*~² 1Ü$å&OàÓ <ªëßV.ø}°O(.ß8ñ·ÑtC]ÿ.v³ô²ó¥BP®QØ=p/ô.¦Öö=U{xÚ'cf¦H»¶¿eRô+ß¶´ñÂ\ylÝ\Õê~k_Ë -û¡ÿùP÷ÖÏó¢Ä< ¯Ø¶¯¥Å²!B!ºPÖÜ=GÝÿÂë~"Ø¶mgÍp2±)äõûVÎJNÆÚn.ðºH~Z|ÖJ¨¾²28ù&yáîïk*F:Å¶¹­zGhÜ¦}sÖêµÒ'Qõûv~Ý¼âÇ×'wVÐ9G.,Ë_<ôâG­g÷}SãN;ýÉâ6ï0«~LÒßÔj7à4þH´òS¬Ø^¦svÅ@ ½ñÄscrCÊ¯þqqLÏO¬¯ÝP²kÛ»«"ý^¾8OWt\øPÀp¢Ì8#1%ÌåVG2Ã?ßÚA/nÎqXæôTL¶]¹ÙyRIse/,îpÛê©LalKtç2aßú¾mZ¡$¦$JHJ¼Ev÷xï°qÈ¡òø¸GM÷.Nèú±hrô¶oZÚ !B!Ð5'8*Êf«ºîUv«uÆNoäÃ@À+KÀ5Y´vGÓVúöxé¬äth¨;èéøOÿ¶duZ|æÊPÍçW¡°7üÓèèsBÁá.¡4|¬«5Ò}0ÎQ[|¤ÎÓ7ÜÊùJ ÛfôôVNÈKÖ®(<uÊ$®±Ójí÷YD%3FoñxýEþhUö4Ußf-qè¯oîk²ÏðÍËÿ·Û  MX¼îg÷>õüµjiÝ^ï¥é^o ülõ&'Óç[«bGòc="ÓîÆ{Ø®Ø«Vù¹" B)ÿ«Ç^Ñ\c³n2A ! lÝíV<%  âS)1úöþß$]}ðúgÃúãðñ[o49;Q<ÃB!BèL¹dÍÌö=ß7Þ7G^¿çã=Æ³'(u:o¸yVÈHÕJ;w2Þ
î\«¥nq{tVrº¯±îÛ°£º=Y¹<tî3«ï²Ób!¿Åiú"¡%.S$ðHà¼:KóWN@vÒ
¡PÈ³¨²ovø  ^·ÂóYU]UTÜ6!Á¤+?Ì)nÐ$d=æ}z½.  â%|³ëª{­Å¶D)¿ÅÚÚÜÕ[é/ÏØ¨ôìîd
bCù\­ëM¦ )©I)axW©ÑÌ×òZN>>c\&Îëqºû +'.+¨+ñÆåÆID|Òa8{´´M<qáuJÝWºòÉØÍâýO^W¥^ÖÂù*ýYrnûÌgGZA?ir¶V)¢Àëhk8]Z×á2vÊÉþ²*29=Z*¢9[cÉ±sþî#qÚ 1>ín9yJ'Ê*HKù¤­áÔÑr HqòäI9ñ2ôÚçJÏêlA µ×ý(ÅrB/ÊHVø´¿³òøZGÜìMUS þÑä².ó!KB¡7þþÏÎÎcQQ²ûzÍ£}þ¥H¿ 1Z Æ$>»Ù`èzµlÛQ¶øh-U,@LáÜ>?MÃg|v]É{¯þõk  hnzäæ Cå®í¯¼ÆÑ·9ÍÜÿúÝzÙîÍOîh Máî&ðuTîÿç«v Hþ~Ë¢ú7Ç¬#óûäÕwT± LöG7­ ¡øÃR>À(gHÉ Q©PwaÐR%ÊÃ_/ìÜ° {ÈsCî°«!c^OÅd ÄsþµýÞéíªhÌPä¬¨°Ï $ðê&÷fCx1:}DOeéwM24ÑÕ¦¡ÓÇ7V
mÞ-Uaæ#B!ºÚI´ê¬ëæ**¿ùbÏÎ]ÆôÛÖ-5õûÖÝ ootJbTªU¼¶`j|Oº×ÜQ·ÃìPÒÉ©ÓÝÙüas
èLMæMrÑQBÍí©ÍXùÊS[ÌüôÉy À¥ÑË¹×ë
åNoDÂ ``S»¾Pd±CçååkR28ãös'?W]
Ñ+ã£º" åâæ3o¶Ú)iâÊh¢²±ìÅªÊ}>yð`J=2¾[öµêP³(Ä¸Ô¹|ÇîÒ¿èE|&
»Jç®ñ p ¼~ÇÄ¦&t}óõþ]¨¤Ü\XômÞ(u\wTjUd¾å|:bR&ÇYO|÷ãmAR?gÊ]ñÍ»>ýÏñF:}ö4-  Ô(ýÑýûwý§¸M:)EÜsDmTSñW_}}°J>+¬;øõþ]ÇÚDéÙZ> 1gÚ¿þòÓÏwHòçäÇ]C$IN¦Î}wàËÿì+±Éò'&ð­Gè\¹ä?_]v( þ¹í¡¸\Õ÷qL¶áþubø_ÛßÃ×daß0êK*Y Îßð³ùü?m¼ë{zÏ>qÝ#Ë4  øÍ]iíOÞ¿þ±Êd+}`^ê*Ìu¬Wþëv4 LX÷å¶?yÏOïÞøüAþÂ_>²0 | 01×3OlÜðèõ)·Þ¹( &ýtÓªW}÷=¾R=??Ú§;N&8séìè¾ð´NÆ*|#Mfz³¾àH~8I¢@À  AÀ¿o²Î0¸®°ì\
³2Ñ]9ðp «AÕz§;ÐÛ~°ÿOi!Cö.îçaÃ«PÌîX¹dÿ#B!úàIä
0ãé£
¼Ìó·°+Rr¥Õ=ëmÑháèèLM% *j²\ÄÝnøÊâà§*äÑá}oS\)ö÷9XÀç5¶dÝ±`¿ó{»ÏY\#I  RÈsÚ¸X bE"ÛÖ³MgÞÔ-A §Êæáñ%Q  A sN{¾$Ie<éàLF]¿éÝ!GÙÃ@Ð©c!JÀ 3Å´ÉÜRq×Áv«o$0CÅç$IÁg5Ú9Îgm³(Òó5Ì7Ü%Ï_pËMËÎÿ·bzroPÊ­?×ê ÓlñòE":[Z¼òÄx>  )O£:ÛûÞÛXj;=>ÚDõÜ6wÀo¯­2c´êîÆíÕ? íÆÎ H.êzs¶Ôv ¶v;®{ h1;/ªÌxR_UgñÏRYÓFªcº^`»Ng@ £Í"Yøy3¶ÞüÇv¡Pøà{{c2ì
ë$bñ?¶½ÓÒr­UKá§­Øüö¿Þ|û_o~ð¯ç×Åycë  Çw/<úð3V9 Ø¯¿k Mª &-!ÓíÚVb`ÙÓï¼òêöï½-%,~üçóíÛÿïÕ LZ4_uîm% p4ìx¯Ä3wrOä¹r÷Î* ¥U-=cÌ°ïb3 køfçwí£~æãf2H²üä®%y©Ú¸xµ&sÊ{2/i8i«#ùkÄJH ÄÔH~>Îñ»#à°ëâ?¶{o$!!©2ÁqÛÐIù½¹Ãáæ&÷Ãø­'P½¹Ï._ÿbëmS*ÆK æw§ôÒ!B!FPweTiÁ
Né;½~×éAoåÔk¥1/»7©±IB ÎVjuûÉ4K| _Ùj¾ÜûQ¿îÍ´~VÙÀ£)¯ÏÛ'°y} tmðûºJzí-(&$Öçü
c$|àâ%Éêä ø|å8UbWÒ.Iñ½2mÞ®£)1Cz}lÏ|mþ`â¥]äü®î³B H JÌÚü=CîuÊQþ^LÒôY2°W­·r ¶ê²i7¤L5µÆø½aÄîè¿´nr°w9=Îçë³   `mlõ¥%¨è½_ "Í§M¾9¡ÛáîjIh¿ÓÕlvÛ½ ºvw7ÝÏØ8òû¼=r>/×»
 @"b óW¤õ9^»N ð{½Ý'Áq `wKKë¶½{ïº?¸áÞ×·þ3=°aT"ùç¶77ëGî8?>Ãw=uèÅw¬ûÝo¥¿ûãn0isï]·pR ÏçC  H5Ñ|¹½§¶¡x¿ b I»óçóÓZÞýÅþ®ð²T-c²7ýkû¦óÇ2hb  àpØ»'½Ï]SN&½¥'4Ýbè¸Êîá/ç^·:÷ºËÜ{$£ÉÎ`HB BFöÈP¦ bº ;é¹)l\\c©ÔÉ.W Ñ¢wÈ_M=KðLPwAB(ßzIJ~O]fÂìê¿xt¹|A"HBÃçD bª(F,èþ4k2Û5cB!B©³Ãê ä3Ì,{ÿotk¥
 ¼MG¾9ÁË»»'ôéhïpr4JI_-âqºÞLt{bLøk5»íìå×Mv4n7/ Î3Èöê>VÈ¥óòò¼X¾ÄånuyÁ,$$Æ«sq@*'Ç-µÛ\. ¾<kcLßFzÎêÂÆyáfX<"Æ$L/°Ú &I àÓ7ÚS²T9sòë?9iºìâ"ÕM­©Í;/>Ö»µ*º£¢­ÀÉ@Ñ¤ðrÎsµ]ø`øwø_.]Cã¿Þ~oÝ=?~ðûL*{û÷t
£~àq©oÝdÃVsLÚæË'ìÞ*}ðñÛÓNÿõß `ÆÏß~dÐVFÚPÙ>aÅßuå&ûÀÇ~å¿_¼e¤OøBæÒOTÔ¬ÝN|¹6£`ÎÜê0G2¸=ÿÃ8õTÍï ÎsõóW@(tÜîí
àÆ
x¤aÌâ|@yèmÉ¾uØX@ÝËëù¸`­iÀÏÓr½³«"3¡&§I!sså½ÿ>ÓxUÕìG!B!tùÆÖ£øYw.×6üÿyùõ}áo_9³ö¾°VÒêI*^¾*NÂ:¾o¬;æáÄ"ÍªDU4øë[jv_Á| ²&Ö×û
pÀÙü/èMlðõÚ.ÞkrzcÅÊ$!Ñêb!èlHR£¤ AÎÀÇ3.  +ôÌàìlP@3=ÄÒaS® E÷4ÉÄU¥&vÚ¼% <çú%7¯üÑÍ+tóòyY2 à©§OÏËúÉ²é[|ÄX¥6nkj$Ñïvúi¸'ÔKJÄp;Üa¤^§F¯Êãç~ñ+TW¯{çßïKÄbyTÔ;ÿ~¿¦¦nÌ=Þ1|>Mj¿£tGIW²pZvB×Îa0ûø ¿ò¤Í»}Õ  ¶ã»­ÏÿÏ«_:f¬` f$h4½ÍFk·Ù%ôl3êu{En28«w½ùÒë©ì
%Ïª/?øÁ/m;ÔÞFò¬²O4yD 
¯Ðð ybA AÎP¨ÜÓÿG¬PwáÐõ1â¡í©Yn7Èî½ÌM¾~¼O$AÄéfWpï«í½Å.ZÈðx!¢eô=z<pÆrcB!Bèja«ØWÒ»4ë
¿üùÏ~ró-K&gNYpCbw¼Ì£;vDç½N2YÊªx© èü¾±î £±+Ôqd ¾µæóNÏhÜDÞÜi± Õ$<
@,+]§õÒÙÝNP5ïiò¯ÅCdFË)·Õ Ö$1RÊg
¹ IË. ´8qìL!"x1ê¤pC±î«P' ¤x¦JÎ%ø¨ìYUÇIy 3ge)F(L "ÑÿñqØÛ|Êìª½±mÐéÐ7»åòâD$ _£&Ûú.Ù7|ÁöÆV¿*'7^Dð¢R¦,^8I;Xb2~GPðì\uí×¶¾ö·7ÏU×L?L|Y´F Ñ$h4fÜ³~±¦ãôwçÀÞa´I  fÆú;sÀÑ2)Àé}ÅöwÎÕH¥I?yàe9LÏ]
> Ýoì2OÞ°~~Àé}Åí +îY¨a Å<õìÝ¤¸U§Ïù4nÀ4mùÍ3TcQé¢W$&C óä®*wà¬Ù÷ÞîZG
äaØÞÏii
 øqLôÕ5Ð ®ó¸}<äòi  tÌåh;[ Xád'Fñ$2¤L¼×:TYábCT×z$A ¼fzìü¬( Ùø`Eç¯WÇ+ø@ Ñü
Ë´[¾hhcEüòÖÓÝÝâs¶F¬tB!B¨WàãÝê{oÎèIÅ(T¦#ë²»ï\vTíÚYÒ:ªU<Ç9KôuÝ ðOøZë>·J( ÀkØa ÄçýGBÀ]ÓV÷£¿h¯­POôµ5  L.¯X)Õµ¹8 ð÷µËk'þ"ä7Ù»sSRnJ×~XkîÛÏÑ¸»3mIÊ¤Y!_µ¹Ä)-+¾ÒJµI·OPüR£±Y¬ g·+$<)nðp?9??¦î»¶+/LI3fÿ(ãÂÇÚÏ|q¨i}lMíþT¾¾¦}èºõì÷§©É¹7ÜXHq^«©úpiëm¥ÇOMÎ´pÉ¼Ööc§õþ+]ØZlÉ¹ó)+¿ÿ¶Æ~Åc `l3]y#ÃxáòxÇ ¨:  ð57<ñÒ
]ÿöÙ
ºâWã4°Ûéß¹ùí;}¥½þBYÑï~¶îÅÙ7þõ?oßôÈOÝú3`
»^~åú¤©ÿ¯LÞüÀ¹>üÆoÁÛýûOùà3Ô~åÕÏt¤xû_ÿ|Ý#Ïo{}ñ»'¬Ûc=üÖâÚÁoO±V«îÌ¦¢%"sÂÄìXº_)éýLm
pØÝí?44u»L$§H;Üfu¹þ??hù< Äs­VÏÀqç41ýpA';=ï4Ú``/Í×2<$ ÇÿÌ!VKüÕu ùñ"  HâÁê<þ~º+¥WOS]EdWö1oýv3d¸+£we¿û_>k4Û/þ`LS±*%­§tÏüÙJcçþÁ!B!PdÍSxèHÉ Pòî¼uV ÀS½g§1oõuZ :Ï~ôÎÎÆ¡+Mti¿Î;ñ|y¤Çà" ûÆe2úÎ j®|_¸ùa
ûA¤]¼úG9²ÁÛ¶|ôÉÑ¶*FÝ@/úPüÄÙ+n[¯¼ ®§ãô¾;ÎZEãÊ@/úÿüñéÁvsT½·å²!ªEÍùé7¦
ßhÄ´¸v÷jY×Ï£VJk|cëà86É4ÂðâyÝ7TÈ(rmxÅqi8ái $qÚÍz]§®ÞåoóÔB0E1rE    IDAT)ü¢ÅióüØUæ³nrOeVæ+ÁPw2 EZqF¨;Ó  Êo0ÙrI­ý=úi»~,Ì½ùó¼{m»ÑäåÓdR¬ 3A45]ÖíòrOo¯ÅP2B!B¡KpÖÊ¯þöÂé)Ó
R¡æh|6´7×¶;pª®£DwÌùYcSmNM8þ7zwkééæ´ùTµ×íÀPòµÀ×|ô~én q@ÜÞ:Ø/4%M>t¬xäËñú!÷­2M   Y|^Ö ò9ÁÛ\ýÆçIø½¿wý{ï Ù}G¢ $àzµxgó÷ a»úß[gye¾²«Ú2A }BÒD Iù¡OJÚ?=Ù²Ä2  |zÔäñqßDS 0<rN|N¼ß
fï3ïÔµ1B!Bh Þ¶Ê£»+ ®î`¤»s­3µ×Ã$-Éz+tº­ß477.¸2\GÙoEúÜBã
3mõºi#ÑÒ¨,^YéóÿÕâX"dó,ÍÁQ·ïÛçé/ðª ÈlÝÆmòs­ìÐ1;añ®ÔHÅAÄXÑ-ß@àuÃÌMÞ 6ÙL %AÁPèÛJëÇÛ-ÎáÕðÙsÒ\¥wß¿T3-cÀ»PüÐÎc¦w¿mõ°cS°!B!BW.ä9­?w:Ò½@¡3*Ñd °pÁ÷ln5ÊbxOAQ32¸³¾@ÏÏÀÆç5ú¹®@íA»'#B¡¯®¥  ÈñË;ûÏh®´øxA`ó
¤n²ú("Dô{ÿ:Ýv§¿Îä©2º/;ÔÛhò<õví­xZ,'Q¬31QLuØý&Oy£óH¥Õì¸²Bó!B!B!teF+ÜÅàÜÃ.ÎpÂÍp{iÑ&×AkÈÍ^?Ý~ÿ>Ù1ªCÔëÞuN?tçB!B]±øÂØÿQpÃJóB#Ëmô pI&ÞØL4®ô¢ãd¸õû¢a·;d2éhÝnwB!B
Ç£þ·3ÏãQý<OòåL¤ÇàÚÂW0$CB7uÁd@ã@À§ú}oâd¸ö4B¡PWiÞQG FB!B¡ñÎÒiíPÈ7[¬ý>e«sðô0ÛCW¯d¬µ~²XF}2 qE(ä[xoâd¸Ö2Î«TVVc4!B!ït
ú¼ÌQ=D^NVC£¾ß§ôûÛ2V'Gz®-«
ß¶õû®qÔ'Wyoâd¸Ö2vìü"4ðu#eçg»¨è¸HB!B!ÐÒÚ6gÖT§Ó
 ÀÐ«ÊI àK%Â©|rHDÛ ó_ä¸ à¼#vtt¾kù2O½\â|9Fi2 q%Ì÷f×dpàd¸ª9-¾nþey¼^*Ïçcy<ê÷ã8È01ÒB!B¡°¤$k£ò ÇI%â+oÍétQe¶XJv»va\Tº4èâ«»ÍKÒ­Î¡ßß6äÆA$'iFp2 q¥ç½ÙÙÐhgûdM´Ráª4¬É@pãò¥yy¹ 0"ò9ÎP(xölå»÷t£É!B!`Ôo§¾&áÀ"FA#RøâÒvF8íg_,I¥±H(  ÀåöºÜÃér¹½^_¤;B!Bè #£!4BFªò¥í`4ùÀ0tfz@ ðx}^/k¶Øõv øB .V%
<OMmë÷Gº³!B!B¡ñ£ÉW?MB\B|\]CË¥ÙÇ6{Àfwuý[Àg&OÊÕ-­CgB!B!B]k¨è8¹äg4®11? ¨ºÃËz8ÎÔÑ­kâÚL8%B!®MAô^""B]³º®)etl¤{FA@A~Ñd1[láïåpºY -Ekj7GúB!P$õ1B!ºô&ãUâU¥`b®Ñdq¹<ÃÝõüþ@j¶­­=Ò'B!ÆA  qá#®ßB!®-}¯)e´ªÏå` ðêð*¨')jXYÉ}±þX$àóiÃó!Bèª×Lôù P(Ô¡Âo
!B×K¯y¡ðæñ)t÷ÐÈàñxZmüÙÊú+iDßÒæöøýC\F!BW
ãÖÏ²]!cèEÆo
!B×¬Þ«DÇ£|^^MãjuúÁ¶ Eqqrº÷'&NL_ºUm>Q«ôÙ B¡±CQ/¤y]¡Þÿã·B¡kYïU"I3üHw$>CÚëeÜBµöO¯¼»õÛÒh Z1í¾¶¾²õ7/'{}¬PÈ04/ÒçB!ÆÍ0¡P°+)9P(ßB!Í0$IîI!ßíñ
ø´"oíoÚP ®ØõþÍ v×sÏ¬Ì³ï~p¨ÙßÏæn·W$DúB!Ð"H*<_9á·B!DÙ³ªºJiEÞýO?¹¡®Ýõâæ·ÊÂõÏ=³2=÷ï?¼øn»ß]<Py(!B× B¡`(B!8¿B!ºv)W¡ïöx/}Vä­{úÉçß¾¾ùo§ pýæß,Í Ýg/¼¸­Ì:PknsB!®Y¡ tÕºtGB!Ð¸Ñä«PÈ÷ôWéB¶pQÚömy}3Èsfd0P»ë­­GÛý·æöx&#B]{0B!.A©ã#Ý4bUJ³Å/zÜÛ¡³DåÏ2ubBgiñ3õMáÌiYÊæ²âFGpÖHÚ;#}Z!BhLy=n   ! ¢H÷!BEF¯6R©Èø|$Ý
§Né¢òÝP´ Ñu|ïW»4SVjÚN­ï? ,h×iuDú´B!Ð:M&#B¡nM¾Ú|Åsº<ý<t7:¥æ-Y´ Ýu|ïW»éUS
PVÈ¥.ètº>0B!º`4!B]
£ÉW"$Õæìÿé »¹¬ø0{Ñæâ£
Å§ôª)s&
jkv]NVÅÈí·ÏÇFú´B!ÐÂh2B!º1iêH÷$>Cg¤iË«t#ÒZ^NjMm3ëDú´B!`,`tG~À,dè?xR0ô{VKI@
CA¹"&Ò}G!BGFºhùX¿Çëð+oJ(à»=>%#Bh<â%yH%_!eXà¡
=8!Bèr`4ù*Ô¬oËHÓ^y;iÚf}[¤Ï!B  À®#¦ÅÁD!Bé çpÆv6A¥oi¿ìF5±­Æ@ôÙ B
)BN;bdAB)B!®ê8UnN¦@ WÇFº/ãEkk×ç«¨¬1¶
#Ñä«SG5#]+.Ïeì.øÓl0Eú<B!  B>G¡dB];Ôqª)ó+«j#Ýñ%%9qÊäüS¥gÃ(ß{Ü¨¤yëÖÌTGº?\uõø¸hX8Ü¥:.º®Aé3@!B!BèJåædb(¹_
ÍUµ¹9áï2ÜÜd:wÒÔ jDÈÖm37V.©µ²£p2ñô}`ÍñººB¡Z!=UãõúÂ/y¡MðÚúæÐÐ}#B!B!4Þñù|%¤¡±97;#üíMg-¾Nåª.-9n´³ ÖdM]´RõÝçG#PfÆË¯ú ºÊõúè¨ü´Úz½×7Ø«$ðÓSµFS¾\ B!B¡«DB|\¤»0®Åg|MfRgª½§wí+± Àa³ô¶Ù«M/¬Ýu¹vsäýõl÷ÖK×øö}þ­RåÎÅPÇ\âø1iÁMËâu%¾ÂdWC[\kßçßºç­X×¾ïccÎ]³ý{Þ?f fæ¼I*1¬ÍPýý¡J£0çâ«>ÚWå 4×¯ß´ïÝC& ä.^Úôñ®jg¤_q¢Ãl³ÙÚ8¡ïv{=Ûãs{¼  
DB¾PÈ
ùNëØñb<ÒýE!B!BGáGimF,e,)ë%wcÎÖØV¤e(ëôÜ4
]¯ó £IR±ÆýÆ 0uÎÒTÉÞÏ«,D3ué¢ùSl»K,A J¡);ºû% ]RCL H4iJWãQ3Hz"/,o8òé^£g/X°xëã½&'G­"« eíR­ÈXµÌi4a(¹/«ohahP(11rP  n×íö-v±Õëó Äî*B!B!Bh|
>DN[ç%µ\&'È(ÎTcàÔ©±  ­Mæ:#'Hï©=YeñÓeFqZFt÷®íµåFõ5êL:I  BMÒ©¯é[/Y)4<atr ¬µª´U§jÎÆvU+ @¢sMµ­LL¬ bÔ*®Õ`ôÀG¬?`³;[õ:ÃÙº³uõ:C«±Ãfwz½¾H÷!Bh¤Ð²5ÿuÃî?fOEº'!BèRgO+\\´hå²×ÏÎÉT©HwiÜN¥h  Ac­[¤¦MSsú}(J®^ñÓ}6æx8§ÍÅ  ÛÔd¬c» 9Uál*± ôÈDLlÑÝwö9 =Jl4 ÑB°Ç«Åæ&$'IEVÙ¢c)ÓI,¸B!tí¢ù) ¢h±$tOÐå¡>ýöcì«-öGº+!ºÊQÒÌÙóçd¦Æ&]=G+5Ú)EfZÎ<pºÉ¼ò#\eÂ&»,6.O©`Àzaz²86òì u­ÜÌ45i¤Ô¬ákc×ps¦âÏ?¯ð^ØZWA×Õ×§¤Ê9£ÓTöÆ£g<ºîÊ}q­¶±ñ]£tÚ½¦(×µBÈÄKÚuF.Òãz5£ãf¯Ùx×¼É±X¾¶ì«­¯|qÚé~!B]ÞÿúÑÓ¹÷~ð¥ËÓ¨ä×¶¤ýïo_k¼âæiõæ7¦/9_N3Ì{?,ßrÄ9òËX Hn5ìl©¡ëÿ³Üö|Þ¾GÿßßëÏ?6iÓ+ÏeÚ°qûH-¦N§-¼)®úã£gÿTÓoâÜõU%FÁB¡J6ïúÊ#í­±tÿþ®¯­.FçÍw]µÿË§ß=y+V&×~ºû\Ïo}&uùôÆ__Aù]¡:UéÔÆwßð+]õºVN3EuÁ.&7-ÊÞ¨3 p¦#hb5©±¬Ag pY QÊÏ'ý%8ûuf¡&I­ÑªlM5¶cvF÷Q¦  &G¡ÎÐF{ZM,8Û­*6Y#µL£se   {Íæß,½ýÄÃëW®}pã+û9wm~|®"ÒýB!ºlÏ/Zµ.-yÔÚ?ûÎww<ºÿG÷ßñ«ã[kø+.¼?st ¾ç«>)Î]±fõÕ¸;OÅµwÍË\yC!Â¤Bµ½dß±6{Ñ-7-½å¦E×OKbÍåU±Yc±ëéAÊ0*]°ºSÇ2_WTÄ­2ØYJ­I2YËU8Õ]Y"h¬5ÂìüIT°q  ¼çLó&ÖZY¡:ñ¢Të¾Ï¿3^ÒxSSû¬é¹b®ÄvÑsÆÚgQÁTýfÎ¾~¦äÜ§»ª`×·ssã)ã1 XLÉ¤<¡_³dG";+Éyì©·w%\ÔÝ±Ùe]×NN§-ylÓ­óÒcV_ºë­çþQÚÙ÷Aè4íßúÊöÃm@=õù]®­»è+²bÆYµç¹?o?í ù¤;ÜxË$ °ºCÛ_io nÁO¬'¶³éÈ^ù¢_gBÖÃõ­32(2<¼÷ì¨è{6äÝ9Y" ¹Áø÷­e»ÚÕÏoÉs¼üÍæÓA ÙÃ/-Xçª¼ã·µ Ìô©»7À6<xanªÏíiléZ§ÂÙ¸ò'Ï=]öZ³èËvWLH]%7>úØêä'ÖeÌNá3~ciíK[u'Ý Qª7æÝ+f8³ÁüÅ?K_;í çä=ñcM¾·ûä·åøw»%!ãÍçs²øã?mýò×"=¬ý[õêÖµoJZ13I!Î³ï¾ðâÇU~ Ñ¤ûbEq5y¿èÊ¡Sþ¿×ÍNUKÀÙV½ï­×_>`´éçVÄ2ðäçºÿÕãLÖÊM÷­-LU2~gó©w_ÿÛÇeî¾ÇàÊþøßñ.sãºìòÍk_<Ü;òé÷mÚX¤dX¾toÏ%®vîÆÿw÷¢l9.cÙþ-/l?Î.yvÛC¼í½omzäS¬¾BwÚX®éh½--¤<ús&J;}Z~¶¡õÑ\~Æ6-]-45yÕ*:ýºij! pÖú£GJ²9·Íd÷í.± ¥¹¶H^öÑ2'PI³ïÈ5}úe]WóÊEs4bJµâÀ×MâÙJ
 <³êl}*1H&.½EyöÝÊXpWþÝ/ë(Í³¢( ÎÛZzä»ZÍ´³2ä9KíáÆÈÀ
?7 \5{÷|yÆ.P¸|ÕÛVÌ+LeôG÷~^|>36ê©XN_ßsíäÑÙsÂ¿`åº{Wß± ÖqâÀcGX}M»,VéªÑ]#´ì=RÏä¬üñ?]STÀè÷ï«v ³P"°:  8s«S,§Ì@£ÇÙl²(§¬^¥èIqíÿxoy' ÐyY«{ãÚ»ÖýùrÕãÉ¼ñõÛÞÞ¸öÖë^<$^úÄãKâºö±2qÿcë~zÓºãn|b}
W´ió-Ì?<´ò¦»7¾eÈÝô4Ðs7nÇîxjõ²[W?üzEâÇîHôH BháÏZwÝÁVëúï³nÇÿqkÏ#¬ÜñóøA2YýÆ>´eÝWtq6pÅÆéw2Í¿Úøåu÷z­EþÄ£ySýæ
t~  *:_ìnÎ +ÓÉ!ÊYëÉr FONì=¾æ¿+ÏÒê'~PQv÷}»ÿºô¤jÂ7¨%@N½½àNñ·wÍüÉþß§oÝ5&7çù
ÑÛ-¾ëË[þWÏ\?íé"!´Ôþì/ÛúÛûÆi( ÀLì¢°íÑn»í[³6lZ@O[ÿÄ*MéVÞ´é¹²üEÝ¸êÁÇf»?þõú¥+zê[zÑ¦õKþÓ¯<¹¥µì}våºWûEs7=±!®ü¥w/[ýçÊTë|h®øÃöwåÉ²~¦`azÉë6ü­xvè5­zö¡¥ËÖ¬{¶X²â¡u4Ðyyhró[Wß¹rÝs{O=¾$ÎõÕS¿ÝcdÏnYw'B¡µ$h6ØY `­å2rñ ÛÙîä Àc1Ú(Y¬dXáS IÆu³¥{?ÿà£{Ój¨N};« @Zî´@¼ ¥Zá1z#Õ3GªlúC»¿®õhfÏÎfO~úþç|ôm}Ôë&H:ª¼`ÖqôówßßùÁÕ\ªV À¤.Lõ~ÿÙÎÞÿò{OÆÂêYZp¹É  à59j83ðóñ»÷ßûîüíG?­¸h;WÙg]¸YýÞëû¶Ôth[SÏNÃ±/
Ç.=îÐ6Ýù6Ëw½W>á?ñÖsomzì®g?^oª­ÒUT:¼÷Ðq½ èóÕÛÞ:Üì8±ý¹?:.7OQýîë] ®òmZöyó_} `Øó~q' ¸J??bZ6gFrçY<ýq lÿxÅßÖ.È¢ëaYË úâ7Þéa@!ÐøÂ[5²§Â ¯ñ3ÜîÀn°±Áç,ÈlÜ[þ¯¢yÿDuôµöóµêTê[s½{¯+·sï;ºU[22Ë?©qnÌT(ÁîÌN1¾ 5S3É]§ùù¢Æ#æÁJÝÑü©Eäî½¥Ý[ñ­-ÿ:`m,H
Æß~ØÞêhoß²»cÅílÚäÓà÷ÝAð{NþûÐâ 9ëúèÊ-Ç,¥¦þïÅÉ/ÏUîmßUözUì~ÿ´ Úí:µñ¼q´dN¾²yÏ»GÛý u»?Ù·jÞM  Ð¼ã¹u{Ù¶N7ûôîÃM«nÌ£÷töiK<se!úóûÇÛü íÇßú¢´è¡¥ôá½Ü^yV ã*ÿ|Wy@¼°ßvY±üümeÛ¹m; ÐÓ.RTo}«¸ÙÐYýÑöâ7CñÕXB
âÜloÒ/)IÊM£t_yÚÐµøÇúb(êüÚo âg¬¼kÚùùTg#P£UZt{lA `
ºV¬¬s5rê5^å¯¯p¥©£¡Ö«¢LÅþZIVõ, púZ{ajSá4±ØïdéìÔTµ³ÉhÓ}· È¤ÔXn¯Á ~C]¤UÑWj¸ÑdÜ§?xîÞò)¹yÓ×l^swÓ{½I8MÆîï0þº£_Õ(n8MM=_lüÍ&d%ÆÑ  N±­ûqc
¥(6=IÊyvßªóÇcÙXp{wÇ§6½òÑÕe§öïÝ¿¿Ê~B!tÕÔì=ùÓ½=?TO<?ëV±é¥ÿ.Ùk¿û{[W<·ñÛÏõ¬íÆ¨¢âiþVÞy~3UAci§ùúè|ºÙe®©þ^¤~,O5i÷òKo¤¦m¸áà:  >CËñÕ¶[*]÷ úLîV  ×ð¥òØ¿¼ØgÇN¥<¸ãÓs'óöi5åæÇw1·úéd@7å¦ßÖ Üâ{ÃÀZmÝ¡^Õùqq´Q!NSÏ×Cs[Ï×%IÊÊMkew,d$«ö¢âq¥D1ãOï/ëóXBpavð¥W48X¡É?X;þ]l+{rÃko­®;[ZV¼g÷¡Óm~Ib¬RÿÄÇ<q~[}b\¤!BÃä`iyCý @Ðvî»Ok9Û;¦2)xë=Ü {s¦{¿Öõ®Â´ø¦$ `XoÏ>¬¥%°ÆVçÄø(g:O¬ñ¹±JÑ
;Îö[b¢Egí¹¦dY?0Þ2`pï;sf-*á:ëK«õF2aÑÚîF)ª¡ 8¸BMFÅo­<±¿òÄþN\þäî¾iWiX¹^ý÷ó6ð³omzäï
<ýß¬Ý5oöÜ¹s>öü_yòé½xÿ B!F[sî¥#êçïÍúäOç#Â>¶sËcþuÑÝ~²§¥H|YPýOçY¹3ºH©Ètßké§å³{ö° X¿ÏÜâëAÜ÷zÈgªÿÙcååçPë}¬%s²ºhºzÁ½3o½¾òg¿oas>¹ü/¿Ãebâahó'Â04@«^0ÂäKü6Å¾§{úx7¾ºíÆ~¶bMýzÓkUCéÿ ~v¨vÚ?þí¦}iSæ-1wÎúçV,Üúë§÷±À:m^ûâá·¥Æ~¼B!tùêÞÅ©Imµ Z=yÁuª¦¯÷V[8  ©I§Nï´;Çy=«®+$}>øë `e&LOb¢lzÇÞÊ¥Æ' £lö~c»ßÍRÀÐèr¡zÊWxLåGMåGI¡zÒÒE3³û,k;³ïÓ3QÃ,ü®uò¹÷=ñÛ[²úô7×ë-@+$àl6¢9    IDAT9%$e×ãtNÑ]kgkºì¹íU©®+E"ïÙåÐÙitê, NKím_¡Õ hBmÕû?ýÇ½ióÿ¢HB!®>ïß©ü^òØõÂ®Ùv)½Íüä ¿ó¤A9=6_n;ÙdËÍ
UÑd¿¦ýl?1MÎ×î¬i´×4Ú/%÷ÕÚà¹$KÔó³HE #*ÁWs¼ñµ×Ýý»zsfrQ²¿µÝÏh$ñ=ÛJTå U¡ÇVsä¹ÙòóÐ©Ó³Îz]wê1#WÇu÷VÈÐÙÜé·tZA«îÞ!5=  S&¥Ñµ{woó ¥¾4\Þ¦3<)­·R²(N+ïg,.½òô×-S@g}ñçÿxõÉú¨3kågÉÉhzÅªDÅ¸BÍr®º]377 ð[êÊÎ P?7ÒW4ÙÌë1è-ÊÔ´( Iéñ©Þ v}»837Úi4sà0Y¹ÑÎ&ÓE1b(>Ct4Im J!³\¸%ëñRQb! 89U À¨ç¬)!ÙÃ@Ð¨3 3ºZIêë'ÆHÝd&£a±]òyëñÔs'iUqqôiK}pº­üpøËöêL]}ßÂt<qÚ]\:Iâê~pýÜDè¸ÉîeûuºcµKïH­]¸vÖRVÜíö3sÖl­¢vßæÿðØl]°~Ë¶§6ÎÖhEjFØi1ý@ª"BèÅÖòÒY·¤duýØnü¢Zp{Þu*há¬uÓßü]Áu" ð,u¦ÌIÎ2Oºl5®¨UÓEÕ½R¶³TÀ}Ï½ É40QÑ÷üjÞ ¹ówß|X) ^rDê÷´Z'¿5¶&¤>V$ H2~æºÿ]Þýç{ |èrûqÅ\ÇÞÝkÊ¸ëÉ_ß2#'-%§`îýÏüâ&Å¹wöÆosß=7qÊM«fJÛü%gK×.ÐiyÎ-«æÅ±  þvK'¨¦ÄÑ Î^òÄ

Ë
ÀÏ² QÄª"ÚujÏ×ä5ëji åîxrËË]wÐÏçEÝî¿ÄU·½¼ii ÄYIb¿±Íê/Û¨M³ú¡%éb qÖÊÇ7o}úÆD ?Ë² OLÅ\F!~ 8îðÑ&fâ¢[å$)i¶]W¥³rÂèÌnYÊV;Öäv£ÎÚGiE+ï¸íæ©ò']±]CgÌF/ X®(%5îÒë\êy+WNV §Þ²få«æh-%û+.¸ÇÕU³¯Z¼|YÕnâ (ÖTUyËV®]sóÚ9ÜSUN`u%dsWÝ¼vÍÍË'
+®r @L:'b¯B¡ Ø,@@@¡T
µüÿ³wïqMÕÿÀßÛ8Ë¦°)lÊ%DC4o©©hÞB+-C¿iéÓ/¦y!-Êâ÷2ýiÒLý*¢)jà¼ 7å&È²íýþÀ» àm¢¯ç£GmgsÎ{g{¬³½OÛ·Fnç-JXâÔù)×mI¨0Ò²_xXH÷VRÒæ'Ç¬Z¬!bZM éîåÂ&÷ÔåË¢Ïié±;Û°ú¿ÛN!á);Ì>§#"§¶ïN|«H]¸umÔÎT9´zkü!í<äbÓd¦Ä­^´1ISë  gÇMÝ[´1Cfu'¾<cvÚ}­£mgõ{¿ >dÃµK$ïÿ·ÇD_ýéWä96y\ëá&D%W6¬OÞrÁDDäÓzË·-Ù¿B6r$ìñI¿Ý´Ë'ÞÛCùcû&¿k¼g×Â¾ÓúSÊë¯TeÐÏðÑÞ¯4whDËò,O;QF¬g³ðq/ölîÐ5hb¶ý½ü#¡gÏÖáÃÜÚ¸0¤+?µáJOäàþíËCéô¯LØ{g½Djºÿa)U_
$ÅRi©t6­ÏËåÜñÝQ£ÛyËÅ¤Õ(³·¯ýewH>èÕr×ÆËûÊNuvõÜÅ»³y"§n¡Nn£ Mæ±-û)d4»öío$/1µ¿¿×æÜ°(ùÍü_m- ë.ÓG¾Ã>Ñ¡BBê¼Ô?V.[súklÔpæÉ´
[å¾cÄ×Ï+ÅÕmiÞRèèWZ($,§Í¿»eÉÚ<fA'ôös.7-~Ã÷kãòyb|ÇÎxÇr£#'®KçësÈ   àñùèá?­ÿ­¦GE:µñqklk®Ðs¬½H¯ÎO=}6µ@÷Hâ×§ßýÏ]&?ïê&?LßÝ¡º{Í   T«>i2Ôî1§É5úaõ ÌaKkksüáÌ  à9W·´ThïØX"2kËÊ+ùz¥É8)        ç\eEYiÅÃoæY¾É          P;ÌMëàc#ÄZ»    xÂT{þóÆ'¼Oy   <*          µC         Ï¬+*kðT«×ñA         Ï,£ÑØÜÓÝÚU<¥{ºÆºG         Ï¬3Zùy#P¾WsO÷V~Þ.fÔ}\         YJUñÙäóþ­|üý¼]]åÖ.çiQ¨,2gÏ+UÅu_ë¤É¸Yw'Ó)³Ó³4¼µ         ÀuJUq½2S¨É#H¥/YþmEÕõÉÈ)ãT(Ëý°zPæ°¥i¦   ¨Lhq¬X»gZ`±v     Ð =|ÌHä.÷$.
)QÝ.È´ì6qÌÐî~n2 Ëi5ÊìÄÍ+×îÏæI}rù×´y<1-Þ§o?^`í    Ötµ¼b@ühd±H   àA<ò¾ÉquÈNù*,0oËñT<ëÞzð1á_1ê±?$ñÅOWÍ<güCÞfWþ~¼ ³   ggì*m,Ô4Áå ZrÊD{¤É    ð >Mæ)Ægùðq¹ÇâëØæÂ½¿´(þëèl""JKX³H§zE¬fdU.>ë;/*Ø¥ÏvÄGý!YÞmâ¤Q½ýXÒ)Sâ/Ú¤!¦gøö1º
1âþÁ¾
)åÆ®Zrªõ¸½åb.{GÔçÑçx"¦yÿI¡£_i¡VþçÚUKùNXýÿ©µ¹~C;ÉÅ,Å¯[¼$±5   ÀÓP¼Ce¼µË     x ~|~ÂüÿËâ±§Ì;¥«ÛjªK¹K§w¼Ä7$ïÞpÛêü¹e-OáÔ±óþ!Zûj|`ÞÚo<:j?1µßõK0J;÷LýÑ¹©à°È¾Å«'gÜÚÜ!#z9ûÐ)¯è·ÏÓðøÃLï°1ý¥DÄ±Þ=;g-{ç_c&nÕu:         Tçç&3-¦L3àVLDD^mï{ëúâþåÖÆå×0ÙW°dnI¡«·Qf]ºv6éHâ)5N
fzKÓW¯MÌã4éÿÛ8ø¿Ý;IüADtiÿÎT¥Ïå:iüÅiÒÏ©¨3¢ËyÑQ£c9FO¤?·7!wÈ Vrf¿KÙÿ{6ODy1ûGupØ«·ö         ðÔy°4ÙÁ»ç ÞÒK¿.ÚsQKDD¬[ÿ1!ª=Ë£Ó«¤õÐÞowÝ¿õrM±æôÆOGoûµëÐ®m@÷qÿ5.íÏ£/V7Xâî"´ ß¾#üÖ²|÷ª©ÄN]µWçH§ÕVíã8"%"4ÒÛÏ%"b%¬.­Ú§TÝ(¯T­#©i2         ÀÝ$M7kàÂJ$T|ü²÷WZËÄ,+v"Õùl=1N­zu°bYî%äß'åUi»Ówo%¦åÈ%KCF÷ûìtu9â´ñ#'ÜN3r"º¯c§þS§¾#ý3bÊI*¤~Ø0èö¬tä         ú÷MNüö³wZmñÆÔ)=¥/új°¿X¯Þáÿ
3î½B#§öö`I04ò«Qm¥ÕlÆ½gè7SÜo[ÂçÏÕDÂT»[­ªHËºyÜìk,vvV?ònLó¶-ÌØè$OD¯½ù+»]ß
ë¢ZSôÄ_          Þi2#vQÜJÅ
¹T&wÜ\ qQHÅf.²K¤.
¶ØW©á<zølP7?7¹ÜÙÝ¯ÓÛSÇô\J8U|Û(ãH"uQH(%.^åööø~^b"±ïà©«¿äNuÀ«5¤h'gHì×/<ØãÄ²I´$ ÿè 'Ú¾Û/KM8©Ê          ÕxÀ«ðÝÂÕr¿&|Êºð¯KÇì7eþHËrZ2ûìê/6nÏ&ß|$Q6~õòvQã¢½&,Ù<^BºÜ´ø¨E{òê0?¹`ûÚýþSC7l£Í;¹aÑâ¤ßLºx²v!G\îñó¶û9±ÚK.[»[ó=         @Ã!hÛ¾kýÖ`ÜúOútbß"./~ùÜpí¦Ì?ÀKLÄå^¹,Né>uLwwHw!feÔÊ¼§qÊoó «çùÇNýÏÖkWbMÊÔWI@"©ÌÙÚ   õª¯
BÈb©´T:IZ»"    °¾ú§ÉÏ¤ÉDH    :H   à^Ýé-z­µK    §Î   ï¹É@tÏÜd;;{kW    Ög4nlkkgí    Àú07î`ï ±v     `}Fáö»8K    "Z»           h &         @í&         @íjìÌóÉÄ[*+­]!<B@Ä°ÃZ»         hªOyÞÈsµkG©Òb©äem­]         4<Õwº0ñ&kÉÄ[»         hªl±X,4¸xFY,E <ð\¥½Ë2Ö~2    P?ÇWT´zªHmíZ     á©&M®5jdÄ6~rQ-Q¢É]`*5[ûùÁ=8Jf/÷+Ê²ÒR®ã1Í    aF,¶·³µõ±yFv>$   @}ØÔwÆE2o´Ô¯ëq9ê°-º|ÊÏÆFäÙL~>õÁhíZ    àq<ÏòDTZvÍÛ»ENn¡É_%   @]Õ;Mæu|¾üj©*1ikE6}^sæk+YS¥ªÄpô/ÍúÈ>½|¼<R/¦#J   x6TYýý¼/¦çX»    h0D
W÷{ò<Wã¼ùï+ÚØ5Þg³¤-ÐÌ©(¨>MtyCñ©ÿkLÉË¶«(8ü+H,ÉÔ%ë¬}<k{ïBcDDööâ{uiêTZV¦ÑY»v    xdL&¨qãF:½áÞG
z@@YÈbgï`íz   Àúê=7tWÊ£ö0óÞËkQª[¾KûOÓX_¦ÐìËµù£¯jKì¨j¼-óæ é0_[)³ÓKïÑ_2ßXØÛXt*Ã¶%»®Å&H²êå%-ÅB*3lÚY²¯êj"ö{¸Ù°T}íÇ=Ú¿D"fà é{-Y©iKªWgc6tH$   5F£TæDW­]    4Â[­è¢fI¡ú ÌÃº]£÷ËMÙeä÷Rã.7T9«?SFD.ÿåXµ"ïÝÕÙrYÄk,C.?hb\ücþ¯Ø|ð¶¬KÕüZ¦ÇK´é§ÂK
(aÿý¤3.DæWR¶8È÷ÅE¿xÓÞ¨YGé¿å\ÔùÁs>K²ôvê"²öáo ìítº
kW    N«;Ø[»
    h00M&²ü¤^ráÞk@ü¡ÞuÅrßu+÷Å\=hOh¶åßÎß;¾éÃ\ïÃ,²{ÍWp:¾üoéÊ?î,ÙQI"»×}§ÿ*;£#¢Ê3]ûÛÎþ5"²pDÿ$ÿc&¢ÊIº&ö/<$=Åm
Ef"#¿+^¯ó¿lKDH&³Ö@DKgKF.SÀëeç­]    <bÏ³,cí*     Áxà4Èl>úGÉ¶ÛcKZÜÕåÍµçeå¿^¹BµäxÊ8H¾îã&}mäd**½>JWTq(ÛÄ;ÚHÉ_rc]£I¥HDD&³êæ$hIC"1¤vá3ÜcfºÇÌtÝHn#rÓ¥¤²ã6?Lr]ô¶ôXLL    x4G,ÙñçÐ7£i¦Ó¿ÎÑìqí¯UèÜoz"   xÒ¤oò-FnÓõ£Øi³ÔKøº_HOWÆø?ñ·Dì¸\þÝÝöèñº¬'¨åqqZ]ä2õ»¨ÿcþ¯ö]Z9ôìåòfÇ²Ï6TÍkGAÄ6Jèº{øm   @£S3ÝÇK^þxÔÖ¬ßäqC¬_ÿ ï£ÏáGt    OÊÃ¥ÉD¼±Rcºu[[pVf?%=¾§ìÄÍËô¹Jèu±ÊL*²iÖHMD$~ÁaÜ´3Å¤2ÝZH¶"¹Ä¢*«$"²É®1ÌE:ÒuvLKG:S5mY$t±©,2b²äçVü/·âñs'8¾&/ÿçµ_OÔÈ£U×.m[:;T½L×TgNK-Ò[»2    x¸ä­qwG¾ûåöü;ä-&J7.Ú{ü>\=SJèç¦m_¹_<(Pî"ÓÆE~±ñÄ~ý¦

2Ä&o\{ùVb¬:wªÿÐýUã6îÉD   ð=D§¦³K£)!N}<l\Ä'G¦K&´´ü}ÑÈ
Ó-/¿êÔÅQ Ù}0@ÖãÎ\q0Ûòò«/DÂ.½¿¤ÕÌ¾¾±;:¶l^ëb/VUÖåj±o½æÐBDdkÓg|YØ}Þ~aÕ[-l\^°YU÷yÔP=QÓÖ½
~Å×ÙÁ|MS\Nå­z½9¬wËFOE/§Îc#>èêdí2    ª«;$½cióaC%±_ø×G#øÕ[L<I}§ýgbXTÛè°îYËfþ{BÔþow`i=zê(ÅÅ#þõÑ¯ã¡¡ïÜÞ1/V²nÓ¿üIn2MÎè   ¤Lîh:÷J{­û*FÃ¿^ÕôjôÞÛ
¹LªÃé?T?þ]ID'þ(^?@ö79;]õ':±§xý iøfR²¨Tú·kÎTM6Nüm~ë½"ºý;µùDDüú-%l°ã¼OHÈ£[²KWDt(¦¤e°Sä¤&R¶ÔxtzWYÝj°/tìß«¹Xw9nÏóWot¸ppy¹ß®­z(-ÝqF]íluqËî}ztl¡ÚÙI[|%ëø¡§õØ5    <}øsk7&¯3îåóSn.¼¼arèfNÏñ§Îæ²dUa3w)áT)åæül¼òó4¿TLî:IÓ7Ç¤óD½vHÿÎóol!müêµ îEÐc
   àÉzè4Ù\yb¿*,ÛiÊ {M¶©Sø2Ãú]õÕ>fäwíRíº{/ü®]E»ª®-Ð.9«½gûË­X~×RaõVåêÇpWöm}edÌ?~+J&"}Qòá$wº7xÉ-íHî½
/töî+Æ»7G_.3ØÝÚô|}à°7´k¶¥!O   hØt«7ö_>>¤ÕäÔ¼{ì+c±ºÌªÅý»yç8""F*HZO\ýÓ8""bY^yQJt3MæUÇTD¤I³öÓ   xÞ<tLDDù¥S3J­ý\àÉrhâÙÔtYç¯ÜæKó.*Í<]<Ø\ýÝ3Fl=}Ò¶Æ¥1ûÄïÛ´/5¹ñþqôëýFßÜlÈPuüÐïñyF"²qi?¤_Wo¹=síþýØe#ûÀ)Cí'Ø½ÒÓ-ÇÂml¾>¸Û®*Wý·÷÷SEUS£mu6ª³©0ãÀ¶ßS®ZûØ   <³T±k·¿þÍÄwU÷[2¾EâÏÖ¤éIÜoñæþµn×jµg7COd   §5ú&Ã³AÄ:ØéËõÕÌ(æÊË9"Ö¡º¿VUWuïí¶7Uç/(DD#x\Ý·nAä¢%¿$Û¼2th äAoôkvíÀÿ-ýï7+·e{ëéiCDf"¯v.ÿl[¹lw.Ùµx}DOÇÌß}³ôÿv_Ú¯¹qlÝ®ñé_~X0óiòéäóT4t   xVüoU¼$xH KDÄHÄ®4/OOäÔöÝîÄ°Ú6¨ñìÆ¸õØ/?ÜÒÚÏ     ¨a§É:ýÌÊÕEÖ.ã¹eæôF"F¶÷>Æ6jÄqzSu+ìÛq@Ù¤÷ÉÓ¦|0jXï®î7RgÏWÚH.'È¼f&2*¦=_jaK¤ûeÙÿÅ¤É¤ËIºTjç"ÈÆpùÔ|Ñ`y¾hséh\Îd,K;½íð?×'Mrþ:]j6k¯¤dØ4u¬õ    <>mËêã$°DÄ§ìßâ<qõÊõ«ÃûçïØ"0ó?Av÷_?}Ã¢hußÍ¿þô¿ÕaþªøÄìºí    ³:]d±X»6xôG÷÷}IÎUc«ÍÚxH
Ò´·_mOÔ´y+7[º}µÚ£7¯IÈ<{´ôiáônïªÍÛâ.S']¡3¿¹mpq QòB§ÝZ7«í$êæ¶Ê¯_LÑÉÉ´Ë®ØFUZ¯+¹Q©D¦¿    ÜT¼yÊG·ÝÕ',ú¨÷¢ªÛw3i÷ÍGb?ªº÷¯ëT;gØYußÿÅðýDD¤KÛóß{¬ý¤    ànÕçj66ÇA¢G¤VäKW·|É«çÀ×DGþJ-Ò^hóZNÍlLùgÎ+ï÷&ÒªsÎ«sÎ'5õáë}_:³úo´g·.Î»shãNÃ¾l8òË²S*QÓÎc?ö¹õàókæb"         x8ÕgÃÌfÅRií
áÑ"
Ã²pÜ¤ý½Ñ«¹o¯7};ä\)%'WOg""²iÖ>°en|F¹ù®µÜ»{Éð×Þ3ÊK®(uä'¶#cÙUBîHyUóEÆ6ÚkF¹§r¶Ul/81ÕTSZZFY*1È-°¼4ù.         ðhT&ÖÖÈ¶[çùjêÛÊ[uíÒÖ×¹§O"ÓµôÓgÒMÞÝû¶ò0h÷Ý²ÎäÔªß0ØÿäëL6¶Mup,MÎPÑÙó¥vî½#YmÓ´Íë£ú8_·þ®TkãåómZ5|½£ìHDtgRlÎ<ÿé[¨b¯Ø4ï9ppKÕ/§ÎÔT¹Í·1üu å*¢ÍÀWlRv'î¼
    õæâ,HìììXyø­   ÀcÂq|EA«7¨Ôu_dá!ËsÏïÏ=¿_d/²FM¾*:.Øg¦ZùLæÝñÙ·ÊêÄ_~1õíÙ~ðÞìlÈ¤-¾ó×ÖmñWòl½4júP;ª(ÉIþ=úÄ5¢kÇöuüî@6ÿïÑ¿çÕoÔ²uÞQ!cïæ#¯~ýãY*Wý³oÇÞËfrª¡lÛ´Òþ} å*|Ú¶±)Ø\@wÜ   ú`/÷+Ê²ÒR®ãykW    5bF,¶·³µõ±yFv>Ï×in¥ mû®Ö®¬Éb±Qú* ÈB$9ß;¦}Ûãè
¸O    IDATª÷¦E>ø42)·í<wÕ\ï
    ÀãÖ½k3çþ¹wy©úªP(¬º:w¥¥ÒIÚôþÛalDîôÌKÑÚÏ     êÁÞÎÖÛ»ENn¡É\{Óc¡µ«gYqhÏçò
T¥øJ   ðlóñòÈÈº(    Á©03³.ûx¹×e0:]ÀãdÖfÄÿaí*    à±riêt¥PYQa°v!    ð **E.M¥EW5÷¹É     ðP$DÉ    
ZÑ(ÛÕ:ì¡æ&u1² Ï=¶cuLªÙ     xþ8ØÛétÖ®    N«;Ø×:¬þi2ãÔª× þ~bbÅÅÉyâÞã?ó8yáÎ8Y·ýpz}"f¦ãÔÒ¿£¾»Cu#' ¡    xº±,Ãñ8q   hÀ8gY¦ÖaõNYë·?Ú[výnnôÚÈð¥aºöö¾kè+â¬eqª{N+ßÉkæ½!¿«Þ³QoGÆG/`x¢Û
wîøV;mÌ8;µãYß    5,ÃpÎñ     ®ê&óªÄå_|'gÄ­ú¼3ä³Õ=]úýûIwÎCæTéÉªÎM¹ÜÅ1E·-Ð)yÒe§&Ý5PÚnÄÈî G\¬¥4<Fú
XlÏâ   À3E,qÐ£ß1    ÔÙôMæ5ÙÉ ÙDD ÇãwtïÞL|älÜ_îÞ=ÀË>,UU[ðÈi²²/ß¹ì¶NUÄýæmÈRàßÖýgg±ü§é(Wt!vËµ y<ÓqêÊñÍì Ñ~©#Ör#Ã&ömí!c9u~rìÚ¨uÉ¢Ng°·³×Ð5k    ½½½V~Ç    PWÂ[W¥Ämß¥ã¥/ü6l\ÈÐ3#"øIuº_ìWrçþÅÔrHÄÔÎÚ­o¿1üí{´]ÃÂ4§ª>A^§·òl«)Câçï? dô¼DIðøÑµ÷ûûS«_xÁÅÞ¾ö«:   @Cá`oç*oZtõzÁsdï¬¬µë¸bÈ¿ÌðtßMØ;c|4_¼ê·ç'uÞW  à9Vÿ¹ÉÒÀÉó?{Ã½ºÿ¥«OFÍÛ#ùÙ¸1óv!.oÄUIîìÔ«owÞÈØË:"Ê>°ápÿå=»»oÝBD¬.uwLª'ÆO,!^£ÖñÄ«R6þçV;´Ïì|o/ÏÌ¬
ü    ás°·óòjy©àIìLúþÎ^®M$dT^H^ûÓú¡g-3kÀü)¼Ò¹GW<ë7cã²¡®7îµI¿­ünK²îIºGÈ#äçMc}o§òÂÜ³~^}Bù$`z|µ5²É!bÔÖ>   ð`ê&s¥YYréî¿³bÄ¥mK_V.&N«Òi³.©k<c½CÿrÛ¼ÝÇÝ?ùe<ä.l«1ÿskú!SäòDDü©R>·bíÛYçS÷ï?WkÓ
¨7åä©üý¼¯ªFN§Õã¢|    
Ë0b½Báu©çM}²®+?ÎmYµàDd^=Þ>aáB×iÖ;uïñÞð6vÌ¬ùDTu"ñ?îòÎ¯Â·©yÿdÊ¬3F.<ó3ë'Ã¨;mM+või<ìý¥+;FMú*:'ö   PWõOuwÏ¹ûÅÔwÀGJiû£¾þe¶þþÉ]S|ë>WIXÛÎ¹SËwçÉÓø§rüåí_ýÙ²]÷ºu´zÆÛ³øq}Læé9rgi&2{;E   ãx}A««HKÏy";dÚøq0ôÅÙ¯OFM;*ã«é]<lrGò.¡LØÖUB:ëè¦ï¢veqä5aí÷mN.H÷ éâ¡h"QY5'b²råDfïíó]ð¬aëèé*¡òÜ3»þ/rÕ)5;pNl6â­9'^ª]±
ÖÊU&ár,õGÕD$mÿÞ'uô¬Úãºï¢öeqä5aã÷mþZSÞglåàI1Ú»VGD·b[¯!3,á½fÌÕ×ß£­¶$5iÍÂÑ<±ÞÁáÓ÷ðV°Ü­Únñè·äûm9aSyô<í£¾þ2´ÉÎùéØ>5ÏúÌ>¶Õ*Ol;Pÿ4+/QæäòDvâÐ¹Â&LëwbRLáí5º0ùÀ?UãÙgBxh¯Ö®,Wx1vÕùT·oQÖ}ÚO³¼Ï6?QçÚýãã{µWHS¦îû%jÕáé2scd£?³CÇúxkAMÉ:}1©_{O­QøÛÒ9Ñgª^õ|söoïul.á
÷DÎþéXï~áÓFõðV4"mafÂßÅd"  xBà*|×IO
é$'eÊþ%6&©Òw/ª&e®Ç©.¦]¾sáýÓI>WUD]}ý¸s<#w©îyÌ8È%¼*;qwvâî{Æ®7¸góíw_îªXCÅÏTs=    x\ØV¯uV\>ôíÁ;ÂTUÌ×ÓbÈuØôÈ7)zÖÈ5ÉZ×>ÓÎ=9gÌüdmÝ§×YgòÃþ:ªÇ¡Ù¿LúÖwççì¢·Âñ¬ÿÇ¡­2MpHÙ(pBÔéÏL¼ó»¬Ûïo'£tXûõa®Êr8=j­52úÖµÏ'Q3gM.??c}út^8~é¥ö>ÏHâ<°wá·3Z"Oû$Ý3åÝñç9àÙs&Otf|t0yÎÖgÄù¿5çóðÜ1ágon!`òì]O.°)c&Ïù¤ýÙc§+øÌþ:ròýi1%5ïóáô þyKÇV*^:+\BçæÕáÒ~Þv.djPYL´¶Ãä9Ú§.;íp!0vÎ×³ïO)ô~?rfÂEÓü¥mþæô¨çdL¾ùòzÌÕ1}Ù¤ù:òÕµpÙ¬à}Yä1gz:oì¦\ãØÀ~¾ë¾>'«£.Õ¿OºN5Ôõ¯oI*Wt_8}Æ/K#"´
n·&rÌ·9² 9Ó#BBåOú¤}áwc§($¯¾SgOÔïÌ¤Bk¼Á  CõOÅÍ3ØÏI&o&Qüu®ÓÁK:+uwýiW§í_¾ò@ÖÃõã9#'ww'1§ËË:zd|äÆTNÞmâWaþ§"Ç­J¿}¼ûÈÕÁK¾^¹?[/v÷õóJU©µ2    ÀóIá*ã
/dÕð¨üµ>­¸¿¾Z¬árý´cØÚáÛ.MVöìªy¾9g/vðÑÁÛ:ür~0ò7­RÃi÷Qökï£ Ä¼;·³é´çgRO9KÚo¶-94uË
åúiËßïÓ­jâºgMb^u~YßaßFDdkËsâæÏÚCD¤=æ8iÕZ(+æPÖä°Vlta`¿²kVÎÑ%®ëy3LgCfÞW½fÂ¢cj"6°__ÙÅ«åpDê´-k
]ÔES}ñ\Î
õ_ßÅäòDyWÚgÂC¾<Ú¼Bêà© VÒ«§ìâÏËçh(eÍÆ¤àÙA=d1çvõÌ=±/KM¤Þô]¶wó ÉzEÌNfFìSÏÀ~>¹;"öei(3fÍ¡AkúôòÜô3ÙjS¢w¥rTãü!.)jÌV«RsD¹ 1g?òôPGD¶Ê1©j"õÿ
YÑ¹í°Dº\KeÅ|=*æq½{   õOYVm¼åDDZÕÙ¸X¢Woo¹ìî¬¯}Ø4²â³z¿óßeþÑ×EGÎu2æÓÍ!RÒe_¹6¿ó$/zÙ÷ÐÑó×KXN!våX¤É     ÖÃÖ´\Þ\An¸êB5'i"cIEÄ¨5×sÄÝ»VÖ~ØÇï¿êÕ%"VÒ­¦s§.¹ãrÄ±ÄÊ}lóÖËN¼{kSi¸¥ªÞÜå}7ú&Käm¾?áû¹IÓ¶äëÝkÊøAí""VbK D$ñTH´ÊÂë3ùø"Rë;fv°Þ19UlÒ¨mÄ¾Ø[ûÊõTÔX|säÞ8\ZUÜU©÷G?¯îKD¤=2ûÝðCuíÿPUsÎYÙ\®ªZy*J\¤Îº1í7ïÄ®¼/ûð9´çöÚÆ1®
ÛÖ¢ÿº-à.Ére#2ªs/×ÖÃµó¨)ïµõT½2Û7¾å«
oü!'WC¥MØ¼úÎÝ93õlÊC{bâó´   OHýÓdMâüÑCçãÞ÷Ó%SÇ¯^C¤=¿|ò¼íiúºnO_:zxµ$-úh@ÕÍØÈ±U·Ò×LµæÆÕñu_w×ZçpëÞåýfî·Þ    jöÿVì¾;âDa9þa.bç9lzÄ@nÍ´ñ¿\ÐyMØø}:®ÉqçW»IuçRw"ºO=·ú&S^Ækëï^& =Öçä çpÄö;õ¾»¶ùÈ²Î(Ûíûõ15qd,xkÎÑ;÷ÍºÞg+lµ7¯ËÝ !"âÕu¸¶ÌÇËT¹D­kÜIõ
häáy.Ý{Ð7÷LÙuý`O.è;í®nÎL{"âjy©Yÿ±S;æ,²+KKL£n;÷®¬ÿîýww´µëk¯v>{ÐðCß~4÷   àI>è|^ìâq"Â¿þfÜÄÈzDÉ     ðà.<©tí3<XqûRyð[fvpªt%¹z»ßH+®
V]¨¬CÊÌø´ö¢ä=U
+Hæå£`k_8Uº\½½ny¸Kê´æXeYòhå#QØv8#"ÆÇßÝ´9J­ÄÃóúo7Ö?ÕÝÈ¨YøUøå¯~ÞGJDÚB¥u÷¼yp$rOYÍ×áT%jjâ!¿^¼ÌÝµÑ=ÏÓä\HK½z!«°Öùº±ÃZqkoÔ|ãX°
¹+©2úÂB%)Ü=¯/v-ô£`o¨<aÉ´Yë²ÚNâAD|N¡<ZµaonÁÝµn¯ IZ·rÕ&EWuÉ §Äöæcd7$yzHI­)äI%Ú¼3û¶Ì5iÔÜ$I~íë¼/   xH&¯ÉNM:¥Âõs    à^üuÿ£m;ùûßìÚÞß¯}÷àÉß/á¯Ý¤%ÕÑ}ÙWJÄ>?ê¡<²ïâýÒdx{È$buÚÖ»C{±²iý\ÕÔH!­C¢¨:ºïûê¨ÉÝå,1®>¿raxwq­«±©§»§»§wÀka{*OºÈ©jù¶sgIìÙgÂØvTÎÊHK>pDí5<´LêÙiì°AíÝl!AÜ£¶©»}¬ .ùÀ¥ÇðIÁ>"ßY3Ô³Æ*òUº¾:4Ø[ÌJ¼Cûy9ÛZK¿óy4j¢ðôp÷ôðkß'$òû¯JÎ­Xy@M7kîåÉ«è0adGJ>pDM©ûå(úMà*·ïã)ÃÚJ¸[ßþr¶}·"ÓkÂ´!DûdÈzý0@ÆÄ£WøÂKBª}ElYkÕÁ¬úGÆhÕÄ«½·XyÐ{J´$Q\lô
þ°'K¬G¯á¯*Ôgr$]#Ö®]ÚÁ%båmüå¬ZÉ   OLý;]      ÔúXäøé¡ïùðóáMXc¹:çÂáù~Éä¨p×·égo+!N}1vÑìjªÂùK9òû-­×óSLë£¶Æpê¬ØU"Î~²"ôë5Úcsk)§p×pÉ'§­KT{bÝ·Qñ:"Ù}Wb¿5wË[×(É¹xdÎì¥:¢Ë×uûï+cCµ¿Íüýç×Î*9gé¬¦}´f×t*Ï=³ëÛÈ}º5;O]·pM»ï'OëwfÚ¥³¾£i£VìÜ´/³#§æFÓ©ë¾[îùÉ;'s¹'6íõÐ¼^srme}g¯íKDÄ(3Nþ6yÝU]¹¥³¾³öÑ½³¤ÎIü-|á5eþ1Wúõo$\á¹Ø¹¶ä{«-F^ô5=ÖNx/eÂ¦-³e3Æ=RFåÊ¿¾XÂU{Ù½ÖÃÚt«óaÉÁ¯ÌýeEâ¬ ßo
ágvý_ÄÂQs®X¨üø6!:·WÔÖé®®0ùçÈU)ÌÙ1iúo#e¶FmanÒÙkÎ<LÛ   ¨AÛö]­]XÅb!¢2õUH*s®vXEÎh¨0MÖ®    
Hdkç`o_ýÌÜRõU¡PHY,J'iÓûlª}Ûã²ö   Ò½k3çþ¹ÿÌMÚUTèzÃ²,[ÏßÒ   ÀÓª²ÒlÐëÈb±wxÖÁ    ðz¾Éð¼0ôk+¬]    <2B¡am
\O    ê
i2Ô®Òl
ñV   xÖÂÊÊJkW    
:]ÀÃªê¼    O-@`í    àY4Bd   âæbe    xHáAÜ%#[   x Dt+A¶X,#Pæ8eç­ýt   à±ÃqµÎ!Mz»-9¾=D¶2e   §DUhl±ªÎÓnÆÊ#PÖWÄb{®i2   @C%8è+µCõs3?®ºaÃ2­H$²v]    P=³Ùl2q<Ç]Ïy ¬Óìíì5tÍÚÏ    ½½½V[Që0¡µëÊBD66­¢d   §H$²µµgl"ª:{äTÅê^p±··³ös   á`oç*oZtUSëH¤Éð ,²X*ÖÖÚ    @0,k±T>¾¾dÙùÞ^   {;o¯æ
ê2. îhl!¡    hBÅB7û[<òf<oÊÉSùûy_)TN«ÇEù    f,Ã%övv
sÖ¥7Õe-¤Éð ,Åb©|   ÇA TÍMUã{äL&óÅô¹³´I½Ë2Ö~Ò    P#ãõ­®"-=§îkÕ#MµèùAO×wMN]ðOÒñt%gí§OÅB©ã    <n·ÏP~TÅ*®½ã    4Dõl2ç>o&ì%WÚ÷ïmÞþGÖÚO     jù     ðpD
W÷:J¸þ9}Ym28¾B«ÉÓ;¶öoZv©Ì­û{}]8{¿¾¯µçgTØ)^êòZPçÎí[¿ä«pW¯¨9¡,àÍw^v,Ì*Ð[Ä~÷uÓ¨åAC)+£»^MçáC¼9ê:µéGÆX¡¯ú½£½½øÞG+ôZaïXd±X,;{ÇPèw¤òyæËöËßcù+
ê+sK6Ìyk×   @DDFCà"ªú·ÉÄ;8Hîl¨ÐªiÌzL'~    ÐÀ<ÜUÔn}f³ìÝ|ØÌ½ÿ=¥&{ïÎ¯½Äfü¹sÃ/Ûw&ê\_yµ3Õç^0ûtòv$b[´kçXp\y%3G+kÑÒñúv[(DÊK9Ö>*ðô°]ô^£;.ÙhP;Ûûµèl÷zØ4ð¯,n/ÛwZ»
        GäÁ¯Â'²wiý«H}¾ðú¼b]öß¹eDdçù¢wéÏÔb´¹çÒÔ[{79Y\¢N>ñF÷.þ¼Þ¿Iqâþ\HQö¢·SÊéR"n"åéBôa~ö²ô°¯ºí&~ÕÞFhÙyºÆ:õÑ¹³ý»çË×+ïyL$ìä0ÌKä$¢Òb~g>öªhÜ§²D$è;´ñ¿Ó7.Ânù¢mëtoîÊýöÛËG9ç@Ûæb]ã·ý¡ÕÓÒauËÖtÑ[c;Ê×+>öã^fÜl×ôë3*y"g»=X9±Üesµ% _Öè=W
r\¥+       @W¿4Ùõ0ªHd#2ë/ÅI¿Þ4Ùl(¿>§X,³'­Zwc%C©Öl/¨Äl.9_ðvpgçÛ/Uýþ_ñ¦Ùé³jgf¢Â¹ÝA}ÛÜ=¹ïKv÷IIc\ÿ7óyíáÍÆËw>$ù@jÿö^àßU<ãMâõúd%}ÐLDfZK-Efº¬'gK½k?6Ân­èÛÍ×2ÌM`ºÙXLDL79ëMzròqøüeÚºëÚÞ«çö¿W^¾¾Øæ½, w¾odóÞ ñ@ÓÓÕ´wÎ7TÌÄ-È¶öÑ        xê{¾Â¿Ê7¹
®òÖcf³Ù\ûXXd6$ìETa&"ªÈÍRvjãã|.»«¨ © E( W©è®M ª¬±²åÂÉ$_ñmøÙço{¾^¸ÇxA_5Æü¸ýcr
´q&s±3ãsÍ«·m­ ½Ùäã&*.0ß¹i(=Ùa&"KR2¯Ê:cMD6I'ùËz"t}É¦ôbùÞ«"*Î6Ä(¿å#Z_,po´è¨Ü´~sÙ}JJÎµöq        x¤êÙéÂÌé´µÒ©µÔL&&ª},v*uf"²÷èÖ©qþ½Ü³G`îîÓ¥f"ªÈÏ(h×ÁÛ[äF9ñE=ºZ^éÒø&Ýsåý/©ÇÖ5Íïmß+[wøæÂÆBg[a§·nÞX Ï1ô°iÍÓÝD¼K(gúz(-©§+ïÞ²ÉR\~ã¶®²l\ª:4*ôUKnnÍoëp[9F!cæ·´Þ·ñMrøó|ÆRSIÖ>ê         Ø÷M®!'³¨C§¶­ÿù+UmvlÐZ¦Ë>^BÄxtjç\|v{A»äÓ·sëÌý)eDÄçdvíÙÖ§âÒ^eåCïF/rïv¶»}IRví-MJ3*¶½Ôè_=lo[j2Çl-_õ®±¦:[g5üm.Öy¤Ô\dÚV\ë~n0ßº°$%ýèµÏï¼3Nk'^¶´éèe;q]jlù«5        ðL>ü&îUyìàßOß·Fz{p }Î#§ÔÄºµïâVz*1#2;Ë¶ëîëHDDæK9HY÷Ü=g
;OòJÌÉ¯1Ç$v2Ôa½ÊØ8CiK)èzö|­²Ø,|ÁùæÌ_s£ªÛæä«ÔÜ lZ¬$*64¶ ô´q¹Ê§Þ;ÝÝFàÜèúM¦±Ð,Eú»÷{ù9717î;4TM_vpðzsÒyã]åó/RàKC%        <Sê17Ù|éÈK5<Vp|ã¯·ßçÇïüû!\ÁÉ­·ÆTÄïÞpó+n$ÒdüSjí£KG6«K|'qõßììÎ,/âÌ|leúËv]ó+|¦w¦_ÑÖSzÙ¥ØÈíÔ)õ}p $ôÕmÕ7Ð.°ÀlöêÀÉw²$]4½d÷^ºnS®Eìf;}mÁ¾k+8»Cä=Úõ¹ùJºk¼ÙTSI¥BQ¥
\         á{.êE(²úuoã¨<{°ÌÚµÀS)ãXE$ÈáúÝä8íú ÷þå8Å4Å¦½{ôõDDú¾ 1ã|ÁT@DdÉPZ\ÚQR~u½M-¯m<½±@§á×ÿa¼BÄÜ9¤ô¢~¾­ý}¯éÌI ºõ¹DdXzTøAïÆëXSå¥ÃÒ£&¾ÆLÇÒ+'wk´¢YÅô]æÝ       @C'hÛ¾«5÷ïöÊÈ¾ÍÌÊÌ£-à¬}0KÊÔWI@"©ÌùÞ1%Wööâ-¥²²²²ÒQÚÄ}p_ã    IDATÚå×;ûÛËhs   Ï2MP(ªþ]Q¡kÒTqïàRõU¡PHY,J'iSk    Ögí¹ÉÇ7®·ö1ÎÀ    
Îâ    à!<«ðÁs_E    ¿   ÀÃ±öÜdh²XÌ&È¦¡½ôÜìhª   ÏÉTuCL    TCá© ¨úãö
.M   x.8ãÍ³¸Ç°y&èËµã4óF/Kåk*ö4%tP »%"]~bôº%;ÓuÖ>>  q%dÜÈîî.Ò©óÎÿ¹uãê#5~6ë6Ø=}÷ñZ/ÖîôÙ¼)]+?ûlï­Áø ëB§¨ÁmSY2+*t:_ëW    °¯¨Ð·ÏJXk2ÓzÜÌÙñÅ£ßõÆ;cFÙcÌ§ãk$ 'íùé©¸eãFí=âÓÈ¾SØ7}kïÞuÐÛ\jÿàc|»Ð_¿=JÆ§( X&Â
BÀRQ¡ÓêÊ,d!µ«   Û H@¡P$´Ù¡PøØCdù»s¤nç|»É]Í"×¤èo=ÌºyH.ªFÇkN¯
àB*ñê>²µBLêì¸ås7&iH0(<t¿ç2cVEnMåB7LuOû·tI(sËâÈ½yrî6®§H·|ÑÆ$µ= <?ß#Û)·NýïÞ""*>·wqdîêCÛ^¥¹hû·¿IàÄ¯³½oâû[G|QÁ}ºA¼vÜ¼sïùÄÓ½ñmhwûllcÄ7e|µ!M#E lH`XDB   ð4H  ª ùñOIæHâçËÍüO6y}¸hÉ»7§ÄÝú ¶.5.mÔ¸álL|Â©³òõü"¢¦|è÷ÅøÍÙNA_ÎM±H7nêvË#öP³~KÃÆ¥-çäm<R>ýÏ¢b& tõ£ï0>¼kiÔ/TNÝ>>z^"~ô
 O¬µ¿üRÂÛåIÈä/§Ä{óÇW-9Òn
·øÖ@Lë{?ñ~¾ÊkÃHõ7V¤Ý¶>>EÀÚ&CýÅBD¡Ph©´XDðVH   à)q{2@  @xóþãÝuvâÙ<åæ³dD·¥»?ÿL<¨Ï1S%âc6.ßÊtòÎOÈæãæ%÷ú0P¾!¶'¢üø¸´1#^v£ãD\zÜ±b"â/¼ÀµjéÀõôULPQiâÞ³ÜgüÄ$4c'Cê$!½Z}çBµNKb¹¤Î
(¼:Uów±Ú¡ø +Cõv+P,nô¹°àá    OÁ­ÿè¶ùItLætÚ7ï}/HØ¹*a'ãÔªë q¡\Ør©øÖZ¼^CÄÅì­íðZ­"N«Ó^ß¨^«cX¬èþ¿UY=/yò [R-µÉòo[(KH§ÒÖ5­é¯zø «Bâ¶@¹êÛÐ/'   àÁYíâ{70Í{{éã¤ë/½xdËæÝÃýZÓt$ËTD$vóêr5:m&ax"b$±V¥ãXøÆBÓjõj.7%òßë.[ûèÀsIzAÔ·ùæÛ>Ü_éæ­:¿\uÇ_Ô$lÍùpõxâ{GâS ¬NøH¶ÂHÝÜ¥¸èóEpµ   Z<Egnv#¦~:åu_)CDÔ/hp87åR~Jb®{Ð`?"§naQ#}Ù¼Äd]óþ=Ý"¦Yïþ~EÉÇ«ÚúõtcÄÝÙËçÒôÉÇÓ]ûwãÞ7ôÐ@ñC P/é7
ùô·ZËÅDsÛ×ÿ1Ò%qcôE´*+o¡ "¦yï®ÍªVàgïJküÄ»>EÀÚÅÜdiàÄù_¾AûÃg¬Âu?COÅ×    hø´hâ»áÆY"Ns)9fQäÞb¢=Qk[¹ê
´ÿÏÞ½ÇEuÞ{ßÿé8ËÂ-Ê @Á DÅT
b«XI¬)¾hhÜò§ê®¶$;îHîz¸KÈ£Ûlr{]¢ÕzHEZ©)hD
Hp0PRf ®ÉÈó£ ÷Ë?k]ëZ×µÆ×2~sù[5¹ë×ä[¬²ù­+2¥0ã-¥VñÕ\Vï½dóW'­%?=åE¬ÙS¼Òþ[/¢Êv¤ñò( ÷éàº¥jLBÌ²Íq½XjNî[ûÚÃÍ"b:øÑ®ÈøÍAM¦Æ¼2ÕO±:i^¾*óí+öTta-¾Íïv{öxèwÆ>9µ×'kãfÇDGðpRDDmª-<¾GFÖÑªµ?0:
V|ÕtAH»ÁiØ­}.^¨·³ãÿM  <ÚÚ,CºÜÚÞÜtaàÀ2`´·_n¿ìhÚß3Ñú-Ùü6-ö^ ½ÀSÀÝëu¥­qüëÓ^KêEDqrKI[ýÒøa]½p~ûÃ]«»ì3lâé£ïqñ]@ôq{{M       x ô2MÖº&,ö×«åÙé+_Z½½FUkv¯|iuZvªõÌò¸·»K
AcBýïíkDµQ±cîé5      àÁÐ»ºÉãæÎ
uúìÔ¤ßç5X¥ä×r¤öTmëÑß×5IrRä¤3}s7w_jÇ0}Ý¨òÔ\9á>ÞZ¹vmfEè-ñã·åÃðôÄ?¶}nIÂ ½¨¦ªÜMë³ÏXÅóÅÍküe nH¿b¿ê5}iâ¼PogE­-Üò~¡IDëðÊ¢?GE,õE9ik3D´;Æ²y¯6z¦¯N1f¥¼Q¸,óõP'´]Á»V¼òni3    nf-Ýô³çû{ ðÀâ)
àîõjo²Îy¬¨UötTH¶Ôªm±Ïß[®K`ÇÚUEÄ5"R·cÅ+Ï?Váa´ìOúMV½z2-ö'/|Þ<GÉZ={QBzâ²@­ªø<Týûå±oäX´ ¯Çù×~°0&ö­§¹ËF:6`ñëñãjÒæÿ$:6%K OZ>ÝØq]cp´{ÎÒØÏ]oµ2.@¯[^¥Ö|0(       ¾©çi²aÜ/6¬~Þ[Dùü5+¦Óê|¾ýßÛß;Z§5Ny9mÃ<Eïyë7,xgEKö~tÂ""ÍùEubtu¹©HÆ°Ð4Üº£´Ù*Ö;JÃ|µb9µåx]Åª
5íHÏ«±´6ÏHyëÑGÊ2Óók¬b5mÏÈ7_R]ÖÖ|X
wjt
öéïo       îg=¯t¡6WTÔÝGêE*ê*L«*ÕgÊ¥®IµMgª+LÞKuEUz'#67®¼LTUEäæËZgo£â1zÍ¹7LAuiQ;ÎÔ»;ëÍõæãÖÃû+DsôcVîøhåõSkÝ;6'ë®4Õ74Áà¤s       pßêyl9³{í:qZ³4Ð¾iGi«HkÞ¦ä¼£¥{Ögxú¼áT´5yíþk_ÌÑª¤'¾¼íüÍ­®ÒQ'£ª¨æÜäëònÖ]º?       p^ÕM¶6flçø!F­½÷éÑS<u"Zcpl\¨ò³êû&Jn¬h¯×v,Ü\o-Èl®i4ë]=:>iGGÆ,âjnh4+®Æ«tÃÜ
WÑ;^í,îb2õÍl      à!Õ«4Y¬5vî(²(îQÉë~1'*61~iâÙs¤¬_5Û]1íÉ<Tw7ñ¬UUUqtwwÔés³©¦ÓÖ8þä
«N±ÿfÿ¢\ÓÈù/{ÝÇÇ$,«·Xrr\çÇO÷Öè|£'o~m{Ç ª[TL»V´ná§º5åW¨¢ÎÙÃè¨ÓöxÂ       ðpëy¥²Ì7VÕÇ,I;fvü´8^DL;Ó×gäÕXîn^y¹Ï¼ê¿39áýÔ$ýÄÔÝ¯4Õåg¬[¸UäæüYÓÞH×'Æ¤e&¹¶pïÚìfæ´76É+ÖgÆëÅR]²vOMGafõdVEhòD½µ¾èôb«HÃ±¼Â91+7ûî{#qÃqö*   wÊjU¿þÚÚ~ùrO zoà­¢Õ*=:ëÿ²öVA¾Ñþ?ÿê¹ÿìï5À¹óà±ON½+éÜÆÍ;oáÌ1Nb*Ü»3sç£µ­ý½ünh#v/±ÜZOùÑÔÞÞ."_5]Ò.bpvkêíìt=   ÷½¶6Ë¡.·¶77]8p  ííÛ/;v1ÕzÉªò^ AZEQßaç_þð;ÁçÖv¢d ¢;y övoòUÚÂÏ7I\HÛ×7¯Ý   ðàøÚúuO úÌ×_[ï<MyDÉ Pwò ¼Û4YDÄZÓß«   pïµ··_¾l0`ÀÝ ÷ööööö;y¬µ··k5ßl$Jð »`_¤Ékvòìþ   ðP0`zé_ý= èKö:;é6`Àâ/o
ÿ\`ÞWx/êÔg¾xÌóñþ¾7 rÝ> ö÷     xßj ÷ Òd     »BàA     Ð{÷O¬ñyúß
tüf³Óä,ôÔôfÄî>fÚ°>3dÁÏç8Þý@èá~ûüÏâ~öÒO'¿qÐîñYqÏG¸+¿»pzë&   ¸ó
ä&Û?üìü]7Ä?:6.~^Ðwý°IDD\^HßþÊ7vºó«.ËÏÈøÿ·Lð"-_Ûñ»×Ó
.v1²â2~^\|ì8ùÓ~ùWUDDybÙûÿwác7öº°;qæêµ³ÙM_³êÇOPÔ³%»Ö½þ»M]\î©Å¯ÄOò¼Òù·¿;XO¾ }©ë(¹"Óýø±º=È®±õ÷Ò¿--u_ü³©µg`÷xä'z8Øôõ¥Ö¶Öª¼mÖÚDÓÌè()ûuëÚyUïòR[UÎÖ*qÿù´[ª«Ê+/µ<´¿q+Òd    ß¦ï}©¢îü%×¾Î'ñ¿òåy^o¬?>â®}þìæ÷';©x<1ÅåÌÿøÝá/Å7æßþêÃ?}ýóÎþæ¯L]µö×Åû>¯¥\kTÿñÎÞ¹ÖÅç÷ßqøNÃý~ýÚ/mùÕÌ=çXºþõ?ýì¯vw`;<>Õ³iûÄ¼2óY¿^óú+ÿý«,ó=øJ ônv%÷ñPDÄè3ü©ÍuÔpMMíÃàµ9úiÿÎ íì¿Ðxÿl²ùãÞøo-ÝûrÎÆnD`Ä#'_ÈøôáMõï­©øÓÏú{¸§H   |þyb{ú ¯éÞ}¦o{6Uèÿý¬çÍªz-á}bþFOßuNDªw¯þÕîÖÃÿíì§zêåóÎ6«Ö¼0WUGÄnzvÌíGVÆÏ Wüö`§¯2åÌ~ñÃúïGW.\
¢ß½§þÿþ¿ü{ÇçvüåÌâ9¾#$«ìÛú |º)pÑÇ@îã®VåUó¡©½cÚ¹DøíDmú¢Êv5ÛÔñö9*¶/.t7®çäÉ^FElm
§óöçÕ¶uÞY8}Úµ¹¶²Õ&-W¦wÔHëÊ£~vºÙ&ófo±9z8¶}QÜââçfo:úñ®ÒfQFL
õsvT4¶Ö¦ª#%"Cfþ0ÐÉÞ~ð ùøcQsÇÀ#¦ýl²úùïù{MkÕgþôË.¦§qô
6ññ¡vbûª®è³çÚDõ¤³½½TÌk
ü¸¦õô¾Ì¼Þn·µ-­0Mðý®"ÒÖ³SíÜ'þ äq£½ÆÖÚøÅgyygÌ"2dÒ3ÓíOUÙ{{8ØÙV«?Ë>pÚ,"¢<vÄ÷éî{ÑxÍýÏKC}+ÛÙÏ÷úE³MD4>Ã&yíEm®=zàÓâ6»Q3fOag?øüá?7zø
l«>°5ûLO¢qå±gCFÚ+ÉþàÚ¹}°ÜßH   ÜûfUUEô;Mÿýç#C¿þû7Ü!ãG4=cîvh¥ÃNQ?ù~ËþÄCÿ³æ¾ÃåÌ_Ï2þåø ew1n¯HI·R¡Û~¶onûN= ÅÙËÃVûç3&Î~|¦¦Æ&¢ÜvtGzi³â6íÇ3ÛjDDL2¤nßÖm5ª£ÿÓóGjª»¸µå\ñ{ÛÄÁ+rÞ´Ðê­VÒÐ¸FUJ÷ý#çÅyâ¬{Ëi»Qá?ôW~ôòÍ'"£gNnù0ï¬È Gvî|&zdãÖ¿ýÉDÒæµåì¹%9Ûb³s6'rò¨ê¬Óª\,ØQ ¨Ý|QããÅ;·}j;¯'O,ÿòÓÎag=½ï]çmvýøéévþ©ÄÜü¬h|f.<¦xßöÿ>«jî¦Ò¯ò=÷'GZÎÕ÷4uüa¤[CöÎ=5mÊÉsfDýigG
&wé÷nk¶iÜ§-<²ü/U6}À§ÔÏ>ÞòE³fxÈ>jûNw~IÍpW½ÛþxÎ&úÀÙs§6n+øJ3bò¬iCÊ÷mÿÓYÕqÔÓsfL¾ða^­íô¾­§exDlÔÄÉ-Ù}PÕ¦ÑHwY«_ø/EB~2Óþæ#}°ÜÇx   ÇéÏ\üëÿ|³KÔª¸À²mï~.ûáO(ßþQy]+ZÌÊø_Û´î¯Uª:X¬t;²~Ò¿/û~ËÊ\ èñq7[UÅE1W·yø8kDD3|¤Q­<ZÚli«-(nüZDD=;4ø¬¦MÄÖ|º¸úR7A¡íâåm6[Ë§ë4?ºyhjWEÔÆÅg;.¨xn*:ZÞbQ/þãóêAùõbÝEµ¥¹­õBíE[k«ªtÝRSy¶Å&"m5§ê.9ºß¥sÅåf¶Æ³Ívßµï< â;rðGÎ«"¶¶/5ý»qlÛÙUEÄÖ«
ö~3_ú^|)vvñbî¾£{xºãHï¡
'Ö´zöèçgõ~>N¾n(+n¶íì¹f½½£W±©ààÍ6õÜçÅ_G¹uùgJsuñ9¹ôtãH7Ñxø{IùÑÏÎvüN(ªäæ3ä¦sVµõú~Ü^_¬÷/ö&   xhø<?ÏçôG¿½¹\ÓÔUoýÚ·ø·ñ<Óûñç9¾qß¹®:µ\R÷yaÙZ¶$n?'ãåz© [ïÿÂï~vãâÍ%Â» Ü
OýÌh4ÕÇsg5Ê`MÛÙ«[<[Û.uü0ØA±µ¶]yªØZ[Z¥ë´ÖnD`èï¡öl¯ùgC§=5¢¹ÔöÏ+Ñ£ÚÒÚq;ûÁÒÚvm«i«©Uq¬ùZíèûµzéa£ÿäÎÑØÛÛ»^ù¥¶òðÎÃd½ÝàK_µ^í¬¶¶Ú¢ñVÓ]½0îJÝäÞì ¨­æ«O{[K«:ØÞ^¤IDljÛÕÙ®¬ÐÞÁ~Ð°&_[v³2X¤ó?,l×n»tÉ¦8(¢ØÛþîÈ§îsíÙªnÚ)¯¶4÷ýá¾Xî_½Ju®cý\SUaåyk/     :(S1¤à÷ûëohszjÕÚÕã¿ümüdõþ¯ÿ"úïÿtºäüûß»Þ=|öä9Y÷ì?¾øQµË(OýÙ=]þãr}PâïÿcFKzÂ/ÿt¿RèíÎ8zADÄñÉOó1ÊÙõÍîZ\ª(WÂK-ªfr%­lßu©
Å+loköÞÌ6ÍÈ§ê¼¯­U½4ÈÎ^#m"¢±¬H«´µ^ïÚÙt<&í
öjk¢GLþa&w×ÎòÈ°i?
ë«[dkm»4Xuz¢Ø;hÔÆ¯ýùÖ¼ÖU¡¿ú½hìK-­]ôn½T»å/åw:e;{æÛkÔsª¨­ê%SÑÞÌ#½3@¾¾W+ïáZpÿêE¥ÇñIë»*eCâl/GïÈ%ëÒ~ÿ6ßúkíºåÓ½uý½¾ð|ióï<×goY   po9Eýäûrð7Ôpz-uõ/ÿ×¿ÿ.¯E¯×ëõÊõ
jú)¯¼ó¿}âÎþ­çüç&ýëöoÊPÆÇþç; ôW?«Çÿ×"g??rQqzbÞ+?õ-Î:lî¬³ôïÿsvKúªÕ=«tL¯¿o!ûÛà³_mëp®ü¬xøÛ¹ò³Êã½4"Êð':¶
6W×¶Ç<é¬hFxØwY$X£Ö¨--ªØôè²óÅÊ³âö¤¿FD3$ `DÇÕêZûÀ>Í'ùõ¥××Ø+[[K«MDâ?Öë»}wO_r8L»Ç¦~¯¡ôË{ñåèÝåÜÍs¼¥¼ìqÌdw;QF<ùä¶ªÒNs^i®,mv~2ä1Gâ0lÄ.ÇdïxýwBsUmØª¿ÔøMt¶ÓÆÎÑ}X×»Ô¿-]®E1qÆÓ~C¾yÎ÷F?ân÷ÖN:ãÞéÍÞdE«­¢hüÆy»Ý¶âë¢ì¯¸õí¦Zß_¼·Úÿo«þíý3×ÚtI;Õù©úßf,
¼u0Ó¾×ßS~ùËý-GÔùkÌËÓº]«Mµ·¦¥çÕÜ´wZ²*=Éé+ö®µ¹Íý¯wg¿ÿöñÆÝ©kr;]¶. :Rûq¡I    Ü¹¡AÑO
<xð`õ¿T÷Ùö¿\êõhÊøe©«Ã!|7í]hÎ[³ä?«""ýð§ãë·ÿ´àzâë;çèÇä±ÕÛ¾ÒröãýÝqUDÄaøãc(¼öïl°_}¸,h°òÊÎ?Å_Øÿúâ´UD ççyÞòjÙ-:& P9âpu3ÿþ»_ÿñWÿsïBõlÁ¾7~»ûb§ÅütÈ/ÿï¾_vôhùÛ«OÿòïìQ"}ø tºòÆk;;/îesåsF<7MZÏ|ùÏ?ßÿþ?|>P£6Wø¢n¸}c·U-ò·h¢¨ÍÕ'«ÚFuÑÙv.÷ÏGDÌüùdi½XYT~±#Åi+ÿôÏvÓÂæ=¡HëÅ/s÷}v¶ó]¨¶ªÏúDÌû¨æÒ_\pÅçéÙ]íìí÷çâÆ´¶ÖæýñÓªÝ¨¦£{óBÂ#ÙÍÜP³¿Ä,¢6R¯4ÈcîÏýÌÕy{³Ë;¯ð`÷xä'z8ØôõX¯Öª¼mÖv³§ÖÎmbè-.=Ýu·â?gÛÿ dîÏi=ÿÅ§û>ëªô²¹hOL8+6Ü^#jËù/>;p¶þ__¬nxì1!­¹<oÑW"b«ÉÛ714bîdElmÍ
'ÿZs^dxÈ³Ów°³<Hf.òjmü|oVQsgã*>OÏuµSìùqÚZ{ðV9þxÆÃ`Å~ð \ä¡¶]ø<ûOÿè,ïj-'WW»bMéÅî²2tÄpãEjnú¦:é{gÀØ'§öô_øÂH_¥æÈ½
½(uÑUïäê¢Ó>lÉú­ëW|P""bmªi£«""Ê¸øÕ Ú­ ©ª¨úÚæq«Ò-]oÑºÎZªì}ígïßøß{]§ÉÝ¬D;eYfLãÊ{öåÜííí"òUÓ í"§a·ö¹x¡ÞÎîAÚg  ;ÔÖf2ÔåÖöæ¦¤½ýrûeGÃÐ.1]l x8ßaÏ{ù üòÌy>Þ?wÝrö³Í_3rjú+âÔxÍ[÷áÎb&m    IDAT{²±n½Ùl)Íy¯4ç[±¥¡®#®5øYU±4Õ©¸óÖ1h=Ì¢*Íåg®ÑX-õµu1qMí&2!Øûý²;=_Ú¼Æ?{ùËÛê´^áKz;ëÅR_qdKê¦ÆÄÌ×CDÒvïZñÊ»5ÇÍtÕ+VsÍÉR3ZÅ0ë-áåéUþ1¡²û#óüè¦·¼y¸£üÍ°ëS£+cS©4
     ð0q1äëªÜ~{¨uEçþbâæ3jû{úSU«ÚË¢c3âkØ°p^ÔÂ¤-
câÃ¯[^¥Ö|0ûwKÃ/5­OX4cþ²õ¥Î±«Ãu"¢ªâ<Õ¹"qåöýYEteC¯qRws~vQ2     ÀC¦ùÈÎOÏ÷÷,{¡{ÇÍyþ)¨¦Òºò°UÉsGÞ6¶Uk²Vl:zû2ÃÏu|ã#}´(­!0jáÇú·¾>Y ß±/þæ6SùMuz­Õd¶UÎd­Ï÷ëÇ¢&(ùk?Èk°ÏKßS>AsLDÑÖÿmkNe³äfLH5äeÄ8%Ä§áHZ)a2      ú­rÏæÊþ ½©t¡Z;RQ«ªZê+«Ê+´·}õ°¹¢ª©ó÷GTg¯MÙ{ýÚ(S^X?÷®V¢ÆgîQE,ÕKON¿]YÝ+Só®¿äÙ¾òõà{ÔíÛ¾üµÌ?TÌ;¸ßáº^%htuS~CëÕÛÑXoÒúEDTK}Ã¾C9¹KEMqÌúD:udõ¡M§îj}   À#gðwìî~ xÝú ôõä© ßõ"Mn>º1yéß\SUae«µò³{q]Umª;UzæÚg{ëÝ¾¹øÔG+SsÍ"¢ZLu&Ëí{©ºòÒ²ÞÂ ÞraÓáMÿ»gìÔàð)Áó_p]ÂÚüétVõZm-È:ÜòT°ñ¸xÕåüþ    #Ò
 , 5½©|R­Õg**ÏTÔv%ß!­ÁQg©;½sÃêW¯-Ð»±BtC]\öW>ê]=Öú[ßâj=}¤Þ/4úG¡>59jûû      À]èMÝäñI)Î¢LûÅºBï snSéÂÚT¶qÅÝ»ý@¼2-Ñ%{mrFaó÷sVLeM"ª¨¢sö0:Ö7Ù}(&é¹K369ÄÍò7I>v»È¥9¹5QÏÌµ¤§6ô÷²       ànô¦n²¢íØ©«U­_À8o·ÛvóP|]0M¶ä§­ÍZ¸eAQ-õ5ßúàUäX^á}÷½¸!uÝæåq+7à$Öú´ÕéyÝ­cÉ:XõL5ç ¯õ      ð`0öÉ©==Gç¾0ÒW©9²coaµ§g?R´§&é>X¸:ï¾
ÕÛÛÛEä«¦2@ÚENÃnísñB½®ÇC  à¾×Öf2ÔåÖöæ¦¤½ýrûeGÃÐ.iµ´ô÷:  /Ùëî°'@ n½Ùl)Íy¯4§¿v¿Óê=&Ä$©ûVäß·Q2       Ü¡Þ¤É¸±o¯yÞØ¾ns)û·      <ðH¿%gÞKøÉ{ý=        è+û{        i2        {¤É       î&       ºG       èi2        {¤É       î&       º×i²ÖàæjÔõ÷        ß>Kµ^³ßMÍ|wY¶¿       èc}&[kòwjcèÊß.ö²ïïuh#öm_B¸
       wmPÏÐyFÇÇEû9*·R´ªb´ôMQW¬ËªµÞ|X;vùÆõ~9gT\i·bËk¡¥k®Î³t´g½³yAÓÚ¸×qÊÐqîÎzEÔ¦Úò¢ýS÷°Ü<¤ÛÜÿz7ªä7®]K²*=É¸uáÒ=¦c$5I¹U:ã6×§fgNe        pßëy¬8ãcì²ÞÙÛI+ßL­%ÍaÁF©hï ½ªøùkóZEDA>R¶þUüb_2ïÝ¸ò­âjÖÅ/tq|LòrSìê<ÓOÕtæèñ.»>7oô¶=9Ö;       Q=OMùoÇÎ{û6´Æ°%)¯Fx)wcê¢Ö[{X

Õ%Ç;f~Ò,"îcJóóÝ|'zkZE´ã¦øJéÖ|ü|=ÌGÒóNYED*ïL¶4Ï06÷h¦ÚÈ¤ÝK,É×åY'¾àá¤¨MµÙé)ï±~íboE^ý`WØ¦ù«s]ÂâÆú´¢6Üº~c^U;qùÆ$ÝLeV¬_É|oîâÁÇ¿ùºóÅ¯ínèïï       ¾}}÷>·ð¥bÊßòÉËm;Y
VÏ ã¸ ®õÇö­4tÑúNôÓV+0kæÏô5\­zl)ÊÙ]ÜÉ7Î-pÁÒ¹ö¹kâ£f,]¯Ø¹bÝ³ûÖ¢Ù«s¬^«[æÏþÉü{Ô)I1"¢ªV%0ÜûØºØÅÿß¶¬#õîÁQ^W÷TRK      àÑÐó½É×híF¹á¼Å*"bµÔ(:i.ÊXÿq¥ÓsóU%Ì ò×æU&z5¦WJmÂ Ã¶:w°¿¾1ÿXX§§¤'.Y³#®±¼´ªäTA^vîÑÚÛìwÅyöÛ[g£ñÔÍu:½XMM«X2^~&CDä·óöhÈ¹Wæl98oýÔPï÷·b)Þ½·¸Á*bÊÉ­
ô}oShÂÇ+%ïçö.Ý      NoÓdïüWW&LPò×®JÊ®³©8sõkÝ×p¬¸:&t¢·¶Pä¯í®°ÖHYýsAãtûK}]LÅy$¤õÄ¶ítä?!`âÉUï\»tSá7£jÕ»1%óúô´þ1«ënêb=öÑ¢UßM_q²°(?ëÜ
7ÖJÖº¥¡®új÷êFtvÑYDmª«¾Ò÷LÖÁªgfM/+ §Ü|èvé6       <z&¾ºjq N­ÈÚ]ÔØ³wØÕäftõ1ø*¥[K¬"%jâD?G}àHsÑÖ³6:sêxÎÑºÿhUZü¢Ù{3k¿1¢µ©¶êTéµÓ´NfÝ7ºÙñÄ^A¡aÁ!SãRfo^ñÚNç¨Üt®z}îsJbæ¶©ccé¹ïÁ      LÏÓdoG,"ª>`ñkßÒEm(ÎÜS{»ÙZWd¢s.Ï.¶µìh©;!\ïg-I-³8¼°$Ü´3åã²«CXk*kdAß«UjízkCeþîÊüÝ{^|wMtçësªoh ®"""Zogi(«·Ê7¯ÖU´(62J Ôæÿ¾ g1:       <Èzþ>ÅÑÝxeë¯Þèæá~_>¾ÞNÚNÎ·*Vý¢f¸×-jÖÂ¢*°(¥,ïXGíæzchÜ²¤çBÆº
3]½ÇOÿÅâ¼Þ,Ò}nò
Q^ö"¢s÷õÐYëEDTqòr5èìOeçWÃÿÈS'bðâX~0çvjÎÍ>©[!YEÉ       !=ßlÊO[ûËkÆéÕkÒM=U­E%Jh°iwaÃÕ!UÇñ8µçZQäm)+ÕØqÉ1½"jSmyQVò­'záÖìL]ï¾$öíôzE5×do\Ý,ÖY¬Ù2:#aÅÖäµº¥qÉ;^ÑJScáÁu)ÛênzOßUC9ùK&ùË)!L      ð(0öÉ©½8Í0>&ùÕyþzÓ·V¥<ÿ%«ÆYï¤®Xþ^åÝu_hoo¯.È i18
»µÏÅõvvº
  û^[eÈP[Û.8PööËí
C»¤ÕÒÒßë ¾d¯s¸Ã< <dº} ö¼ÒoMzë£Ü¢â
G%JÖjuÆËçzîÙñ°DÉ       pz^éâ
«éxÆkÇû{ú÷vê²ÌWÔS9)oåú{2       põ:M~äX¦Ì>Øß       ~ÒËJ       G
i2        {¤É       î&       ºG       èi2        {¤É       î&       º7¨ÇÒ\}Ü¥©ª¼¶ÕÚß       ô¡¾IµßÙK^^ü""êéÍ+3K[û{i       >Ó.´3'%tDÉÒx õíý%»¾öá½àÙOWïqÖ;»6þÂOÛßó       ^ê½É ³NÐ)ãõÙuV{£Á\Sg¹µæÖ÷ï­m8¶øµ
7¹<¨ioRljq§2tÑÚÜMw7g­[øÒWcB¨µ¹Þyû`Ý­]BV¥'?¥»Þ Zê+ìØ¾m×       =w¿7ÙÞgÂÊ²×YDDë8qIÒæ
Ë¶ïä,Õ¬s½¡Å14ÒW5«]_L9Æénç¬
WºðE±©çÇ-;±MÃê©^L}11öÅÄÅ¿ÙxÀðZb¸á®ï       <hî~o²¢è®f±ÎI'¢¿*iæHEjNÏ²Vù{oË¨èh0FyUTúz\é`?zNüÒ¹AFk÷¦§¼_h²,óõP'´]Á»V¼ònMÀüåq'tSù±ë×î9eéÆÈß\6;ÐMQkóÓ×%ræÎZ'']ýßÊ,"ªªJo´Zêkë®ì®­«Xk·eA¸6ç°Ut¾Ñ/,0ÒI±k
27mÜQÔ*âûÒæÕþÇÒ«ýæu4æ¾¿îêfí+ãcVÆs7(ª©üØÎ´µ{NXDDë·4.Ôß¨UÊ¤§n8x^DS^X:Î¨µ±${ëúô¼Þo       ?ÜýÞdµ©¡ùÊú1 ïn=°{SòÌk:Ë>µê±ÜcpßÏîa!ùG¯nMÖú-Xç[±j~ôØ·æ&.¯µ^·4½J­ù(aö+ïÚ/_k8²8&ú¥ôr÷¤øqZÅej¸>;eáÂ¸ÙÖà¸¡º[¯ÞZrªÑcBDøÓûdl=z­*¢("b¸r±±x}Â¢ó¥
]¢ëè¡øMªHM|æù¸mÐÄ%37®;8aù,¢M±Ñ¢_J¯öYã+"âµ iy9#iáüÄ¤½±|Ù|7¯¹IË'·%Ïýù+ö§&®ëùíýV       .Üml?/aæÈÛª?ßÐyLkÉÏ*2FhED<£ÂÜJ²¯´n]ºxUJvÅjm8SØ óñv¾étÝ¤¨ Já¶£
­Ú¼ÍkS35wlVö¤¬³XOd¬W½o-L¡õôp²ê§Æ,Ð¼eÅª7³ÏÃtÒgÔY>êÉ¼"«è&EOÜ­G¬b=4}O¡5áÊmµ(kW¥UÄZ³7«Põ
 ¼¡Üµ`}BâÒù
V«¥6?«ÈââîªìQ»9ûÉrþÄ¶MÉ÷[Å;2Ü§fÏæì3Kåþ-«ó uïÃ/       îØÝTºÐ§Ä%¿åszjyö¦y
]íùµäg$ÄÓõ5Ür¨Y »6¶aÜ¸S=´"¢èêomtuSáÕJóv¸¨MMWZU«*[ouÀE4äl?¤!U%µ­¢
};QÖ&n(úætÀøÌ]qW~VsCÁö·6eD¼\ôàßnqCçcÇUë®N@,âo¸)Ïv° á¹1ºR­ÖÅè,¦ªú+]ê~R'¢
7:+£ã2÷Å]?¹©ÊE+»       pïõ:MÖºÅ%/ò¸Õ«öí-0ëµjC]EiAnÑùn3OË±ùÚÄ¨ öêIú¢ô\D\=ä>÷åÖ-¿YYÚ,âùâæ5Á·®È-Iñ0D.xFÉIXQa(sÙ°dedYrSx°¤ºÝ|O}´25×,"Ð¥¯F36¾wüjYµqûÄwK¿qVÇçN®õIJªÞûÉh'.ß|½ÆíRùc©Ñ¿É!=      Ðïz&k½#º\k0þÃ[)×Ö;d-Î:lM
§üßÜj}üFJQêöÒfÃHã-IkC]½\öRÚ*"ºÀé½w||¾Ûk:¹;©±^DLùëöjÒz®~ëª·lUkcuåÈõÛÒÄG%ïni¨ªY^:é¡ØÝ¦Úf«âdtÕJUDg4¯
¨÷óu1¤e±8û¸é«Xëe«HkøáÊÁ­å
2Õ×_Ó17­ÑÕ©©®h      @èEÝd­{DÉ""ÖÙGÌfJAÖÍU&LÍwÐ8h
óÃ]L¢7:jETQEçìatÔ©YÇÔàEán¯Ä¸Þb¾KVýf%DúuNÖªj»¥Þ¢3èìuÚ®N¬Ø¹i{CÀâåÓÝEÄRuÈ2nA\¸V´c[¶!1âjA}`Tl £VÇ>7}ZwìúÒÌ
Íª~äXo{Ñy!.Do³È©ìüjcøâ9FÃ°±ÏÅ%Ì
Ð«ÖìrChlLA+:·¥o®Mèr       ðméy¬5'Ø¥!wýÚ¬j¹(YDDJsr¤éPÎÍ[­'¶}°Ï¼åÃbÜnJÞyR¹*íßcy¼róÅµë¶Ôø&¼¾cCOMFÒÆÂ;Ù¶k=^çóÂêÌÓG)RÓëü×ìÈLmìúÌ3[R÷Ôû-Z:ÇU¤5/5%íÔ°Å>8°{cR¤uß[©Y¦~jõá#ú5;vmL©é»M7qlëæcÚÙo§ïËLÝÉ©¹åÆYëßî^¹5ym¾2wÕÌMÉ3µ¹kßÙQ+R¹3ù­êÔe»?Ú±aGé¦äôb¶&      èÆ>9µggh=¾½fñhETõî¢äçK×øg/y[]ÏäNµ··ÈWMd´ÝÚçâz;;]Ï   }¯­Í2d¨Ë­íÍM(H{ûåöË¡]Òjiéïu @_²×9ÜaO 2Ý> {^7Ùzf×¦tï%QÒóþ¦Ì"¢d       xøõæ-|Òýo.Ýßß3       Ü;½IÑ¹3ï.þIÏ       ú^ÏßÂ       xô&       ºG       èi2        {¤É       î&       ºG       èi2        {¤É       î&       ºG       èi2        {ý&;Lûl´ÿwú{ù       ;2èN;:=7{Ã­íõGÿ°¯¢íù¾±´î_"Ò+ÛÔþ^>       àÜqüÕÉO¶hL1Õ±ü@ÎiMDlmw%8¨9RZ÷/Ëæ¦Æþ^;       àNÝql³ÍVùj³ÙÚþùù_""¢æ?)äáßS4¶¶Ç©j±Ø¹Méò=ETKS]I^nûQ´ÿwID¬kUÖöÓnsg?½{w6pö·òCµ.cwúæ_µÇý­¼EDì\Â§f'æúòÏª
O?ñÏO¶ïïû       ¦;N;a7rRÔcÙ»Klz×'£"¾ôÕ'Ç¾ræ!Ç³3N·ÞyBDhÈ¨úÝÇ÷rd>°íðE·+\ÑóY½ã«ËúQóÇxT®Ö¸N
óQNÜVxAãòä´Ð!ÔÚúûf      À#ë.ßÂ÷ÇF
o+ÿ¼´É*rÙ\w¢¨^çå3DD¬jµØÌGv}´»ÄÒÅ(j]YéWEÄ\î+ÍwìD¹¹i
ÛlÍu¨ïïû       ¶»Ü¬sÒk]fþüëM_Û¾£±Õ~^èóthôÂ'.«¯­<]UýµóAlmæ«Y³Í&"ÅN§iûgËÝÈêÿùµSß*       xÝm¥[cþîÝ%ÿúFëùØVîèâááåá3möèúÜ¬¿T©=UÓß7       p»¬tai2ÞÉñZö«Ø}G#"2PQ´¶¶æºÓEÏÞ÷òË®£+=×ÖÖf³ûÃq:¹èî>ö       ôÚ]¦Éÿúòt£fäØ .ßhç57jªË@q½ b«N#"Êw|O«Ûl"6(úïêÝî<¶¯?/Îþ´s;v{       ?Ýíß¶ªCYvBÂ¢cíDÚL_?x¨þ²ÈüI!S¢bôÊ [ÛÅºS9ùõ6såÕjØ¤ùs]r¶ìvÜ¼\ç§#SëN}VÒ<l­¿ï       <º}rjÏ¡35r¹#BþÞQs<ªvì-3÷÷>ííí"òUÓ í"§a·ö¹x¡ÞÎN×ß3  @ßkk³êrk{sÓÊÒÞ~¹ý²£ah´ZZú{ ÐìuwØ L·À»¬tñ­Ñ¸|Áüè`g;h¾ç4ê»_Õ7%      @¹__ng«?rðdø)ÏùÛ
R-UGr
û{N       ðèº_ÓdµþTÖÎSý=       Èý[é       p?!M       t4       Ð=Òd       @÷H       Ý#M       t4       Ð=Òd       @÷H       Ý#M       toP¡µ7ºtQ,õ5u
k¯       Ð÷î*MÖy/1ÁMµ¥©âÈ¾ÌRÇq³¼OíLû¤Ìò-/@´{%yáº<rl       øÖô:MÖ§Ä%¿å£ÚPUXQ×$:wOïIÏ¿>&øP~j±83»ì6µ¾¿xoÍlãõÕÜX]µ9uçQSß       Àíô2MÖùE­\å£
·¦¦d6\í½Ã­\å35HDÔ®P«÷®IÚy¾ãÞ=xaü¤W­Wìièï;       ¸UïÒdÇq3gÓKùÎuIï_«e¡5úùêU¥û!TssMmÝµ;Sôcv$ëöì¶Ö-$áE~XêrÒÖf5ç¾³9¼<½Àcæ$NL'3×®ÛQzãÎgûÑsâÎ
ò0êÄ\[¸7=åýB5leærÝæØ×vwìzÖ¯Ù§¦.yí`kßy       xìÍIZµéÈ½7EÖ|Gº\-¢\_Sk¾ãZÆªª^ÙË¬
Xüzü¸ôù?MÉRÂO7XEq-¿æei5¾xßxq¿+ã|«3VÍ^ûV±ÓÜÄÅãµCY¹fßð°a}tSCýÕ¬CDÉ       Ð3½ÚlmÎ[?ãÖæÚUÏäôb<­[pÂsAJEF¡E´ãÃ#eÓók¬"¦²íùÑoöïO¶°ÈùÜ½ ¯¥úÚÕK·.]¼ÓÜÐl±Ï)lçí,Ç³7§º¼³Fì§øªÇ×æó¾>       è¡^¤ÉZC`øü°[Õ#»÷ÖÜÏjMêR»¯è|ç±­â³`Í¾¹W~Vµ¾('eí»³~ÌÊ­¼Þ¹ÖÝ(bQë¯Vh¶64Ü%
D    IDAT7É£Q{ã¼ÆÍ[8ÕÓI+"ÞI©±È>Rÿvh¨ÛÎLSPx %wu1a2       ôTÏÓd­sDLÜóWK#«¦¢âÌÊk ­Öý©¸ñCÍù§r:
nÕê½ë÷6¸(9Î~÷Æôð©¢s®ËûÆ¹Æ?*W:_ã>÷åÖ-¿YYÚ,âùâæ5ÁJsrk¢Â#=wU³$"L      ëUÝä«ÔÜ´7ÞÙu=J­186f4æf4tÛªæÆÊ3gN}¼qs[lâ,o­¹¡Ñ¬¸z\ËuÃÜ
W7 +.W7#k
Nbª1]O±}üFJQÖöÒfÃHãµWÉ:Xå1!|voÓ¡É       Ðs½NÕ¦&Uq]·`Æ_w½Áè9ñGKÖ¯_aTK¶¦n>Ü|ÇCÏJý Ä}ÁÊO­µ('·Áu~ütoÎ7zyòæ×f¹_íêÿ£E!F­è<gÏ¤¯ÉÏo¸>J©Yñg­!`~b¸IôFÇì¹æ`N{Tl`snvYßp       x õ¢n²Úd¶¹nËoÒ"¬ðzhÂõµ~¿ný'g,=²aÿúÐ´¸ÄØÃ«Þ+-N{c¼²`}f¼^,Õ¥¹õEDÔæÜè7ÓZµ¡ í­=5"W÷-[Olû`_\òUSÕôw¬[fNþ·÷Ë¤!?«(ÎßUÙß÷       LÆ>9µ§çh
þFKIéy«Î-xö¨p¿aÚ\]¹-÷éÛ©%aõÎæYå+7öb|Ï6'ûì]¶ìãóßÊÜdííí"òUÓ í"§a·ö¹x¡ÞÎN×ß3  @ßkk³êrk{sÓÊÒÞ~¹ý²£ah´ZZú{ ÐìuwØ L·À^ìM«éÌ Ó-µùkó3û{Ój
ÎÁÏ%ÎP¤d%      @/õ&M~ÂS¶ÄûNn_×³ê       ë4¹aÏË³÷ôø,Óþe³÷÷÷Ô      à7°¿'        x &       ºG       èi2        {¤É       î&       ºG       èi2        {w&ë­huÃ:­h
Ãºþ^        ¯ÝMl?6&ióFE,_¶<Ôhð}s]JL y2       <dõúLWP³Þ=xág'?L_¼¤ÙÇ]ç¤{UåT¶ö÷Ò        }¦{u^sS6,f´N·Ð§BýDFE<5ÉCýèè¤
I½ì»D;eÙö}íz-äNö2»Í
÷ú¶îÖ+|þ×okt       xðõ|o²Î7:ñù#=#·åTo8ªwznQ¨û¨Ø7×íOKÝsÊÒÙ@ö¡Aê±s`T!o·©ë«º>7oô¶=9Öoá&hýg.¯lÜu¸îÛ       ½¨t¡+Ï8<ëKsë½fÅNpT®²6ûhwic¨»sSmYy¥IíbCht %õVsâê¨0×Ý×h}ñÞjñ/Ü,"Z¿%[ÞöÜ±øeÕÚÅÞ¼úÁ®°MóWç×ô¥óB½1ÕålNÍÈkmØÊq-{uQ3}]R½iý±Å1|:µò£_ï<aÑzF½²$vÊH½Ê¤oÚp°qlâÚÎ¬Úôâ;GßèÄNé¤XÍ56î(¢j      G]Ï+]XÎälÛ´yoYDDqréãîæqå×Hw""b)ß±a[^E§åÿgïî¢<óüßÜ÷º3Òmèn¨0Ñ «²c àâ!G×vøI
!5*5õ¦&dU>eHé2KÒåC*>· ìþD³ £À0¤Ò
¦c·ø»ïAÎHÔ6 £ïWQ¥}Ý×uÝ]Õ|ê[ß;891Òuº¬¾¹âdgXrbèNÙ¹wí¶r·VµqÕ*t%:ûÃhÇîìo¤¦o«2¤¬Ë}Õ:0Ñh8²&ýVl¼`[Ü]ôÛ¬73Û§-_ñ/]½fîõk3RR³ò¾Tr2RLú¹õõóÄ¦ÔôßÑýæç¬Ë´^Ø½jaÚ{ëÒ×g
«       <ÕF&¢×<ð~¼ñA ï¼3ßt¿ SR§¶¬h¹x¢ª%8!5Jæù¨Só]ÕÑ]JöÕj  ·NÔVöù§þ|»¦´T_ÔE\Íçb²HÇ¡Íé[´^×õsÇªÛÕÀéÖ»ÏkOª=¥gºèÝgÔ©1)±Ã½6       xZ¼ÓûRÙ¡Ã2/~a¬å³ìgË«NV´¸>ªD¥$XÛ¸$"r¹ª¢iùäõuÃi[l¶Ý]ß7kÖ;º<
kçÀ¸¦kâq»öÓ4MDUEDSRs'EXTÕ¨zZÔ»w·¦¸.]xÇXÉ_¤ûq~       ð¤y¬÷;öi»Çð 4ÙÓrbÏ'=÷9ê÷ZM5¥òÇôUUÝ) º5Z¾»âàÇÑþ)¹¹oÊóÖl8ãÐÅ´ø÷%¥uí_óI/ä      ÛF&¢»eÃ`MöÊ²/·û
».ËlåV§eëÖî:ãºwøÔXC]ñúÂ³á±:3óã)ü+¦¨%L{ûi¸;ºÜÆÀ£ì¬X-6é:ìÐÅêíÊ)³¦)-ûqè"¢DÛTiùÁG]L3HÓ@îg
R{      <ãFÞ7Ùu¡dãGù¥µnó+«×­ñý_ÂÊ5¯D<5¥[×m,­s
±uAb´Ô>Ú|±õÒ­¿¦òÃg=ÑÉ VéêpIHÔL«¦¼¹hú}é±&æi&^_Qå1?XÅ¹,Fê+ª\Ã¸r½Ûé[TUCÄ«ëjÁlRDtM£Éb3ù)Ú²èåA(þ³­/ÜdÆæ       ðTy,º«µ®bßî¢/ÛÜ¢­A!ÁwüYMªxZ¾Ü]´¯úLë%½©ÉáîSeU;¯×«u&¦Në9^\ÚQôÙÎß²ÊPYÕ¢*"úù²S]!Ë7|¬_(üÝ®º U.ÊvÌÛZ10Y¤ó@qY{Äê»KrÂÏo+9«Åånûíl©«¬qFeæ$®Wl.lÈÜ±»üðÎ¼dýøÆ²áí       O±q³~1o´kýæälËª]÷ÁM²;» 3íã¼¸úMuÑnY¿\u^qÒ/b2Ü;çÛ+v__Ã·  À¯·×3éÛ½ã=Î+ãÇqã¤¿ÿfÿMÓØäºçÚXß <J~ç9@ O¯?#ï|Þ~¶ê¸ã|»Óå>YU.ÍNgOõ
wGç(Þ¥       x=Lm2Ô&  <Ë¨M{Qàåõp}       ÏÒd       w¤É        ïH       Þ&       ¼#M       xG       ð4       ài2       À;Òd       wÏbb
hTEDsv4·\¾®ß}Ü452Ø_­§½©­Ã£â,       'ÇÈÓdSôZ?jm}÷úëß7DenI ùþsGÙµ»Î¹ë]LùMÑ¦È¹ïìë¼k8èÕþ9#ÁÔùÙGÑ·¬ÍÙÑD®
       £1â4Y1Xl¦;>«SVf;¾OicpLÈLª»c\Óâm%ËÝ[Wo¨¼C[_ßXeØÿwÿÐzk9¹;7O«HÏÞÓ1Ú{MNª¼ÌâIþñ-       <EFÓéâlQIK¢F¸ÆU{¦ceÚÜJe."â$ ­Ý""ÊÔùQ¦ö5£E£Ñ ÎK
ëºuô»        äQ¤ÉZÃÑ]{Ïz¾ÿl]½hªêeUgM}Wú¼H¥æ.¢Ì3ÍUuRiø¼Â#"Ö¸HSWÃ©6%xAÆH"ZWCeéöÕº2'wgáÈ^uqzÄüoo¬LY±%?ÍóÙ®îÿ+÷ÿ´¨±÷ÄýUÜ`±"7#-*Ð¨êîóvìm_[kþtõú×EüÓ¶ìÌ¶eÿúÓF]¨Õ%[JV8åd'Ï1«órÝâÍÖ=ÞÖ       ð?ÒºãBYeûö®5ÕVªø;~èàñÆïÃeOCeysnÅí§.8MásEDé1r©úX³{ZL´""b
Ñ«u¶</7N+ÍK[òikhssòVNMÓÕ¨ÄÐ³ÛÒ3wÖÜÞÞ~îújYþÆÿïÄÿ³îhÖX¼bIînW8û'æ¾nmÞ½jaÚ{Û,éësÕæ3M®2cVP]Â#Í""¶)æç/._³Ô¯jSVÊÂåéj²Ò£±þâ       àG5â4YôÎ²­¹K¾´ð¤´õEõ NY³:.x0_Õ/WïX³*i`ÂÂUïTwõê;½ñt;0:*@DBfÏ0¶ÖÖ4Ö6Høé_\ìT­þt.ÓãBEÇ.yD<­%=!óBEDDõ\8|ôÃu}p{eú²uë¦7oÿhÏ9Ï}.Þ«ÖìÛ]íÐEï®.>Rg«×m3OiQ¦ÏsTî°Ìðñ
²7Õ:£è.§GÝQ¿ç7³vÔó6?       Ï§Éwò4ïÿÝ5N±½µ&#qþÜ¸ùsãæD³Vo>Ó¤ÅÎ4H@t¥ýìy~þL«!zv (3çLSZÎ^ðb³ZÄÑÙ>¸¦½£KL""¢9;ÛïuÍ±yAuÅ;+÷?©5Ð&.»ãÖ«ÿDë²»Õâªon·N4mv¸´ÖVÕwÅNUðYÓ<
g;õ³Kê-¶}ÝÚ·gY)L      ðÌy¸4YD¿\±}W¹]ÑKsò?\ÿáúÍ;vm;|òõSÍm9'¸«®¾[äzÝÙË¶¨ÁÓc"mÕ_õÜ»æ®vÌºvçÛ4C{½'nåªY{µ!Gµ
)³"¢§û·Ô7Û.É´àajÛz]ôK>ÈYñÛ½õó¼ÍyiÓË       O¬MEtG}UÝÝåÀfkqõ»úÚuÊä0Ï3""úöàÙáæuÑí.±ÜZ¡ZÄÑe¢ÏÖ²oÛúßí,W×eEß7Ëvt:Åd³úÝúh1évGèÍg%,6aNP×¹&]¿x¾Ånk­­ÓE?«I\­5?ýýúßäíw§.òc|9       ðÄxø4ù!8j«;, fHcmÃ@@ÜQÛàh¯¯ènÑx¢¦ÝùÚ)"%}®KeÅÅ¡6ÓDÄSWø/=Ûoè3zN>©Å-[>Çª8?cq¤ûtÙY]D¯ûêm^J§¹Á!âint¦.Ú~öK$xi~Éi~"b1èvG       À³äÑ¤ÉÚ0FÒYWße¶Z¾:«ÚXo>sQµ=
gÛn´æo­Qç8þÇ½^Õ*·åïë|À¯vo>¡%½5ß4äñëÕÛ3×í.?°);èRáGÅÕOýùv«ÅxñBHOC«n³ºê;E¤ãPÁöúô-ÅåÇØ²ØX¹³ði2      gË¸Y¿÷ÐøÏZ³.#Æ6ðÉy~AAÑ©nýá6Å£¿¿_D®:¯È8é1îóí»¯ï°Þ­  Þ^Ï¤l÷÷8¯?^Æþþý7ýM/<`ëkc} ð(ùæL~ <e¼þ >÷(ÎÒsn_þ[ûÆú^       ÍöM       üD&       ¼#M       xG       ð4       ài2       À;Òd       w¤É        ïH       Þ&       ¼{è4Yñ5)c}#       Çè¹Q®Sæ,]µ"yFd°IÍy¹¥¾fïÒêËúXß       àUm²¿9#!z0JÕùÊùÿü^Ê4¿ùä¼ãûßOy4       <6£Hý¦/]½æËÐ­ñkrßeé+¶ÿ±üø¿üzÚhîA?»;oãÁûD/X8ªÅ0#õõhÓ¨      ÀÓdäi²ajbòLõþÇÕÐÄÿí9-1%¸­¦Þ´hÆh*]Î|uÉußÃ ËÞHÍÆJTJzòLó(V      ÀÓeÄ}%ÄK±®HpxJlÂ,i®>QUÓÚã­²2kQ¹é`^eLáÛÑ;/X`OË]½"6Ð¬»£¹¼¸`Ç©î!ä¼Ã«=ù+¶UëþsÞÎÉNbV5çåºÅ?í^¸}kf¨*ïïþbÁ®´N½µfiLÕ îËuG7ZçeVnA¾áH¡+.-6Ðfû©=ù[+ìsßÛûaY¤ð¸/Ö¾ûIÓXW       0vF\¬ë[ó2EÿYó.ÍÈÿdgaî«ÓÜøBIkh¨¬ê8YU§Æ§Î»Õv9xÙêÌàæÍ«R³ÖÕr2
CÞÞ)jù¥~U²R.OßTc\Õµwí¶r·VµqÕ*$bùºðö=ëÓR§o¼`^9[ÑÄûêúìôJû B¬\¥è§¶­)nÓ:f/!J      ð¬y§gó&×'¯vY>¨aÉYù¹ê3ax%1N=_vòºxjÊÎjÑÉ &Åh4¦¹Ýºè=ç¿ùÖæ
Ïwîe0îrztÑõ{Þy3kGý]ÑzSéÌõOtztÝñUEÃ:Ø ÚQ³·²[Ñ/oqlA¼Ô       ny¬wWí;ÒrßòdWÍçUê°;Ìó¯½_'å¤äílEGDôµî¨Ä$«èJ«ÔÂÿúñ;¿~-:X¹ßàvö`I½%óâÏ¶¯[ûvâ,ë=°b~=§°äßööoû?Ë[|»ÿ³æêrn£é"òÖÐ       ðÌqßdQ^O SEDÓD½3su6|Z¡%¿³fÞ:+["£
§z<÷î¡Õ÷Ïø¬ªª¤¼6åÀ§ärÅÇ§KfÇ'ÌK\¹þÍEeë~ûé¹¡¾ßM¿tàòi1 âæÏËØ¼(±hí·Ï¼ôuÉzÉ¹{zD¦üºhSÜX       ð0ò4YUÄqzé¥êcU
Z`tÔÌ°iþr¹¹ábfI[:Ddí>µÌÓ%¸Êów¤}pÄ¶è½¼WR¦ïÙÕ¨ú¤§ã«½_UìÝ·ø÷EKS¢ök2Ü;x;MVü¬FÝÑZs¸µæð#¿þdSê)öÜ>1Uêö7õ¦Y)@      ayì¹Töé§.©¼t¦ÒoÖÛys_º4ÛÕÒÔ9Da²:ÏÒþå¶ÖKß]<TÑ¼85ê@ØòíéZiÞÖ²F1Å,=ÕCê÷êb¾µ6xi~Ñ¢Îí¿ÛYÖzÝbÐíhbh:ërºzÔØhSuÌXhsjõW¤ë~×­&KÕßîìñè       Ï¬÷MÂõÊê÷}»ë¨ï¹wÜgj+;vé®ÑËUeME/oÝY¥¾º¹¤´üxqaF`]AÁþË=¼½´ãPÁöúô-ÅåÇØ²ØX¹³ðDèçËNu,ßTòáß;÷í>îÉ/ùã++wå:oL^_øöÏïwå³Õu·®hSf/å      ðL7ëóÉF¦¨ÅkrW&Ù;ÂQ·vWµâÞ'Q¿\u^qÒ/b2Ü;çÛ+v__Ã·  À¯·×3éÛ½ã=Î+ãÇqã¤¿ÿfÿMÓØäºçÚXß <J~ç9@ O¯?>¶ÉÁäL7ÍGÿ£æëïúúnööÞÐnxº¿®/?z¶åê>ßI]jZ¯ÝëÇûùß½×eÈ©qïu·¢Ðc  à)ô·¿é~~Æ{Çoô^7n'"ýÒ?Á×ïèº& ðQÔÿc3ùðñú8ò¾É ÷4Vj¬<4Öw
       xÄIßd       ÀS4       ài2       À;Òd       w¤É        ïH       Þ&       ¼#M       xG       ðî¥ÉJÀôÙqs"
c}?       Çá¹[®"âÒ^_4ï%*""Î¶ªÊ²Wsèc}k       Gæ¡j
Ë7oÉ}ë©ZýáÍks²·»ÜeIXµ}Ëê9¦éä¼ãûß¯üH§      gÓÃÔ&+Æà@*"ªÑ4="Æl
·S`I9ãz`yrÐÒýÃª°v}±6gGýêõ³»óÒòVBf¤&+U×¹ÆúB       àá=d§[Ì¡1KBcD\
_Ùþexæ"EÎ2ÍU^¿÷âCº³cÁ°ëÒ¯~¤5"JTJzrWi2      §Â£IØn[WÐlL~/]ü·Bw;:/¶Þ^ÝVÒRPe{=1Ìd2êÍ{·nÝÛ°­dscÆÇ§æ®(ÜÚÿë¦7®öä¯ØVm\üûÄâ¶È ²/÷ìë
^±&#!Ò¤ÖÕPYº}gu®ÌÊ-È7)tÅ¥ÅÚb?µ'kELùuá¦È³»Ú§/f1z.l,Õ^;mzYéªÚµiKe·(Aó³ß]á¯Ç^_Q¸uÏ(ÖÈðª)KÃm&ÖQ^øÑ§5ïíý0Á,RøEÜkßý¤i¬¿g       x8£îì:wªñ®AÅ4#av Ñ4gQâiþ£ìf¬H`R²áÀÚwßz+§ðâôIVWME=/æÖAqÁ=5ÍwDÑ&¸yúÞµ9ëvÊ´åy¹qZi^ÚH[{D·rÊÀæÆØWçÔd§ÿSÚ²`å(EDQ#_iÜúî[+r÷:gd~¼:ôÄæLÏXW©$­\<]Qfd~ÝQö©éËÔÄ¼ÜW­g6Å§çef½¾µÎùúýÔ¶5ÅmZÇÁì%DÉ       £¨Möµlõñ!ªhó5õZtTÐ@_Û¢
{h®³ÍÆ¹Ye»­|Ï®í7{ÜIµ,ùx÷Â;G:dgïh}Ñpôà9ôÔÔwÊÒ@ÒSõesöÊ¸h¥æ.Öyq!®ÚíºX×j"ªbÿ²´¢µGD¦'Ç8*6»äÖÊ7¶ÏKý´TDÄQ³·²[ç[ÜmAÔæ<[Vî®ÖÕX{ø«i©¿¤-²ØDZ¢LÍEÅ5º«yÿÔâL:."r¹l_KD<Î\`"Æú      GiÄi²böz|ªµY_ð§ßôä¬¼wlµEvî¯ïktzNÎ[±S-®>µ­Â1Ô^÷öMÖzÚoý¯Ç9ø?MED\§ª²Þ?]9Sï0wªýä§ºÜUþ¬yìàZ±Y-âèÜMoïèdM·æêrkºÜjòìv÷è·Î¨iîçàé51¨"Æ`Ù8sÝënïr°õÖe;wÔDeM6       <±F^¬FQC^É*z%Ã­©FUÜ.·ÕbsLæ]énj4¸ìÍ`Pe Ä½îÓ7ù~\5M++©óC»j
ï~'Å    IDATÝP»ÏfÃz+ çG5ÑÜUù+¶Uß}
Å*       ðÔußäªÑ][´võÿy°E»sTi9º53-'ïP[ýî÷è©ú²Ù=7.ÒQSÖúºÝÑ%ÖÀ[P8ºìÃ®ïåvt¹ÕÀï³cC@°d       ÏLE\mu»ïI=-g/\ôxÍn£)08è®?«áA­ëTU)&3yjûÉªÜºñDM»51óµ)SDJú\ÿÊ/y0½¾¢Êõj¨AÄ_´aqðýçk¢Ábõ79      øéq§ÝÓcwÜÑÞA
{óõ°ôP-³ç¯X®ºØÝ÷k?aJz[ÒÝcíÖÿãûÞUSÑ±&ªó³¼\hkiþVÃüï*âìª«Ü¶y_çCu4Ö/þn¼»|ûÞ,£xÚª6o=Òqÿg«ë^_¹®(üøïrv|õEÑ       ð7ëóF¸D±Î^±8)ÔôýæøKÕ5vãÌ1!ÆÛÃÎÆª]Å®õmâ¾úûûEäªó~9àÞ9ß^±ûúÆúJ  ðèõöz&½`»w¼Çyeüøñ2nô÷ßì¿éozá\÷\ëû GÉÏðü0gòà)ãõpiò- è¤E)ó­=ÕGÕyë
vÿôy©fªUUsPû¤#M  x&À½H<³c§i2  À³4 îEàåõð¡ßÂ       x&       ¼#M       xG       ð4       ài2       À;Òd       w¤É        ïH       Þ&       ¼#M       xG       ðîII}BÒÇÛÆú2        CAì3uAú[sÏuôÙÏ78Çúq        ôÜX_À í½{¬¯       p"MöñH
4ùúôiÎojOnrÞßÀÄ¹S|Åmoù_í¦_½üÝ±ýµÝ¢¼<ï/[>79×¤ÆÄûÞSi÷ IX9W/+=Ý2wE~ºÎççF¥ÏÙòåõvmà,ñ1!&Usµ~Õ¨½ïÿçÏËZô±~       ðLxø4Y IX?±½ìP¹½WµÅ-HI¿¶ÿT§O`ü0õ/ûê®øØ~ñËIÏißõøØf%F¾©<öyg_@tü/CTi¿k»¾>ßsUÙ§5Ë¼¥þî¥¶Ïÿ|mbd|¼ÍsòíýYDÂ¼X£t÷õõÓ      gÅC¿ÏgrxÏ×uçì½7EnØ¿jìT'ÿ<p¼ùtÕ×uõöÝtwþ÷9û­éC&û:[jÛ=}}7ì_ÿZójÓ¿þ¹K¾+»Åh6B~æn;ÿ×«7Eëiªisûøÿ       é¡Ód£Á(7ÜWoÞúØç¹Öëó¼ÑWõ5øôz®Ýª¾é´÷7ñFß âöôÞíêvU_Ü×{íÖ}Ò'âã#&úJ¯ÓskûÛo{)L      ÏC§ÉCëûûÈ¨b`¡       ÆÎC§ÉîïÜ}÷Q
þ¾}×®j}½½}¾¿7ÛÏÜìí½ác Þý³ ó0Câ^w¯øN4Üúdô÷÷%]      ÏÓdÕo¢ÁhüóU¤ïÆö¾£gÚ|E|³§Ûz;ì7ûºíÝbé¯ÊxßÀY³n¿Îö+9,Ê6AD xyV:ÌWé]ûÆ~ÃêK!Æñ¢úGÄy       üÙlÉ¿\zûóÕCê;OUNM|óÿö¾kÎÎågì}"½mÕU_Å%¯Öz:ÿWCOÀK}"Ò×YûIøerjDÇþÿ®·OÞ©»ëNÿË¥iÒëjýêü×æøçÇúÙ      À³cÜ¬_Ì{l÷%Ä_Ny=¤íÀÑf·ø¾·ö)?_øzóÄálçã#·*}_YßWyð¿:Çøñ=úûûEäªó~9àÞ9ß^±ûúF¼5   x½½I/Øîïq^?~¼'ýý7ûoú^xÀ&×=×Æú> àQò3·@ O¯?é-|">¶¿_gñõ!1/ýìª½Ë-"æ´·ý}ÁGÆgÍ¸ñMûwÃÙÏù«o&D ¶èéAÒõu÷ú(      àY6²N#Ðg?]y>qîÜe¾Ïi®¶Óu=""Îs5~9÷µLòù[¯ëëÿ:m¿9ýÜ9}Ò³0m¾ÚwÝùM}ùévm¬       <3k§üÐé  àYF§ ¸. <³Æ®Ó       à)B       ð4       ài2       À;Òd       w¤É        ïH       Þ&       ¼#M       xG       ðî¡ÓdÅ?4"<Ø¤õ        £çF»P »<seb\¨IÍùª}¥EGëúXß       àQ]m²ßô××oÿðPæh«9yºîb_JÊÚ°=71Ô0Ö÷teVÎÎã[^5õu       ÀOÚhjM³W­Ë1;k7|Qß3P¬X£Óssßzeõ:G×O/x¼!<5keÚìpYU5½£¹j_qQe'eÍ       ðdym²°4!D<5{¿EDwÔì,­ÓÔ°ähë·ðOÌÍËè9°u}úi¿ÙTÒä¿0w]zÍ      à 5òÚdsà¬iqV}ÕõRb½£¶¢Þ>'È¿ÚÑsß)s"}»Õ-"âºPV°ÍÝ1CÜ""bOÍy{EìT³ª»;j÷îÚy þºf¯\lR5WËÙC[óÿ¾$±¥¸-reìËýû<sÞÎÉ^4#Ä(ÎÆª¢]e­§4D¯þ(39Ü¦zZ*ó¶V;Æú¹      ÀOËkÅ`TE<.»û¾ºËîòÌÆn¡w^¼,aÉoÌòê¬þüOÕu¿ù9ë2­¶g¯ZöÞæúôõYó
"J\vîb[ý®ôÔå©¿)n]¹fe¸hXâæé{×æ¬;Úi}í½¼d9üAVê
%®5ï¯.""ê´íàôkÉ«Ò£(      qm²®{ÜÁd3*»eÅd3D<N÷÷èþâ_
s3òþ¨u´5\l>wªºüd³C1Ä§ÆJÕÆÒ3]¤ûLñºä¬X¥º²v{vêîvé"kÊê= Áiöh"ªbÿ²´¢µG$ -9Ü}*ÿ¦]zïÚ¦ÍVÜEÄuºäÓ:­ªs&Ø©§E3       ÀÈ;]8;Ï´zbcRfV»tg(kK2ãôÖï¡_®Þ±¦º(hF\TÌ¬ØðÔôÓÿsóa5Ðl4ÅýséÂ;&7üEzl±Ë³Í1("¢MjÓ`}±æ±;<""%Ô*ÎÊÁþeÇDD1h®Nûà5]DTëcýä      à§däi²ÞYs´Êµ>O-(<zÁ¡<wyvÎªÖpôHkX;y._¨¸|¡âaÆowäg®;¾ODëÚ¿6ç¦»j·órbÚwæ§»äeNîÎüÛ/ú       Ñû&ëÔîüµNÕ¿·dë¦
ë¶|øFYDÔÈEo$M{`câi¯®Ýðv¢éO[£CSÕÑfÿiÁ~Ö EÄns×>qÉ#"b 2¨÷n«w]t-4ðÖ¹­Ñio¿:Ë        74YäzãçÖüî`ÕE§ÆÍVìåE?ÚþeXÖ}tÿ@ÙÑ£F¤®Ù°:uvx°5À4#qYNz^wò¼ÇS[vÒ½<#1HÅÖ²õ;rLâvôhÆ©³BýD ÿvÆ|£GÛ÷í®:Ñ¬Î]>;Ðd
O]9/PÓÆú      ÀSaä.nÑ;NíÙpjBMZG[ÇÀùNæk·îuÿ,ò?Ê.ÕÂS³yí¦ô¥+ÞÿhQÍcïh®Ù_t¬[Dª6æ¼¹cwQo,(s--:û^æâ7µ®º£Åù1ùoÿ¸+{ã];lÎÊ|ë[Fq6Vmß¸§QYcý      à)0nÖ/æ=â-ÀÜ¼u¯X´×¬ÝÓèë[Äõ÷÷ÈUç'ý"&sÀ½s¾½b÷õ¥i  ÀS¨·×3éÛ½ã=Î+ãÇqã¤¿ÿfÿMÓØäºçÚXß <J~ç9@ O¯?£®M¾?½³¬`x2¥ÍM£        x*<4YD<Ê
6õ½       Ñ½       ðl!M       xG       ð4       ài2       À;Òd       w¤É        ïH       Þ&       ¼#M       x÷ÜÃn ÎÏÈÈN±IWÍâÂâ}¬ï        ð¨=dm²ºhuÞÒQÄh[úÞESØmNî¿ÿ8q¸;(Ñk?ûã¦d?)¿)úãïþhO
       5£ªMVæ¼cì¨©º¨Dª·¨!Qæ£Zh\B°§æË:ÇuÊJøoÿ°iõîA­vsZ~Õ¡myjçÈ»lªptás      §ÛhÒdChBzÎªHIÙÿ»M>/Ýï:(k+ÕØùï§É_:÷6]¿ÏZûÑmùGïÈ5]Oë3£¹ëõucú      à)74ÙÓTV´'&?cææÕwª¦ ã@¬yB¬9+¢fÚTO]ñã÷ED4w×ÅÖKw)srwæö¤~P!ÖÈðª)KÃm&ÖQ^øÑ§Õ.%<íýwÒc-ª»«æó
íÖÂ)¿)Úy"÷}Ê¯7E-h }#.Øb6¸ê·å»¤(AkÞ_lÐöîiS÷Ü?\öóvNvò³ª9/×(Þüik¬¿       x®oòõsû6åþES-Ñ±1¡A!ÁA!ÁA!¡/EÇÎ´©ÒMùû.<l,kO
-ÏËÌz3}k9%óõ)"ºòÌÎ¢ß¬Z¾¹"8!Îø5ºùJ£xý?¦¯ÊÞÓ±<Á "KrW'x¬K_µbãééËRÂTñ(QË×,õ«Ú²pyú¦ã¢¬ô¨hû       O¯Q¿Ow^¾>X,îúÃûë=4gkû\Ûå²}u.ñ\8sQÌÁEãb-ÎSG_ÖEï¬(®hõÞeîú²/Zué¨o¶«P!f~¨^sèÈ9îiýÓö£m·¦FÑ]N.º£~Ï;ofí¨yÓf       x¼Ó)ú·[Ö/ ¾+ÆÕ¢f$¼¿«ì}Ñ:ÊòÖî:3t²¶|[ùò;:ggî¹kÖãtþWtE`8;_ÓçîrºµV'ætöèË4QE¬³¸ß èjm³k3ED?{°¤~}æ'ÅiÏ×Õ×«:ç M      !<MÖz.^lkj
²ï3ÇÝÕîÒÜÛÚ}·i?±uóÑî;¶íjÖÜÑBÖ*&Ö/ø §|ZLÂ¸ùó26/J,Z»á@ëC<N       xJ<Mö\:¼éýÃ¢'¯/Ì*OöÔìÊÏ;ÑùÀ*_Msv66]º{Ð[Ïb½Ûéè`"ÝºmFuX-5\]Nñ7LÙ4mªm Vü¬FÝÑZs¸µæð#¿þdSê)~øn@       ÀÃôMv´Ù>ÔÕâp=Õõ]¶¹NóSSRÞNÑ´aU'»: KSB
b½(p f:xi~Éi~"b1èvGÏc¹p       øe¬ÍÏÎy#lèSßÊÉHòVh<*{vµfîØs¸ä½ù­GÊÞEDäÒÞ=
Öå{ÿXÓ¸¯j GÇ¡íõé[Ë<°e±±rgá Òd       Â¸Y¿7Ò55.ûãõKÅyrwáYKêÒ8óÅÒúâôªCeØÌy&é(Ëû ¸ú z©¢(º®(Qï|lÙ»bÃaÏX_Ô ¿¿_D®:¯È8é1îóí»¯¯a¬¯   ^o¯gÒ¶{Ç{WÆ/ãÆIÿÍþþ¦°ÉuÏµ±¾ xüÏs&? 2^ GÞ7YDÙ ÙOçmýÓETÛ%"":<p´²Ó-ë³#ü¥:ytüS·d*eyJ´©o®1_<TG       Ã6Úä"%h~ö»«",FñØªþ¥¸âòS7=¨M  xQ ÷¢6À3ëñÔ&ÿé«w¬­Þ1Ö       ?Q£|       àB       ð4       ài2       À;Òd       w¤É        ïH       Þ=7ªUiZx¤Õpëæiom¶»u]ë»       <#OÀÔ÷óÖÌ³Ü1tù­Rg+e»s(      ÀShÄ.køü(Ë½Ã¶y«ò7,eRÆú        Þ(:](ª:ôãô7ò7HÞG¥ÃªPZú¯XöÃÑ®/Öæì¨ôÎÊ´Ä%Öæ§:ùÎ       ð,]ßä0æßm: ¦©Ã^§¹Êò÷^¼sHwv<^Jä¢åiêÎ/NuÒ       Fá¤É¦wó?Ø~YPçÖBÝíè¼ØúÃ7øõËº7gn«ö?*Ê0¯ï«¸ß%¶×,1Äu~ïÖmt%xAÆH"ZWCeéöÕº(ÖÎðL[djüJ3×¢ÊúÃQUy¿þ}û¼Õë2"­Ñ\í'm/8Ò8¼Ë      gÖû&â?kÙ;¿}-Ü0ªÕïÚëÉÎ¡ßåÑ­¥Ûuè¢ZHÉo³Þ|ó½ÂðÌå¡"2my^nV¶äÒÖÑææä­2°fI4þ)/sý¦ÿg]a½æ<±)5ý÷gd~vNv(/mái¿ÙÕ¼|Í²)còè      à'äÔ&Aµ/Ì·óó÷5ß·ðWµ,ùx÷Â;G:dgï¹(ö%nÉÈ¼Ø7×µwíÁã
ÇJÏyD¤»êhmö3â¬¢&Ç8*6»äÖÊ7¶ÏKýôR»¨=¥ñ»ã¤ªªjÇãË5;²WÝÃ      G&kµUM]níûøÌ¬xQ;ÛÝAqëòÜùùQï+ïé¬õ´ÞZºýhÌöwÛK×ïo½}Ôî¸ÕCwô8e¦Õêg³ZÄÑÙ~kÞÞÑ%É"í"¢uÙ÷Ôszï¡Wór
ö/kn¨¯­8QQÑÔ3¦_       ü<|¬µ,Ýþé÷È~sr¶m^d<jj<qÉ3ôËïî,""³Õ_41Z-ª\bÆÀ»þ´¡/mÈ^?÷éû+'Ì?^Ê-Öo8ÑýX.       <->MV#o:¼üögûÑRÖ©QKóÖ¯tmÞUåÐG¼©aîÊìØKÔ&nÈÈ}~ËW×EDTUÑED1ùÅÕáºnwtIl`ÈE%$Ô"fûÎ¨L·£¹âóæÏ÷ÌÉ-ÈO78âúq;       ü´<¦·ð&¬|#ÒS¾ycqõ²dÅh
ºëÏjPÄïÜS|¸¾¬ð¨'éÝ9¯ó|mÕ|«")KÆ;jjÒx¢¦ÝùÚ)"%}®KeÅÅH×41,6_TFaI^öÜ@bf5¸]î±þ       à ÷xÞÂ§woÍ«Ó:;\,KVMIïoKº{¬ýÐÛÕ$wÙ£"rqOñóò²3*2÷h=UÔó¬æ¨-Üx¤CDZKó·ÖdäxWgW]å¶Íû:ï½ ºÊgNVQaÌæÌüâ¬5Y|hP5WK}Ùæ]5#/      gË¸Y¿7²Ö¸¶¯O2ßï°ÖP¼~Í¾K>µ.þ}Ñâµ9;È~¥þþ~¹ê¼"ã¤_Äd¸wÎ·Wì¾¾o
  '^o¯gÒ¶{Ç{WÆ/ãÆIÿÍþþ¦°ÉuÏµ±¾ xüÏs&? 2^ G^ì¨-ÚT¬-i½'^Ô<íg}Q2       `L¢Óî¨?²¥þÈX_9       àÇóxú&?#ï,!Â      ±1~¬/        ð@       ð4       ài2       À;Òd       w¤É        ïH       Þ&       ¼#M       xG       ð4       ài2       À»1J}C_[õZ¬y¬ï       0<ÃM}Bæ®\á{{aHÒÿôflÀí)þ±KÿaYÜ¤±¾#       À£7Ü4¹ÏÞÙ-lßÏáÅ ¿ùZ^88`´L6ö~ÓþíXß       àÑ{n¸µ®¯»%6ÐâÓfïs E¾iµ[&N«7DDµM6÷uë ¶cÿ.ròDUúz¿m­;sºåZ<µdáä¶³ÿ;,öE÷Ù=UwìlùÕ¢XõÏ'Ên¼ÿw'ùúü­×ÕÙPûîÒ|CSßë:õÿË/}qs¶òô_¯Þo~)~þËÍFUz¿³7­øs&"¢Ø^9ÙßW®u·­üïV÷M% 2vþË'ª>}½ß¶~uætÛµ¾±~ô       ð2ü¾É7.·çcèul´ø:;/t~71p²*"2Þ8Iº;í}âÿ«Õ¿^²ûÀç5Ésÿ>6@Dnø:OÛWùõí$×gRlRìÄöªÿh¸Ö0óÑZO|þoÿ¾o_y» "Òçó³¿$g¾8¼÷³cÕW_·à¥"b÷Âµ²=ÿ¾o_å7¾ÑscmãEÄ7lÞ¯"}.øüß?;^ëü÷I3Í"¾SãS^VN.Ù}àóSßMNøûZ6      ÀHà-|nû7î[­-&þìjç7N{W¯Ùà#"/Ù|ºÛ»4ðâK­íÜn]ä¦»ý\ÓðbØ`3åîvO¯vspKÃ´ ?w×êÒDÄGõé»©iºÈÍÞîÆc¥ÇNw®k8ïìí
ßôNì+â<xÿñÿj÷ôÉÍ^{Ëe·:É¬Lx1Ì¢µkrê}Úµ¿Öü¯?Û5ðâK{[þ»É©Ütw«·¦Ñß       F`Ø.DÄÙùMïK'Ûdö|sê\µwIüÒ©Ù&«ß5uÞdö·Ó3¸æF»Ï×hð"}î«;úK(ÙfØ®Þßæ°7ÔÚ__úÆî®oÚÛÚÚ½""Òw£Ç=@÷~§e¢¯H¯o@dÌ/¦N2ú¨¾>Nñ`6»íÆàäo[ÛDdÙèão[ôO/ß>÷ßú&øÐì       i$i²¸¾¶k?´ø:'h]ç®È¯»_ú{-F÷7ß¸½îpóö}|ßÚÝ£fÛZ«ìÈµ¦òÃ­m/½vúhyö|þ1FÎýU~öÄ±N]äù¨%_|Ðyûºjn¸!       QA§ööoûÌ§LîËNÝ=ÆÉ/z;;""§[fÃà¿Ñ§÷®äA}¦Êª²ÊóÚÔøy!(lç>    IDAT¾êxíªý¯>û_¨uOy^DÄgÂóÆÁë4þÌWn\ío¶¤»¥É©¨&Ë@²xnhþÙ­É¾§}.ÉßgðÌªï       ÀÒdé³wv«¶!ßÄ½öoÜæ°Ú7í.¹ñuK:uÖ³"2~âÔ¨fOkË·CnÖ'"ÎÆ:ÏsãC|Å¹`Ù¢9Ó&/X|ûzÝ·ª^eóñy>âeê¼|¹÷f¯ûÆs'¨"ê¤¹Sø'øÈ¯[º|¦Î²MPÕç§ÅÅÇ=/}7¾þKÏÔY±¶ "ã}mQ)KSæÙþöî=¾ªò@ô÷ÀÞ\²m+AîE¤\AJÕR<m­lG-SF*Òñ2G©t¦Òþ¼t¼,=´cõÔKU8"U©H@.I½öòûQÈK¸Eñy>üAÖ~×Zï^òìoïªß    ø«×J!d×¿µ±ÏÖ5KÖåÞÛ²eÃúlÏîÉµ/m|om+æý©Y¿³³O2ìJo~cÎÕ:ä¿Î_Ðög·}lÎü¿|þÌ>C/97Ùhç¶w*WÌ{~U.4aWæ­UÛ»_ð!©dvËÚysV¤CHÿõåe-û
Ñ~×¶Ío¼8ÿ¹Ê~õtá¶gøëü?5ë7`ÐEg6[7®úË³¯UVÍÕ¬ÏAlÂ¶·^3¯rw     à åõ<½CÏáu¼ðÒ/n1óÀICVWWBØR½)äº[~tÌæMÍÔûÐ  |âmÛ9±Eën¯­ÞòòB]ÝîºÝE-pw3[ú} IÍN8È¾Çè7@>     §&    WÏu½moÎüÝ
=     Ï:÷&  '/¯¡g pÄäåÕ'øGæ   Æ
=#¦Q£zü3nß ãÉÁ|üÄ¯t  |²%ÉPvíÚYW·»¡çpèòòò5jH&~ß ãÃÁT ÃlÒ$&
=cÍ7@à³ÆJ     Ä©É     Ä©É     Ä©É     Ä©É     Ä©É     Ä5>¤½Eºt+)xï«lfÍÊUéws¹~7     õ¯É/ºaâøþ­>´iíã·><ûä¹÷M[¥(    ê½ÒE¢¤Ë­>²9YÜã¢7P¨÷JÝõø½?é¡ÝUS~×ðú     °¯CXé"LîÿdÇ!o
nºß;O|bBï}6®yôúïM÷OW¥+ÜÔ    ðÉuhë&ï£ 8±êßòD2M'!ì?
g³§üäw>¼¥f]Èå½²±¡¯     rDjrÑÀM¸÷ê?ß:öÖY?9­®Xýæ>/»kÊ°×»ãõm,èrÑ¸ï§Oûâd.]±ðûî}¸üÝ
Ïüþ¸±Ok[ÌV¯]4{êäß,ªiè+    ðYPïuæÆ]7ºdÉíc¯¸àk&·yý!ÑcÄø¿pË!yKYjè=ê¿L3  À§\^^^COáÓÁ#ëpîMÎVWmHgßû"YÐ¦uñTA¿ú~þàËU¹6¾<õÉEÇé(Ë¤B®¦:¹ªòéW_:½/  °W£ºpA:¿tW~]uÞÁÊº¼¼PØ=³ù®ºXúÌÏÏÿú°!íÛµ­««K¥
zî[Óü¼¼U«×üñ§êêêz: ð©w5¹âiÓËªß¯É¥çÕ¯õ÷H¦úM|âlÈÝzÅõåWrrqª¨ï¿=xÁ¶--*ÌÍxdZùõ£ïzÉ¯-*/5óÅUÝ  
¯Ùî0fKã¼ºB^Pë£ äÝá;ò»ìhtoQvÛÇåfÍÿÑ¼¼<÷Û¼R!Óº}ñ´n_¼õÿÜ¾}GCÏ >Ý£&9ªËîMnÕ:¶G6ûÚ´§/Ê~°%]©ýÝðkÇÝóú>±xãÃ7{¶Cïúè?jòÐs§\{ÓÃ+ú Àg[£ºpåÆy:ò!Ë!äå0¦&qGñÎýÞ@?þGcòó?k~Òíéï~òÃ»å |ºFMN¯[Z¾üý{S%ÉââVÉïÍT.[¾lDüÑ\µª2kÛ¡ ¼^B¡yIdõÚÚ\¢yI*Wµ²ìeOLò÷ÜrÑ v¯\ÝÐ×  >ÓÎ7¿Q8|ùyy_ÍäÏ.ØýÑþÛó¤äÃwá_ùÔz" ð)vÉlX¶`áËïÿªØ=ôcísä³æezunDHö~ýÝw;¯(^<iÚãthB((íÒ¶ WYUÛÐ  >ëÚçòë,|$ÔÕö¹ýFëÜ©CCÏîxÐ¥³Ë å0îM.é7ú~GgVïÎ½sòÝã¾?úßMLê%OýüÎY5!<zçí¥WüÅÔëRÉlzíÒÙ÷Þ>[M ·;XãâÈÈyu!¯®nÇñY+ùÉËËËËó8> 8dõ®É¹\mu:â®©MïïÙxÙ.½¿ª¼úëOBX}ÏèËö^þÄ-7<±ï¹WÏºõY
}É  k.t9!¯î#×³®®®  yCOíx*h.%Àá¨ÿ½ÉU§Ü25;|@·}_ÊfÖ?÷ÀCË3
ý®     8²a¥\Uù¿(²¡g    À±së&  ¤dóîS©ÄßnÍí|ë·ÞÝÝÐ³;îì¬YúÌï_Þ÷Æ-¾xþ7jjè~4íü?/>õ§ÿeMCÏ 5  8ºòOêÿ¥;~XÚ.¹ßWß}úç¼®çA9móÞOJ!ìÜô_Ï<ÿÅmz%ê}ÔÃ·æ¿º?}þÄ¿ë¾~ïobâËgÜñ½?À;²Û*kª^Z¶ø×k÷mÛ:wÉ¼ñ§wúíÀAS £+Ñ¹OËvÉ°cÝ9olûÐ3»óS-õJ}íª>ÙÜüÉó2Ù£8fç\zÚèþ'Ò*Ñ$ìÚ¼îWf¿>ùÿm>nöÎí;?þµmxñ#¶.2yæª=¿oÜ(j]zêÎéÕöÃ_Ës.ùÁÎõNÉ¹ÊÅÝÙåô6ÍÎU;°U/_ýÕ[5jÒìó§µézÅµüÑ¯TÆ¢szÞ}ÉzÇÝù |j¨É  ÀQÖ$Ù(wgO{uÒâ¿íÍ[NÜoX«æÃ~xz:Sv÷âG)(vi
Þùèýóo\ÞlÞ½×ñßísÓ?_;oGC_OÆïûÝçÔxçÎí[×¯~õùY÷ßý_ß¸rÄE~ÈfEmÚÂnkçÏ(+iÛ@59ìÊ®ß¾½:É¼±éíç7}yÚWúýð­Ç¹)üÏ}³_ÿ+JíJWWü®ì¥jþ6ïg@³Ë|ãªÂW.U1÷¢9oô¾¶oÇÞ©dÈ¦¼¹àÞ^Ó o HM  ì6&??ôÂ¿_ºv}®>G<XMºwN¥_^p÷¼Úl!¼óü_M×TB¡yá|é²^©/­ë6?2mñ=w
þÇó'&}óçkªC!õìÇ¾tõÙÿûènõL¥ÂîÍoUÞ?å¯3ÞúÄÜVºýíò¹Ï¿¼zc.Õã¼GöÐO(<áBª¨¨EÛníZÞ{ß¯uù»î'l]0åÖWº½rPËBØZ6íeÇ]=°péf¦³½ìùµ[·ïlÚ~À¥ÃÏjû¡[×|h¥­ËùÃÌ«6ílÜ¢]ß¿qAT;ß~uÆ}}}í*é|ÎÐKû·i¶jÆ¿O[Þnÿ×Åç½rPËíoÍøãó+Ö§w6.lwúyCô(<ëfT¯}íO[sJQrÓ~ýÎÿajùM?5{Ó~½¾róyg­tÞ_>ÿåý
>ëÏ¹É¼ÿ{ýÚÝ¡ ëÍJ×Ïú¢·Þ ;åÆó¾rãö?þÃëcø à ä7ô  ÏÄ)_h¾ÏÊÉÉ©S
öþ>¬÷1Rî­;NìÕþâNMöbç«sVÍXº#üÓ¾Ýklçôý7Îþòå¾qiË®êzVbçó6g;·>»ùÁMÎ>³0½¨bÎ»Í^Õç²ÄÚºzÖ9£^¸g]Ñu?>íôOÊÂ¿Û*æ>üÐÜòUëÖ¯]»>]¥,ê¯Eßsº7¬Üö±#¡q¨]T¶ñüãÿyÂ.5ÏüáéÊýÝøÒô^?á¼¿¿á_~üþáÕþøÊÖ6Îùýã«[^xåÄýó?ý]§ôÓÏª¡ýÐ~íäÆ­¿6þ_¯Ô2l-ÿãÿz~gß¿ûñÍÿzÝø[¬zü?³þ_ò-o¼³«8õ¹òÅ¥/_2{aûüòòJ|è³vt@;wé\³ì?ßz'Bú·~ýÆÎJåöm 8ÊÜ  3¾wÎ_¾× §ÞýÒ´Åw|iô¿
»aËkoÕ¾¶¨rÆ¼o½BØ½äÿ¾8â±Üú-»CØùÒ7¯tbá¥Eo¿¾4¨Wãóvæ-wÎ½rÏÆlËS¾ÕmÇì®Z²%ýV^|W§Áó_]ú¸=y[zk-Î5nhÄ¶Õ={OhYRÔ¦ChzQmúÓ®Y¡Y§·({uÅÆÐú£6.[¼¾ÅõhÑ,f}^Ö´²q¡å NÐø¦¥=»µxiùút(M}h¿ôòWÐ÷Ê3NjB8¡Ë þ¥æ¼ZyÁÐÖáXÛR+N6;kðC?´õµT2Ôìýâã| ÿTªIÉY\~ÖÛ¶m:)] ðI£&  ÇÜL®IÁ1¼­÷ÝÍ¿ýÿþüûÏÞ«èìn-ÏþvßMÿþW/Þ¾xg²ðÄËFv<§]&!DâÄd:ÞÝ0{i¸®«Ô¼·Ã_èÛxóâÝÉÎ;)êþoÃ.ûà¸»²-úR6ñIí}R_*
éÍ[÷÷ù³f}m(*Ü»sa!¶W,õÌ«kk¶ï!ìLïj¹s»­k××ìZÿô=ÿüô7­
áXÖäâÓU®Ngw}.ìÚòàSÿªæo_?µï
ûðÝ!ìÚñöÜ!Ï¾uE  G  SéG~9ÿöÛRÝºþòNÝÚòÝRûÒÚæ¬
ÿqàøïòÈâÊAWõ]þãkß\²%Sº>ø³=yxçÞFØÐäÌ¢ì¢W_ÊÂlÍÝ×ÌýíÆ¾1Í
KOjRV»ÿG¶8©uêðBþ¶õµ[°ý ÆG×ÝÈðáÕ=<}^ã¡#¯ìwRÓ6Í¹ë¾¥ûÙ©Qû¯ÿxtßTìØGKë=¾Ú¬zæÊ°-U¹+uÊç¡fOcO´.ÕÜ]xÛ;!¼UZÞZB!Ù´ 8©üDÜô ã0×MNºúþágÿõ]Wö-ú¤¬  |bmØ<çmÙªWW¾òö19ãçK®úÇÞ#:}èÃO.³üí!Ñ$ø|÷SÂ«Ú³xE(n÷¹öÖíôÒ·_'êÙjp·Üó6gCÈn|§:4ë|ÊûÇirÊ>©·ç1üÊ1Ã¿vÎûõ?ûC¿¾|Þ7¾û£/l×ìp«óüê¦{¶ïàÎ÷×OÞZþ`ØöÚ­{¯em:¤N<a+:©0lÜTûÞWµËç½´tcØ¸ª2´?£ßIMCaÛ¦5µ»>úOj6Vlzÿém[ÓGåÖ(yRÓ¦mt.*ùf¯óîî×zý²ù¿~'ÝëfTd{÷8ó«ù!$zwýò¡ý¿úáOÇ;`WØÕ¨8*ÎÏcõo¤:þ}×Å!¤
Jÿið7nïQtÒ ë0krAÛ>Ý;¥BHuëÑ¥õø]»«¦üþ®á'×{¿aw=~ïOºêÙ  ð ×ªä[½
!ÿ¤n§jwLÎ¸e[º°õØþßûxJËf'}ásg}õK×j¶~iÕaÇæÚF{Xò»µ¿~PóÍ!qRa~!¼»qöpú·;vÏl±geäO.m4èÛ§Ó2?$5²Ï¯ÿåKç4oèëù1m{uÁ!ÚBûÃ6d`¿n­O¨ÿÇ¦[k·nMo­Ù´fé?üzÚ¼í]^ØµYáEMk+VÕBÍkóÕ~prãÊ²g_¯É°õõ9e
;wÚï -OíyÒ¦ùO½Z¹u[úí²Yxö¿¶6
©ÂTXÿÖm!l«?óÚ¦a[M:Ð¸qã°½jãÖí¹êÒ»ÓÎeÏ<³*ÂÎ­«^þ«_ÏXuT=9åÒoÿþÒoM»à+Wìz~ÞW/Ú!ÝÿÌ¯6}îC/wù·oî°kæy3ÿ¦mÜ3Wo9¥Ï°¾Ò±mæõþ¼<Ûù+_~ÅCûR5÷¦ò«^ ð t?J¯-{ðÁÎ7°xÃSÓg­ÈÜN.?¹ÿ¯¼ÿu6]±üÙ¦Þ={õ¡ÿ0¹zþÝ?]®8ê?  êmGæÃK4tÕ¹¹ïºÉÙÜî£ÏÞùí/Ëv|·Ë·FöùAa¢IØµyÝ;¯Ì~õ?lÎæÂo¨è>²Ïc¿Û½ù­·ï¹çÕW~pöØ°õßÿrÏÝ/ÍÛ|Â?¼uöÒ×Þû ±íÑ{0ºÛõ·
ùeßÞ8åW}þÝ¾¸¶s{ºrÕÚµ;ÓÛsáP×·Ø¹¥ì·ÿQB¦ZzþÎëÓö½;Ûa÷é3ïû÷çSE-»êß©¼lï^M»ö-ý¯é·>¼q{ãÂÎC.;ïcV4nyÖeÃ·<öô´_>²³qv}_Òïúé»ê÷O^Ð´°Ýé½¬tÆÿ{JÑß>µgççgLÿÕÚ¾#Çëñïm1ãá»oªÝÙ¸°u·GmïÿËöñã_Þ]óØO=¶ÏíoüÃoh@Ø=ÿC^ÙûÕú×<±ðè½ 8"òzÞ¿»$JÏ8wHÿö{§JµëÛÿÅ!T¿°¨"®ZþÜìÕ°ê&ºüäþ{-¸eâ£C!YØmðåc/.záûÅ+'_5ån³'\ýÐº¾2uuu!-ÕB^¨¡¨x?wlÞTÙ¬YACÏ #oÛ¶Ì-öùj«7åçç¼¼PW·»nwaQäX¥LÒöº«NýZ»·c]åý÷ÿõ·KwÂmEûù<uã
ã¼W®â{ï»~ÿ/þÝ+/ív^úðM7ýÞõC;»S¬ýüö |Õû·¾£'X¼ïöÖ=^Ð#0¤WÁºñ¿Y½M9®­X»'¯«¸ï¾Ò>·×¿Kâ÷÷K¸~êÄä½Ý<7BHô½ñkR÷]qýì\¢Í¹ão¸ü¼ÒlÕ¦¯0¡÷¢«&Üv×a+®wÇë'ÿàî[º-¸sEÇoõ-mU\P³hêmf®ÎÂ3¿?nìàÓÚ'³ÕkÍ:ù7jb  ô[k&^·fbCOã¸(pÉððüË«7nûÛÞïüÎ
ö´: àxRÿ
(Hðï!©Ô!,Ùlò ]nùõ WÌ<xÝÈ'W{Ý+:%7ÌÝçP!Ùí+çþôúï­Ì~óæ)£F3ù#Æ_ÜüÙÇL+Ï÷1ñ¦1#_wG¹1  ãCÓ/ô8ÿ²
= à¸Vï§ðå2µkÞ\õÂÔÇþßUïg@ª¤}ß¯¾ëÿüú®qJj]®æ8¯4³hÞªxÜ-è= c®ìÑ'×ä2+¾}ÆªýJÏz|e.PQ¾¼2ÙªcQ©«©ÎäB®ª|úÕ  nÜü\æ 8Lõ¿7¹¦ìñ{¬°úWõ\´Ïë©>WLìBaÐy½*Uµßhì4â§.ÞóÛd2»¡lúm·¿xÏ¯(iUjî=fÍÊUÙî­®®}oD6dCÉ[ðÈ´òëGß3õ7_[T^6kæ«Ôd    u½MµiªÖÕâ¢ý/N
!BÈÔTg?®Øf×Ì¸mÒ
!l6S]µ1S´{H8·úáÇ=Û¡÷ÀA}ô5yè¹S®½éáGöb ÀgQ&Ô¼Åq"êòêêêòþæzæååmMgNHy2öáÚÎäååíy9 pêÿ¾6ç^wÇ¾ÙUj
{uÜÏßf*gß<öÞúwI.ÿòÇ?ç.ÞðæÊÕ<U6¼¿rª°8²!
Õ¡°¸(±§)uhßú V[!Ñ¼$«ZYöÄÊ²'¦?ù{n¹hP»#   B^»|dä}Rr¡®®ÎÕ=R¤d 8õ^79LPÜ¾WÇ=k\Ô¬(ÿì¼×Ö¤÷¾
ÙÌºg?7wíA¬\ñ±rkVÖ½û÷~n§=k/­(xñ¡ Ã¹c=¸Ã^<iÚãthB((íÒ¶ WYU{L®0  çV'êBBw$ÔÕ­LìÞï+o¼¹ªÇb?ÞxãÍ |ºÂJcÍ;Çß¹(BÉ kî¾a`ñYÅìß=ÞgÌuÓ~®©]1{Ö³5í[ÂêîÞiÂ»¸<]QöÀC/tÐý öè·^9òS¯K%³éµKgß{ûl5  §ïì¶#çîÙÃ7»`ÿ5yæÿûS¯§å¹ÊgæSÏ4ô àÓ-¯çéýëµC¢Í×&ß3¦×Þõ%²ËãôeÙÂ3ÇÜ<yhBåGß¹(sçH$r¹\!$z\=íg­øÎMOÍóßöü;¯-ÕB^¨¡¨¸åGÇlÞTÙ¬5Ú  CÛ¶eNlÑú£Ûk«7åçç¼¼PW·»nwaQ§Y]ÝÄ®¼Ð¸.Ï ê!ï?vlûø?Ú´irÂO®Êf³M4ièù~Êd³Ùd2ùËÛîÞ±ã ÿu+ °õ^é"WµdÖUï/kìØ{@ÇæTsû´ !ªOÌY}4ÓnáE¿úð/.ïYHu¹ôòÞÅoÕt
  DmËË»£xçkMv§óë2ÁªõÎ«Kç×½¬»­(·íÐ¶oÏþÛ-w,þëÒ­[Ó[·¦úiétfëÖô¢ÅK~öóÛ¥d 8|õ¾7¹Á%Úû£+ÎëÚ*2¯¿0å?¦>·6×Ðúso2 ÀgÙº7ùÃòêêê,ÈpÐíråååyÜÁp¡ àÈ:Üu½ÜÚ¹w\;÷  °_Rr½ÚåRH GV½Wº     à3HM     NM     NM     NM     NM     NM     NM     NM     ®qýw)ì9üÊñ÷kÍV½ö{ïöâÆ\C¿O     G½kr¢¤÷w÷kÌTVÔd<4YÐ¶¤û¥Ãû=·àÉ7nNnwÕ[ºÍpõCëêi     >³êor"Lðæ¬?~àFhóµÉ÷é,ÜÏkEÃn6"}ë7ÍywÏoþ|Ú?\õ£ûW¾·÷îÜá¹c§W4ô5     ÖM®YørE¢ÛÙÝï}Ý¼W6!ÛªWïmH´Ð£hMy    ðIpë&ëÊÊ7ìß»[¢lq.D÷3;Ô¼0/×·O÷ÇËJúv+Ú°ôÅU!$J?j`·¢DÈnX:çÁÛï[K9áÞO>6²ëIßyä'Ú}ç.ÉünüOÎö¿òºQ»lÍyÞ~çË2]®rs·S×týVßdØðÂon»}öº\Eg\~Ýs{%³5+<z÷­O.ÎÎ^ÈV-vêwÌÙB(9ûûãG
ìUR²Î~ðö©s+¬
    ×èÞäÖ¼¸¤º¨Ë¥!8µw·°zîÌåé½{%B¡¨O¶ÙåsåB'ôÍ>8ñ¯_vÉµOfÏ7ñòv!l6ìqnÇ·}oÙ%·pÀë¿5éçOWcÇ
Ì>:ñ¾uÉU÷--1~x»²!$;
ê÷æã.ýî¨±e»ò}ÇNÖºü¾¸èª©k:^>þò.!ÐaÄÄ ½ÓÓ'~çq ²W    IDATgó&\sI:\<qB¿ôCöL)ÝÜu·kÀÿ     Ç@ÕäÜ²ùÒ'ïYÚ¢í§¥V.,[¶pièræ©÷íÓ>[>Q.:¸oÛªç¦Ì\ !³ò¹isjÛöØ1B2³äKªjÞÝ§¿îºSß~óôÅÉd2Íd2!dÖÝ1öøÍê=ã²å³_!W1cÖ¢l=ÜÂÛÇoYU.Y[6«<ÓºôäNÜ·mÅSf¯®Él\üÐ}î}zE.t|n§'§ÌÞ3¥§§ýy]§AKö?#    ÀQv¨+]¤Zõêß·uö@CEíÿrnùË¯çÎëÓ½à±×zõhµfÎk\æåß9ãä°¬Õ+¦/ÉDëV¡jÝ½û¬©Ø·jé²ÕëÖ|h}â>£&öh³èç«
!ÿÀ£_8îÎ?_¾´|ás³{îõÚBÙÊª
{÷«­ÎnEE!lhÝgÄØáÝÛ$BÉTQòõDØsöUï
^÷òÌu!$Î-i<uÔOúàÜÕ«Z'Å.    ãØ¡Öäcoxx§~·ìÅåáÊÞ½Â¥o!,Z°vü î¥§Ü-µêáWjCHì³ÏßÔéÜcv²u²òLßË¯è9ï¾Å¹Â»sÃwfvxöýÿÅ°sï¼þ¦Ùïí¹Ïa]/8®÷{'¹:gN¸wRÉþÏ¹GvÁÝøz    |vÂJ¹l¶£³ÙÌÇ½)_¸"ÙîÌÁ½;e¼\BUåK*K{<£KqÅEU!\eÕPrrÛ÷öH´íØ*Tm¨ÜOÇÍ®xè¶ëzï³És¯Ó« EE¡jùsýæg×4'×wp¿¢BHü^¥N¶j]ªk6¤ºvi^øÄìÕBhÕ©MA2|ôì'ûýËtkª6Ò.ÝöîDÉÉ%     p|«wMÎU-[¾á g¾¸¤òãnâ­Z8·¢ÕÀ¡§eîS±pi¦ÝEO®,/Û³ºÅ²ÙekJÎ}a»ºyvá9Ï½¹¿eCEwÿÇsað±g4Oôu÷´cÏ>¹ DQûN%éê
éB©CFö(LÂÃ¿Ö+»dî\ºª6jß³cóh9àû£¤2¡ Uë÷ÏþÍÓJZö>jìÅ§¥²¹7g?·¢hàÈËO+J6ÆÿìÖÉ£NÓ   ã[ýWºÈ­{âæq/tèÒ­¤à½-É3¿yå×OM]1{êój÷Þ»­^¹dYÕX·¨|Ãè[Mí½A¹å/¿¼ æ©«ÞÛ²òÁI·5éá%BõEsnüÐº®ñ¾Ì+¿<û´É?3÷'÷N:fü[þd¶fEù¬É÷åB»²k^ºü»&Ó«½sê5!,xpÊkFÿbê¥Ù
fLtgïI7
»ýgÆÞ¸çì×OS­zíÙ[ïzxmáÑI?/?êFô/Þ7iê«^     Ç·¼§÷?Ô}¿yýícz§>úJú¿¦Ü8é×ßmèw÷Qí®rK·Ù®~h]CÏä¢®®.°¥zSÈu!·üèÍ*5+¨÷¡ øÄÛ¶-sbÖÝ^[½)???äåººÝu»Z4ôL hxú¾Bé
+Þ\[üÇÔekÖU¦Ý­    pü8«sß5sú     pôÖ½ÉB«ï}YCÏ    àÓ'¿¡'     À§    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @    @L\~~þîÝ»z  a»wïÎoÔ¨¡g À§L\&Ír¹¬  ðÿ·wï_MÝy¿Àß;{$\E­m©Tlq¬C©½<}:óéjÏ®³f~8?Ì?qÖ×ñY}æ´c;ö2½ØZÇ±Z/tðRiÁÂ4(È=&ì°wr~ 6VÞ¯ÕµjöõìõÍ}?D"££a½ÞëÑOëÐO@|¼1
MSc=""""º3t¢¨×Ë ñÆX~2&Óí :ÑcR¬BDDDDDDDDD1ÃNDDDDDDDDDDt{L    B¬Ç@DDDD÷8K$"""¢IL  ¿$Ñõ8?$"""¢è4÷U[èTU+Nï""""R'æÂxñ gDDDDUUuá°ëaP©ae¢Õ C±ÅØù¡n¬JßH
+bb9
 ÅX~lª:B¡N  0::ø~ """ZTuTQB2¢ÓéÆþv-
Tuß¬k³DaYÞJMÕ´DE4Ö#£ÇØ
UNÔI:Q§Ó:"D"ZDðý@DDD´ÐL¨ÓÂø=ø¢Ñ("ß f èD &DÅ(8-\XNÔ  :AÐÀ÷Ñ4>? LÜOå·"""¢lr(étB4*
nrRÈÉá}oòÝ U't:Ñh|?-,7ÍA ?Fø­hÁ¹i(ÍA ¢"Fy~
Éÿ ×þ5þUÂÄûaüßDDDD÷½çÑhÀXßäu%-, ÂµY¢ 8½>.N/R¬GDDDDDDDDDD÷¦GÃêhXÓËøXîE:Q4ñ §õ`è'éu:ëaÑ=MÐÀ»gÑ½Jf5IH0Äz8÷¹`0$:¯/ÐÝëºa wÞ#""""""""¢{N§+²å·_îv¹ÂáÑXgAÐëãd}ÜÚ¢
Hdê*]¬ÇFDDDDDDDDD4
A@-ÿ»mÃþ £äM8<:ìol³¯Î¿aÓd"""""""""ºe¤YÛ/wÇzWûåîÌôÅS0M&""""""""¢{ÙdTX;2j2%N]òû&R|¼Q/©á`pDÆúÍlIK5ËãMq÷»ü¦ÅzTDDDDDDDD¦ilpCJxTÓ®ë<÷4YJLÏÍ[¾Ì(N,Ñ®+í-ß«±~~l2Koiç ì[wTÚLSyÎíÿFZ|ñØ©Î@¬GDDDDDDD´%$ÄÏf3Ùj«T¼.w@3æ¿ü}j¡Æït2ì+caêÃ¹¥ÉzKÝ¾Üj¸~©h´.+²¦¹[Ú=áX?Áûhrlû÷§óïöï=Ôìc¢<_i¶<ÓMKEsÞº3K|VÝÎ1DDDDDDDD÷,ÑTðäö*e2åt×¿½§ºßëêïvÁ JFË" $ZL¬Ï§9¤ÉBB¦Ý±Ü7ÃjCÊJmôÌwW³ï{!smöd¨<
ç¯x§ÛÕSRZ ^øò|waÉ*ÛÊTh#®æómWo¯%SÞkV$
Õlò`Ú£¯|ÝàMøÑ´îÓ_wÝ6þNLÏÔ¹º}³/¼Ö[Òô ³äÁÞoºGfÿÏh¯w^Í³=°m0Ï@YÎ()«Xj
\íiú×áS­Þ;:ÚyÈÛúÚSþ½®¼Ëç¤>R¦ã¹çñÉÇÓÊ©e¿z9åÔ>sòGQ¬È©EÉß{±Í¥ ªªù;úhJãçï6Êç/[tc)e[JóS·«îØ3ÊÏ4VnÅï_°]×{¸»úOïÖÿ
F±pûÿv8w}Ðóüëµî~ç|pîÇÈùùïÊï91ð_ðY§ÉBBÖ£ä1q)¶5YÚ+ÙåÉ¥À¯«{CÌµ%BouïÆ]ã3×,5Â?>Ü´U,>÷U7*Yl%®ö¨Ìy%kÑú\ñª_Iá 9öeJË)WúÙ>ñ¤ôåY¡¡9¤ÉRJnnêåÞw÷ÅË©ÛÒ]ßöÞÑmÍÛvìÃOÕµÏ/P36½ðËßWÿ|ÿo|ª9Í^VQùqßî#í?ðÃrßëÄgûÎ ´$LîEÑ5W8ÖwC#g<÷ÒÚ×Ú!ååÏ)[Û7§·öþ{A@N]_ùò3åî7µÞÁ@ÈÛðîÇ;cýZÝ³MSz¶eCÃCjÂ¢DÎeêj¹©ÆXX²zcA¸¶¦m ôKz$«çLKò"­¿¡w@¨»Ýµbmº ¾ëKc
¶¥£:|¶±ÇñIÍ×éP¯uËãe`2çÕëjÅå§M{/ÕõÔ
ÌÆLÛÚåÉ² Bt66v¬kÌL>ü¨¡átÛ`Rú¶\K<
»ZûsÖÚrÍz0ìm>ïÍ)^c×%=Zü}]]w»;U~Roóð½j·íøbÇ¶yÊF[¹CjøøÀN
 ¼}õÿÜ»Ö MOo,0I ¼<ÞêmÏ¿^ì>5Zj6¡³úh÷²
EV³Yì>öùçÍ>cÉ¯fwSÓW¦¡£5AÛ#©fÚ~ä½Ã
Ä¢í¥Y¢¥ëôÁ/j{4cÉ¯f;O«ËV§$
Ásû÷éÑ`±mßöXAñ»*Æ~`\Q^õd~hÁ/4Þåp×¸zë«'ø¼õ÷Ù¶ÔUn]c  t×;ðMW?·y¥Y¸[ÝÙ%âÉ7ÿÑi]·­â¡ yî?Å~DDDDDDDDw1÷±ç]))'ìkM®ºEl¶.Rz[:Çê|þ³Þj_WVñTU¦4ÚÿM§Ù'Z·%.±Un^c´óä40W=oÔP×éGê4ÖuÏnytòºz¦Ä³©¶í¿¶çeu áÀ§§:À³q[Ý"·­zßa§w<­Zc}§QÛ3yþª{÷}pªg.Ynv  ÌÓ®ñ÷?×ÐÒ­¬Ú°hQ¼pÓVQ×GJÉ+Ö[3»"ÆxýÈðD6âÑÇ'^WëÓ
òÐq¡g²VÖïÒëè­iÊ÷ºzîhpø}6ätzµoæ
p}ÆñjÝ©ã'¿ªíOXµ*K¯|×äQ}í_nó qÕrßù'O¨íOXeË±¼@ßûõÉã'Ï^4¦[ôÞ¶¥¿ñt]WQo¯GZ»ÀÛvüÃOëûTÓÛvl)4sÝ?#+5pù»Î©o_ûyg¿cQEeëÀîÝÿùÆ_÷õgUn¶¨ÈLÅ>úË³JaÅSæú¿½ûþ[Çó×¤ PaÈ¶í}çÍ}M£òõÄýyÏ7ZÑ:0Ú¶l¶´º{ç®ÿ÷akrù&»q|ejÍÞwÞÞó^ühi¾ÙödYjÏ]oìùËa_J¶ °>úÄ²¡îÙ¹ëÍ]5¨ù©wãÕ¼3ÒÊ·­7|³wç»w~P/­zC ælÜ?tø¯;ßxÿ7ßhmm06½·ëÍ»öê¶Ø²b=r"""""""¢ûyEùÏ®Ëçû>9Ûº½ßã Mö´:E[ÕóeY)2 ÅëU4@.¬¨²¾ýæîzÿhÀ^õdÙ'Z·e-ßVØ¼o×®Ý»>j]´©b0;ª6§wïß³ó7ß9+mØVåä¦÷ÞØýçÎ"#íZzmjø`÷Î?}xö-¥V Ù¥ì¡³oízsçÛ5þÂòÇ³1VIgßß¹ëÍwêÅ
[K¯kÆÜM;£Í-JÆìk¥xýDð¬
]nëÒeÚ²tþÞoë¾WR×<­µ¨îÑ«=+'´%«Õ4Ü_ÒD®
w4¢A§nKVÛrÝåo{ÃX2yó§äÁ²²Ñ§ôÖ}fÄ'Äá¶[ür Ü}îDOTöøFS
ñÀèµµ ©y°½3ìíÎËJÑwµxkv÷R¿ÏÓÖà¹ñ%
2$øgßvyöª?üT|ùû[+ÞOÌåâËY
¹¦ëi!æ¬Hj­îQ h=NÿKùb«íÝ ¾¡Oisiæõù
&#0àl  ðõànïðxB6xÿö4EÐßÙ*0/±æÖC>)ÛkÞ¥³¦Oàmjè){ ¡\\Tçmm÷4þãã»ð:Sýn_hâ$[Íõ· ü<cß& x[zÊÉN)uhp××;KË¨þ jÎ/.ì=×Ú×Y}àþø3"""""""¢{h.Üôâ6ÛbZþùù¾ó.
ÒuèÍ7fÜCq~þö^ûz½tKEªêv«©>sIÉ)L÷7}Ø  ´×:CÏ®ÌD³L´®g¶ÿòökBûþÏ¬lc×úA
§©a`½=7¡ ù©
ô( Í
JWZÄþlËPÛ·ÀÕÔìÚP0~¡ÖÆvÀ`S«Üf«óð_ÿKÔ ®·oaÉÏ6vý«5À{þÀ®f(È ¥T=aªûh_ëÜÿ\~Ö}µÈµKoÄPcÃ·¸FÓÖ<´2yêQ"ÓGQWßàåÖøKÝ4³¯§)H$
(wªÓD&³[iqa¾|åü`J©s|}MbïéÃª»vcé¯¯Ìö.wq85¬Ü*~6X¯Ê_l"H\|z®_)ÅÅYÖ¿P<úhWó×ÿ·2gMYQ\èêå;<×÷HVÃJDÒ_×ãM9EËxúçxíÕ¢-FÀ}ãI6w"gVd5HPM»´ uìùL}Vêø2¨×VC `Ê/-4Ï$«3èÑ  
¢IDATj0Ð4±rm;($Õ=èj¡ÐØ|µÀ%_*«Ò\-5GÝ¥Nî¦'×R)ÅöÔ+o×£ýz²¤*¿ãÒBj0Ë0È¢øÇ_9_  ÉvéØ{ÇÖo,yú7[e{í¡Ãßt²ÓÑü=µÉ¶¾÷]k*Ê¦D¼ÊÌR ¯áØ¡ rrvQiå³UØ½7d9vü¾hlI.ÆÌ*ÑºÞÍ}³ó
-¯¿öÔøááï4 K¥¯þnýÄ)µ¦DI6ÊÄ1ýÊäÁÀxRTÈ²Èö-OØRPU11ý eª]K«&ö6o^ÕyNù!Û,Óäè7  i¬P[¶®Z·ú¿kûuKí7DÉð¦
l£®-gIRØäíjøÃñI  ãGþÉ=MY)²)¥¤<'
Ée%ß÷§þÃ* u¸Ï¥,OY$\C}ò­è3W9Ô=ïQÕåk®_RGG]MÕ®?] ÏY×çYT¼våðñÆÐN9¢Éö³íU6ü¿øôxwn_ëéè6<fÏ;/]{ìKÔ³Õ&e  r¬*!uö¿v±¨¼*Ï÷·=w*@îßÿl¦1©!U2ÆÈc]´]µ»j!³K_üEEqçGµÞÙxNRl?5Ë¦¹EÉ üJH2ÆoÚ'd)äVÒT9aü9 F£¨æn>µ·ùädûÖUO¸vì¸Oh ô®®vú
&n3&gU¼²£X­{OuÏtI¯1£ ­cëÁÎojêþ='5ZR®Ýû³×m|óþ3%Z·æWB!çÑëïõg\«¨=5ÿõAãa6²a<©K4N¶Ñã
²E µ`=óþ[ç}Lë~ù«| ~EL«d³Ey (-÷6TUn.èþlÎÕÉ³ìð°khJL*§®z´ì±Go¯8<ý!¢W»<útÓp »ÝbÚ²ÌxBÂÒ\«Ößë`É\(ÀsþdõÑ5ÇOÖ¯nvkCMÕß´«þpâbk< ñKRÆèñ]ng44*éå·% a¿_¥Ùæ8!N 
qz @°ÿªi H¦<»-3ÆâW- ¨#¾u¬z¢.nü4^Ö©aåvC3ÑTð³íUEø/ññ¡ú¹!ÐòU­²zkåÆÉ²(Êæ,Ç3ÛÊÖü~­»­wQ=C g;ò;ó+d[Äd#Ý Ê3dÓ®Î9»(KDÍ óþËJY´Û¸+5Þ Ð`OWgçøÝ¾9Êãì¤ÛL `¶Ù3íípwõ#Ý+bJ#G/oÊ(¾~¯97½&"""""""¢i{ëë¯EÉ $Q 3ÕJJKìÛ*c÷µÍ+v³«£?ÜÑÜXäkl.,ßQ5C3]¢u[Öö@VqI §=òLÝÀ%gÿ[ñh)úù3ThÝóSE@L+.´^;À¢<[ÀT`³u÷)eYñz`Ìu¬NAáq^;¹¨â¼àH ÅëlÿòHkjYeÑïæ5ëÓWÛ¥ÁÂÉøXwó¾çR{ß'¢în¯cu°±a,§z[ë/Ù.[#ª~×¥ºïý ¤äekrÜÿ´ñ¶^hµ­zø\ ¶6~?<eÐÕO÷¢~øgéíûöøRâà°OKONÄÀðØcÑ²æñ-ÈþÆ#;z2W-UBÃmm=E6»#ýë.h[_f¸pêbëw(*Þ¸\¨¾Öú{/ûÖ®Ú°IHÐu¡Ñn×H~Ñc$5ió¾á; Onn>Q2 h=Õ½(«xòÅÌ2Bî¶ÆO>¨ïÔÆ#<]ùú+ÕíÜw°uy§·ùEå¯¾îðû]uÕÕ·VTþÂöYûÍ/~YSðlå~§ø=Îö Ëµ?énUhÁî³ÇîFa2 Å×ÑêtO\*C¶ieåÖCAåÿ8ñÀßôî®#Ç÷­Üºã·¥ tÔúj óÄ±·¾ò[ÅçnmjõZDÀÝ\Û¿­ü7¡Bõ8±0(F¼ç¿øD*+ßöFÐüî®¦ýÎx ÏK*¶¼öP]§öÎPo9]¢u{®¯ö­Üºãw¥" ¸«÷yÔï;\õì+æk=y¨@í±¯²~ù9BÞ¾ºö5[ ÝÊC/ý*Ól§áÀY ©ñìøÅ+¿
Ýí5Çk¬U¥UÞ?¾ÿlÕÖþð@ïéýg{V<v~¥ëÈAç«ÏT8:?¯KÚ&¬}ð±YokÈ,*±gÌx_B¥¿éÌùÞ;Õwâ.=¶2Twª-øcpÑê
«"ugïàAåì²ÿöUÅÂ²§Ö§¥2_UôÔú²É}W:
ßÌ¶_«Èù3îo:ðÖßw¨­qÚ×V÷ï>Ú3ÿCÝÿöúÖ[l çVüæfpD³í¹_WäfìtA·vÃ%K;Üh¨»±.µ¯Í¦C¿»±îÂÀ=%^uv¬X»äÒÅ»×0aøÌeVÇé;%
2¼¿øt²*Y^jvëÅÕ(iòÔÀP 9æ×¼ùuÂN~ä×;òë?zï¼OÎµçÉ®£ý±~ÊDDDDDDDD÷Ås¹Ûo[i«üíVùÛ»¼ï¹Ô&OìoÉÈËM_/é  ¢x».utyB÷t<ÁS¼Ö|¥¶Áÿ±n->½äAkï·
Ý#ó?ÝEÆ¢
¥¶óÝUUñv6þ«¦©~?käª­Lª6ØôåG´Òx"""""""¢¸ÛÖ&bJQÙt£4S§VMñv>\Óêe¹åqÃ%øi2Ñ]·rùÒï¯ÄzÚ
@ëñMCE½>.Ö£X¸d}N¼®èi2Ý¼¾Ì49vdYïõú§.aLDDDDDDDDD÷¢î^W~nf¬G±påçföô]ºDLËÈõ¨¦1puè5ËÁ MÄz8¬3&ÄÛVå~wáûh4:uïÂGDDDDDDDDD÷´ôÅfSbD$$b=û\0Ò:¯×CUò)ÖÃ#"""""""""ºÞ«=½Wç'öM&"""""""""¢ÛÓE4-Öc """""""""¢{ZDÓt££áXîi££aIQB@Tô¢ÄÊDDDDDDDDDDtMUU5¬(ÊÿîØð½j    IEND®B`
------geckoformboundary8b16d4e7cd276021ba6835fc52c18c21--
```

---

## **4. Modelo `Contact` con campo `profile_picture` habilitado**

### **Ruta: `app/Models/Contact.php`**

```php
protected $fillable = [
    "name",
    "phone_number",
    "age",
    "email",
    "user_id",
    "profile_picture"
];
```

- **Explicación**
  - *`fillable`: Define qué atributos pueden asignarse masivamente (mass assignment).*
  - *Al incluir `"profile_picture"`, permites que Laravel guarde la ruta de la imagen al crear o actualizar el modelo con `$contact->create($request->all())`.*

> [!TIP]
> *No incluir un campo en `$fillable` puede causar un error tipo `MassAssignmentException`.*

---

## **Análisis del Envío de Archivos en Laravel (`UploadedFile` y almacenamiento)**

- **Objetivo**

*Observar cómo Laravel gestiona los archivos enviados por un formulario HTML, cómo se almacenan temporalmente, y cómo se pueden guardar de forma permanente en el disco configurado (`storage/app/...`).*

---

## **1. Inspeccionar el objeto `$request`**

### **Código en el controlador `store()`**

```php
dd($request);
```

> [!NOTE]
> *Esto nos muestra toda la estructura del request, incluyendo archivos, cabeceras, parámetros, etc.*

---

### **Resultado parcial (resumen del objeto)**

```bash
App\Http\Requests\StoreContactRequest {#1280 ▼ // app/Http/Controllers/ContactController.php:135
  +attributes: Symfony\Component\HttpFoundation\ParameterBag {#1282 ▶}
  +request: Symfony\Component\HttpFoundation\InputBag {#1279 ▶}
  +query: Symfony\Component\HttpFoundation\InputBag {#1281 ▶}
  +server: Symfony\Component\HttpFoundation\ServerBag {#1285 ▶}
  +files: Symfony\Component\HttpFoundation\FileBag {#1284 ▶}
  +cookies: Symfony\Component\HttpFoundation\InputBag {#1283 ▶}
  +headers: Symfony\Component\HttpFoundation\HeaderBag {#1286 ▶}
  #content: ""
  #languages: null
  #charsets: null
  #encodings: null
  #acceptableContentTypes: null
  #pathInfo: null
  #requestUri: null
  #baseUrl: null
  #basePath: null
  #method: null
  #format: null
  #session: Illuminate\Session\Store {#1256 ▶}
  #locale: "en"
  #defaultLocale: "en"
  -preferredFormat: null
  -isHostValid: true
  -isForwardedValid: true
  #json: Symfony\Component\HttpFoundation\InputBag {#1287 ▶}
  #convertedFiles: array:1 [▶]
  #userResolver: Closure($guard = null) {#1216 ▶}
  #routeResolver: Closure() {#1225 ▶}
  #container: Illuminate\Foundation\Application {#2 …37}
  #redirector: Illuminate\Routing\Redirector {#1278 ▶}
  #redirect: null
  #redirectRoute: null
  #redirectAction: null
  #errorBag: "default"
  #stopOnFirstFailure: false
  #validator: Illuminate\Validation\Validator {#1297 ▶}
  pathInfo: "/contacts"
  requestUri: "/contacts"
  baseUrl: ""
  basePath: ""
  method: "POST"
  format: "html"
}
```

**Dentro de esta instancia, encontramos:**

- *`+files`: Contiene los archivos subidos (`FileBag`)*
- *`+request`: Campos enviados por POST (texto)*
- *`+method`: `"POST"`*
- *`+format`: `"html"`*
- *`#session`, `#headers`, etc.: Metainformación de la solicitud*

---

## **2. Interés específico: sección `files`**

### **Ejemplo de archivo subido (`joker.png`)**

```bash
 +files: Symfony\Component\HttpFoundation\FileBag {#1284 ▼
    #parameters: array:1 [▼
      "profile_picture" => Symfony\Component\HttpFoundation\File\UploadedFile {#34 ▼
        -test: false
        -originalName: "joker.png"
        -mimeType: "image/png"
        -error: 0
        path: "/tmp"
        filename: "phpnjSAAK"
        basename: "phpnjSAAK"
        pathname: "/tmp/phpnjSAAK"
        extension: ""
        realPath: "/tmp/phpnjSAAK"
        aTime: 2025-06-18 01:24:22
        mTime: 2025-06-18 01:24:22
        cTime: 2025-06-18 01:24:22
        inode: 6192090
        size: 45996
        perms: 0100600
        owner: 0
        group: 0
        type: "file"
        writable: true
        readable: true
        executable: false
        file: true
        dir: false
        link: false
      }
    ]
  }
```

### **Explicación clave: `realPath`**

- **`realPath`: `"/tmp/phpnjSAAK"`**

  - *Es la **ruta temporal** del archivo en el sistema operativo.*
  - *Laravel mueve este archivo a una ruta permanente **solo si tú lo haces explícitamente** con `store()` o `move()`.*

> [!TIP]
> *El archivo se elimina automáticamente si no es manipulado al finalizar el ciclo de la petición.*

---

## **3. Almacenar el archivo subido con `store()`**

### **Código:**

```php
$path = $request->file('profile_picture')->store('profiles');
dd($path);
```

### **Resultado esperado:**

```bash
"profiles/rJWjOc45tWhxYd22zMqjeuRF2AoxQjvULPpPSfng.png"
```

---

### **Explicación técnica de `store()`**

- *`file('profile_picture')`: Obtiene el archivo como objeto `UploadedFile`.*
- *`store('profiles')`:*
  - *Almacena el archivo en la carpeta `storage/app/profiles/` (por defecto, disco `local`).*
  - *Laravel le asigna un **nombre aleatorio con hash** para:*
    - **Evitar sobrescribir archivos con el mismo nombre.**
    - **Proteger la ubicación de los archivos contra técnicas de *fuzzing* (búsqueda de rutas predictivas).**
- *El nombre de archivo generado es único y seguro.*

> [!IMPORTANT]
> *Si quieres que el archivo sea accesible desde el navegador, necesitas moverlo al disco `public`:*

```php
$path = $request->file('profile_picture')->store('profiles', 'public');
```

**Este último comando lo guarda en: `storage/app/public/profiles/` y puede ser accedido públicamente desde:**
*`http://tu-sitio.com/storage/profiles/xxxxx.png`*
**(*si ejecutaste previamente `php artisan storage:link`*)**

---

## **1. Método `store()` en `ContactController`**

```php
public function store(StoreContactRequest $request) {
    $data = $request->validated();

    if ($request->hasFile(key: "profile_picture")) {
        $path = $request->file(key: "profile_picture")->store(path: "profiles");
        $data["profile_picture"] = $path;

        dd(Storage::url(path: $path));
    }

    $contact = auth()->user()->contacts()->create($data);

    return redirect(to: "home")->with(key: "alert", value: [
        "message" => "Contact $contact->name saved successfully",
        "type" => "success"
    ]);
}
```

- **Explicación**

- *`validated()`: Devuelve los datos validados desde la request.*
- *`hasFile(...)`: Verifica si el archivo fue subido correctamente.*
- *`store('profiles')`: Guarda el archivo en `storage/app/profiles/` con un nombre aleatorio y hash.*
- *`Storage::url($path)`: Genera una URL pública, como `"/storage/profiles/archivo.png"`.*

---

## **2. Verificación en la base de datos**

```sql
SELECT * FROM contacts WHERE name = 'Sky';
```

```sql
 id | name | phone_number |     email     | age | user_id |     created_at      |     updated_at      |                    profile_picture                    
----+------+--------------+---------------+-----+---------+---------------------+---------------------+-------------------------------------------------------
  7 | Sky  | 123456789    | sky@gmail.com |  12 |       1 | 2025-06-18 01:38:11 | 2025-06-18 01:38:11 | profiles/9DvfzSWicW9bR7qxRITjBOqVNCtLstMDnLzrcuz9.png
```

> [!NOTE]
> *La imagen fue guardada correctamente, pero aún no está accesible desde el navegador.*

---

## **3. Problema: la imagen no se carga desde el navegador**

### **Intentamos acceder a:**

```bash
http://localhost:8000/storage/profiles/LhwMsbjjhJ5UqRx8vA0H02Qa3DLmvudvzar1BJ8d.png
```

### **Resultado:** *error 404 (no encontrado)*

---

## **4. Diagnóstico**

### **Revisamos la carpeta `public/`**

```bash
ls -lAh public/
```

**Salida esperada:**

```bash
total 28K
-rw-r--r-- 1 d4nitrix13 d4nitrix13  603 Apr 20 17:08 .htaccess
drwxr-xr-x 2 d4nitrix13 d4nitrix13 4.0K Apr 20 17:08 css
-rw-r--r-- 1 d4nitrix13 d4nitrix13    0 Apr 20 17:08 favicon.ico
drwxr-xr-x 2 d4nitrix13 d4nitrix13 4.0K Jun 17 23:43 img
-rw-r--r-- 1 d4nitrix13 d4nitrix13 1.7K Apr 20 17:08 index.php
drwxr-xr-x 2 d4nitrix13 d4nitrix13 4.0K Apr 20 17:08 js
-rw-r--r-- 1 d4nitrix13 d4nitrix13  199 Jun 17 23:43 mix-manifest.json
-rw-r--r-- 1 d4nitrix13 d4nitrix13   24 Apr 20 17:08 robots.txt
```

> [!WARNING]
> *Laravel **no publica automáticamente** el contenido de `storage/app/public`. Se necesita un enlace simbólico.*

---

## **5. Solución: Crear el enlace simbólico**

```bash
php artisan storage:link -v
```

**Salida:**

```bash
INFO  The [public/storage] link has been connected to [storage/app/public]
```

### **Verificación:**

```bash
ls -lAh public/
```

**Ahora veremos algo como:**

```bash
total 28K
-rw-r--r-- 1 d4nitrix13 d4nitrix13  603 Apr 20 17:08 .htaccess
drwxr-xr-x 2 d4nitrix13 d4nitrix13 4.0K Apr 20 17:08 css
-rw-r--r-- 1 d4nitrix13 d4nitrix13    0 Apr 20 17:08 favicon.ico
drwxr-xr-x 2 d4nitrix13 d4nitrix13 4.0K Jun 17 23:43 img
-rw-r--r-- 1 d4nitrix13 d4nitrix13 1.7K Apr 20 17:08 index.php
drwxr-xr-x 2 d4nitrix13 d4nitrix13 4.0K Apr 20 17:08 js
-rw-r--r-- 1 d4nitrix13 d4nitrix13  199 Jun 17 23:43 mix-manifest.json
-rw-r--r-- 1 d4nitrix13 d4nitrix13   24 Apr 20 17:08 robots.txt
lrwxrwxrwx 1 d4nitrix13 d4nitrix13   42 Jun 18 02:00 storage -> /App/ApplicationLaravel/storage/app/public
```

> [!NOTE]
> *Este enlace simbólico conecta `public/storage` con `storage/app/public`.*

---

## **6. Problema persistente: Laravel sigue guardando en `app/`**

*Por defecto, `store('profiles')` guarda en el disco definido en `.env`:*

```ini
FILESYSTEM_DISK=local
```

*Esto significa que los archivos van a `storage/app/profiles/`, **no accesible públicamente**.*

---

## **7. Solución final: usar disco `public`**

### **Modifica la línea de guardado así:**

```php
$path = $request->file(key: "profile_picture")->store(path: "profiles", options: "public");
```

- *`"public"` es el disco configurado en `config/filesystems.php`.*
- *Ahora se guarda en `storage/app/public/profiles/`.*

### **URL generada:**

```php
dd(Storage::url($path));
```

**Resultado:**

```bash
/storage/profiles/P5sTunivKbOYUxtOcJ3gft1KpxGJEvumMjtz7lfI.png
```

### **URL accesible desde el navegador:**

```bash
http://localhost:8000/storage/profiles/P5sTunivKbOYUxtOcJ3gft1KpxGJEvumMjtz7lfI.png
```

> [!NOTE]
> *¡Ahora la imagen es pública!*

---

## **8. Limpieza (opcional)**

*Borra las imágenes que fueron guardadas en la ubicación incorrecta:*

```bash
rm -r storage/app/profiles/
```

---

## **Estilizado, Visualización y Eliminación de Imágenes de Perfil en Laravel**

- **Objetivo**

*Estilizar y mostrar imágenes de perfil de manera circular en las vistas de Laravel, compilar el CSS para aplicar estilos actualizados, y eliminar el archivo de imagen del almacenamiento cuando se elimina un contacto.*

---

## **1. Mostrar la imagen de perfil en la lista de contactos**

### **Archivo:** `resources/views/contacts/index.blade.php`

```php
@extends('layouts.app')

@section('content')
  <div class="container">
    @forelse ($contacts as $contact)
      <div class="d-flex justify-content-between bg-dark mb-3 rounded px-4 py-2">
        <div>
          {{-- Application/resources/img/logo.png --}}
          <a href="{{ route('contacts.show', ['contact' => $contact->id]) }}">
            <img src="{{ Storage::url($contact->profile_picture) }}" class="profile-picture">
          </a>
        </div>

        <div class="d-flex align-items-center">
          <p class="me-2 mb-0">
            {{ $contact->name }}
          </p>

          <p class="me-2 mb-0 d-none d-md-block">
            <a href="mailto:{{ $contact->email }}">
              {{ $contact->email }}
            </a>
          </p>

          <p class="me-2 mb-0 d-none d-md-block">
            <a href="tel:{{ $contact->phone_number }}">
              {{ $contact->phone_number }}
            </a>
          </p>

          <a class="btn btn-secondary mb-0 me-2 p-1 px-2" href="{{ route('contacts.edit', $contact->id) }}">
            <x-icon icon="pencil" />
          </a>

          <form action="{{ route('contacts.destroy', ['contact' => $contact->id]) }}" method="POST">
            @csrf
            @method('DELETE')
            <button type="submit" class="btn btn-danger mb-0 me-2 p-1 px-2">
              <x-icon icon="trash" />
            </button>
          </form>

        </div>

      </div>
    @empty
      <div class="col-md-4 mx-auto">
        <div class="card card-body text-center">
          <p>No contacts saved yet</p>
          <a href="{{ route('contacts.create') }}">Add One!</a>
        </div>
      </div>
    @endforelse
  </div>
@endsection
```

> [!NOTE]
> *`Storage::url(...)` genera una URL pública accesible desde `/storage/...` para la imagen.*

---

## **2. Estilo CSS para imágenes circulares**

### **Archivo:** `resources/css/app.css`

- **Añadimos La Siguiente Clase**

```css
.profile-picture {
  border-radius: 50%;
  width: 4rem;
  height: 4rem;
}
```

- *`border-radius: 50%`: convierte la imagen en un círculo.*
- *`width/height`: define un tamaño fijo de 4rem (\~64px aprox).*

---

## **3. Compilar los cambios del CSS**

*Usa uno de los siguientes comandos:*

```bash
npm run dev
```

- *Compila el CSS una sola vez.*

```bash
npm run watch
```

- *Observa los archivos `.css`, `.js`, etc. y recompila automáticamente cada vez que se detecta un cambio.*

> [!TIP]
> *Si ya tienes `npm run watch` corriendo, **no necesitas ejecutar `npm run dev` otra vez**, los cambios se aplicarán automáticamente.*

---

## **4. Mostrar imagen en la vista principal (`home.blade.php`)**

### **Archivo:** `resources/views/home.blade.php`

```php
@extends('layouts.app')

@section('content')
  <div class="container pt-4 p-3">
    <div class="row">
      {{-- @if ($contacts->count() === 0)
    @endif --}}
      @forelse ($contacts as $contact)
        <div class="col-md-4 mb-3">
          <div class="card text-center">
            <div class="card-body">

              <div class="d-flex justify-content-center mb-2">
                <a href="{{ route('contacts.show', $contact->id) }}">
                  <img src="{{ Storage::url($contact->profile_picture) }}" class="profile-picture">
                </a>
              </div>

              <a class="text-decoration-none text-white" href={{ route('contacts.show', $contact->id) }}>
                <h3 class="card-title text-capitalize">{{ $contact->name }}</h3>
              </a>
              <p class="m-2">{{ $contact->phone_number }}</p>
              <a href="{{ route('contacts.edit', $contact->id) }}" class="btn btn-secondary mb-2">Edit Contact</a>
              <form action="{{ route('contacts.destroy', ['contact' => $contact->id]) }}" method="POST">
                @csrf
                @method('DELETE')
                <button type="submit" class="btn btn-danger mb-2">Delete Contact</button>
              </form>
            </div>
          </div>
        </div>
      @empty
        <div class="col-md-4 mx-auto">
          <div class="card card-body text-center">
            <p>No contacts saved yet</p>
            <a href="{{ route('contacts.create') }}">Add One!</a>
          </div>
        </div>
      @endforelse
    </div>
  </div>
@endsection
```

- *El `img` está envuelto en un enlace que redirige a la vista detallada del contacto.*

---

## **5. Mostrar imagen en la vista individual (`show.blade.php`)**

### **Archivo:** `resources/views/contacts/show.blade.php`

```php
@extends('layouts.app')

@section('content')
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">Contact Information</div>

          <div class="card-body">
            <div class="d-flex justify-content-center mb-2">
              <img src="{{ Storage::url($contact->profile_picture) }}" class="profile-picture">
            </div>

            <p>Name: {{ $contact->name }}</p>
            <p>Email:
              <a href="mailto:{{ $contact->email }}">
                {{ $contact->email }}
              </a>
            </p>
            <p>Age: {{ $contact->age }}</p>
            <p>Phone number:
              <a href="tel:{{ $contact->phone_number }}">
                {{ $contact->phone_number }}
              </a>
            </p>

            <p>Created At: {{ $contact->created_at }}</p>
            <p>Updated At:{{ $contact->updated_at }}</p>

            <div class="d-flex justify-content-center">
              <a href="{{ route('contacts.edit', $contact->id) }}" class="btn btn-secondary mb-2 me-2">Edit Contact</a>
              <form action="{{ route('contacts.destroy', ['contact' => $contact->id]) }}" method="POST">
                @csrf
                @method('DELETE')
                <button type="submit" class="btn btn-danger mb-2">Delete Contact</button>
              </form>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
@endsection
```

> [!NOTE]
> *Esto permite tanto visualizar como subir una nueva imagen en la misma vista.*

---

## **6. Eliminar la imagen del servidor al borrar un contacto**

### **Controlador:**

```php
public function destroy(Contact $contact)
{
    $this->authorize(ability: "delete", arguments: $contact);

    $path = Storage::url($contact["profile_picture"]);
    $realPath = str_replace('storage/', 'public/', $path);

    if (Storage::exists(path: $realPath)) {
        Storage::delete(paths: $realPath);
    }

    $contact->delete();

    return back()->with(key: "alert", value: [
        "message" => "Contact $contact->name deleted successfully",
        "type" => "success"
    ]);
}
```

### **Explicación:**

1. *`Storage::url(...)` genera la URL pública: `/storage/perfil123.png`*
2. *`str_replace('storage/', 'public/', $path)` transforma esa URL en una **ruta válida del disco**, como `public/perfil123.png`, que Laravel necesita para eliminar el archivo físico.*
3. *`Storage::exists(...)`: verifica si el archivo realmente existe.*
4. *`Storage::delete(...)`: elimina la imagen del servidor.*
5. *`$contact->delete()`: elimina el registro del contacto de la base de datos.*

> [!WARNING]
> *Este código asume que usaste el disco `public` al guardar la imagen con `store('profiles', 'public')`.*

---

## **Depuración de Errores en Consultas SQL en Laravel**

- **Objetivo**

*Entender cómo Laravel maneja los errores al ejecutar consultas (queries) y cómo podemos utilizar esa información para depurar fácilmente en desarrollo.*

---

## **Consejo de depuración**

*Cuando realizas una consulta en Laravel (Eloquent o Query Builder) que genera un error, **Laravel muestra automáticamente información útil en el navegador** si estás en **modo desarrollo (`APP_DEBUG=true`)**.*

> [!TIP]
> **Esta función es extremadamente útil para identificar rápidamente errores como:**

- *Campos inexistentes en la tabla*
- *Problemas de sintaxis SQL*
- *Tipos de datos incompatibles*
- *Relación mal definida*
- *Problemas de conexión a base de datos*

---

### **Detalle que muestra Laravel:**

- *Query SQL fallida*
- *Parámetros pasados*
- *Archivo y línea donde ocurrió*
- *Stack trace completo*

---

## **Requisitos para que Laravel muestre esta información**

1. *Tener el entorno de desarrollo activo en `.env`:*

    ```env
    APP_ENV=local
    APP_DEBUG=true
    ```

2. *No haber capturado el error con un `try-catch` que lo silencie.*
3. *No estar en producción (`APP_ENV=production`), ya que en ese caso Laravel mostrará solo un error genérico.*

---

## **¿Cómo registrar estos errores de forma persistente?**

**Laravel también los guarda en:**

```bash
storage/logs/laravel.log
```

> [!NOTE]
> *Puedes revisar este archivo con `tail -f storage/logs/laravel.log` en consola para ver errores en tiempo real.*
