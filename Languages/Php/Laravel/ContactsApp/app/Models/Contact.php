<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;
use Illuminate\Database\Eloquent\Relations\BelongsToMany;

/**
 * Contact Model
 *
 * @property string $name
 * @property integer $phone_number
 * @property string $email
 * @property interger $age
 */
class Contact extends Model
{
    use HasFactory;

    // En lugar de personalizar la tabla y la clave primaria, seguimos la convención de Laravel.
    // Laravel asume por defecto que la tabla se llama 'contacts' (plural y en minúsculas) y
    // que la clave primaria es 'id'.
    // protected $table = 'my_custom_name_table';
    // protected $primaryKey = 'contact_id';

    protected $fillable = [
        "name",
        "phone_number",
        "age",
        "email",
        "user_id",
        "profile_picture"
    ];

    public function user()
    {
        return $this->belongsTo(related: User::class);
    }

    function sharedWithUsers(): BelongsToMany
    {
        return $this->belongsToMany(related: User::class, table: "contact_shares");
    }
}
