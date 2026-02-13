<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Cache;

class HomeController extends Controller
{
    /**
     * Create a new controller instance.
     *
     * @return void
     */
    public function __construct()
    {
        $this->middleware('auth');
    }

    /**
     * Show the application dashboard.
     *
     * @return \Illuminate\Contracts\Support\Renderable
     */
    public function index()
    {
        $contacts = Cache::remember(
            key: auth()->id(),
            ttl: now()->addMinutes(value: 30),
            callback: fn() => auth()->user()->contacts()->latest()->take(9)->get()
        );

        return view(view: 'home', data: compact("contacts"));
        // return view(view: 'home', data: [
        //     "contacts" => auth()->user()->contacts()->latest()->take(9)->get()
        // ]);
    }
}
