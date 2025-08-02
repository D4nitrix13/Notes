<?php

namespace App\Http\Controllers;

use App\Http\Requests\StoreContactRequest;
use App\Models\Contact;
use Illuminate\Http\Request;
use Illuminate\Http\Response as HttpResponse;
use Illuminate\Support\Facades\Cache;
use Illuminate\Support\Facades\Gate;
use Illuminate\Support\Facades\Response;
use Illuminate\Support\Facades\Storage;

class ContactController extends Controller
{
    // protected $rules = [
    //     "name" => "required",
    //     "phone_number" => "required|digits:9",
    //     "email" => "required|email",
    //     "age" => "required|numeric|min:1|max:255"
    // ];

    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        // dd(Contact::all());
        // return view(view: "contacts.index", data: ["contacts" => Contact::all()]);

        // $contacts = Contact::where(
        //     "user_id",
        //     "=",
        //     auth()->id()
        // )->get();

        // $contacts = Contact::where(
        //     "user_id",
        //     auth()->id()
        // )->get();

        // $contacts = Contact::query()->where(
        //     "user_id",
        //     "=",
        //     auth()->id()
        // )->get();

        // $contacts = auth()->user()->contacts()->get();
        // $contacts = auth()->user()->contacts;

        $contacts = auth()
            ->user()
            ->contacts()
            ->orderBy('name', 'desc')
            ->paginate(6);

        return view(view: "contacts.index", data: compact(var_name: "contacts"));
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        // return Response::view("contact");
        return view(view: "contacts.create");
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(StoreContactRequest $request)
    {
        // * Example [1]
        // if (
        //     is_null($request->get("name"))
        // ) return Response::redirectTo("/contacts/create")->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [2]
        // if (
        //     is_null($request->get("name"))
        // ) return redirect("/contacts/create")->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [3]
        // if (
        //     is_null($request->get("name"))
        // ) return redirect(route("contacts.create"))->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [4]
        // if (
        //     is_null($request->get("name"))
        // ) return redirect()->route("contacts.create")->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [5]
        // if (
        //     is_null($request->get("name"))
        // ) return redirect()->back()->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [6]
        // if (
        //     is_null($request->get("name"))
        // ) return back()->withErrors([
        //     "name" => "This field is required"
        // ]);

        // * Example [*]
        // // No Recomendable
        // Contact::create(
        //     $request->all()
        // );

        // * Example Validation [1]
        // $request->validate([
        //     "name" => "required",
        //     "phone_number" => ["required", "digits:9"],
        //     "email" => ["required",  "email"],
        //     "age" => ["required", "numeric", "min:1", "max:255"]
        // ]);

        // $data = $request->validate($this->rules);


        // $data["user_id"] = auth()->id();
        // Contact::create($data);

        $data = $request->validated();
        if ($request->hasFile(key: "profile_picture")) {
            $path = $request->file(key: "profile_picture")->store(path: "profiles", options: "public");
            $data["profile_picture"] = $path;
        }

        // dd(Storage::url(path: $path));
        $contact = auth()->user()->contacts()->create($data);

        Cache::forget(key: auth()->id());
        // return response("Contact Created");

        // session()->flash(key: "alert", value: [
        //     "message" => "Contact $contact->name saved successfully",
        //     "type" => "info"
        // ]);

        return redirect(to: "home")->with(key: "alert", value: [
            "message" => "Contact $contact->name saved successfully",
            "type" => "success"
        ]);
        // return redirect()->route(route: "home");
    }

    /**
     * Display the specified resource.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function show(Contact $contact)
    {
        // if ($contact->user_id !== auth()->id()) abort(code: 403);
        // if ($contact->user_id !== auth()->id()) abort(code: HttpResponse::HTTP_FORBIDDEN);
        // abort_if(boolean: $contact->user_id !== auth()->id(), code: HttpResponse::HTTP_FORBIDDEN);

        // if (!Gate::allows('show-contact', $contact)) {
        //     abort(403);
        // }

        // Gate::authorize(ability: "show-contact", arguments: $contact);

        $this->authorize(ability: "view", arguments: $contact);

        return view(view: "contacts.show", data: compact("contact"));
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function edit(Contact $contact, Request $request)
    {
        // dd($contact, $request);
        // public function edit(int $contactId)
        // dd(request()->route(param: "contact"));
        // dd($contactId);
        // $contact = Contact::findOrFail($contactId);

        $this->authorize(ability: "update", arguments: $contact);
        return view(view: "contacts.edit", data: compact(var_name: "contact"));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function update(StoreContactRequest $request, Contact $contact)
    {
        // dd($request["contact"]);
        $this->authorize(ability: "update", arguments: $contact);

        $data = $request->validated();
        if ($request->hasFile(key: "profile_picture")) {
            $path = $request->file(key: "profile_picture")->store(path: "profiles", options: "public");
            $data["profile_picture"] = $path;
        }

        // $data = $request->validate($this->rules);

        $contact->update($data);
        
        Cache::forget(key: auth()->id());

        // return redirect()->route(route: "home");
        return redirect(to: "home")->with(key: "alert", value: [
            "message" => "Contact $contact->name updated successfully",
            "type" => "success"
        ]);
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  \App\Models\Contact  $contact
     * @return \Illuminate\Http\Response
     */
    public function destroy(Contact $contact)
    {
        $this->authorize(ability: "delete", arguments: $contact);
        // dd(Storage::url(path: $contact["profile_picture"]));
        $path = Storage::url($contact["profile_picture"]);
        $realPath = str_replace('storage/', 'public/', $path);
        if ($realPath !== "/public/profiles/default.png" and Storage::exists(path: $realPath)) {
            Storage::delete(paths: $realPath);
        }

        $contact->delete();
        Cache::forget(key: auth()->id());

        // El método destroy() se utiliza para eliminar uno o varios registros a la vez.
        // Por ejemplo: Contact::destroy([1, 2, 3]) elimina varios contactos por sus IDs.
        // $contact->destroy();
        // return redirect(to: "home");

        // return redirect(to: "home")->with(key: "alert", value: [
        //     "message" => "Contact $contact->name deleted successfully",
        //     "type" => "success"
        // ]);

        return back()->with(key: "alert", value: [
            "message" => "Contact $contact->name deleted successfully",
            "type" => "success"
        ]);
    }
}
