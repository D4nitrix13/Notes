<?php

namespace Database\Seeders;

use App\Models\User;
use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class DatabaseSeeder extends Seeder
{
    /**
     * Seed the application's database.
     *
     * @return void
     */
    public function run()
    {
        // User::factory(count: 10)->create();
        
        // Crea un usuario llamado "Testing" con 30 contactos
        $testUser = User::factory()->hasContacts(30)->createOne([
            "name" => "Testing",
            "email" => "test@test.com",
        ]);

        // Crea 3 usuarios, cada uno con 5 contacto
        $users = User::factory(count: 3)->hasContacts(5)->create()->each(
            fn($user) => $user->contacts->first()->sharedWithUsers()->attach($testUser->id)
        );

        // Comparte el primer contacto del testUser con los 3 usuarios anteriores
        $testUser->contacts->first()->sharedWithUsers()->attach($users->pluck("id"));

        // \App\Models\User::factory()->create([
        //     'name' => 'Test User',
        //     'email' => 'test@example.com',
        // ]);
    }
}
