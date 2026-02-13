@extends('layouts.app')

@section('content')
  <div class="container">
    <h1 class="text-center"> Contacts Shared with me </h1>
    @forelse ($contactsSharedWithMe as $contact)
      <div class="d-flex justify-content-between bg-dark mb-3 rounded px-4 py-2">
        <div>
          {{-- Application/resources/img/logo.png --}}
          <a href="{{ route('contacts.show', ['contact' => $contact->id]) }}">
            <img src="{{ Storage::url($contact->profile_picture) }}" class="profile-picture">
          </a>
        </div>

        <div class="d-flex align-items-center">
          <p class="me-2 mb-0">
            {{ $contact->name }}
          </p>

          <p class="me-2 mb-0 d-none d-md-block">
            <a href="mailto:{{ $contact->email }}">
              {{ $contact->email }}
            </a>
          </p>

          <p class="me-2 mb-0 d-none d-md-block">
            <a href="tel:{{ $contact->phone_number }}">
              {{ $contact->phone_number }}
            </a>
          </p>

          <p class="me-2 mb-0">
            Shared by <span class="text-info"> {{ $contact->user->email }} </span>
          </p>

        </div>

      </div>
    @empty
      <div class="col-md-4 mx-auto">
        <div class="card card-body text-center">
          <p>No contacts where shared with you yet</p>
        </div>
      </div>
    @endforelse

    <h1 class="text-center"> Contacts Shared by me </h1>
    @forelse ($myContactsSharedWithOthers as $contact)
      @foreach ($contact->sharedWithUsers as $user)
        <div class="d-flex justify-content-between bg-dark mb-3 rounded px-4 py-2">
          <div>
            {{-- Application/resources/img/logo.png --}}
            <a href="{{ route('contacts.show', ['contact' => $contact->id]) }}">
              <img src="{{ Storage::url($contact->profile_picture) }}" class="profile-picture">
            </a>
          </div>

          <div class="d-flex align-items-center">
            <p class="me-2 mb-0">
              {{ $contact->name }}
            </p>

            <p class="me-2 mb-0 d-none d-md-block">
              <a href="mailto:{{ $contact->email }}">
                {{ $contact->email }}
              </a>
            </p>

            <p class="me-2 mb-0 d-none d-md-block">
              <a href="tel:{{ $contact->phone_number }}">
                {{ $contact->phone_number }}
              </a>
            </p>

            <p class="me-2 mb-0">
              Shared with <span class="text-info"> {{ $user->email }} </span>
            </p>

            <form action="{{ route('contacts-shares.destroy', $user->pivot->id) }}" method="POST">
              @csrf
              @method('DELETE')
              <button type="submit" class="btn btn-danger mb-0 me-2 p-1 px-2">
                Unshare
              </button>
            </form>

          </div>

        </div>
      @endforeach
    @empty
      <div class="col-md-4 mx-auto">
        <div class="card card-body text-center">
          <p>You did not share any contacts yet</p>
          Share contacts
          <p>
            <a href="{{ route('contacts-shares.create') }}">here</a>.
          </p>
        </div>
      </div>
    @endforelse

  </div>
@endsection
