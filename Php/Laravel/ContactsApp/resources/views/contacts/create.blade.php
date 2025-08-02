@extends('layouts.app')

@section('content')
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">Create new contact</div>

          <div class="card-body">
            <form method="POST" action="{{ route('contacts.store') }}" enctype="multipart/form-data">
              {{-- <input type="hidden" name="_token" value="{{ csrf_token() }}"> --}}
              @csrf
              <div class="row mb-3">
                <label for="name" class="col-md-4 col-form-label text-md-end">Name</label>

                <div class="col-md-6">
                  <input id="name" type="text" class="form-control @error('name') is-invalid @enderror" required
                    value="{{ old('name') }}" name="name" autocomplete="name" autofocus>
                  @error('name')
                    <span class="invalid-feedback" role="alert">
                      <strong>{{ $message }}</strong>
                    </span>
                  @enderror
                </div>
              </div>

              <div class="row mb-3">
                <label for="phone_number" class="col-md-4 col-form-label text-md-end">Phone Number</label>

                <div class="col-md-6">
                  <input id="phone_number" type="tel" class="form-control @error('phone_number') is-invalid @enderror"
                    required value="{{ old('phone_number') }}" name="phone_number" autocomplete="phone_number">
                  @error('phone_number')
                    <span class="invalid-feedback" role="alert">
                      <strong>{{ $message }}</strong>
                    </span>
                  @enderror
                </div>
              </div>

              <div class="row mb-3">
                <label for="email" class="col-md-4 col-form-label text-md-end">Email</label>

                <div class="col-md-6">
                  {{-- type="email" --}}
                  <input id="email" type="text" class="form-control @error('email') is-invalid @enderror" required
                    value="{{ old('email') }}" name="email" autocomplete="email">
                  @error('email')
                    <span class="invalid-feedback" role="alert">
                      <strong>{{ $message }}</strong>
                    </span>
                  @enderror
                </div>
              </div>

              <div class="row mb-3">
                <label for="age" class="col-md-4 col-form-label text-md-end">Age</label>

                <div class="col-md-6">
                  <input id="age" type="text" class="form-control @error('age') is-invalid @enderror" required
                    value="{{ old('age') }}" name="age" autocomplete="age">
                  @error('age')
                    <span class="invalid-feedback" role="alert">
                      <strong>{{ $message }}</strong>
                    </span>
                  @enderror
                </div>
              </div>


              <div class="row mb-3">
                <label for="profile_picture" class="col-md-4 col-form-label text-md-end">Profile Picture</label>
                <div class="col-md-6">
                  <input id="profile_picture" type="file"
                    class="form-control @error('profile_picture') is-invalid @enderror" name="profile_picture">
                  @error('profile_picture')
                    <span class="invalid-feedback" role="alert">
                      <strong>{{ $message }}</strong>
                    </span>
                  @enderror
                </div>
              </div>

              <div class="row mb-0">
                <div class="col-md-6 offset-md-4">
                  <button type="submit" class="btn btn-primary">
                    Submit
                  </button>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
@endsection
