<?php

use App\Http\Controllers\ApiTokenController;
use App\Http\Controllers\ContactController;
use App\Http\Controllers\ContactShareController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\StripeController;
use App\Models\Contact;
use Illuminate\Http\Request;
use Illuminate\Http\Response as HttpResponse;
use Illuminate\Support\Facades\Auth;
use Illuminate\Support\Facades\DB;
use Illuminate\Support\Facades\Response;
use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// Route::get(
//     uri: "/contacts/create",
//     action: [ContactController::class, "create"]
// );

// Route::get(
//     uri: "/contacts/{contact:email}/edit",
//     action: [ContactController::class, "edit"]
// )->name(name: "contacts.edit");


Route::get('/billing-portal', [StripeController::class, "billingPortal"])->name(name: "billing-portal");

Route::get('/subscription-checkout', [StripeController::class, "subscriptionCheckout"])->name(name: "subscription-checkout");

Route::get(uri: "free-trial-end", action: [StripeController::class, "freeTrialEnd"])->name("free-trial-end");

Route::get(uri: '/', action: fn() => auth()->check() ? redirect()->route(route: "home") : view(view: "welcome"));

Auth::routes();

Route::middleware(["auth", "subscription"])->group(callback: function () {
        Route::get(uri: '/home', action: [HomeController::class, 'index'])->name('home');
        Route::resource(name: "contacts", controller: ContactController::class);
        Route::resource(name: "contacts-shares", controller: ContactShareController::class)
                ->except(methods: ["show", "edit", "update"]);
        Route::resource(name: "api-tokens", controller: ApiTokenController::class)
                ->only(methods: ["create", "store"]);
});

// Route::middleware(["auth", "subscription"])->resource(name: "contacts", controller: ContactController::class);

// Route::get(
//     uri: "/contacts/create",
//     action: [ContactController::class, "create"]
// )->name(name: "contacts.create");


// Route::get(
//     uri: "/contacts/{contact}/edit",
//     action: [ContactController::class, "edit"]
// )->name(name: "contacts.edit");

// Route::put(
//     uri: "/contacts/{contact}",
//     action: [ContactController::class, "update"]
// )->name(name: "contacts.update");


// Route::post(
//     uri: "/contacts",
//     action: [ContactController::class, "store"]
// )->name(name: "contacts.store");

// Route::delete(
//     uri: "/contacts/{contact:id}/",
//     action: [ContactController::class, "destroy"]
// )->name(name: "contacts.destroy");

// Route::get(
//     uri: "/contacts/{contact:id}/",
//     action: [ContactController::class, "show"]
// )->name(name: "contacts.show");

// Route::get(
//     uri: "/contacts/",
//     action: [ContactController::class, "index"]
// )->name(name: "contacts.index");


// * Route Example [1]
// Route::get(
//     uri: "/contact",
//     action: fn() => Response::view("contact")
// );

// * Route Example [2]
// Route::post(
//     uri: "/contact",
//     action: function (Request $request) {
//         $data = $request->all();

        // // $contact = new Contact();
        // // $contact->name = $data["name"];
        // // $contact->phone_number = $data["phone_number"];
        // // $contact->save();

//         Contact::create(
//             $data
//         );

//         return Response::json(
//             ["message" => "Contact Stored"],
//             200
//         );
//     }
// );

// * Route Example [3]
// Route::post(
//     uri: "/contact",
//     action: function (Request $request) {
//         $data = $request->all();
//         DB::statement(
//             "INSERT INTO contacts (name, phone_number) VALUES (?, ?)",
//             [
//                 $data["name"],
//                 $data["phone_number"]
//             ]
//         );

//         return Response::json(
//             ["message" => "Contact Stored"],
//             200
//         );
//     }
// );

// * Route Example [4]
// Route::post(
//     uri: "/contact",
//     action: function (Request $request) {
//         return Response::json(
//             ["message" => "Hello My Name Is Daniel"]
//         )->setStatusCode(200);
//     }
// );

// * Route Example [5]
// Route::get(
//     uri: "/change-password",
//     action: fn() => Response::view("change-password")
// );

// * Route Example [6]
// Route::post(
//     uri: "/change-password",
//     action: function () {
//         if (Auth::check()) return new HttpResponse("Authenticated");
//         else return (new HttpResponse("Not Authenticated"))->setStatusCode(401);
//     }
// );

// * Route Example [7]
// Route::post(
//     uri: "/change-password",
//     action: function (Request $request) {
//         if (auth()->check()) return response(
//             "Password Changed to {$request->get('password')}"
//         );
//         else return new response("Not Password Changed", 401);
//     }
// );
