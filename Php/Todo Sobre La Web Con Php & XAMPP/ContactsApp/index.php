<?php require "partials/header.php" ?>

<div class="welcome d-flex align-items-center justify-content-center">
  <div class="text-center">
    <h1>Store Your Contacts Now</h1>
    <!-- light -->
    <a id="get-started" class="btn btn-lg btn-<?php 
      if ($_COOKIE["Theme"] == "flatly") {
        echo "light";
      } else {
        echo "dark";
      }
      ?>" href="register.php">Get Started</a>
  </div>
</div>

<?php require "partials/footer.php" ?>