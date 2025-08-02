<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class StripeController extends Controller
{
    public function subscriptionCheckout()
    {
        return auth()->user()
            ->newSubscription('default', config(key: "stripe.price_id"))
            ->checkout();
    }

    public function billingPortal()
    {
        return auth()
            ->user()
            ->redirectToBillingPortal();
    }

    public function freeTrialEnd()
    {
        return view(view: "free-trial-end");
    }
}
