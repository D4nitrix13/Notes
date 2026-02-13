<?php

namespace Tests\Unit;

use App\Models\Contact;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ContactControllerTest extends TestCase
{
    use RefreshDatabase;
    /**
     * A basic test example.
     *
     * @return void
     */
    public function test_authenticated_user_can_store_valid_contact_data()
    {
        $this->withExceptionHandling();
        $user = User::factory()->create();
        $contact = Contact::factory()->makeOne(
            attributes: [
                "phone_number" => "123456789",
                "user_id" => $user->id
            ]
        );

        // Authentication
        $response = $this->actingAs(user: $user)->post(
            uri: route(name: "contacts.store"),
            data: $contact->getAttributes(),
            headers: []
        );

        $response->assertRedirect(
            uri: route(name: "home")
        );

        $this->assertDatabaseCount(table: "contacts", count: 1);
        $this->assertDatabaseHas(
            table: "contacts",
            data: [
                "user_id" => $user->id,
                "name" => $contact->name,
                "email" => $contact->email,
                "age" => $contact->age,
                "phone_number" => $contact->phone_number
            ]
        );
    }

    public function test_store_contact_fails_when_required_fields_are_missing_or_invalid()
    {
        $this->withExceptionHandling();
        $user = User::factory()->create();
        $contact = Contact::factory()->makeOne(
            attributes: [
                "phone_number" => "Wrong Phone Number",
                "email" => "Wrong Email",
                "name" => null,
            ]
        );

        // Authentication
        $response = $this->actingAs(user: $user)->post(
            uri: route(name: "contacts.store"),
            data: $contact->getAttributes(),
            headers: []
        );

        $response->assertSessionHasErrors(keys: [
            "phone_number",
            "email",
            "name"
        ]);

        $this->assertDatabaseCount(table: "contacts", count: 0);
    }

    /**
     * @depends test_store_contact_fails_when_required_fields_are_missing_or_invalid
     *
     */
    public function test_only_contact_owner_can_update_or_delete_contact()
    {
        $this->withExceptionHandling();
        [$owner, $notOwner] = User::factory(count: 2)->create();
        $contact = Contact::factory()->createOne(
            attributes: [
                "phone_number" => "123456789",
                "user_id" => $owner->id
            ]
        );

        // Authentication
        $response = $this->actingAs(user: $notOwner)->put(
            uri: route(name: "contacts.update", parameters: $contact->id),
            data: $contact->getAttributes(),
            headers: []
        );

        // $response->assertStatus(status: 403);
        $response->assertForbidden();

        $response = $this->actingAs(user: $notOwner)->delete(
            uri: route(name: "contacts.destroy", parameters: $contact->id),
            data: $contact->getAttributes(),
            headers: []
        );

        // $response->assertStatus(status: 403);
        $response->assertForbidden();
    }
}
