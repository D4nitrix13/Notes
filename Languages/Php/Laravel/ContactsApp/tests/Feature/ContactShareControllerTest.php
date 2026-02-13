<?php

namespace Tests\Feature;

use App\Models\Contact;
use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Tests\TestCase;

class ContactShareControllerTest extends TestCase
{
    use RefreshDatabase;

    /**
     * @group contact-share
     */
    public function test_authenticated_user_can_share_a_contact_with_another_user()
    {
        $this->withExceptionHandling();
        [$user1, $user2] = User::factory(count: 2)->create();
        $contact = Contact::factory()->createOne(
            attributes: [
                "phone_number" => "123456789",
                "user_id" => $user1->id
            ]
        );

        $response = $this
            ->actingAs(user: $user1)
            ->post(
                uri: route(name: "contacts-shares.store"),
                data: [
                    "contact_email" => $contact->email,
                    "user_email" => $user2->email
                ]
            );

        $this->assertDatabaseCount(table: "contact_shares", count: 1);

        $sharedContacts = $user2->sharedContacts()->first();
        $this->assertTrue(condition: $contact->is(model: $sharedContacts));
    }

    /**
     * @group contact-share
     */
    public function test_user_can_view_a_contact_shared_with_them()
    {
        $this->withExceptionHandling();
        [$user1, $user2] = User::factory(count: 2)->hasContacts(5)->create();

        $contact = $user1->contacts()->first();
        $contact->sharedWithUsers()->attach($user2->id);

        $response = $this->actingAs(user: $user2)
            ->get(
                uri: route(
                    name: "contacts.show",
                    parameters: $contact->id
                )
            );
        $response->assertOk();
    }

    /**
     * @group contact-share
     * @depends test_authenticated_user_can_share_a_contact_with_another_user
     */
    public function test_user_cannot_share_a_contact_that_is_already_shared_with_the_same_user()
    {
        $this->withExceptionHandling();
        [$user1, $user2] = User::factory(count: 2)->hasContacts(5)->create();

        $contact = $user1->contacts()->first();
        $contact->sharedWithUsers()->attach($user2->id);

        $response = $this->actingAs(user: $user1)
            ->post(
                uri: route(
                    name: "contacts-shares.store",
                    parameters: $contact->id
                ),
                data: [
                    "contact_email" => $contact->email,
                    "user_email" => $user2->email
                ]
            );
        $response->assertSessionHasErrors(keys: [
            "contact_email"
        ]);

        $this->assertDatabaseCount(table: "contact_shares", count: 1);
    }
}
