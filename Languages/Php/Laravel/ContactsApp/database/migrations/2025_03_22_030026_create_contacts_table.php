<?php

use App\Models\User;
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
        Schema::create('contacts', function (Blueprint $table) {
            $table->id();
            $table->string(column: "name");
            $table->string(column: "phone_number");
            $table->string(column: "email");

            // Definición de un campo de tipo tinyInteger sin signo (edad)
            // Es equivalente a: $table->tinyInteger("age", false, true);
            $table->tinyInteger("age", unsigned: true); // Disponible en PHP 8 en adelante
            // Explicación detallada sobre tinyInteger:
            // - Un `tinyInteger` almacena valores enteros pequeños (-128 a 127 o 0 a 255 si es unsigned)
            // - Ocupa solo 1 byte de espacio en la base de datos, optimizando almacenamiento y rendimiento
            // - Se diferencia de `integer` que ocupa 4 bytes y permite un rango mucho mayor
            // - Se usa para valores pequeños como edades, contadores de intentos, estatus de un campo, etc.

            // $table->foreign('user_id')->references('id')->on('users');
            $table->foreignIdFor(model: User::class);

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     *
     * @return void
     */
    public function down()
    {
        Schema::dropIfExists('contacts');
    }
};
