<?php

namespace App\Http\Requests;

use App\Models\Contact;
use Illuminate\Foundation\Http\FormRequest;
use Illuminate\Validation\Rule;

class StoreContactRequest extends FormRequest
{
    /**
     * Determine if the user is authorized to make this request.
     *
     * @return bool
     */
    public function authorize(): bool
    {
        // $contact = Contact::find(
        //     $this->route('contact')
        // );
        // return $contact && $this->user()->can('update', $contact);
        return true;
    }

    /**
     * Get the validation rules that apply to the request.
     *
     * @return array<string, mixed>
     */
    public function rules()
    {
        return [
            "name" => "required",
            "phone_number" => "required|digits:9",
            "email" => [
                "required",
                "email",
                Rule::unique(table: "contacts", column: "email")
                    ->where(column: "user_id", value: auth()->id())
                    ->ignore(id: request()->route(param: "contact"))
            ],
            "age" => "required|numeric|min:1|max:255",
            'profile_picture' => 'image|mimes:jpeg,png,jpg|max:2048',
        ];
    }

    public function messages()
    {
        return [
            "email.unique" => "You already have a contact with this email"
        ];
    }
}
