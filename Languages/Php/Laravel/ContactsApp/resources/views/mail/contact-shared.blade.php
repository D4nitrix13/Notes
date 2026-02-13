<x-mail::message>
  # New contact was shared with you

  User: {{ $fromUser }} shared contact {{ $sharedContact }} with you.

  <x-mail::button :url="route('contacts-shares.index')">
    Button Text
  </x-mail::button>

  Thanks,<br>
  {{ config('app.name') }}
</x-mail::message>
