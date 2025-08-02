<?php

namespace App\Http\Controllers;

use Illuminate\Contracts\View\View;
use Illuminate\Http\Request;

class ApiTokenController extends Controller
{
    public function create(): View
    {
        return view(view: "api-tokens.create");
    }

    public function store(Request $request)
    {
        ["name" => $name] =  $request->validate(rules: ["name" => "required|string"]);

        $token = $request->user()->createToken($name);

        // return ['token' => $token->plainTextToken];
        return view(
            view: "api-tokens.show",
            data: compact("token")
        );
    }
}
