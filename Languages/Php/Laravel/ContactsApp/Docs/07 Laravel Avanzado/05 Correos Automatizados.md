<!-- Autor: Daniel Benjamin Perez Morales -->
<!-- GitHub: https://github.com/D4nitrix13 -->
<!-- Gitlab: https://gitlab.com/D4nitrix13 -->
<!-- Correo electrónico: danielperezdev@proton.me -->

# **Laravel - Automated Emails (Mailables)**

## **Recursos oficiales**

* **Mailtrap Inbox:** *[https://mailtrap.io/inboxes](https://mailtrap.io/inboxes "https://mailtrap.io/inboxes")*
* **Laravel Mail Docs:**

  * *[Overview](https://laravel.com/docs/12.x/mail "https://laravel.com/docs/12.x/mail")*
  * *[Generating Mailables](https://laravel.com/docs/12.x/mail#generating-mailables "https://laravel.com/docs/12.x/mail#generating-mailables")*
  * *[Sending Mail](https://laravel.com/docs/12.x/mail#sending-mail "https://laravel.com/docs/12.x/mail#sending-mail")*

---

## **Configuración inicial con Mailtrap**

*Para entornos de desarrollo, Laravel puede enviar correos a través de [Mailtrap](https://mailtrap.io "https://mailtrap.io"), que simula el envío real sin mandar mensajes a usuarios verdaderos.*

*Una vez registrado y creada una inbox, selecciona la opción **Laravel 9+** en Mailtrap y copia las siguientes variables en tu archivo `.env`:*

### **Configuración de Mailtrap SMTP para Laravel 9+ (En Desarrollo)**

> [!NOTE]
> *Mailtrap te permite **probar el envío de correos en Laravel** sin enviar mensajes reales. Esto es muy útil durante el desarrollo de aplicaciones.*

---

### **Dónde obtener los tokens y credenciales SMTP?**

1. *Ve al [**dashboard de Mailtrap**](https://mailtrap.io "https://mailtrap.io")*
2. *En el menú lateral, haz clic en **Sandbox***
3. *Selecciona tu inbox llamado **My Sandbox***

    *![Sandbox Seleccionado](/Docs/Images/Sandbox%20Seleccionado.png "/Docs/Images/Sandbox%20Seleccionado.png")*

4. *Ve a la pestaña **Integration***
5. *En el área de **Code Samples**, selecciona **PHP: Laravel 9+***

*![Credenciales SMTP y Ejemplo Laravel](/Docs/Images/Credenciales%20SMTP%20y%20Ejemplo%20Laravel.png "/Docs/Images/Credenciales%20SMTP%20y%20Ejemplo%20Laravel.png")*

```env
MAIL_MAILER=smtp
MAIL_HOST=sandbox.smtp.mailtrap.io
MAIL_PORT=2525
MAIL_USERNAME=aed07c8ea4fa81
MAIL_PASSWORD=c486dada69cb3f
MAIL_ENCRYPTION=tls
MAIL_FROM_ADDRESS=no-reply@example.com
MAIL_FROM_NAME="${APP_NAME}"
```

### **Explicación de cada variable**

* *`MAIL_MAILER=smtp`: Usa el protocolo SMTP para enviar correos.*
* *`MAIL_HOST`: Servidor SMTP proporcionado por Mailtrap.*
* *`MAIL_PORT=2525`: Puerto SMTP alternativo compatible con firewalls.*
* *`MAIL_USERNAME / MAIL_PASSWORD`: Credenciales únicas generadas por Mailtrap.*
* *`MAIL_ENCRYPTION=tls`: Encriptación segura para el canal de envío.*
* *`MAIL_FROM_ADDRESS`: Email del remitente.*
* *`MAIL_FROM_NAME`: Nombre del remitente, tomado del nombre de la aplicación (`APP_NAME`).*

---

## **Generar una clase Mailable**

**Usamos el comando Artisan para generar una clase de email (Mailable):**

```bash
php artisan make:mail ContactShared -m
```

* **Output**

```bash
INFO  Mailable [app/Mail/ContactShared.php] created successfully.  
```

### **Detalle del comando**

| **Parte**             | **Descripción**                                                         |
| --------------------- | ----------------------------------------------------------------------- |
| *`make:mail`*         | *Comando para generar una clase de correo*                              |
| *`ContactShared`*     | *Nombre de la clase que se creará en `app/Mail/ContactShared.php`*      |
| *`-m` o `--markdown`* | *Crea automáticamente una plantilla Markdown en `resources/views/mail`* |

#### **Otras opciones útiles de `make:mail`**

```bash
Description:
  Create a new email class

Usage:
  make:mail [options] [--] <name>

Arguments:
  name                       The name of the mailable

Options:
  -f, --force                Create the class even if the mailable already exists
  -m, --markdown[=MARKDOWN]  Create a new Markdown template for the mailable [default: false]
      --test                 Generate an accompanying PHPUnit test for the Mailable
      --pest                 Generate an accompanying Pest test for the Mailable
  -h, --help                 Display help for the given command. When no command is given display help for the list command
  -q, --quiet                Do not output any message
  -V, --version              Display this application version
      --ansi|--no-ansi       Force (or disable --no-ansi) ANSI output
  -n, --no-interaction       Do not ask any interactive question
      --env[=ENV]            The environment the command should run under
  -v|vv|vvv, --verbose       Increase the verbosity of messages: 1 for normal output, 2 for more verbose output and 3 for debug
```

| **Opción**          | **Descripción**                                                         |
| ------------------- | ----------------------------------------------------------------------- |
| *`--force`*         | *Sobrescribe si la clase ya existe*                                     |
| *`--markdown=NAME`* | *Especifica el nombre del archivo blade para la plantilla*              |
| *`--test`*          | *Genera automáticamente una prueba unitaria para el Mailable (PHPUnit)* |
| *`--pest`*          | *Genera prueba con Pest en vez de PHPUnit*                              |
| *`-v / -vv / -vvv`* | *Muestra más detalles del proceso*                                      |

---

## **Estructura del Mailable**

### **`resources/views/mail/contact-shared.blade.php`**

```php
<x-mail::message>
  # New contact was shared with you

  User: {{ $fromUser }} shared contact {{ $sharedContact }} with you.

  <x-mail::button :url="route('contacts-shares.index')">
    View Contacts
  </x-mail::button>

  Thanks,<br>
  {{ config('app.name') }}
</x-mail::message>
```

### **Explicación de la plantilla**

* *`<x-mail::message>`: Componente base para correos Markdown.*
* *`{{ $fromUser }}` / `{{ $sharedContact }}`: Variables recibidas desde el Mailable.*
* *`<x-mail::button :url="route('contacts-shares.index')">`:*

  * *`:url=` pasa una expresión PHP (no uses `{{ }}` aquí).*
  * *`route('contacts-shares.index')` genera la URL de la ruta `contacts-shares.index`.*
* *`{{ config('app.name') }}`: Muestra el nombre de la app desde `.env`.*

---

## **Clase ContactShared (app/Mail/ContactShared.php)**

```php
<?php

namespace App\Mail;

use Illuminate\Bus\Queueable;
use Illuminate\Contracts\Queue\ShouldQueue;
use Illuminate\Mail\Mailable;
use Illuminate\Mail\Mailables\Content;
use Illuminate\Mail\Mailables\Envelope;
use Illuminate\Queue\SerializesModels;

class ContactShared extends Mailable
{
    use Queueable, SerializesModels;

    /**
     * Create a new message instance.
     *
     * @return void
     */
    public function __construct(public string $fromUser, public string $sharedContact)
    {
        $this->fromUser = $fromUser;
        $this->sharedContact = $sharedContact;
    }

    /**
     * Get the message envelope.
     *
     * @return \Illuminate\Mail\Mailables\Envelope
     */
    public function envelope()
    {
        return new Envelope(
            subject: 'Contact Shared',
        );
    }

    /**
     * Get the message content definition.
     *
     * @return \Illuminate\Mail\Mailables\Content
     */
    public function content()
    {
        return new Content(
            markdown: 'mail.contact-shared',
        );
    }

    /**
     * Get the attachments for the message.
     *
     * @return array
     */
    public function attachments()
    {
        return [];
    }
}
```

### **Explicación clave**

* *`__construct()`: Acepta parámetros para usarlos en la vista (Blade).*
* *`Envelope`: Define metadatos del correo, como el asunto (`subject`).*
* *`Content`: Indica la plantilla Markdown que se usará.*
* *`attachments()`: Puedes retornar archivos para adjuntar. Aquí está vacío.*

---

## **Enviar el correo**

**Desde tu controlador, puedes enviar el correo con:**

```php
Mail::to(users: $user)->send(mailable: new ContactShared(fromUser: auth()->user()->email, sharedContact: $contact->email));
```

* **Code**

```php
<?php

namespace App\Http\Controllers;

use App\Mail\ContactShared;
use App\Models\Contact;
use App\Models\User;
use Illuminate\Contracts\View\View;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Mail;
use Illuminate\Validation\Rule;
use Symfony\Component\HttpFoundation\Response;

class ContactShareController extends Controller
{
    public function index(): View
    {
        // Contactos que otros usuarios me han compartido
        $contactsSharedWithMe = auth()->user()->sharedContacts()->with("user")->get();

        // Contactos míos que compartí con otros usuarios
        $myContactsSharedWithOthers = auth()
            ->user()
            ->contacts()
            ->with(['sharedWithUsers' => function ($query) {
                $query->withPivot('id');
            }])
            ->get()
            ->filter(fn($contact) => $contact->sharedWithUsers->isNotEmpty());


        return view(view: "contacts-shares.index", data: compact("contactsSharedWithMe", "myContactsSharedWithOthers"));
    }

    public function create(): View
    {
        return view(view: "contacts-shares.create");
    }

    public function store(Request $request): string
    {
        $data = $request->validate([
            "user_email" => "exists:users,email|not_in:{$request->user()->email}",
            "contact_email" => Rule::exists(table: "contacts", column: "email")
                ->where(column: "user_id", value: auth()->id())
        ], [
            "user_email.not_in" => "You can't share a contact with yourself",
            "contact_email.exists" => "This contact was not found in your contact list"
        ]);

        $user = User::where("email", $data["user_email"])->first(["id", "email"]);
        $contact = Contact::where("email", $data["contact_email"])->first(["id", "email"]);

        $shareExists = $contact->sharedWithUsers()->wherePivot("user_id", $user->id)->first();
        if ($shareExists) {
            return back()->withInput(input: $request->all)->withErrors([
                "contact_email" => "This contact was already shared with user $user->email"
            ]);
        }
        $contact->sharedWithUsers()->attach([$user->id]);

        Mail::to(users: $user)->send(mailable: new ContactShared(fromUser: auth()->user()->email, sharedContact: $contact->email));

        return redirect()->route(route: "home")->with(key: "alert", value: [
            "message" => "Contact $contact->email shared with $user->email successfully",
            "type" => "success"
        ]);
        // dd($user, $contact);
    }

    function destroy(int $id)
    {
        // $contact = auth()->user()->contacts()->with(
        //     [
        //         "sharedWithUsers" => fn($q) => $q->where("contacts_shared.id", $contactShare)
        //     ]
        // )->firstOrFail();

        // $contact = auth()->user()->contacts()->with(
        //     [
        //         "sharedWithUsers" => fn($q) => $q->where("contact_shares.id", $id)
        //     ]
        // )->get()->firstWhere(fn ($contact) => $contact->sharedWithUsers->isNotEmpty());

        // dd($contact);

        $contactShare = DB::selectOne(query: "SELECT * FROM contact_shares WHERE id = ?", bindings: [$id]);
        $contact = Contact::findOrFail($contactShare->contact_id);
        abort_if(boolean: is_null(value: $contact->user_id !== auth()->id()), code: Response::HTTP_FORBIDDEN);

        $contact->sharedWithUsers()->detach($contactShare->user_id);

        return redirect()->route(route: "contacts-shares.index")->with(key: "alert", value: [
            "message" => "Contact $contact->email unshared",
            "type" => "success"
        ]);

        // abort_if(boolean: is_null(value: $contact), code: Response::HTTP_NOT_FOUND); // Response::HTTP_NOT_FOUND -> 404

    }
}
```
