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

        return redirect()->route(route: "contacts.create")->with(key: "alert", value: [
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
