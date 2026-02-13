@extends('layouts.app')

@section('content')
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <div class="card">
          <div class="card-header">Create new contact</div>

          <div class="card-body">
            <form method="POST" action="{{ route('contacts-shares.store') }}" enctype="multipart/form-data">
              {{-- <input type="hidden" name="_token" value="{{ csrf_token() }}"> --}}
              @csrf

              <div class="row mb-3">
                <label for="email" class="col-md-4 col-form-label text-md-end">Contact Email</label>

                <div class="col-md-6">
                  {{-- type="email" --}}
                  <input id="contact_email" type="text" class="form-control @error('contact_email') is-invalid @enderror" required
                    value="{{ old('contact_email') }}" name="contact_email" autocomplete="contact_email">
                  @error('contact_email')
                    <span class="invalid-feedback" role="alert">
                      <strong>{{ $message }}</strong>
                    </span>
                  @enderror
                </div>
              </div>


              <div class="row mb-3">
                <label for="email" class="col-md-4 col-form-label text-md-end">User Email</label>

                <div class="col-md-6">
                  {{-- type="email" --}}
                  <input id="user_email" type="text" class="form-control @error('user_email') is-invalid @enderror" required
                    value="{{ old('user_email') }}" name="user_email" autocomplete="user_email">
                  @error('user_email')
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
